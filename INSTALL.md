# Install VLA Expert

Clone the repository and preserve the complete `skill/` directory. The current
source guide, complete index, manifest and historical memory work together.
Copying only `VLA_EXPERT_MEMORY.md` installs an old snapshot.

```bash
git clone https://github.com/sou350121/VLA-expert-skill.git
```

## Codex: project skill

From the target project, copy into an unused skill directory:

```bash
mkdir -p .agents/skills
cp -r VLA-expert-skill/skill .agents/skills/vla-expert
```

If `vla-expert` already exists, review its local changes before updating it.
Do not replace project AGENTS.md or global instructions. Start a new session to
discover the skill. See [official skills documentation](https://developers.openai.com/codex/skills).

## Claude Code

Copy the complete `skill/` folder into the target project's unused
`.claude/skills/vla-expert/` directory. Preserve existing instructions.

## Cursor

Keep the complete skill as `vla-expert/` in the project and add the portable
`platforms/cursor/.cursorrules` adapter through your Cursor version's rule settings.
The adapter points to `vla-expert/SKILL.md` and its references. Do not overwrite
an existing rules file or assume a renamed legacy rule uses the current rule schema.

## Other tools

Use `platforms/codex/SYSTEM_PROMPT.md` as a portable adapter together with the
canonical skill and references, through your tool's documented context mechanism.
This repository does not prescribe undocumented command-line flags.

## Verify and update

Ask about a concrete VLA method. Confirm the answer cites an accessible source,
identifies the source date/version and separates evidence from inference.
An elaborate debate format is not proof of a successful installation.

Pull updates in the clone and review changes before updating the installed copy.
Updating the clone does not update previously copied installations automatically.

## Maintainer sync

The existing server cron runs at **20:00 Asia/Shanghai**. It calls
`scripts/cron-build-expert-memory.sh`, with a common lock and a 900-second limit.
Only three generated current-source files may be automatically committed.
Code changes and manual knowledge edits require maintainer approval.

The generator reads committed Handbook objects, includes the complete source
inventory, and pins every entry to a commit. It never recalibrates historical
beliefs or calls GPT, qwen or OpenRouter. Changed evidence uses one bounded call
to the existing DeepSeek account; failed extraction, invalid quotes, dirty
worktrees and rejected pushes fail visibly instead of reporting no update.

The daily GitHub workflow validates published artifacts; it does not copy an
old `updates` branch into `main`. It needs no model secret. The server receipt
distinguishes draft validation from a remotely verified publication.
