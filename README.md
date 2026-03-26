<p align="center">
  <h1 align="center">🤖 VLA Expert Skill</h1>
  <p align="center">
    <strong>一句话让你的 AI 编程助手变成 VLA 领域专家</strong><br/>
    328+ 篇论文压缩记忆 · 对抗性三视角辩论 · 每日自动更新<br/><br/>
    <img src="https://img.shields.io/badge/Claude_Code-支持-blueviolet?logo=anthropic" alt="Claude"/>
    <img src="https://img.shields.io/badge/Cursor-支持-00C7B7" alt="Cursor"/>
    <img src="https://img.shields.io/badge/Codex-支持-412991?logo=openai" alt="Codex"/>
    <img src="https://img.shields.io/badge/OpenCode-支持-333" alt="OpenCode"/>
  </p>
  <p align="center">
    <a href="https://github.com/sou350121/VLA-expert-skill/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License"/></a>
    <a href="https://github.com/sou350121/VLA-Handbook"><img src="https://img.shields.io/badge/知识来源-VLA--Handbook-orange?logo=github" alt="VLA-Handbook"/></a>
    <img src="https://img.shields.io/badge/论文覆盖-328%2B-brightgreen" alt="Papers"/>
    <img src="https://img.shields.io/badge/更新频率-每日-blueviolet" alt="Daily Update"/>
  </p>
</p>

---

## 什么是 VLA Expert Skill？

这是一个 **Claude Code / Cowork Skill**。安装后，Claude 立刻获得 VLA（Vision-Language-Action）领域的专家级判断力——不是泛泛的知识问答，而是能做**研究方向判断、论文价值评估、技术选型决策**的对抗性分析。

> 💡 **核心理念**：不给你"正确答案"，而是用 🔴 Bull（看多）/ 🔵 Bear（看空）/ 🟢 Arbiter（套利）三视角互相攻击，**逼你重新思考**。研究表明，即使有偏差的 AI 也能让人类预测准确率 +29%——机制就是**强制重新审视假设**。

### 你问 Claude，它这样回答：

| 你的问题 | 回应模式 | Claude 做什么 |
|---------|---------|-------------|
| "π0 用了什么架构？" | 🔍 **事实查询** | 直接从记忆中查找，2-5 句话搞定 |
| "Diffusion vs Flow Matching？" | ⚖️ **对比** | 对比表格 + Bull/Bear 辩论 + 判断 |
| "帮我看这篇 VLA 论文" | 📄 **论文评估** | 快筛 → 三视角辩论 → 信念更新 |
| "该投入什么方向？" | 🎯 **方向判断** | 完整辩论 + 致命实验 + 逆共识检查 |
| "怎么部署到真机？" | 🔧 **部署指南** | 工具 + 步骤 + 常见坑 |
| "PI 这家公司怎么样？" | 💼 **产业分析** | 竞争定位 + 护城河 + 风险矩阵 |
| "最近 VLA 有什么变化？" | 📰 **知识更新** | 时间线叙事：旧状态 → 新状态 |

## 知识覆盖

