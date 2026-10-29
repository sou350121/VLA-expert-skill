# VLA Handbook 當前來源

> 同步日期：2026-10-29（Asia/Shanghai）；來源 commit：`815996afe46eb7d60b0ef3c33270fe0a35fefa4d`。
> 此日期只代表已發布檔案的同步，不代表所有研究結論或產業來源已在當日重核。
> 上游文章仍須核對一手來源；自報、歷史補錄及採集缺口維持上游原標記。

涵蓋 798 份理論 Markdown，其中 628 份檔名為論文拆解；兩者不等同獨立論文數。

完整論文／產業／報告／部署入口見 [來源索引](HANDBOOK_INDEX.md)，按需搜尋與讀取。
舊 [專家記憶](VLA_EXPERT_MEMORY.md) 是歷史快照，信念百分比與相變狀態未由本次同步重校準。

## DeepSeek 閱讀導覽

引用為上游節選；閱讀建議為模型建議，並非原論文結論。

### REKI：把记忆注册进 VLA（REKI: Registering Knowledge in VLAs）

來源：[theory/frontier/reki_registering_knowledge_in_vlas_dissection.md](https://github.com/sou350121/VLA-Handbook/blob/815996afe46eb7d60b0ef3c33270fe0a35fefa4d/theory/frontier/reki_registering_knowledge_in_vlas_dissection.md)

> REKI 要解决的是：VLA 只看当前帧，遇到两个看起来都像“该往对方走”的位姿时，会在 A、B 之间来回摆。它把每帧 VLM 上下文压成 32 个 register token，只把 K/V 留在 action expert 的 self-attention cache 里，让策略用极低开销看到最近约 2 秒。

閱讀建議（推斷）：可先從問題動機讀起，理解作者如何把短時記憶放進動作專家，再回頭檢查實驗與部署限制。

### N₀-VTLA：把触觉变成“未来接触”的 latent 条件

來源：[theory/tactile/n0_vtla_latent_tactile_tokens_2026.md](https://github.com/sou350121/VLA-Handbook/blob/815996afe46eb7d60b0ef3c33270fe0a35fefa4d/theory/tactile/n0_vtla_latent_tactile_tokens_2026.md)

> 这篇论文的核心不是给 VLA 加一路“触觉相机”，而是把触觉从观测上下文移到动作专家的预测条件上：冻结 DINOv2 编码基线差分触觉图，轻量 predictor 估计未来 50 步的接触变化 latent z，z 不进入视觉语言 prefix，只条件 action expert。

閱讀建議（推斷）：建議先抓住觸覺被放到哪個介面，再區分預測條件與觀測輸入的差別，最後留意版本差異帶來的解讀風險。

### VLA-Touch：用双层触觉反馈增强 VLA / Enhancing Vision-Language-Action Models with Dual-Level Tactile Feedback

來源：[theory/tactile/vla_touch_dual_level_tactile_feedback_2025.md](https://github.com/sou350121/VLA-Handbook/blob/815996afe46eb7d60b0ef3c33270fe0a35fefa4d/theory/tactile/vla_touch_dual_level_tactile_feedback_2025.md)

> VLA-Touch 不是把触觉 token 塞进 VLA 继续预训练，而是把触觉拆成两个接口：高层用 Octopi 把 GelSight 序列读成语言，交给 GPT-4o 重规划；低层用 BRIDGeR 以 RDT-1B 动作为起点做触觉条件精炼。

閱讀建議（推斷）：可先看雙層介面的分工，再思考模組化設計的取捨，並把外部服務與控制頻率視為需要權衡的工程條件。

### VLA 双周前沿报告 | 2026-10-08 至 2026-10-21

來源：[reports/biweekly/2026-10-21.md](https://github.com/sou350121/VLA-Handbook/blob/815996afe46eb7d60b0ef3c33270fe0a35fefa4d/reports/biweekly/2026-10-21.md)

> 本期是回溯性回顾，而不是完整周期的结论。14 天窗口里只有 6 天（10-16 至 10-21）有完整采集收据；10-08 至 10-15 共 8 天缺失或未验证。因此下面每一条都只是“已采集样本内的观察”，不能据此判断领域衰退、成熟、收敛或无突破，也不能当作全领域画像。

閱讀建議（推斷）：閱讀時先確認樣本覆蓋範圍，把內容當成有限窗口內的觀察，而不是對整個領域下定論。

### 🏭 行业判断地图

來源：[companies/industry_mainline.md](https://github.com/sou350121/VLA-Handbook/blob/815996afe46eb7d60b0ef3c33270fe0a35fefa4d/companies/industry_mainline.md)

> 来源陈述：据Agility Robotics官方2026-10-13公告（周档2026-10-18补录），拟议合并的S-4已生效，股东会定于11月2日，交割仍须股东批准及其他条件。判断/待核问题：这只是资本程序节点，不能写成完成上市或完成交割；11月股东会与最终交割条件待核。

閱讀建議（推斷）：建議把公告拆成程序進展與條件成就兩層來讀，避免把階段性節點誤當成最終結果。
