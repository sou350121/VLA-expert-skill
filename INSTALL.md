# VLA Expert Skill — LLM 安装指南

> **给 LLM 的说明**：你正在帮用户安装 VLA Expert Skill。请先判断你所在的环境，然后按对应方式完成安装。

## Step 1：判断你的环境

检查以下信号判断你在哪个平台：

| 信号 | 平台 | 安装路径 |
|------|------|---------|
| 你能访问 `.claude/` 目录或看到 `SKILL.md` frontmatter | **Claude Code / Cowork** | → Step 2A |
| 你能访问 `.cursor/rules/` 或 `.cursorrules` | **Cursor** | → Step 2B |
| 你在 Codex CLI / OpenCode / Aider 等终端工具中 | **Codex / OpenCode / 其他** | → Step 2C |
| 你不确定 | **通用方式** | → Step 2D |

## Step 2A：Claude Code / Cowork

```bash
# 1. Clone repo
git clone https://github.com/sou350121/VLA-expert-skill.git

# 2. 复制 skill 文件到项目
mkdir -p .claude/skills/vla-expert/references
cp VLA-expert-skill/skill/SKILL.md .claude/skills/vla-expert/
cp VLA-expert-skill/skill/references/VLA_EXPERT_MEMORY.md .claude/skills/vla-expert/references/

# 3. 验证
ls .claude/skills/vla-expert/
# 应该看到：SKILL.md 和 references/VLA_EXPERT_MEMORY.md
```

安装完成后，用户对话中提到 VLA 相关问题时，你会自动加载这个 Skill。

## Step 2B：Cursor

```bash
# 1. Clone repo
git clone https://github.com/sou350121/VLA-expert-skill.git

# 2. 复制规则文件
mkdir -p .cursor/rules
cp VLA-expert-skill/platforms/cursor/.cursorrules .cursor/rules/vla-expert.md

# 3. 复制知识库
mkdir -p docs
cp VLA-expert-skill/skill/references/VLA_EXPERT_MEMORY.md docs/

# 4. 验证
cat .cursor/rules/vla-expert.md | head -5
```

或者更简单——直接在 Cursor Settings → Rules 中添加：
1. 打开 Cursor → Settings → Rules for AI
2. 粘贴 `platforms/cursor/.cursorrules` 的内容
3. 将 `VLA_EXPERT_MEMORY.md` 放在项目根目录或 `docs/` 下

## Step 2C：Codex / OpenCode / Aider

这些工具通常支持 system prompt 或 instructions 文件：

**Codex CLI：**
```bash
# 将 SYSTEM_PROMPT.md 设为 codex 的 instructions
cp VLA-expert-skill/platforms/codex/SYSTEM_PROMPT.md codex-instructions.md

# 运行时指定
codex --instructions codex-instructions.md
```

**OpenCode：**
```bash
# OpenCode 使用 .opencode/instructions.md
mkdir -p .opencode
cp VLA-expert-skill/platforms/codex/SYSTEM_PROMPT.md .opencode/instructions.md
```

**Aider：**
```bash
# Aider 使用 .aider.conf.yml 或 --system-prompt
cp VLA-expert-skill/platforms/codex/SYSTEM_PROMPT.md .aider.prompt.md
aider --read .aider.prompt.md
```

**所有平台通用**：确保 `VLA_EXPERT_MEMORY.md` 在项目中可被 LLM 读取。

## Step 2D：通用方式（任何支持 system prompt 的工具）

1. 将 `platforms/codex/SYSTEM_PROMPT.md` 的内容复制为 system prompt
2. 将 `skill/references/VLA_EXPERT_MEMORY.md` 作为上下文/附件传入
3. 开始对话

## Step 3：验证安装

安装后问一句测试：

> "Diffusion Policy 和 Flow Matching 哪个更好？"

如果回答中出现 🔴 Bull / 🔵 Bear / 🟢 Arbiter 三视角辩论，说明安装成功。

## 保持更新

知识库每日更新。定期拉取最新版本：

```bash
cd VLA-expert-skill
git pull
# 然后重新复制 VLA_EXPERT_MEMORY.md 到对应位置
```

---

📚 知识来源：[VLA-Handbook](https://github.com/sou350121/VLA-Handbook)（70+ 论文深度拆解，300+ 社区笔记）
