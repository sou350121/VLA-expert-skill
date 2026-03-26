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
    <img src="https://img.shields.io/badge/Papers-328%2B_covered-brightgreen" alt="Papers"/>
    <img src="https://img.shields.io/badge/Updates-Daily_Auto-blueviolet" alt="Daily Update"/>
  </p>
  <p align="center">
    <b>English</b> · <a href="./README.md">中文</a>
  </p>
</p>

---

## What is this?

VLA Expert Skill is a **composable domain knowledge module**—it doesn't manage your workflow, doesn't replace your development tools. It does one thing:

**When your AI assistant encounters a VLA (Vision-Language-Action) question, it gets expert-level judgment based on 328+ papers and deployment experience.**

It sits quietly most of the time. When you ask about VLA architecture trade-offs, paper evaluations, direction calls, or deployment pitfalls, it activates, provides deep analysis grounded in evidence, then hands control back to you.

> 💡 It has a **complementary relationship** with frameworks like [Superpowers](https://github.com/obra/superpowers): Superpowers manages **how you code** (brainstorm → spec → implement → test), VLA Expert Skill manages **what decisions you make in the VLA domain**. Both can be installed together without interference.

## When does it activate?

| You ask | Activates? | What happens |
|---------|-----------|--------------|
| "Help me refactor this Python module" | ❌ No | That's workflow—your dev tools handle it |
| "What action head does π0.6 use?" | ✅ Yes | Query from 328-paper memory in 2-5 sentences |
| "Diffusion Policy vs Flow Matching—which should we use?" | ✅ Yes | 🔴🔵🟢 Three-perspective debate + calibrated confidence |
| "Is this VLA paper worth reading?" | ✅ Yes | Information value triage → debate → belief update |
| "Write a unit test" | ❌ No | Development task, not domain knowledge |
| "What direction should we bet on next for VLA?" | ✅ Yes | Full debate + crucial experiments + contrarian checks |
| "How do I deploy π0 on a FR3 arm?" | ✅ Yes | Step-by-step + hardware picks + common pitfalls (300+ community notes) |
| "Is Physical Intelligence worth tracking?" | ✅ Yes | Competitive positioning + moats + risk matrix |

## Demo: Without vs With

**You ask**: "Which is better—Diffusion Policy or Flow Matching?"

| Without VLA Expert Skill | **With VLA Expert Skill** |
|---|---|
| "Both have trade-offs. Diffusion is more mature, Flow Matching is newer…" (correct but useless) | 🔴 Bull: FM hits 50Hz on π0 with 5-20 reasoning steps—engineering already favors it `[signal: §2]`<br/>🔵 Bear: FM's multimodal coverage on high-DoF bimanual tasks lags Diffusion `[inference]`<br/>🟢 Arbiter: 79% confidence → FM (calibrated to 71%). Falsifiable: if 6-month window sees Diffusion win on bimanual, drop to 60%. |

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

When activated, it doesn't just fetch knowledge—it runs a strict judgment framework:

| Mechanism | What it does | Why |
|-----------|-------------|-----|
| **Three-perspective debate** | 🔴 Bull / 🔵 Bear / 🟢 Arbiter directly attack each other | Forces blind spots into the open, improves judgment quality ([AI-Augmented Predictions](https://arxiv.org/abs/2402.07862)) |
| **Source tagging** | Every claim marked `[signal]` / `[inference]` / `[wager]` | Distinguish hard data from speculation |
| **Humility discount** | >80% confidence auto-scaled ×0.9 | LLMs overconfident in high-certainty range ([ForecastBench](https://arxiv.org/abs/2409.11839)) |
| **Falsifiability** | Every judgment includes "what would prove me wrong + deadline" | Non-falsifiable = invalid |
| **Hallucination shield** | When memory has no answer: "Not recorded" instead of making it up | Wrong numbers harm worse than admitting ignorance |

## Installation

> **Note:** Installation varies by platform. VLA Expert Skill installs as a knowledge module and doesn't interfere with existing workflow configs (like Superpowers).

### Claude Code / Cowork

```bash
git clone https://github.com/sou350121/VLA-expert-skill.git
cp -r VLA-expert-skill/skill/ your-project/.claude/skills/vla-expert/
```

Claude Code automatically activates this Skill based on conversation context—only triggers on VLA topics.

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

Start a fresh session and ask: "Diffusion Policy or Flow Matching—which is better?"—if you see 🔴🔵🟢 three-perspective debate, installation succeeded.

## Standalone vs Deep Mode

| Mode | Condition | Depth |
|------|-----------|-------|
| **Standalone** | VLA Expert Skill only | Compressed memory covers ~90% of scenarios |
| **Deep Mode** | Also clone [VLA-Handbook](https://github.com/sou350121/VLA-Handbook) | On-demand access to full paper breakdowns; 5-20× more context |

## Related Projects

| Tool | What it does | Relationship with VLA Expert Skill |
|------|-------------|-----------------------------------|
| [Superpowers](https://github.com/obra/superpowers) | Development workflow framework (spec → plan → implement → test) | **Complementary**. Superpowers manages how you code; VLA Expert Skill manages what decisions you make in VLA domain |
| [VLA-Handbook](https://github.com/sou350121/VLA-Handbook) | Complete VLA knowledge base (70+ paper breakdowns + 300+ community field notes) | **Upstream data source**. Skill knowledge is compressed from Handbook; use both together to unlock deep mode |
| Cursor Rules / .codex | Platform-level AI configuration | **Coexist**. VLA Expert Skill installs as a rule alongside your others—no conflicts |

## Daily Updates

Knowledge is synced daily via automation pipeline. Stay current:

```bash
cd VLA-expert-skill && git pull
```

## File Structure

```
VLA-expert-skill/
├── skill/
│   ├── SKILL.md                    # Skill definition (activation triggers + intent routing + debate protocol)
│   └── references/
│       └── VLA_EXPERT_MEMORY.md    # Compressed knowledge base (328+ papers, daily updates)
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
  <sub>Built on <a href="https://github.com/sou350121/VLA-Handbook">VLA-Handbook</a> · Daily-updated knowledge base · Composable domain knowledge module</sub>
</p>
