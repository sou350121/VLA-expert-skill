# VLA Handbook 當前來源

> 同步日期：2026-11-14（Asia/Shanghai）；來源 commit：`9f3feca20d500d2fbd92558d6837b19b059cfb33`。
> 此日期只代表已發布檔案的同步，不代表所有研究結論或產業來源已在當日重核。
> 上游文章仍須核對一手來源；自報、歷史補錄及採集缺口維持上游原標記。

涵蓋 849 份理論 Markdown，其中 679 份檔名為論文拆解；兩者不等同獨立論文數。

完整論文／產業／報告／部署入口見 [來源索引](HANDBOOK_INDEX.md)，按需搜尋與讀取。
舊 [專家記憶](VLA_EXPERT_MEMORY.md) 是歷史快照，信念百分比與相變狀態未由本次同步重校準。

## DeepSeek 閱讀導覽

引用為上游節選；閱讀建議為模型建議，並非原論文結論。

### REKI：把记忆注册进 VLA（REKI: Registering Knowledge in VLAs）

來源：[theory/frontier/reki_registering_knowledge_in_vlas_dissection.md](https://github.com/sou350121/VLA-Handbook/blob/9f3feca20d500d2fbd92558d6837b19b059cfb33/theory/frontier/reki_registering_knowledge_in_vlas_dissection.md)

> REKI 要解决的是：VLA 只看当前帧，遇到两个看起来都像“该往对方走”的位姿时，会在 A、B 之间来回摆。它把每帧 VLM 上下文压成 32 个 register token，只把 K/V 留在 action expert 的 self-attention cache 里，让策略用极低开销看到最近约 2 秒。

閱讀建議（推斷）：可先抓住短時記憶如何進入動作專家，再回頭檢查它與視覺語言主幹的耦合程度。

### N₀-VTLA：把触觉变成“未来接触”的 latent 条件

來源：[theory/tactile/n0_vtla_latent_tactile_tokens_2026.md](https://github.com/sou350121/VLA-Handbook/blob/9f3feca20d500d2fbd92558d6837b19b059cfb33/theory/tactile/n0_vtla_latent_tactile_tokens_2026.md)

> 这篇论文的核心不是给 VLA 加一路“触觉相机”，而是把触觉从观测上下文移到动作专家的预测条件上：冻结 DINOv2 编码基线差分触觉图，轻量 predictor 估计未来 50 步的接触变化 latent z，z 不进入视觉语言 prefix，只条件 action expert。

閱讀建議（推斷）：閱讀時可把重點放在觸覺條件進入動作通路的位置，而不是把它誤讀成單純增加一種觀測模態。

### VLA-Touch：用双层触觉反馈增强 VLA / Enhancing Vision-Language-Action Models with Dual-Level Tactile Feedback

來源：[theory/tactile/vla_touch_dual_level_tactile_feedback_2025.md](https://github.com/sou350121/VLA-Handbook/blob/9f3feca20d500d2fbd92558d6837b19b059cfb33/theory/tactile/vla_touch_dual_level_tactile_feedback_2025.md)

> VLA-Touch 不是把触觉 token 塞进 VLA 继续预训练，而是把触觉拆成两个接口：高层用 Octopi 把 GelSight 序列读成语言，交给 GPT-4o 重规划；低层用 BRIDGeR 以 RDT-1B 动作为起点做触觉条件精炼。

閱讀建議（推斷）：建議先區分高層重規劃與低層動作精煉的職責，再評估模組化設計帶來的延遲與整合成本。

### VLA 双周前沿报告 | 2026-10-22 至 2026-11-04

來源：[reports/biweekly/2026-11-04.md](https://github.com/sou350121/VLA-Handbook/blob/9f3feca20d500d2fbd92558d6837b19b059cfb33/reports/biweekly/2026-11-04.md)

> 本报告标称覆盖 14 个日历日，但只有 2026-10-30 至 2026-11-04 共 6 天有可验证的采集回执；2026-10-22 至 10-29 这 8 天缺失或未经验证。因此下面所有内容都只描述**已采集到的样本**，不能据此判断领域整体走向、成熟度或无突破。

閱讀建議（推斷）：閱讀時先把樣本覆蓋範圍放在心上，避免把局部觀察當成整體趨勢。

### 🏭 行业判断地图

來源：[companies/industry_mainline.md](https://github.com/sou350121/VLA-Handbook/blob/9f3feca20d500d2fbd92558d6837b19b059cfb33/companies/industry_mainline.md)

> 据NVIDIA在2026-11-09发布的博客，开放的GR00T 2支持灵巧操作技能学习与跨机器人本体迁移，在RoboCasa365、RoboLab、RoboDojo和MolmoSpaces基准的视觉语言动作与世界动作模型类别中位列前三，Nexuni、Foxconn与Siemens有测试、应用或评估动作。

閱讀建議（推斷）：可把焦點放在能力宣稱與實際部署證據的差距，避免把基準排名直接當成產線可靠性。
