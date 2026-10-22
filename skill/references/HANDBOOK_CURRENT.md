# VLA Handbook 當前來源

> 同步日期：2026-10-22（Asia/Shanghai）；來源 commit：`91beb57c102b2b29325c4d4b3c1ee532ae15fe0c`。
> 此日期只代表已發布檔案的同步，不代表所有研究結論或產業來源已在當日重核。
> 上游文章仍須核對一手來源；自報、歷史補錄及採集缺口維持上游原標記。

涵蓋 774 份理論 Markdown，其中 605 份檔名為論文拆解；兩者不等同獨立論文數。

完整論文／產業／報告／部署入口見 [來源索引](HANDBOOK_INDEX.md)，按需搜尋與讀取。
舊 [專家記憶](VLA_EXPERT_MEMORY.md) 是歷史快照，信念百分比與相變狀態未由本次同步重校準。

## DeepSeek 閱讀導覽

引用為上游節選；閱讀建議為模型建議，並非原論文結論。

### REKI：把记忆注册进 VLA（REKI: Registering Knowledge in VLAs）

來源：[theory/frontier/reki_registering_knowledge_in_vlas_dissection.md](https://github.com/sou350121/VLA-Handbook/blob/91beb57c102b2b29325c4d4b3c1ee532ae15fe0c/theory/frontier/reki_registering_knowledge_in_vlas_dissection.md)

> REKI 用 2.4B 纯公开数据 VLA，把 action expert 里的 register token 变成可缓存的短时记忆，在 LIBERO-Plus、RoboTwin Clean2Rand、RoboCasa365 上冲到公开数据组的性能-规模 Pareto 前沿，并把编译后单 chunk 推理压到 21.8 ms。

閱讀建議（推斷）：建議先讀摘要與快速判斷，再對照機制與實驗章節，留意作者如何界定公開資料組的比較範圍。

### N₀-VTLA：把触觉变成“未来接触”的 latent 条件

來源：[theory/tactile/n0_vtla_latent_tactile_tokens_2026.md](https://github.com/sou350121/VLA-Handbook/blob/91beb57c102b2b29325c4d4b3c1ee532ae15fe0c/theory/tactile/n0_vtla_latent_tactile_tokens_2026.md)

> 冻结 DINOv2 编码基线差分触觉图，轻量 predictor 估计未来 50 步的接触变化 latent z，z 不进入视觉语言 prefix，只条件 action expert。

閱讀建議（推斷）：可先掌握作者把觸覺放在動作條件而非觀測前綴的設計，再檢查訓練階段與評測邊界。

### VLA-Touch：用双层触觉反馈增强 VLA / Enhancing Vision-Language-Action Models with Dual-Level Tactile Feedback

來源：[theory/tactile/vla_touch_dual_level_tactile_feedback_2025.md](https://github.com/sou350121/VLA-Handbook/blob/91beb57c102b2b29325c4d4b3c1ee532ae15fe0c/theory/tactile/vla_touch_dual_level_tactile_feedback_2025.md)

> VLA-Touch 不是把触觉 token 塞进 VLA 继续预训练，而是把触觉拆成两个接口：高层用 Octopi 把 GelSight 序列读成语言，交给 GPT-4o 重规划；低层用 BRIDGeR 以 RDT-1B 动作为起点做触觉条件精炼。

閱讀建議（推斷）：閱讀時可把重點放在模組化接口與固定基礎模型的取捨，並區分作者報告與待核驗的出版狀態。

### VLA 双周前沿报告 | 2026-10-08 至 2026-10-21

來源：[reports/biweekly/2026-10-21.md](https://github.com/sou350121/VLA-Handbook/blob/91beb57c102b2b29325c4d4b3c1ee532ae15fe0c/reports/biweekly/2026-10-21.md)

> 本期是回溯性回顾，而不是完整周期的结论。14 天窗口里只有 6 天（10-16 至 10-21）有完整采集收据；10-08 至 10-15 共 8 天缺失或未验证。

閱讀建議（推斷）：建議先看採集範圍說明，再把條目當作樣本內觀察，不宜外推為領域整體判斷。

### 🏭 行业判断地图

來源：[companies/industry_mainline.md](https://github.com/sou350121/VLA-Handbook/blob/91beb57c102b2b29325c4d4b3c1ee532ae15fe0c/companies/industry_mainline.md)

> 只依据公开官方来源；事件日期与补录日期分开标注。官方自报不等于独立验证；原文没有的数字不补，不把媒体转述当官方事实。

閱讀建議（推斷）：可先讀口徑與張力記錄，留意官方自報、程序節點與獨立驗證之間的界線。
