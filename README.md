# VLA Expert Skill

> A Claude Code / Cowork skill that gives Claude deep expert knowledge in **Vision-Language-Action (VLA)** — the frontier of embodied AI.

## What is this?

This skill turns Claude into a VLA domain expert backed by a compressed knowledge base distilled from **328+ research papers**, industry analyses, and weekly tracking reports. It covers:

- **Model architectures**: RT-2, OpenVLA, π0 series, GR-2, etc.
- **Action generation paradigms**: Diffusion Policy, Flow Matching, FAST tokenization
- **Training paradigms**: Behavior Cloning, Co-training, RL post-training
- **Emerging frontiers**: World Models, Tactile sensing, Sim-to-Real, Dexterous manipulation
- **Industry landscape**: Physical Intelligence, Figure, Tesla Optimus, NVIDIA GR00T, Unitree, AGIBOT, etc.
- **Deployment**: Real-robot deployment guides, community field notes

## Key Features

- **Adversarial Triad Debate** (🔴 Bull / 🔵 Bear / 🟢 Arbiter) for every major judgment
- **Calibration discipline**: Confidence scores with humility discounts and falsifiability deadlines
- **Anti-hallucination protocol**: Source-level attribution (`[Signal]` / `[Inference]` / `[Bet]`)
- **8 response modes**: Lookup, Compare, Paper Eval, Direction, Deploy, Business, Interview, Catch-up
- **Daily updates**: Knowledge base refreshed daily with latest papers and industry signals

## Installation

### For Claude Code users

```bash
# Clone this repo
git clone https://github.com/sou350121/vla-expert-skill.git

# Copy to your project's .claude/skills/ directory
cp -r vla-expert-skill/skill/ your-project/.claude/skills/vla-expert/
```

### For Cowork users

Place the skill files in your Cowork workspace's `.claude/skills/vla-expert/` directory.

## File Structure

```
vla-expert-skill/
├── skill/
│   ├── SKILL.md                    # Skill definition + routing logic
│   └── references/
│       └── VLA_EXPERT_MEMORY.md    # Compressed knowledge base (328+ papers)
├── .github/
│   └── workflows/
│       └── daily-update.yml        # GitHub Actions: daily sync placeholder
├── CHANGELOG.md                    # Update history
├── LICENSE
└── README.md
```

## Knowledge Base Coverage

| Section | Topics | Depth |
|---------|--------|-------|
| §0 What is VLA | Core concept, I/O, promise | Overview |
| §1 Architecture Timeline | RT-1 → π0.6, key inflection points | Detailed |
| §2 Action Generation | Diffusion, Flow Matching, FAST, Autoregressive | Deep |
| §3 Training Paradigms | BC, Co-training, RL, Self-improvement | Deep |
| §4 Belief Network | 10 conditional beliefs with calibrated confidence | Analytical |
| §5 Convergence Map | 5-phase tracking with critical thresholds | Analytical |
| §6 Tactile & Multi-modal | Tactile sensing, force feedback, multi-modal fusion | Moderate |
| §7 Deployment | Real-robot guides, community field notes | Practical |
| §8 Industry | Company profiles, competitive dynamics, moats | Moderate |
| §9-15 | Hot topics, interview prep, calibration | Various |

## Usage Examples

Once installed, just talk to Claude naturally:

- *"Diffusion Policy vs Flow Matching，哪个更好？"* → COMPARE mode with Bull/Bear debate
- *"帮我看这篇 VLA 论文"* → PAPER_EVAL mode with belief update
- *"VLA 下一步该投入什么方向？"* → DIRECTION mode with full adversarial debate
- *"π0 用了什么架构？"* → LOOKUP mode, concise answer
- *"Physical Intelligence 这家公司怎么样？"* → BUSINESS mode with moat analysis

## Daily Updates

The `VLA_EXPERT_MEMORY.md` knowledge base is updated daily to track:
- New paper releases and breakthroughs
- Belief network confidence shifts
- Convergence phase transitions
- Industry moves and funding events
- Community deployment experiences

## License

MIT License — see [LICENSE](LICENSE) for details.

## Contributing

Contributions welcome! If you have VLA-related insights, paper analyses, or deployment experiences to share, please open an issue or PR.

---

*Built with the [VLA Handbook](https://github.com/sou350121/vla-expert-skill) research system. Knowledge base version updated daily.*
