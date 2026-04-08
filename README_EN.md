<p align="center">
  <h1 align="center">🤖 VLA Expert Skill</h1>
  <p align="center">
    <strong>Give your AI assistant expert-level judgment in VLA</strong><br/>
    Composable domain knowledge module · Activate on-demand · Never interferes with your workflow<br/><br/>
    <a href="#installation"><img src="https://img.shields.io/badge/Claude_Code-supported-blueviolet?logo=anthropic" alt="Claude"/></a>
    <a href="#installation"><img src="https://img.shields.io/badge/Cursor-supported-00C7B7" alt="Cursor"/></a>
    <a href="#installation"><img src="https://img.shields.io/badge/Codex-supported-412991?logo=openai" alt="Codex"/></a>
    <a href="#installation"><img src="https://img.shields.io/badge/OpenCode-supported-333" alt="OpenCode"/></a>
  </p>
  <p align="center">
    <a href="https://github.com/sou350121/VLA-expert-skill/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License"/></a>
    <a href="https://github.com/sou350121/VLA-Handbook"><img src="https://img.shields.io/badge/Knowledge_Source-VLA--Handbook_⭐100+-orange?logo=github" alt="VLA-Handbook"/></a>
    <img src="https://img.shields.io/badge/Papers-332%2B_covered-brightgreen" alt="Papers"/>
    <img src="https://img.shields.io/badge/Updates-Daily_Auto-blueviolet" alt="Daily Update"/>
  </p>
  <p align="center">
    <b>English</b> · <a href="./README.md">中文</a>
  </p>
</p>

---

## What is this?

VLA Expert Skill is a **composable domain knowledge module**—it doesn't manage your workflow or replace your development tools. It does one thing:

**When your AI assistant encounters a VLA (Vision-Language-Action) question, it gets expert-level judgment based on 332+ papers and real-world deployment experience.**

It sits quietly most of the time. When you ask about VLA architecture trade-offs, paper evaluations, direction calls, or deployment pitfalls, it activates, provides deep analysis grounded in evidence, then hands control back.

