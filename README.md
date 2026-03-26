# VLA Expert Skill

> 讓 Claude 成為 **Vision-Language-Action (VLA)** 領域的深度研究專家。基於 328+ 篇論文的壓縮知識庫，搭配對抗性三視角辯論協議。

## 這是什麼？

這是一個 Claude Code / Cowork 的 Skill，安裝後 Claude 會獲得 VLA（具身智能）領域的專家級知識，涵蓋：

- **模型架構**：RT-2、OpenVLA、π0 系列、GR-2 等
- **動作生成範式**：Diffusion Policy、Flow Matching、FAST Tokenization
- **訓練範式**：Behavior Cloning、Co-training、RL Post-training
- **前沿方向**：World Model、觸覺感知、Sim-to-Real、靈巧操作
- **產業格局**：Physical Intelligence、Figure、Tesla Optimus、NVIDIA GR00T、智元、宇樹等
- **部署實戰**：真機部署指南、社區踩坑筆記

## 核心特色

- **對抗性三視角辯論**（🔴 Bull 看多 / 🔵 Bear 看空 / 🟢 Arbiter 套利）— 每個重要判斷都經過交叉檢驗
- **校準紀律**：置信度自動謙遜折扣，高確定性區間額外謹慎
- **防幻覺協議**：所有事實性聲明標注來源級別（`[信號]` / `[推斷]` / `[投注]`）
- **8 種回應模式**：事實查詢、對比、論文評估、方向判斷、部署、產業分析、面試、知識更新
- **每日更新**：知識庫追蹤最新論文與產業動態

## 安裝方式

### Claude Code 用戶

```bash
# Clone 這個 repo
git clone https://github.com/sou350121/VLA-expert-skill.git

# 複製到你的專案 .claude/skills/ 目錄
cp -r VLA-expert-skill/skill/ your-project/.claude/skills/vla-expert/
```

### Cowork 用戶

將 `skill/` 資料夾放到你的 Cowork 工作區的 `.claude/skills/vla-expert/` 目錄下。

## 文件結構

```
VLA-expert-skill/
├── skill/
│   ├── SKILL.md                    # Skill 定義 + 意圖路由邏輯
│   └── references/
│       └── VLA_EXPERT_MEMORY.md    # 壓縮知識庫（328+ 篇論文）
├── .github/
│   └── workflows/
│       └── daily-update.yml        # GitHub Actions 每日更新
├── scripts/
│   └── sync-to-github.ps1         # 本地同步腳本
├── CHANGELOG.md                    # 更新記錄
├── LICENSE                         # MIT 授權
└── README.md
```

## 知識庫涵蓋範圍

| 章節 | 主題 | 深度 |
|------|------|------|
| §0 VLA 是什麼 | 核心概念、輸入輸出、核心承諾 | 概述 |
| §1 架構演化時間線 | RT-1 → π0.6，關鍵拐點 | 詳細 |
| §2 動作生成 | Diffusion、Flow Matching、FAST、自回歸 | 深入 |
| §3 訓練範式 | BC、Co-training、RL、自我改進 | 深入 |
| §4 信念網絡 | 10 條條件依賴信念 + 校準置信度 | 分析 |
| §5 收斂地圖 | 5 個 Phase 追蹤 + 臨界閾值 | 分析 |
| §6 觸覺與多模態 | 觸覺感知、力反饋、多模態融合 | 中等 |
| §7 部署 | 真機指南、社區實戰筆記 | 實操 |
| §8 產業 | 公司分析、競爭動態、護城河 | 中等 |
| §9-15 | 熱點專題、面試準備、校準紀律 | 各異 |

## 使用範例

安裝後直接跟 Claude 自然對話：

- *「Diffusion Policy vs Flow Matching，哪個更好？」* → 對比模式 + Bull/Bear 辯論
- *「幫我看這篇 VLA 論文」* → 論文評估模式 + 信念更新
- *「VLA 下一步該投入什麼方向？」* → 方向判斷模式 + 完整三視角辯論
- *「π0 用了什麼架構？」* → 事實查詢模式，簡潔回答
- *「Physical Intelligence 這家公司怎麼樣？」* → 產業分析模式 + 護城河評估

## 每日更新機制

`VLA_EXPERT_MEMORY.md` 知識庫每日更新，追蹤：

- 新論文發布與突破性進展
- 信念網絡置信度變化
- 收斂 Phase 狀態轉移
- 產業動態與融資事件
- 社區部署實戰經驗

## 授權

MIT License — 詳見 [LICENSE](LICENSE)。

## 貢獻

歡迎貢獻！如果你有 VLA 相關的洞察、論文分析或部署經驗，歡迎開 Issue 或 PR。

---

*基於 VLA Handbook 研究系統構建。知識庫每日更新。*
