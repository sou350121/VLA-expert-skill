#!/usr/bin/env bash
# cron-build-expert-memory.sh — daily wrapper that regenerates the
# VLA-expert-skill knowledge base from the local VLA-Handbook, then commits +
# pushes. Revives the server-side `vla-expert-bot` pipeline that died 2026-06-26.
#
# Behaviour:
#   * best-effort fast-forward the VLA-Handbook checkout so the generator sees
#     the day's newest deep-dives (never clobbers the radar/sweeper's local work)
#   * supplies TODAY (UTC) so the Python stays reproducible
#   * runs the deterministic generator (mechanical index/paper refresh + ONE
#     guarded LLM change-summary line; belief/phase state carried forward verbatim)
#   * if the KB is byte-identical afterwards -> log "no change" and exit 0
#   * else commit as vla-expert-bot and push (pull --rebase + retry once on a
#     non-ff, e.g. the merge GHA advanced origin; abort cleanly, never wedge)
set -uo pipefail

REPO="/home/claudeuser/VLA-expert-skill"
HANDBOOK="/home/claudeuser/vla-handbook-work"
KB="skill/references/VLA_EXPERT_MEMORY.md"
LOG="/tmp/vla-expert-skill-gen.log"
TODAY="$(date -u +%F)"

log() { echo "$(date -u +%FT%TZ) $*" | tee -a "$LOG"; }

cd "$REPO" || { echo "cannot cd $REPO" >&2; exit 1; }
log "=== cron-build-expert-memory START TODAY=$TODAY ==="

# Freshen the handbook (FF only; leaves radar/sweeper local work untouched).
git -C "$HANDBOOK" fetch origin -q 2>>"$LOG" && \
  git -C "$HANDBOOK" merge --ff-only origin/main >>"$LOG" 2>&1 || \
  log "handbook FF-sync skipped (diverged/other-agent work) — using local state"

PY="python3"; command -v python3.11 >/dev/null 2>&1 && PY="python3.11"
"$PY" scripts/build-expert-memory.py "$TODAY" >>"$LOG" 2>&1
rc=$?
if [ "$rc" -ne 0 ]; then
  log "generator FAILED rc=$rc (guards protect the KB; nothing committed)"; exit "$rc"
fi

if git diff --quiet -- "$KB"; then
  log "no change to KB — nothing to commit"; exit 0
fi

git add "$KB" CHANGELOG.md
git -c user.name=vla-expert-bot -c user.email=sou350121@gmail.com \
  commit -m "daily update: $TODAY (auto-regen: index+papers refreshed; beliefs carried)" >>"$LOG" 2>&1 \
  || { log "git commit FAILED"; exit 1; }

if git push origin main >>"$LOG" 2>&1; then
  log "pushed OK"
elif git pull --rebase origin main >>"$LOG" 2>&1 && git push origin main >>"$LOG" 2>&1; then
  log "pushed after rebase"
else
  git rebase --abort >>"$LOG" 2>&1 || true
  log "push FAILED — will retry next run"; exit 1
fi
log "=== cron-build-expert-memory DONE ==="