> 💡 It has a **complementary relationship** with frameworks like [Superpowers](https://github.com/obra/superpowers): Superpowers manages **how you code**, VLA Expert Skill manages **what decisions you make in the VLA domain**. Both can be installed together without interference.

## When does it activate?

| You ask | Activates? | What happens |
|---------|-----------|--------------|
| "Help me refactor this Python module" | ❌ No | That's workflow—your dev tools handle it |
| "What action head does π0.6 use?" | ✅ QUICK | Query from memory, 2-5 sentence answer |
| "Diffusion Policy vs Flow Matching—which should we use?" | ✅ DEEP | Evidence from both sides + adversarial thinking + actionable advice |
| "Is this VLA paper worth reading?" | ✅ DEEP | Triage (does it change any belief?) → expand if worthwhile |
| "Write a unit test" | ❌ No | Development task, not domain knowledge |
| "What direction should we bet on next for VLA?" | ✅ DEEP | Analysis + actionable advice + what signal means you should bail |
| "How do I deploy π0 on a FR3 arm?" | ✅ QUICK | Step-by-step + hardware picks + common pitfalls (300+ community notes) |
| "Is Physical Intelligence worth tracking?" | ✅ DEEP | Competitive positioning + risks + judgment |

## Demo: Without vs With

**You ask**: "Which is better—Diffusion Policy or Flow Matching?"

| Without VLA Expert Skill | **With VLA Expert Skill** |
|---|---|
| "Both have trade-offs. Diffusion is more mature, Flow Matching is newer…" (correct but useless) | FM hits 50Hz on π0 with 5-20 inference steps—engineering already favors it `[fact: §2]`. But FM's multimodal coverage on high-DoF bimanual tasks remains unproven `[inference]`. **Judgment**: current evidence leans FM, but if a direct comparison shows Diffusion winning on bimanual within 6 months, this call needs revision. Deep mode available for full paper breakdowns of both paradigms. |

## v3 Upgrade: Thinking Discipline > Output Templates

v2 spent 54% of its instruction budget on format compliance (forced three-perspective debates, ×0.9 calibration arithmetic, 7 output templates). v3 cuts all of that and gives the context budget back to reasoning.

| v2 | v3 |
|---|---|
| 8 intent routes | 2: QUICK / DEEP |
| 7 output templates | Format follows content—no forced structure |
| Mandatory 🔴🔵🟢 three-perspective output | Adversarial thinking as internal discipline, not performance |
| Full memory load (~16K tokens) | Source Map with line numbers, selective loading |
| References 3 non-existent files | Cleaned up—only references files that actually exist |

**What stays**: adversarial thinking, anti-hallucination, falsifiable judgments, honest source tagging.

## Knowledge Coverage

Sourced from [**VLA-Handbook**](https://github.com/sou350121/VLA-Handbook) (⭐100+), compressed into on-demand domain memory:

```
Model architectures          RT-1 → RT-2 → Octo → OpenVLA → π0 → π0.5 → π0.6
Action generation paradigms  Diffusion Policy · Flow Matching · FAST Tokenization · Autoregressive
Training paradigms           Behavior Cloning · Co-training · RL Post-training · Self-improving loops
World models                 Cosmos · Video prediction · Physics simulation · Planning augmentation
Tactile & multimodality      TacVLA · Vision-touch fusion · Force feedback · Proprioception
Deployment in the wild       300+ EN/CN community field notes · Real-robot guides · Sim-to-Real
Industry landscape           PI($2.4B) · Figure · Tesla Optimus · NVIDIA GR00T · Unitree · Rhoda AI($4.5B)
Belief tracking system       10 calibrated beliefs (+ contrarian signals) · 5 convergence phases · falsifiable experiments
```

## Built-in Cognitive Discipline

When activated, it doesn't just fetch knowledge—it applies strict thinking discipline:

| Mechanism | What it does | Why |
|-----------|-------------|-----|
| **Two-sided evidence** | Finds supporting evidence, then opposing evidence—both taken seriously | One-sided arguments lead to self-deception |
| **Source tagging** | Key claims marked `[fact]` / `[inference]` / `[judgment]` | Distinguish hard data from speculation |
| **Falsifiability** | Every important judgment includes "what would prove me wrong + by when" | Non-falsifiable = invalid |
| **Honest disagreement** | When support ≈ opposition, marked as high-signal divergence point | False consensus is worse than admitting uncertainty |
| **Hallucination shield** | When memory has no answer: "Not recorded" instead of making it up | Wrong numbers harm worse than admitting ignorance |

## Installation

> **Note:** Installation varies by platform. VLA Expert Skill installs as a knowledge module and doesn't interfere with existing workflow configs.

### Claude Code / Cowork

```bash
git clone https://github.com/sou350121/VLA-expert-skill.git
cp -r VLA-expert-skill/skill/ your-project/.claude/skills/vla-expert/
```

Claude Code automatically activates based on conversation context—only triggers on VLA topics.

### Cursor

```bash
git clone https://github.com/sou350121/VLA-expert-skill.git
mkdir -p .cursor/rules
cp VLA-expert-skill/platforms/cursor/.cursorrules .cursor/rules/vla-expert.md
cp VLA-expert-skill/skill/references/VLA_EXPERT_MEMORY.md docs/
```

### Codex

Tell Codex:

```
Fetch and follow instructions from https://raw.githubusercontent.com/sou350121/VLA-expert-skill/main/platforms/codex/SYSTEM_PROMPT.md
```

Full docs: [platforms/codex/SYSTEM_PROMPT.md](platforms/codex/SYSTEM_PROMPT.md)

### OpenCode

Tell OpenCode:

```
Fetch and follow instructions from https://raw.githubusercontent.com/sou350121/VLA-expert-skill/main/platforms/codex/SYSTEM_PROMPT.md
```

Or manual install:

```bash
git clone https://github.com/sou350121/VLA-expert-skill.git
mkdir -p .opencode
cp VLA-expert-skill/platforms/codex/SYSTEM_PROMPT.md .opencode/instructions.md
```

### Other AI Tools

Use the contents of [`platforms/codex/SYSTEM_PROMPT.md`](platforms/codex/SYSTEM_PROMPT.md) as your system prompt, and attach [`skill/references/VLA_EXPERT_MEMORY.md`](skill/references/VLA_EXPERT_MEMORY.md) as context.

### Verify Installation

Start a fresh session and ask: "Diffusion Policy or Flow Matching—which is better?" If the answer includes specific paper evidence, opposing arguments, and a falsifiable condition, installation succeeded.

### Standalone vs Deep Mode

| Mode | Condition | Depth |
|------|-----------|-------|
| **Standalone** | VLA Expert Skill only | Compressed memory covers ~90% of scenarios |
| **Deep Mode** | Also clone [VLA-Handbook](https://github.com/sou350121/VLA-Handbook) | On-demand access to full paper breakdowns; 5-20× more context |

## Related Projects

| Tool | What it does | Relationship with VLA Expert Skill |
|------|-------------|-----------------------------------|
| [Superpowers](https://github.com/obra/superpowers) | Development workflow framework (spec → plan → implement → test) | **Complementary**. Superpowers manages how you code; VLA Expert Skill manages what decisions you make in VLA |
| [VLA-Handbook](https://github.com/sou350121/VLA-Handbook) | Complete VLA knowledge base (70+ paper breakdowns + 300+ community field notes) | **Upstream data source**. Skill knowledge compressed from Handbook; use both to unlock deep mode |
| Cursor Rules / .codex | Platform-level AI configuration | **Coexist**. Installs as a rule alongside your others—no conflicts |

## Daily Updates

Knowledge is synced daily via automation pipeline. Stay current:

```bash
cd VLA-expert-skill && git pull
```

## File Structure

```
VLA-expert-skill/
├── skill/
│   ├── SKILL.md                    # Skill instructions (intent routing + thinking discipline + anti-hallucination)
│   └── references/
│       └── VLA_EXPERT_MEMORY.md    # Compressed knowledge base (332+ papers, daily updates, line-number indexed)
├── platforms/
│   ├── cursor/.cursorrules         # Cursor Rules adaptation
│   └── codex/SYSTEM_PROMPT.md      # Codex / OpenCode / universal system prompt
├── INSTALL.md                      # LLM-readable self-service guide
├── .github/workflows/              # GitHub Actions automation
└── README.md / README_EN.md
```

## License

[MIT](LICENSE)—use, modify, distribute freely.

## Contributing

Contributions welcome! Paper analysis, deployment experience, bug reports—open an Issue or PR.

---

<p align="center">
  <sub>Built on <a href="https://github.com/sou350121/VLA-Handbook">VLA-Handbook</a> · Daily-updated knowledge base · v3: thinking discipline > output templates</sub>
</p>
