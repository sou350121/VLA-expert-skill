# VLA Handbook 當前來源

> 同步日期：2026-11-28（Asia/Shanghai）；來源 commit：`a94a5f72e5330862918218dcc4a4c392e3af975f`。
> 此日期只代表已發布檔案的同步，不代表所有研究結論或產業來源已在當日重核。
> 上游文章仍須核對一手來源；自報、歷史補錄及採集缺口維持上游原標記。

涵蓋 878 份理論 Markdown，其中 708 份檔名為論文拆解；兩者不等同獨立論文數。

完整論文／產業／報告／部署入口見 [來源索引](HANDBOOK_INDEX.md)，按需搜尋與讀取。
舊 [專家記憶](VLA_EXPERT_MEMORY.md) 是歷史快照，信念百分比與相變狀態未由本次同步重校準。

## DeepSeek 閱讀導覽

引用為上游節選；閱讀建議為模型建議，並非原論文結論。

### REKI：把记忆注册进 VLA（REKI: Registering Knowledge in VLAs）

來源：[theory/frontier/reki_registering_knowledge_in_vlas_dissection.md](https://github.com/sou350121/VLA-Handbook/blob/a94a5f72e5330862918218dcc4a4c392e3af975f/theory/frontier/reki_registering_knowledge_in_vlas_dissection.md)

> REKI 要解决的是：VLA 只看当前帧，遇到两个看起来都像“该往对方走”的位姿时，会在 A、B 之间来回摆。它把每帧 VLM 上下文压成 32 个 register token，只把 K/V 留在 action expert 的 self-attention cache 里，让策略用极低开销看到最近约 2 秒。

閱讀建議（推斷）：可先抓住短時記憶如何被放進動作專家，再區分機制主張與基準表現，避免把摘要中的定位當成獨立驗證。

### N₀-VTLA：把触觉变成“未来接触”的 latent 条件

來源：[theory/tactile/n0_vtla_latent_tactile_tokens_2026.md](https://github.com/sou350121/VLA-Handbook/blob/a94a5f72e5330862918218dcc4a4c392e3af975f/theory/tactile/n0_vtla_latent_tactile_tokens_2026.md)

> 这篇论文的核心不是给 VLA 加一路“触觉相机”，而是把触觉从观测上下文移到动作专家的预测条件上：冻结 DINOv2 编码基线差分触觉图，轻量 predictor 估计未来 50 步的接触变化 latent z，z 不进入视觉语言 prefix，只条件 action expert。

閱讀建議（推斷）：閱讀時先分清觸覺表徵的放置位置與訓練階段，再把作者報告與未披露的實驗細節分開看。

### VLA-Touch：用双层触觉反馈增强 VLA / Enhancing Vision-Language-Action Models with Dual-Level Tactile Feedback

來源：[theory/tactile/vla_touch_dual_level_tactile_feedback_2025.md](https://github.com/sou350121/VLA-Handbook/blob/a94a5f72e5330862918218dcc4a4c392e3af975f/theory/tactile/vla_touch_dual_level_tactile_feedback_2025.md)

> VLA-Touch 不是把触觉 token 塞进 VLA 继续预训练，而是把触觉拆成两个接口：高层用 Octopi 把 GelSight 序列读成语言，交给 GPT-4o 重规划；低层用 BRIDGeR 以 RDT-1B 动作为起点做触觉条件精炼。

閱讀建議（推斷）：可先看雙層介面的分工，再留意模組化設計帶來的依賴與評測限制，不宜把自述結果視為獨立核驗。

### VLA 双周前沿报告 | 2026-11-05 至 2026-11-18

來源：[reports/biweekly/2026-11-18.md](https://github.com/sou350121/VLA-Handbook/blob/a94a5f72e5330862918218dcc4a4c392e3af975f/reports/biweekly/2026-11-18.md)

> 本期可核验的采集窗口只有 11-13 至 11-18 共 6 天，11-05 至 11-12 这 8 天缺少完整采集记录。因此以下所有观察都只描述「已采集样本」，不构成对两周全周期、乃至 VLA 领域整体的判断。数据覆盖不支持趋势推断，本报告也不做趋势推断。

閱讀建議（推斷）：閱讀時先注意資料覆蓋範圍，再把樣本觀察與全領域判斷區分開，避免過度外推。

### 🏭 行业判断地图

來源：[companies/industry_mainline.md](https://github.com/sou350121/VLA-Handbook/blob/a94a5f72e5330862918218dcc4a4c392e3af975f/companies/industry_mainline.md)

> 来源陈述：据 Agility Robotics 在 2026-11-18 发布的公告，公司任命 Daniel Diez 为总裁、Christopher Sullivan 为首席产品官、Ana Lang 为首席行政官，并称此次调整旨在支撑上市公司运营并聚焦增长。

閱讀建議（推斷）：可把來源陳述與判斷分開閱讀，留意治理人事消息不等於融資或估值更新。
