<p align="center">
  <h1 align="center">🤖 VLA Expert Skill</h1>
  <p align="center">
    <strong>一键让你的 AI 编程助手变成 VLA 领域专家</strong><br/>
    328+ 篇论文 · 对抗性辩论 · 每日更新 · 多平台支持<br/><br/>
    <a href="#快速安装"><img src="https://img.shields.io/badge/Claude_Code-支持-blueviolet?logo=anthropic" alt="Claude"/></a>
    <a href="#快速安装"><img src="https://img.shields.io/badge/Cursor-支持-00C7B7" alt="Cursor"/></a>
    <a href="#快速安装"><img src="https://img.shields.io/badge/Codex-支持-412991?logo=openai" alt="Codex"/></a>
    <a href="#快速安装"><img src="https://img.shields.io/badge/OpenCode-支持-333" alt="OpenCode"/></a>
  </p>
  <p align="center">
    <a href="https://github.com/sou350121/VLA-expert-skill/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License"/></a>
    <a href="https://github.com/sou350121/VLA-Handbook"><img src="https://img.shields.io/badge/知识来源-VLA--Handbook_⭐100+-orange?logo=github" alt="VLA-Handbook"/></a>
    <img src="https://img.shields.io/badge/论文-328%2B_篇-brightgreen" alt="Papers"/>
    <img src="https://img.shields.io/badge/更新-每日自动-blueviolet" alt="Daily Update"/>
  </p>
  <p align="center">
    <a href="./README_EN.md">English</a> · <b>中文</b>
  </p>
</p>

---

## 为什么需要这个？

你让 AI 助手帮你分析 VLA 论文，它给你一堆正确但没用的废话。你问它方向判断，它两边都说好。

**问题不是 AI 不够聪明，是它没有领域知识 + 没有判断框架。**

VLA Expert Skill 解决这两件事：

1. **注入 328+ 篇论文的压缩知识**——不是摘要，是拆解后的工程细节、架构选择、训练配方
2. **强制三视角对抗辩论**——🔴 看多 / 🔵 看空 / 🟢 套利，每个判断都被交叉攻击

