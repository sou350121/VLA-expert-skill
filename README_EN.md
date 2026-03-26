<p align="center">
  <h1 align="center">🤖 VLA Expert Skill</h1>
  <p align="center">
    <strong>Turn your AI coding assistant into a VLA domain expert — in one step</strong><br/>
    328+ papers · adversarial debate · daily updates · multi-platform<br/><br/>
    <a href="#quick-install"><img src="https://img.shields.io/badge/Claude_Code-supported-blueviolet?logo=anthropic" alt="Claude"/></a>
    <a href="#quick-install"><img src="https://img.shields.io/badge/Cursor-supported-00C7B7" alt="Cursor"/></a>
    <a href="#quick-install"><img src="https://img.shields.io/badge/Codex-supported-412991?logo=openai" alt="Codex"/></a>
    <a href="#quick-install"><img src="https://img.shields.io/badge/OpenCode-supported-333" alt="OpenCode"/></a>
  </p>
  <p align="center">
    <a href="https://github.com/sou350121/VLA-expert-skill/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License"/></a>
    <a href="https://github.com/sou350121/VLA-Handbook"><img src="https://img.shields.io/badge/Source-VLA--Handbook_⭐100+-orange?logo=github" alt="VLA-Handbook"/></a>
    <img src="https://img.shields.io/badge/Papers-328%2B-brightgreen" alt="Papers"/>
    <img src="https://img.shields.io/badge/Updates-Daily-blueviolet" alt="Daily Update"/>
  </p>
  <p align="center">
    <b>English</b> · <a href="./README.md">中文</a>
  </p>
</p>

---

## Why?

You ask your AI assistant to analyze a VLA paper — it gives you a polite, correct, but useless summary. You ask for a direction call — it hedges both ways.

**The problem isn't that AI isn't smart enough. It lacks domain knowledge and a judgment framework.**

VLA Expert Skill fixes both:

1. **Injects compressed knowledge from 328+ papers** — not summaries, but engineering details, architecture choices, and training recipes
2. **Enforces adversarial three-perspective debate** — 🔴 Bull / 🔵 Bear / 🟢 Arbiter, every judgment gets cross-attacked

