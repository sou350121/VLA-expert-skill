#!/usr/bin/env bash
# Original daily 20:00 Asia/Shanghai cron entry remains unchanged.
set -euo pipefail
REPO="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
exec timeout 900 python3.11 "$REPO/scripts/sync-expert.py" --publish \
  --heavy-lock /home/claudeuser/.vla-expert-state/shared-heavy.lock
