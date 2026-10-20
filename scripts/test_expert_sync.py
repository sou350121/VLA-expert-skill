import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
import sys
import contextlib
import io
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('build', Path(__file__).with_name('build-expert-memory.py'))
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)


class BundleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.source = self.base / 'source'; self.source.mkdir()
        self.repo = self.base / 'expert'; self.repo.mkdir()
        self.git('init', '--quiet', '--initial-branch=main')
        self.git('config', 'user.name', 'test')
        self.git('config', 'user.email', 'test@example.invalid')
        self.put('theory/tactile/manual.md', '# Manual without dissection suffix\n\nPublic evidence boundary.\n')
        self.put('companies/industry_mainline.md', '# Industry\n\nThis is the exact public source quotation for regression verification.\n')
        self.put('reports/biweekly/2026-10-15.md', '# Report\n\nCollection was incomplete; not a complete market trend.\n')
        self.commit()
        self.notes = [{'source': 'companies/industry_mainline.md',
                       'quote': 'This is the exact public source quotation for regression verification.',
                       'reading_tip': '請先核對公告與實際交付的差別'}]
        self.fixture = self.base / 'notes.json'
        self.fixture.write_text(json.dumps(self.notes), encoding='utf-8')

    def git(self, *args):
        return subprocess.check_output(['git', '-C', str(self.source), *args], stderr=subprocess.DEVNULL)

    def put(self, path, text):
        p = self.source / path; p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding='utf-8')

    def commit(self):
        self.git('add', '.'); self.git('commit', '--quiet', '-m', 'fixture')

    def build(self, date='2026-10-20'):
        return b.build(self.repo, self.source, date, self.fixture)

    def test_full_inventory_has_no_eighty_item_cap(self):
        for n in range(125):
            self.put(f'theory/a/paper-{n}_dissection.md', '# Article\n\nSame arxiv reference is not a path identity.\n')
        self.commit(); manifest, changed = self.build()
        self.assertTrue(changed)
        self.assertEqual(manifest['counts']['theory_markdown'], 126)
        self.assertEqual(manifest['counts']['dissections'], 125)
        self.assertEqual(len(manifest['source_hashes']), 128)

    def test_only_committed_source_objects_are_exported(self):
        self.put('theory/tactile/manual.md', '# Unpublished replacement')
        self.put('theory/private-draft.md', '# Never published')
        m, _ = self.build()
        self.assertNotIn('theory/private-draft.md', m['source_hashes'])
        text = (self.repo / b.OUTPUTS[1]).read_text(encoding='utf-8')
        self.assertIn('Manual without dissection suffix', text)
        self.assertNotIn('Unpublished replacement', text)

    def test_same_source_no_api_no_date_or_content_churn(self):
        self.build(); before = {p: (self.repo / p).read_bytes() for p in b.OUTPUTS}
        with patch.object(b, 'deepseek_notes', side_effect=AssertionError('unexpected API')):
            m, changed = b.build(self.repo, self.source, '2026-10-21')
        self.assertFalse(changed); self.assertEqual(m['synced_date'], '2026-10-20')
        self.assertEqual(before, {p: (self.repo / p).read_bytes() for p in b.OUTPUTS})

    def test_deleted_and_renamed_sources_do_not_remain_current(self):
        self.build()
        self.git('mv', 'theory/tactile/manual.md', 'theory/tactile/renamed.md')
        self.git('commit', '--quiet', '-m', 'rename fixture')
        m, _ = self.build()
        self.assertNotIn('theory/tactile/manual.md', m['source_hashes'])
        self.assertIn('theory/tactile/renamed.md', m['source_hashes'])

    def test_manipulated_quote_and_foreign_source_fail(self):
        excerpts = b.evidence(b.snapshot(self.source)[1])
        for updates in [{'quote': self.notes[0]['quote'] + ' unsupported'}, {'source': '../secret'},
                        {'reading_tip': 'Guaranteed 99% success'}, {'reading_tip': 'Read https://evil.invalid'}]:
            with self.assertRaises(ValueError):
                b.validate_notes([{**self.notes[0], **updates}], excerpts)

    def test_tampering_with_output_or_source_manifest_is_detected(self):
        self.build()
        target = self.repo / b.OUTPUTS[1]; original = target.read_bytes()
        target.write_bytes(original + b'fabricated entry')
        with self.assertRaises(ValueError):b.validate_bundle(self.repo, self.source)
        target.write_bytes(original)
        target = self.repo / b.OUTPUTS[2]; m = json.loads(target.read_text())
        m['counts']['theory_markdown'] += 100
        target.write_text(json.dumps(m))
        with self.assertRaises(ValueError):b.validate_bundle(self.repo, self.source)

    def test_api_failure_writes_no_new_bundle(self):
        with patch.object(b, 'deepseek_notes', side_effect=ValueError('deepseek_unavailable')):
            with self.assertRaises(ValueError):b.build(self.repo, self.source, '2026-10-20')
        self.assertFalse(any((self.repo / p).exists() for p in b.OUTPUTS))

    def test_legacy_beliefs_are_not_modified(self):
        legacy = self.repo / 'skill/references/VLA_EXPERT_MEMORY.md'
        legacy.parent.mkdir(parents=True);legacy.write_bytes(b'Historical belief 80%\n')
        self.build();self.assertEqual(legacy.read_bytes(), b'Historical belief 80%\n')

    def test_every_index_link_is_pinned_to_exact_source_commit(self):
        m, _ = self.build()
        index = (self.repo / b.OUTPUTS[1]).read_text(encoding='utf-8')
        for path in m['source_hashes']:
            self.assertIn(b.link(m['source_commit'], path), index)

    def test_invalid_date_does_not_write_artifacts(self):
        with self.assertRaises(ValueError):self.build('2026-99-99')
        self.assertFalse((self.repo / b.OUTPUTS[2]).exists())

    def test_snapshot_hashes_ignore_checkout_line_ending_configuration(self):
        before = b.snapshot(self.source)
        self.git('config','core.autocrlf','true')
        self.assertEqual(before,b.snapshot(self.source))


