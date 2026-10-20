# VLA Expert Skill

[English](README_EN.md) · 中文

用已發布的 [VLA Handbook](https://github.com/sou350121/VLA-Handbook) 來源支援 VLA 論文、架構、部署與產業判斷。按問題讀取證據，不接管你的開發流程。

## 現行知識與歷史快照

- [當前來源導覽](skill/references/HANDBOOK_CURRENT.md)：來源提交、涵蓋範圍及 DeepSeek 閱讀建議。
- [完整來源索引](skill/references/HANDBOOK_INDEX.md)：理論、公司、雙周報與部署頁；每個連結固定到上游提交。
- [逐檔清單](skill/references/handbook-manifest.json)：實際檔案計數、內容 SHA、來源 commit。
- [歷史專家記憶](skill/references/VLA_EXPERT_MEMORY.md)：保留舊版內容；信念機率、相變百分比、估值及預測並未因同步重新校準。

「理論 Markdown 檔數」與「論文拆解檔數」是不同口徑，不能當成獨立論文篇數。同步日期也不代表所有論文已重新查核。產業頁的自報、補錄與覆蓋缺口須照原文保留。

## 如何使用

| 問題 | 處理 |
|---|---|
| 某個模型的 action head、訓練配方 | 找對版本，簡短回答並引用支持它的來源 |
| Diffusion Policy 與 Flow Matching 選型 | 對照任務、控制頻率、action chunk、推理成本與評估條件 |
| 論文是否值得讀、方向是否值得投入 | 分析機制、最強正反證據、失效條件及可推翻判斷的訊號 |
| 公司、發布或部署消息 | 區分公告、規劃、交付與獨立驗證，不把不同指標當可比結果 |
| 一般重構、寫測試、無關話題 | 保持原開發流程，不啟動本模組 |

QUICK 問題簡短答；DEEP 問題依內容決定形式。沒有強制三視角演出，也沒有機械式信心折扣。記憶裡有一句話不代表它已被證實；找不到來源就明示未核。

## 安裝

完整說明見 [INSTALL.md](INSTALL.md)。請複製完整 `skill/`，不要只複製舊記憶檔。

Codex 的專案安裝示例（在目標專案執行，先確認沒有同名技能）：

```bash
git clone https://github.com/sou350121/VLA-expert-skill.git
mkdir -p .agents/skills
cp -r VLA-expert-skill/skill .agents/skills/vla-expert
```

Claude Code 使用 `.claude/skills/vla-expert/`；Cursor 及其他工具使用 [平台轉接說明](platforms/codex/SYSTEM_PROMPT.md) 和完整參考檔。既有規則與本地修改須保留；複製安裝後，原 clone 的 `git pull` 不會自動更新安裝副本。

## 自動更新

伺服器沿用每日 **20:00（Asia/Shanghai）** 排程，不依賴本機或 Codex 開著。

1. 鎖定單次執行，檢查乾淨工作區及 GitHub；錯誤明確失敗，不以「沒有更新」掩蓋。
2. 讀取已發布的 Handbook 提交，全量同步入口，沒有按日期或前若干篇截斷。
3. 有新導覽證據時，現有 DeepSeek 產生有限閱讀建議；引用必須是來源節選的逐字子字串，不接受無來源數字或網址。不使用其他模型供應商。
4. 核驗完整清單與生成檔，只提交三份當前來源產物，推送後回讀 SHA。歷史記憶與人工正文不由日更改寫。

GitHub Actions 沿用每日檢查時間，核對固定版本上游及生成產物，不再從舊 `updates` 分支覆蓋內容。失敗保持告警；同步完整不等於上游所有來源完整。

## 開發驗證

```bash
python -m unittest discover -s scripts -p 'test_*.py'
python scripts/build-expert-memory.py --handbook /path/to/VLA-Handbook --check
```

程式、路由或發布流程修改仍須維護者批准。自動產物的有限維護範圍見 [AGENTS.md](AGENTS.md)。

[MIT](LICENSE) · [更新記錄](CHANGELOG.md)