> 研究表明（[AI-Augmented Predictions, 2024](https://arxiv.org/abs/2402.07862)）：即使有偏差的 AI 也能让人类预测准确率 +29%。机制不是"AI 更准"，而是**强制你重新思考**。

## Demo：安装前 vs 安装后

**你问**：「Diffusion Policy 和 Flow Matching 哪个更好？」

| | 普通 AI 助手 | **装了 VLA Expert Skill** |
|---|---|---|
| 回答 | "两者各有优劣，Diffusion 更成熟，Flow Matching 更新…"（正确的废话） | 🔴 Bull：FM 在 π0 上 5-20 步推理达 50Hz，工程上已胜出 `[信号: §2]`<br/>🔵 Bear：FM 在高维双臂任务上的多模态覆盖不如 Diffusion `[推断]`<br/>🟢 Arbiter：79% 置信度选 FM（校准后 71%）。致命实验：如果 6 个月内出现 Diffusion 在 bimanual 上显著胜出的对比实验，降至 60%。 |

## 它能做什么

| 你的问题 | 回应模式 | AI 做什么 |
|---------|---------|----------|
| "π0.6 用了什么架构？" | 🔍 事实查询 | 直接从 328 篇论文记忆中查找，2-5 句 |
| "Diffusion vs Flow Matching？" | ⚖️ 对比 | 对比表格 + Bull/Bear 辩论 + 校准判断 |
| "帮我看这篇 VLA 论文" | 📄 论文评估 | 信息价值快筛 → 三视角辩论 → 信念更新 |
| "VLA 下一步该投什么方向？" | 🎯 方向判断 | 完整辩论 + 致命实验 + 逆共识 + 时间套利 |
| "怎么在 FR3 上部署 π0？" | 🔧 部署 | 步骤 + 硬件选型 + 常见坑（来自 300+ 社区笔记） |
| "Physical Intelligence 怎么样？" | 💼 产业 | 竞争定位 + 护城河 + 风险矩阵 |
| "VLA 面试怎么准备？" | 🎤 面试 | 结构化答案 + 高频考点 |
| "我半年没关注了，有什么变化？" | 📰 追赶 | 时间线叙事：旧共识 → 新共识 |

## 知识覆盖

知识来自 [**VLA-Handbook**](https://github.com/sou350121/VLA-Handbook)（⭐100+）——全中文、工程实战导向的 VLA 知识库。

```
模型架构演化     RT-1 → RT-2 → Octo → OpenVLA → π0 → π0.5 → π0.6
动作生成三范式   Diffusion Policy · Flow Matching · FAST Tokenization · 自回归
训练范式        Behavior Cloning · Co-training · RL Post-training · 自我改进闭环
World Model    Cosmos · 视频预测 · 物理仿真 · 决策辅助
触觉 & 多模态   TacVLA · 视触融合 · 力反馈 · 本体感觉
部署实战        300+ 中英文社区踩坑笔记 · 真机部署指南 · Sim-to-Real
产业格局        PI($2.4B) · Figure · Tesla Optimus · NVIDIA GR00T · 智元 · 宇树 · Rhoda AI($4.5B)
信念追踪系统     10 条校准信念（含逆共识） · 5 个收敛 Phase · 致命实验截止日
```

## 内置的纪律（不只是知识库）

普通 RAG 只是"检索+回答"。这个 Skill 有严格的认知纪律：

| 机制 | 做什么 | 为什么 |
|------|--------|--------|
| **来源分级** | 每个论点标 `[信号]` / `[推断]` / `[投注]` | 你知道哪些是硬数据、哪些是推测 |
| **谦逊折扣** | >80% 置信度自动 ×0.9 | LLM 在高确定性区间系统性过度自信 ([ForecastBench](https://arxiv.org/abs/2409.11839)) |
| **保守偏误修正** | 强证据最小更新 ±5%，共识更新 ±10% | LLM 信念更新幅度系统性不足 ([EvolveCast](https://arxiv.org/abs/2310.15145)) |
| **推翻条件** | 每个判断附带"什么能推翻 + 截止日期" | 不可证伪 = 无效判断 |
| **防幻觉** | 记忆中没有就说"未记录"，不编造 | 具体的错误数字比承认不知道更有害 |

## 快速安装

```bash
git clone https://github.com/sou350121/VLA-expert-skill.git
```

| 平台 | 一行安装 |
|------|---------|
| **Claude Code / Cowork** | `cp -r VLA-expert-skill/skill/ .claude/skills/vla-expert/` |
| **Cursor** | `cp VLA-expert-skill/platforms/cursor/.cursorrules .cursor/rules/vla-expert.md` |
| **Codex CLI** | `codex --instructions VLA-expert-skill/platforms/codex/SYSTEM_PROMPT.md` |
| **OpenCode** | `cp VLA-expert-skill/platforms/codex/SYSTEM_PROMPT.md .opencode/instructions.md` |
| **任何 LLM 工具** | 用 `SYSTEM_PROMPT.md` 作为 system prompt，附加 `VLA_EXPERT_MEMORY.md` |

> AI 助手自助安装：让你的 AI 读 [INSTALL.md](INSTALL.md)，它会自己判断环境并完成安装。

### 验证安装

问一句：「Diffusion Policy 和 Flow Matching 哪个更好？」——如果回答出现 🔴🔵🟢 三视角辩论，安装成功。

### 独立模式 vs 深度模式

| 模式 | 条件 | 深度 |
|------|------|------|
| **独立模式** | 只装 VLA Expert Skill | 压缩记忆覆盖 90% 场景 |
| **深度模式** | 同时 clone [VLA-Handbook](https://github.com/sou350121/VLA-Handbook) | 按需读取原始论文拆解，信息量 5-20× |

## 每日更新

知识库由自动化 pipeline 每日同步，追踪：新论文与突破、信念网络置信度变化、收敛 Phase 转移、产业动态与融资、社区部署经验。

保持最新：
```bash
cd VLA-expert-skill && git pull
```

## 文件结构

```
VLA-expert-skill/
├── skill/
│   ├── SKILL.md                    # 完整 Skill 定义（意图路由 + 8 种模式 + 辩论协议）
│   └── references/
│       └── VLA_EXPERT_MEMORY.md    # 压缩知识库（328+ 论文，每日更新）
├── platforms/
│   ├── cursor/.cursorrules         # Cursor Rules 适配
│   └── codex/SYSTEM_PROMPT.md      # Codex / OpenCode / 通用 system prompt
├── INSTALL.md                      # LLM 可读的自助安装指南
├── .github/workflows/              # GitHub Actions 自动化
└── README.md / README_EN.md
```

## 相关项目

| 项目 | 描述 |
|------|------|
| [**VLA-Handbook**](https://github.com/sou350121/VLA-Handbook) ⭐100+ | 本 Skill 的知识来源。全中文 VLA 知识库：70+ 论文深度拆解、300+ 社区踩坑笔记、每日自动更新。**推荐搭配使用获得深度模式。** |

## License

[MIT](LICENSE) — 随意使用、修改、分发。

## Contributing

欢迎贡献！论文分析、部署经验、Bug 报告，请开 Issue 或 PR。

---

<p align="center">
  <sub>基于 <a href="https://github.com/sou350121/VLA-Handbook">VLA-Handbook</a> 构建 · 知识库每日更新 · 让 AI 帮你做更好的研究判断</sub>
</p>
