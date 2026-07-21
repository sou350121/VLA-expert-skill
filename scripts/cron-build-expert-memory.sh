#!/usr/bin/env bash
# cron-build-expert-memory.sh — GAP-FILLER regenerator for the VLA-expert-skill KB.
#
# History: the PRIMARY generator is the server-side `vla-memory-bot` (sophisticated
# belief recalibration, e.g. "B8 70->75"). It died 2026-06-26; I rebuilt this simpler
# from-source regenerator as a fallback (2026-07-07). vla-memory-bot then REVIVED
# 2026-07-11 — so this now DEFERS to it and only fills LONG gaps:
#   * reset --hard to origin every run  -> always builds on vla-memory-bot's latest,
#     preserving its belief work; two generators can never diverge.
#   * regen ONLY if the KB header date is >= GAP_DAYS old (primary clearly dead, not
#     merely on its ~4-day cadence).
#   * on a push race (primary pushed first) just bail; next run resets fresh (never
#     rebase -> no conflict loop, which is what wedged it 07-11..07-20).
set -uo pipefail
REPO="/home/claudeuser/VLA-expert-skill"
HANDBOOK="/home/claudeuser/vla-handbook-work"
KB="skill/references/VLA_EXPERT_MEMORY.md"
LOG="/tmp/vla-expert-skill-gen.log"
TODAY="$(date -u +%F)"
GAP_DAYS=7
log() { echo "$(date -u +%FT%TZ) $*" | tee -a "$LOG"; }

cd "$REPO" || { echo "cannot cd $REPO" >&2; exit 1; }
log "=== gap-filler START TODAY=$TODAY ==="

# Always rebuild on the primary's latest (discard any stale local regen).
git fetch origin -q 2>>"$LOG" && git reset --hard origin/main >>"$LOG" 2>&1 || log "reset-to-origin skipped"

# Defer to the primary if it refreshed the KB within GAP_DAYS.
KB_DATE=$(head -1 "$KB" | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}' | head -1)
if [ -n "$KB_DATE" ]; then
  age=$(( ( $(date -u +%s) - $(date -u -d "$KB_DATE" +%s) ) / 86400 ))
  if [ "$age" -lt "$GAP_DAYS" ]; then
    log "KB ${age}d old (< ${GAP_DAYS}d, primary active) — deferring"; exit 0
  fi
  log "KB ${age}d stale (>= ${GAP_DAYS}d, primary silent) — gap-filling"
fi

git -C "$HANDBOOK" fetch origin -q 2>>"$LOG" && \
  git -C "$HANDBOOK" merge --ff-only origin/main >>"$LOG" 2>&1 || log "handbook FF-sync skipped"

PY="python3"; command -v python3.11 >/dev/null 2>&1 && PY="python3.11"
"$PY" scripts/build-expert-memory.py "$TODAY" >>"$LOG" 2>&1 || { log "generator FAILED"; exit 1; }

if git diff --quiet -- "$KB"; then log "no change"; exit 0; fi
git add "$KB" CHANGELOG.md
git -c user.name=vla-expert-bot -c user.email=sou350121@gmail.com \
  commit -m "gap-fill: $TODAY (index+papers refreshed; beliefs carried from vla-memory-bot)" >>"$LOG" 2>&1 \
  || { log "commit failed"; exit 1; }
if git push origin main >>"$LOG" 2>&1; then
  log "pushed OK (gap-filled)"
else
  log "push rejected (primary raced) — next run resets fresh"; exit 0
fi
log "=== gap-filler DONE ==="
