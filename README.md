<p align="center">
  <h1 align="center">🤖 VLA Expert Skill</h1>
  <p align="center">
    <strong>给你的 AI 助手注入 VLA 领域专家知识</strong><br/>
    可组合的领域知识模块 · 按需激活 · 不干扰你的开发流程<br/><br/>
    <a href="#安装"><img src="https://img.shields.io/badge/Claude_Code-支持-blueviolet?logo=anthropic" alt="Claude"/></a>
    <a href="#安装"><img src="https://img.shields.io/badge/Cursor-支持-00C7B7" alt="Cursor"/></a>
    <a href="#安装"><img src="https://img.shields.io/badge/Codex-支持-412991?logo=openai" alt="Codex"/></a>
    <a href="#安装"><img src="https://img.shields.io/badge/OpenCode-支持-333" alt="OpenCode"/></a>
  </p>
  <p align="center">
    <a href="https://github.com/sou350121/VLA-expert-skill/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License"/></a>
    <a href="https://github.com/sou350121/VLA-Handbook"><img src="https://img.shields.io/badge/知识来源-VLA--Handbook_⭐100+-orange?logo=github" alt="VLA-Handbook"/></a>
    <img src="https://img.shields.io/badge/论文-332%2B_篇-brightgreen" alt="Papers"/>
    <img src="https://img.shields.io/badge/更新-每日自动-blueviolet" alt="Daily Update"/>
  </p>
  <p align="center">
    <a href="./README_EN.md">English</a> · <b>中文</b>
  </p>
</p>

---

## 这是什么

VLA Expert Skill 是一个**可组合的领域知识模块**——它不管理你的开发流程，不替代你的 workflow 工具。它只做一件事：

**当你的 AI 助手遇到 VLA（Vision-Language-Action）相关问题时，给它专家级的判断力。**

平时它安静地待着。当你问到 VLA 架构选型、论文价值、方向判断、部署踩坑时，它被激活，提供基于 332+ 篇论文的深度分析，然后交还控制权。