@unittest.skipIf(sys.platform == 'win32', 'server runner requires Linux flock')
class RunnerTests(unittest.TestCase):
    git = BundleTests.git
    put = BundleTests.put
    commit = BundleTests.commit

    def setUp(self):
        BundleTests.setUp(self)
        spec = importlib.util.spec_from_file_location('sync', Path(__file__).with_name('sync-expert.py'))
        self.m = importlib.util.module_from_spec(spec); spec.loader.exec_module(self.m)
        self.state = self.base / 'state'
        self.remote = self.base / 'expert.git'
        self.run_git(self.repo, 'init', '--quiet', '--initial-branch=main')
        self.run_git(self.repo, 'config', 'user.name', 'test')
        self.run_git(self.repo, 'config', 'user.email', 'test@example.invalid')
        (self.repo / 'legacy.txt').write_text('Preserve human content')
        self.run_git(self.repo, 'add', '.')
        self.run_git(self.repo, 'commit', '--quiet', '-m', 'fixture')
        self.run_git(self.base, 'clone', '--quiet', '--bare', str(self.repo), str(self.remote))
        self.run_git(self.repo, 'remote', 'add', 'origin', str(self.remote))
        self.notes_patch = patch.object(self.m.builder, 'deepseek_notes', return_value=self.notes)
        self.mock_notes = self.notes_patch.start();self.addCleanup(self.notes_patch.stop)
        self.upstream_patch = patch.object(self.m.builder, 'UPSTREAM', self.source.as_uri().removesuffix('.git'))
        # Runner appends .git to the public upstream URL; a local bare fixture is equivalent.
        self.source_remote = Path(str(self.source) + '.git')
        self.run_git(self.base, 'clone', '--quiet', '--bare', str(self.source), str(self.source_remote))
        self.upstream_patch.start();self.addCleanup(self.upstream_patch.stop)

    def run_git(self, repo, *args):
        return subprocess.check_output(['git', '-C', str(repo), *args], stderr=subprocess.DEVNULL)

    def invoke(self):
        with patch.object(sys, 'argv', ['sync', '--repo', str(self.repo), '--state', str(self.state), '--publish']):
            return self.m.main()

    def receipt(self):
        return json.loads((self.state / 'latest.json').read_text())

    def test_actual_local_git_publish_and_noop(self):
        self.assertEqual(self.invoke(), 0)
        self.assertEqual(self.receipt()['status'], 'success')
        self.assertTrue(self.receipt()['remote_verified'])
        self.assertEqual(self.run_git(self.repo, 'rev-parse', 'HEAD'),
                         self.run_git(self.remote, 'rev-parse', 'main'))
        self.assertEqual(set(self.run_git(self.repo, 'diff-tree', '--no-commit-id', '--name-only', '-r', 'HEAD').decode().splitlines()), set(b.OUTPUTS))
        self.assertEqual(self.invoke(), 0)
        self.assertEqual(self.mock_notes.call_count, 1)

    def test_dirty_worktree_is_failed_and_preserved(self):
        (self.repo / 'human.md').write_text('Uncommitted human draft')
        self.assertEqual(self.invoke(), 1)
        self.assertEqual(self.receipt()['reason'], 'worktree_dirty_preserved')
        self.mock_notes.assert_not_called()
        self.assertEqual((self.repo / 'human.md').read_text(), 'Uncommitted human draft')

    def test_fetch_failure_is_not_a_successful_noop(self):
        original = self.m.command
        def fail(args, cwd=None, timeout=90):
            if args[:2] == ['git', 'fetch']:raise RuntimeError('fetch_failed')
            return original(args, cwd, timeout)
        with patch.object(self.m, 'command', side_effect=fail):self.assertEqual(self.invoke(), 1)
        self.assertEqual(self.receipt()['status'], 'failed');self.mock_notes.assert_not_called()

    def test_rejected_push_can_retry_without_regeneration(self):
        original = self.m.command
        def reject(args, cwd=None, timeout=90):
            if args[:2] == ['git', 'push']:raise RuntimeError('push_rejected')
            return original(args, cwd, timeout)
        with patch.object(self.m, 'command', side_effect=reject):self.assertEqual(self.invoke(), 1)
        self.assertEqual(self.receipt()['status'], 'failed')
        self.assertEqual(self.invoke(), 0)
        self.assertEqual(self.mock_notes.call_count, 1)

    def test_cancel_restores_outputs_and_never_pushes(self):
        original = self.m.command;calls=[]
        def track(args, cwd=None, timeout=90):
            calls.append(args[:2]);return original(args, cwd, timeout)
        with patch.object(self.m.builder, 'build', side_effect=self.m.Cancelled()), patch.object(self.m, 'command', side_effect=track):
            self.assertEqual(self.invoke(), 143)
        self.assertNotIn(['git', 'push'], calls)
        self.assertEqual(self.receipt()['status'], 'failed')

    def test_unapproved_code_commit_cannot_be_published_by_content_job(self):
        (self.repo / 'code.py').write_text('print("unapproved")')
        self.run_git(self.repo, 'add', '.');self.run_git(self.repo, 'commit', '--quiet', '-m', 'not content')
        self.assertEqual(self.invoke(), 1)
        self.assertEqual(self.receipt()['reason'], 'unapproved_pending_commit')
        self.mock_notes.assert_not_called()

    def test_shared_heavy_lock_prevents_any_fetch_or_model_call(self):
        import fcntl
        lock_path = self.base / 'shared.lock';lock_path.write_text('')
        with lock_path.open('rb') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            with patch.object(sys, 'argv', ['sync','--repo',str(self.repo),'--state',str(self.state),
                                           '--publish','--heavy-lock',str(lock_path)]):
                self.assertEqual(self.m.main(), 75)
        self.mock_notes.assert_not_called()
        self.assertFalse((self.state / 'latest.json').exists())

    def test_owner_health_probe_is_read_only_and_has_no_model_calls(self):
        self.assertEqual(self.invoke(),0)
        before=(self.state/'latest.json').read_bytes();self.mock_notes.reset_mock()
        output=io.StringIO()
        with contextlib.redirect_stdout(output),patch.object(sys,'argv',[
                'sync','--repo',str(self.repo),'--state',str(self.state),'--health']):
            self.assertEqual(self.m.main(),0)
        result=json.loads(output.getvalue())
        self.assertTrue(result['hashes_ok']);self.assertFalse(result['dirty'])
        self.assertEqual(before,(self.state/'latest.json').read_bytes());self.mock_notes.assert_not_called()
        self.assertNotIn('notes',result)

    def test_reverted_code_history_still_cannot_be_published(self):
        f=self.repo/'code.py';f.write_text('print("unapproved")')
        self.run_git(self.repo,'add','.');self.run_git(self.repo,'commit','--quiet','-m','code')
        f.unlink();self.run_git(self.repo,'add','-u');self.run_git(self.repo,'commit','--quiet','-m','revert code')
        self.run_git(self.repo,'fetch','--quiet','origin','main')
        self.assertEqual(self.run_git(self.repo,'diff','--name-only','origin/main..HEAD'),b'')
        self.assertEqual(self.invoke(),1)
        self.assertEqual(self.receipt()['reason'],'unapproved_pending_commit');self.mock_notes.assert_not_called()


if __name__ == '__main__':
    unittest.main()