基于 [**VLA-Handbook**](https://github.com/sou350121/VLA-Handbook) 的 328+ 篇论文深度拆解，压缩为 ~15K tokens 的自足知识底座：

```
模型架构        RT-1 → RT-2 → Octo → OpenVLA → π0 → π0.5 → π0.6
动作生成        Diffusion Policy · Flow Matching · FAST · 自回归
训练范式        BC · Co-training · RL Post-training · 自我改进闭环
World Model    视频预测 · 物理仿真 · 决策辅助
触觉 & 多模态   力反馈 · 视触融合 · 本体感觉
部署实战        真机指南 · 300+ 社区踩坑笔记（中英文）
产业格局        PI · Figure · Tesla · NVIDIA · 智元 · 宇树 · Rhoda AI
信念网络        10 条校准置信度信念 · 5 个收敛 Phase 追踪
```

## 防幻觉 & 校准纪律

这不是一个"什么都能聊"的知识库。它有严格的自我约束：

- **来源标注**：每个论点标记 `[信号]`（有数据）/ `[推断]`（逻辑推导）/ `[投注]`（方向判断）
- **谦逊折扣**：所有 >80% 置信度自动 ×0.9（LLM 在高确定性区间系统性过度自信）
- **诚实层**：记忆中没有的数据点，说"记忆中未记录"，不编造
- **推翻条件**：每个判断附带"什么能推翻我 + 什么时候之前"

## 快速安装

> **给 LLM 的提示**：如果你是 AI 编程助手正在帮用户安装，直接看 👉 [**INSTALL.md**](INSTALL.md)，里面有你的完整安装指南。

```bash
git clone https://github.com/sou350121/VLA-expert-skill.git
```

| 平台 | 安装方式 |
|------|---------|
| **Claude Code / Cowork** | `cp -r skill/ .claude/skills/vla-expert/` |
| **Cursor** | `cp platforms/cursor/.cursorrules .cursor/rules/vla-expert.md` |
| **Codex CLI** | `codex --instructions platforms/codex/SYSTEM_PROMPT.md` |
| **OpenCode** | `cp platforms/codex/SYSTEM_PROMPT.md .opencode/instructions.md` |
| **其他工具** | 将 `SYSTEM_PROMPT.md` 作为 system prompt + 附加 `VLA_EXPERT_MEMORY.md` |

所有平台都需要 `VLA_EXPERT_MEMORY.md` 在可读取的位置。详见 [INSTALL.md](INSTALL.md)。

### 独立模式 vs 深度模式

| 模式 | 条件 | 能力 |
|------|------|------|
| **独立模式** | 只装了这个 Skill | 用压缩记忆回答，覆盖 90% 场景 |
| **深度模式** | 同时挂载 [VLA-Handbook](https://github.com/sou350121/VLA-Handbook) | 按需读取原始论文拆解，深度 5-20× |

> 🔗 推荐搭配 [**VLA-Handbook**](https://github.com/sou350121/VLA-Handbook) 使用——100 stars、70+ 篇论文深度拆解、300+ 社区实战笔记、每日自动更新的活知识库。

## 文件结构

```
VLA-expert-skill/
├── skill/                          # 核心 Skill 文件
│   ├── SKILL.md                    #   Claude Code 格式的完整 Skill 定义
│   └── references/
│       └── VLA_EXPERT_MEMORY.md    #   压缩知识库（每日更新）
├── platforms/                      # 多平台适配
│   ├── cursor/.cursorrules         #   Cursor 规则文件
│   └── codex/SYSTEM_PROMPT.md      #   Codex / OpenCode / 通用 system prompt
├── INSTALL.md                      # LLM 可读的安装指南
├── .github/workflows/              # GitHub Actions 自动化
├── CHANGELOG.md
├── LICENSE (MIT)
└── README.md
```

## 每日更新

知识库由自动化 pipeline 每日更新，追踪：

- 📄 新论文发布与突破性进展
- 📊 信念网络置信度变化
- 🔄 收敛 Phase 状态转移
- 💰 产业动态与融资事件
- 🔧 社区部署实战经验

## 相关项目

| 项目 | 描述 | Stars |
|------|------|-------|
| [**VLA-Handbook**](https://github.com/sou350121/VLA-Handbook) | 全中文、工程实战导向的 VLA 知识库。70+ 论文深度拆解，300+ 社区笔记，每日自动更新 | ![Stars](https://img.shields.io/github/stars/sou350121/VLA-Handbook?style=social) |
| **VLA-expert-skill**（本项目） | 把 Handbook 的知识压缩成 Claude Skill，一键安装即可使用 | ![Stars](https://img.shields.io/github/stars/sou350121/VLA-expert-skill?style=social) |

## License

MIT — 随意使用、修改、分发。

## Contributing

欢迎贡献！如果你有 VLA 相关的洞察、论文分析或部署经验，欢迎开 Issue 或 PR。

---

<p align="center">
  <sub>基于 <a href="https://github.com/sou350121/VLA-Handbook">VLA-Handbook</a> 构建 · 知识库每日更新 · 让 AI 帮你做更好的研究判断</sub>
</p>