> 💡 它和 [Superpowers](https://github.com/obra/superpowers) 这类开发流程框架是**互补关系**：Superpowers 管你**怎么写代码**，VLA Expert Skill 管你**在 VLA 领域做什么决策**。两者可以同时安装，互不干扰。

## 什么时候会被激活

| 你说的话 | 激活？ | 做什么 |
|---------|--------|--------|
| "帮我重构这个 Python 模块" | ❌ 不激活 | 这是开发流程的事，交给你的 workflow 工具 |
| "π0.6 的 action head 用了什么？" | ✅ QUICK | 从记忆中查找，2-5 句话直接回答 |
| "Diffusion vs Flow Matching 选哪个？" | ✅ DEEP | 双向取证 + 对抗性思考 + 可操作建议 |
| "帮我看这篇 VLA 论文值不值得读" | ✅ DEEP | 快筛（改变信念吗？）→ 值得则展开分析 |
| "写个单元测试" | ❌ 不激活 | 开发任务，不是领域知识 |
| "VLA 下一步该赌哪个方向？" | ✅ DEEP | 论述 + 可操作建议 + 什么信号出现就该撤 |
| "怎么在 FR3 上部署 π0？" | ✅ QUICK | 步骤 + 硬件选型 + 常见坑（300+ 社区笔记） |
| "Physical Intelligence 值不值得关注？" | ✅ DEEP | 竞争定位 + 风险 + 判断 |

## Demo：有 vs 没有

**你问**：「Diffusion Policy 和 Flow Matching 哪个更好？」

| 没有 VLA Expert Skill | **有 VLA Expert Skill** |
|---|---|
| "两者各有优劣，Diffusion 更成熟，Flow Matching 更新…"（正确的废话） | FM 在 π0 上 5-20 步推理达 50Hz，工程上已胜出 `[事实: §2]`。但 FM 在高维双臂任务上的多模态覆盖尚未被充分验证 `[推断]`。**判断**：当前证据偏向 FM，但如果 6 个月内出现 Diffusion 在 bimanual 上显著胜出的对比实验，这个判断需要修正。搭配 VLA-Handbook 深度模式可读完整 Diffusion Policy 和 Flow Matching 的论文拆解。 |

## v3 升级：思考纪律 > 输出模板

v2 把 54% 的指令预算花在格式合规上（强制三视角、×0.9 校准算术、7 个输出模板）。v3 砍掉了这些，把上下文还给推理。

| v2 | v3 |
|---|---|
| 8 种意图路由 | 2 种：QUICK / DEEP |
| 7 个输出模板 | 格式跟着内容走，不硬套 |
| 强制 🔴🔵🟢 三视角输出 | 对抗性思考是内在纪律，不是表演 |
| 全量加载记忆（~16K tokens） | Source Map 行号索引，选择性加载 |
| 引用 3 个不存在的文件 | 已清理，只引用真实存在的文件 |

**核心不变**：对抗性思考、防幻觉、可证伪判断、诚实标注来源。

## 知识覆盖

知识来自 [**VLA-Handbook**](https://github.com/sou350121/VLA-Handbook)（⭐100+），压缩为按需激活的领域记忆：

```
模型架构演化     RT-1 → RT-2 → Octo → OpenVLA → π0 → π0.5 → π0.6
动作生成范式     Diffusion Policy · Flow Matching · FAST Tokenization · 自回归
训练范式        Behavior Cloning · Co-training · RL Post-training · 自我改进闭环
World Model    Cosmos · 视频预测 · 物理仿真 · 决策辅助
触觉 & 多模态   TacVLA · 视触融合 · 力反馈 · 本体感觉
部署实战        300+ 中英文社区踩坑笔记 · 真机部署指南 · Sim-to-Real
产业格局        PI($2.4B) · Figure · Tesla Optimus · NVIDIA GR00T · 智元 · 宇树 · Rhoda AI($4.5B)
信念追踪系统     10 条校准信念（含逆共识） · 5 个收敛 Phase · 致命实验截止日
```

## 内置认知纪律

激活时不只是查知识库，还有严格的思考纪律：

| 机制 | 做什么 | 为什么 |
|------|--------|--------|
| **双向取证** | 先找支持证据，再找反对证据，两者都被认真考虑 | 单向论证容易自我说服 |
| **来源分级** | 关键声明标 `[事实]` / `[推断]` / `[判断]` | 区分硬数据和推测 |
| **可证伪** | 每个重要判断附带"什么能推翻 + 什么时候之前" | 不可证伪 = 无效判断 |
| **分歧诚实** | 支持≈反对时标注为高信号分歧点，不和稀泥 | 假共识比承认不确定更有害 |
| **防幻觉** | 记忆中没有就说"未记录"，不编造 | 错误数字比承认不知道更有害 |

## 安装

> **Note:** 安装方式因平台而异。VLA Expert Skill 作为知识模块安装，不影响你已有的开发流程配置。

### Claude Code / Cowork

```bash
git clone https://github.com/sou350121/VLA-expert-skill.git
cp -r VLA-expert-skill/skill/ your-project/.claude/skills/vla-expert/
```

Claude Code 会根据对话内容自动判断是否激活——只在涉及 VLA 话题时触发。

### Cursor

```bash
git clone https://github.com/sou350121/VLA-expert-skill.git
mkdir -p .cursor/rules
cp VLA-expert-skill/platforms/cursor/.cursorrules .cursor/rules/vla-expert.md
cp VLA-expert-skill/skill/references/VLA_EXPERT_MEMORY.md docs/
```

### Codex

告诉 Codex：

```
Fetch and follow instructions from https://raw.githubusercontent.com/sou350121/VLA-expert-skill/main/platforms/codex/SYSTEM_PROMPT.md
```

详细文档：[platforms/codex/SYSTEM_PROMPT.md](platforms/codex/SYSTEM_PROMPT.md)

### OpenCode

告诉 OpenCode：

```
Fetch and follow instructions from https://raw.githubusercontent.com/sou350121/VLA-expert-skill/main/platforms/codex/SYSTEM_PROMPT.md
```

或手动安装：

```bash
git clone https://github.com/sou350121/VLA-expert-skill.git
mkdir -p .opencode
cp VLA-expert-skill/platforms/codex/SYSTEM_PROMPT.md .opencode/instructions.md
```

### 其他 AI 工具

将 [`platforms/codex/SYSTEM_PROMPT.md`](platforms/codex/SYSTEM_PROMPT.md) 的内容作为 system prompt，并附加 [`skill/references/VLA_EXPERT_MEMORY.md`](skill/references/VLA_EXPERT_MEMORY.md) 作为上下文。

### 验证安装

启动新会话，问：「Diffusion Policy 和 Flow Matching 哪个更好？」——如果回答包含具体论文证据、对立面分析、以及可证伪条件，安装成功。

### 独立模式 vs 深度模式

| 模式 | 条件 | 深度 |
|------|------|------|
| **独立模式** | 只装 VLA Expert Skill | 压缩记忆覆盖 90% 场景 |
| **深度模式** | 同时 clone [VLA-Handbook](https://github.com/sou350121/VLA-Handbook) | 按需读取原始论文拆解，信息量 5-20× |

## 与其他工具的关系

| 工具 | 它做什么 | 和 VLA Expert Skill 的关系 |
|------|---------|---------------------------|
| [Superpowers](https://github.com/obra/superpowers) | 开发流程框架（spec → plan → implement → test） | **互补**。Superpowers 管怎么写代码，VLA Expert Skill 管 VLA 领域该做什么 |
| [VLA-Handbook](https://github.com/sou350121/VLA-Handbook) | 完整的 VLA 知识库（70+ 论文拆解 + 300+ 社区笔记） | **上游数据源**。Skill 的知识从 Handbook 压缩而来，搭配使用可解锁深度模式 |
| Cursor Rules / .codex | 平台级 AI 配置 | **共存**。VLA Expert Skill 作为一条规则安装，不覆盖你的其他规则 |

## 每日更新

知识库由自动化 pipeline 每日同步。保持最新：

```bash
cd VLA-expert-skill && git pull
```

## 文件结构

```
VLA-expert-skill/
├── skill/
│   ├── SKILL.md                    # Skill 指令（意图分类 + 思考纪律 + 防幻觉）
│   └── references/
│       └── VLA_EXPERT_MEMORY.md    # 压缩知识库（332+ 论文，每日更新，含行号索引）
├── platforms/
│   ├── cursor/.cursorrules         # Cursor Rules 适配
│   └── codex/SYSTEM_PROMPT.md      # Codex / OpenCode / 通用 system prompt
├── INSTALL.md                      # LLM 可读的自助安装指南
├── .github/workflows/              # GitHub Actions 自动化
└── README.md / README_EN.md
```

## License

[MIT](LICENSE) — 随意使用、修改、分发。

## Contributing

欢迎贡献！论文分析、部署经验、Bug 报告，请开 Issue 或 PR。

---

<p align="center">
  <sub>基于 <a href="https://github.com/sou350121/VLA-Handbook">VLA-Handbook</a> 构建 · 知识库每日更新 · v3：思考纪律 > 输出模板</sub>
</p>
