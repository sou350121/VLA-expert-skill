#!/usr/bin/env python3
"""Server-owned, bounded sync. Draft by default; cron explicitly uses --publish."""
import argparse
import datetime as dt
import fcntl
import importlib.util
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('expert_build', ROOT / 'scripts/build-expert-memory.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class Cancelled(BaseException):
    pass


def cancel(*_):
    raise Cancelled()


def command(args, cwd=None, timeout=90):
    result = subprocess.run(args, cwd=cwd, capture_output=True, timeout=timeout)
    if result.returncode:
        # Git stderr can contain credentials embedded in origin; never log it.
        raise RuntimeError('command_failed:' + Path(args[0]).name + ':' + str(result.returncode))
    return result.stdout.decode().strip()


def clean(repo):
    if command(['git', 'status', '--porcelain'], repo):
        raise RuntimeError('worktree_dirty_preserved')


def content_only_pending(repo):
    commits = command(['git','log','--format=%H','origin/main..HEAD'],repo).splitlines()
    for commit in commits:
        paths = command(['git','diff-tree','--root','--no-commit-id','--name-only','-r',commit],repo).splitlines()
        if not set(paths) <= set(builder.OUTPUTS):
            raise RuntimeError('unapproved_pending_commit')


def write_json(path, value):
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    temporary.replace(path)


def health(repo, state):
    def read(path):
        try:return json.loads(path.read_text(encoding='utf-8'))
        except (OSError, ValueError):return {}
    receipt = read(state/'latest.json')
    manifest = read(repo/'skill/references/handbook-manifest.json')
    expected = set(builder.OUTPUTS[:2])
    artifacts = manifest.get('artifacts', {})
    valid = set(artifacts) == expected
    for path, checksum in artifacts.items():
        if path not in expected:
            valid = False
            continue
        f = repo/path
        valid = valid and f.is_file() and hashlib.sha256(f.read_bytes()).hexdigest() == checksum
    return {'receipt':{k:receipt[k] for k in ('status','started_at','finished_at','source_commit',
            'head','remote_verified') if k in receipt}, 'manifest':{'source_commit':manifest.get('source_commit')},
            'hashes_ok':valid,'head':command(['git','rev-parse','HEAD'],repo),
            'dirty':bool(command(['git','status','--porcelain'],repo))}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', type=Path, default=ROOT)
    ap.add_argument('--state', type=Path, default=ROOT.parent / '.vla-expert-state')
    ap.add_argument('--publish', action='store_true')
    ap.add_argument('--health', action='store_true', help='Read-only sanitized owner-side health probe')
    ap.add_argument('--heavy-lock', type=Path, help='Existing shared host lock; opened read-only')
    a = ap.parse_args()
    if a.health:
        print(json.dumps(health(a.repo,a.state)))
        return 0
    a.state.mkdir(parents=True, exist_ok=True)
    os.chmod(a.state, 0o755)
    with (a.state / 'sync.lock').open('a') as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            return 75
        heavy = None
        if a.heavy_lock:
            try:
                heavy = a.heavy_lock.open('rb')
            except OSError:
                write_json(a.state/'latest.json', {'status':'failed','reason':'heavy_lock_unavailable',
                    'finished_at':dt.datetime.now(dt.timezone.utc).isoformat()})
                return 1
            try:
                fcntl.flock(heavy, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                heavy.close()
                return 75
        state = {'started_at': dt.datetime.now(dt.timezone.utc).isoformat(), 'status': 'running',
                 'publish': a.publish, 'phase': 'preflight'}
        receipt = a.state / 'latest.json'
        write_json(receipt, state)
        prior_signal = signal.signal(signal.SIGTERM, cancel)
        try:
            clean(a.repo)
            command(['git', 'fetch', '--quiet', 'origin', 'main'], a.repo)
            command(['git', 'merge', '--ff-only', '--quiet', 'origin/main'], a.repo)
            content_only_pending(a.repo)
            source = a.state / 'handbook'
            state['phase'] = 'source_fetch'; write_json(receipt, state)
            if not source.exists():
                command(['git', 'clone', '--quiet', '--depth', '1', builder.UPSTREAM + '.git', str(source)])
            else:
                clean(source)
                command(['git', 'fetch', '--quiet', '--depth', '1', 'origin', 'main'], source)
                # Each source fetch is shallow: use a detached pointer to the fetched
                # published commit, only after proving this bot-owned checkout clean.
                command(['git', 'checkout', '--quiet', '--detach', 'FETCH_HEAD'], source)
            source_head = command(['git', 'rev-parse', 'HEAD'], source)
            remote_source = command(['git', 'ls-remote', 'origin', 'refs/heads/main'], source).split()[0]
            if source_head != remote_source:
                raise RuntimeError('upstream_moved_retry_next_run')
            state.update(phase='build', source_commit=source_head); write_json(receipt, state)
            before = {p: (a.repo / p).read_bytes() if (a.repo / p).exists() else None for p in builder.OUTPUTS}
            try:
                manifest, changed = builder.build(a.repo, source,
                    dt.datetime.now(dt.timezone(dt.timedelta(hours=8))).date().isoformat())
            except BaseException:
                # Restore only the three generator-owned outputs changed by this run.
                for p, data in before.items():
                    target = a.repo / p
                    if data is not None:
                        target.write_bytes(data)
                    elif target.exists():
                        target.unlink()
                raise
            builder.validate_bundle(a.repo, source)
            state.update(phase='publish', changed=changed, counts=manifest['counts']); write_json(receipt, state)
            if a.publish:
                if changed:
                    command(['git', 'add', '--', *builder.OUTPUTS], a.repo)
                    staged = command(['git', 'diff', '--cached', '--name-only'], a.repo).splitlines()
                    if not set(staged) <= set(builder.OUTPUTS):
                        raise RuntimeError('unexpected_staged_paths')
                    command(['git', '-c', 'user.name=vla-expert-bot', '-c',
                             'user.email=noreply@users.noreply.github.com', 'commit', '--quiet',
                             '-m', 'auto: sync verified published VLA Handbook sources'], a.repo)
                # A previous successful commit may need its push retried. Never publish
                # human or code changes through this daily content-only path.
                content_only_pending(a.repo)
                command(['git', 'push', '--quiet', 'origin', 'HEAD:main'], a.repo)
                head = command(['git', 'rev-parse', 'HEAD'], a.repo)
                remote = command(['git', 'ls-remote', 'origin', 'refs/heads/main'], a.repo).split()[0]
                if head != remote:
                    raise RuntimeError('remote_readback_mismatch')
                clean(a.repo)
                state.update(status='success', head=head, remote_verified=True)
            else:
                state.update(status='draft_verified', remote_verified=False)
            state.update(phase='finished', finished_at=dt.datetime.now(dt.timezone.utc).isoformat())
            write_json(receipt, state)
            print(json.dumps(state))
            return 0
        except BaseException as error:
            state.update(status='failed', reason=str(error) if isinstance(error, (ValueError, RuntimeError))
                         else type(error).__name__, finished_at=dt.datetime.now(dt.timezone.utc).isoformat())
            write_json(receipt, state)
            print(json.dumps(state))
            return 143 if isinstance(error, Cancelled) else 1
        finally:
            signal.signal(signal.SIGTERM, prior_signal)
            if heavy:
                heavy.close()


if __name__ == '__main__':
    raise SystemExit(main())