> Research shows ([AI-Augmented Predictions, 2024](https://arxiv.org/abs/2402.07862)): even a biased AI improves human prediction accuracy by +29%. The mechanism isn't "AI is more accurate" — it's **forcing you to rethink**.

## Demo: Before vs After

**You ask**: "Diffusion Policy vs Flow Matching — which is better?"

| | Vanilla AI assistant | **With VLA Expert Skill** |
|---|---|---|
| Answer | "Both have pros and cons, Diffusion is more mature, Flow Matching is newer…" (correct but useless) | 🔴 Bull: FM achieves 50Hz in 5-20 steps on π0, engineering winner `[Signal: §2]`<br/>🔵 Bear: FM's multi-modal coverage on high-dim bimanual tasks lags Diffusion `[Inference]`<br/>🟢 Arbiter: 79% confidence → FM (calibrated: 71%). Kill experiment: if a Diffusion-beats-FM bimanual comparison appears within 6 months, drop to 60%. |

## What it can do

| Your question | Mode | What AI does |
|--------------|------|-------------|
| "What architecture does π0.6 use?" | 🔍 Lookup | Retrieves from 328-paper memory, 2-5 sentences |
| "Diffusion vs Flow Matching?" | ⚖️ Compare | Comparison table + Bull/Bear debate + calibrated verdict |
| "Analyze this VLA paper for me" | 📄 Paper Eval | Value filter → adversarial debate → belief update |
| "What VLA direction should I bet on?" | 🎯 Direction | Full debate + kill experiments + contrarian check + temporal arbitrage |
| "How to deploy π0 on FR3?" | 🔧 Deploy | Steps + hardware picks + common pitfalls (from 300+ field notes) |
| "How is Physical Intelligence doing?" | 💼 Business | Competitive position + moat analysis + risk matrix |
| "Preparing for VLA interviews" | 🎤 Interview | Structured answers + high-frequency topics |
| "Haven't followed VLA for 6 months" | 📰 Catch-up | Timeline narrative: old consensus → new consensus |

## Knowledge Coverage

Knowledge sourced from [**VLA-Handbook**](https://github.com/sou350121/VLA-Handbook) (⭐100+) — an engineering-focused VLA knowledge base in Chinese, with daily auto-updates.

```
Architecture     RT-1 → RT-2 → Octo → OpenVLA → π0 → π0.5 → π0.6
Action Gen       Diffusion Policy · Flow Matching · FAST Tokenization · Autoregressive
Training         Behavior Cloning · Co-training · RL Post-training · Self-improvement
World Models     Cosmos · Video prediction · Physics sim · Decision support
Tactile          TacVLA · Visuo-tactile fusion · Force feedback · Proprioception
Deployment       300+ community field notes (CN+EN) · Real-robot guides · Sim-to-Real
Industry         PI($2.4B) · Figure · Tesla Optimus · NVIDIA GR00T · AGIBOT · Unitree · Rhoda AI($4.5B)
Belief Tracking  10 calibrated beliefs (incl. contrarian) · 5 convergence phases · kill experiment deadlines
```

## Built-in Cognitive Discipline

This isn't just a RAG knowledge base. It has strict epistemic guardrails:

| Mechanism | What it does | Why |
|-----------|-------------|-----|
| **Source grading** | Every claim tagged `[Signal]` / `[Inference]` / `[Bet]` | You know what's hard data vs speculation |
| **Humility discount** | Confidence >80% auto-multiplied by 0.9 | LLMs are systematically overconfident at high certainty ([ForecastBench](https://arxiv.org/abs/2409.11839)) |
| **Conservative bias fix** | Strong evidence → min ±5% update; consensus → min ±10% | LLMs under-update beliefs ([EvolveCast](https://arxiv.org/abs/2310.15145)) |
| **Kill conditions** | Every judgment has "what would overturn this + by when" | Unfalsifiable = invalid |
| **Anti-hallucination** | If not in memory, says "not recorded" — never fabricates | A wrong specific number is worse than admitting ignorance |

## Quick Install

```bash
git clone https://github.com/sou350121/VLA-expert-skill.git
```

| Platform | One-liner |
|----------|----------|
| **Claude Code / Cowork** | `cp -r VLA-expert-skill/skill/ .claude/skills/vla-expert/` |
| **Cursor** | `cp VLA-expert-skill/platforms/cursor/.cursorrules .cursor/rules/vla-expert.md` |
| **Codex CLI** | `codex --instructions VLA-expert-skill/platforms/codex/SYSTEM_PROMPT.md` |
| **OpenCode** | `cp VLA-expert-skill/platforms/codex/SYSTEM_PROMPT.md .opencode/instructions.md` |
| **Any LLM tool** | Use `SYSTEM_PROMPT.md` as system prompt + attach `VLA_EXPERT_MEMORY.md` |

> AI self-install: have your AI assistant read [INSTALL.md](INSTALL.md) — it will detect its environment and install automatically.

### Verify installation

Ask: "Diffusion Policy vs Flow Matching?" — if the answer shows 🔴🔵🟢 three-perspective debate, you're good.

### Standalone vs Deep Mode

| Mode | Requirement | Depth |
|------|------------|-------|
| **Standalone** | Just this Skill | Compressed memory covers 90% of scenarios |
| **Deep** | Also clone [VLA-Handbook](https://github.com/sou350121/VLA-Handbook) | On-demand access to full paper dissections, 5-20× more detail |

## Daily Updates

The knowledge base is auto-synced daily, tracking: new papers & breakthroughs, belief confidence shifts, convergence phase transitions, industry moves & funding, community deployment experiences.

Stay current:
```bash
cd VLA-expert-skill && git pull
```

## File Structure

```
VLA-expert-skill/
├── skill/
│   ├── SKILL.md                    # Full Skill definition (routing + 8 modes + debate protocol)
│   └── references/
│       └── VLA_EXPERT_MEMORY.md    # Compressed knowledge base (328+ papers, daily updates)
├── platforms/
│   ├── cursor/.cursorrules         # Cursor Rules adapter
│   └── codex/SYSTEM_PROMPT.md      # Codex / OpenCode / generic system prompt
├── INSTALL.md                      # LLM-readable self-install guide
├── .github/workflows/              # GitHub Actions automation
└── README.md / README_EN.md
```

## Related Projects

| Project | Description |
|---------|-------------|
| [**VLA-Handbook**](https://github.com/sou350121/VLA-Handbook) ⭐100+ | The knowledge source for this Skill. Full Chinese VLA knowledge base: 70+ paper dissections, 300+ community field notes, daily auto-updates. **Recommended for Deep Mode.** |

## License

[MIT](LICENSE) — use, modify, distribute freely.

## Contributing

Contributions welcome! Paper analyses, deployment experiences, bug reports — please open an Issue or PR.

---

<p align="center">
  <sub>Built on <a href="https://github.com/sou350121/VLA-Handbook">VLA-Handbook</a> · Knowledge base updated daily · Let AI help you make better research decisions</sub>
</p>
