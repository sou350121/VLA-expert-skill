# VLA Expert Skill

English · [中文](README.md)

Use published [VLA Handbook](https://github.com/sou350121/VLA-Handbook) evidence for VLA papers, architecture choices, deployment and industry questions. Read relevant sources on demand while keeping your development workflow in control.

## Current evidence and historical memory

- [Current guide](skill/references/HANDBOOK_CURRENT.md): source commit, coverage boundary and DeepSeek reading suggestions.
- [Complete index](skill/references/HANDBOOK_INDEX.md): theory, companies, biweekly reports and deployment pages, linked to a specific commit.
- [Manifest](skill/references/handbook-manifest.json): actual file counts, source hashes and artifact hashes.
- [Legacy memory](skill/references/VLA_EXPERT_MEMORY.md): historical content. Its belief probabilities, phase percentages, valuations and predictions are not recalibrated by a source sync.

Theory Markdown counts and dissection filename counts are different; neither proves an independent paper count. A sync date does not mean every claim was independently rechecked. Preserve upstream labels for company claims, historical backfills and missing coverage.

## Use

Give brief, sourced answers for concrete lookups. For comparisons or decisions, examine mechanisms, evaluation conditions, the strongest supporting and opposing evidence, failure modes and falsifiers. Distinguish policy inference rate, control rate and action chunks. Industry announcements, plans, deliveries and independent results are different evidence.

Do not force a three-voice debate or mechanically discount probabilities. A statement stored in memory is not automatically a verified fact. Ordinary coding and unrelated topics retain their existing workflow.

## Installation

See [INSTALL.md](INSTALL.md). Copy the complete `skill/` directory, including all references.

Codex project example, after checking for an existing installation:

```bash
git clone https://github.com/sou350121/VLA-expert-skill.git
mkdir -p .agents/skills
cp -r VLA-expert-skill/skill .agents/skills/vla-expert
```

Claude Code uses `.claude/skills/vla-expert/`. Cursor and other tools can use the supplied adapters with the canonical skill and references through their documented context mechanism. Preserve local changes. Pulling updates in the clone does not update previously copied installations.

## Automatic updates

The existing server schedule runs at **20:00 Asia/Shanghai** without an open local computer or Codex session. The bounded, locked job verifies Git state, reads committed Handbook objects and exports the complete inventory without a date or item cap.

Changed reading-guide evidence uses the existing DeepSeek account for one bounded call. Quotes must be exact source substrings; reading suggestions cannot introduce numerical claims or URLs. No other provider is used. The job validates outputs, publishes only three generated current-source files, and verifies the remote commit. It does not rewrite historical beliefs or human research content.

GitHub Actions retains its daily verification time and checks artifacts against the pinned upstream commit. It no longer copies an obsolete `updates` branch into `main`. Failures remain failures; a complete sync does not imply complete upstream coverage.

## Verification

```bash
python -m unittest discover -s scripts -p 'test_*.py'
python scripts/build-expert-memory.py --handbook /path/to/VLA-Handbook --check
```

Changes to code, routing or publication policy require maintainer approval. See [AGENTS.md](AGENTS.md) for the limited generated-file maintenance scope.

[MIT](LICENSE) · [Changelog](CHANGELOG.md)
