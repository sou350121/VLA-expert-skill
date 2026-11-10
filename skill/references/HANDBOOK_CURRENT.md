# VLA Handbook 當前來源

> 同步日期：2026-11-10（Asia/Shanghai）；來源 commit：`cbc81117914834ab0fb88c587ec44afc31ea4abb`。
> 此日期只代表已發布檔案的同步，不代表所有研究結論或產業來源已在當日重核。
> 上游文章仍須核對一手來源；自報、歷史補錄及採集缺口維持上游原標記。

涵蓋 832 份理論 Markdown，其中 662 份檔名為論文拆解；兩者不等同獨立論文數。

完整論文／產業／報告／部署入口見 [來源索引](HANDBOOK_INDEX.md)，按需搜尋與讀取。
舊 [專家記憶](VLA_EXPERT_MEMORY.md) 是歷史快照，信念百分比與相變狀態未由本次同步重校準。

## DeepSeek 閱讀導覽

引用為上游節選；閱讀建議為模型建議，並非原論文結論。

### REKI：把记忆注册进 VLA（REKI: Registering Knowledge in VLAs）

來源：[theory/frontier/reki_registering_knowledge_in_vlas_dissection.md](https://github.com/sou350121/VLA-Handbook/blob/cbc81117914834ab0fb88c587ec44afc31ea4abb/theory/frontier/reki_registering_knowledge_in_vlas_dissection.md)

> REKI 要解决的是：VLA 只看当前帧，遇到两个看起来都像“该往对方走”的位姿时，会在 A、B 之间来回摆。它把每帧 VLM 上下文压成 32 个 register token，只把 K/V 留在 action expert 的 self-attention cache 里，让策略用极低开销看到最近约 2 秒。

閱讀建議（推斷）：建議先辨識問題設定與機制描述，再區分論文主張與已獨立驗證的結論；把重點放在記憶如何被使用，而不是只記住效能口號。

### N₀-VTLA：把触觉变成“未来接触”的 latent 条件

來源：[theory/tactile/n0_vtla_latent_tactile_tokens_2026.md](https://github.com/sou350121/VLA-Handbook/blob/cbc81117914834ab0fb88c587ec44afc31ea4abb/theory/tactile/n0_vtla_latent_tactile_tokens_2026.md)

> 这篇论文的核心不是给 VLA 加一路“触觉相机”，而是把触觉从观测上下文移到动作专家的预测条件上：冻结 DINOv2 编码基线差分触觉图，轻量 predictor 估计未来 50 步的接触变化 latent z，z 不进入视觉语言 prefix，只条件 action expert。

閱讀建議（推斷）：閱讀時可先抓住觸覺條件的注入位置，再檢查訓練階段與評測限制；把作者報告與獨立核驗分開看待，並留意版本差異。

### VLA-Touch：用双层触觉反馈增强 VLA / Enhancing Vision-Language-Action Models with Dual-Level Tactile Feedback

來源：[theory/tactile/vla_touch_dual_level_tactile_feedback_2025.md](https://github.com/sou350121/VLA-Handbook/blob/cbc81117914834ab0fb88c587ec44afc31ea4abb/theory/tactile/vla_touch_dual_level_tactile_feedback_2025.md)

> VLA-Touch 不是把触觉 token 塞进 VLA 继续预训练，而是把触觉拆成两个接口：高层用 Octopi 把 GelSight 序列读成语言，交给 GPT-4o 重规划；低层用 BRIDGeR 以 RDT-1B 动作为起点做触觉条件精炼。

閱讀建議（推斷）：建議把重點放在分層介面的分工與固定基礎模型的取捨，並區分工程設計、作者報告與尚未獨立核驗的出版狀態。

### VLA 双周前沿报告 | 2026-10-22 至 2026-11-04

來源：[reports/biweekly/2026-11-04.md](https://github.com/sou350121/VLA-Handbook/blob/cbc81117914834ab0fb88c587ec44afc31ea4abb/reports/biweekly/2026-11-04.md)

> 本报告标称覆盖 14 个日历日，但只有 2026-10-30 至 2026-11-04 共 6 天有可验证的采集回执；2026-10-22 至 10-29 这 8 天缺失或未经验证。因此下面所有内容都只描述**已采集到的样本**，不能据此判断领域整体走向、成熟度或无突破。

閱讀建議（推斷）：閱讀此類週期整理時，先確認覆蓋範圍與缺口，再把樣本觀察當作線索而非領域結論；遇到強烈趨勢語句時，回到採集限制檢查。

### 🏭 行业判断地图

來源：[companies/industry_mainline.md](https://github.com/sou350121/VLA-Handbook/blob/cbc81117914834ab0fb88c587ec44afc31ea4abb/companies/industry_mainline.md)

> 来源陈述：据NVIDIA Robotics 2026-10-29消息，NVIDIA发布Isaac Lab 3.0，新增Newton物理、可切换后端、渲染选项、集群级并行训练、实验性RL后训练及LEAPP部署导出。判断/待核问题：这是训练与部署工具链更新，可能降低仿真到实机门槛；但来源未给出真实机器人性能、成本或采用数据，不能当作量产或可靠性证明。

閱讀建議（推斷）：閱讀產業地圖時，宜把來源陳述、判斷與待核問題分層看待；工具鏈發布可視為能力訊號，但不宜直接推成量產或可靠性結論。
