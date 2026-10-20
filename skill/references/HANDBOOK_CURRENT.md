# VLA Handbook 當前來源

> 同步日期：2026-10-20（Asia/Shanghai）；來源 commit：`a972ac7178c3cf530c6bf1d44fac9059920895e0`。
> 此日期只代表已發布檔案的同步，不代表所有研究結論或產業來源已在當日重核。
> 上游文章仍須核對一手來源；自報、歷史補錄及採集缺口維持上游原標記。

涵蓋 762 份理論 Markdown，其中 593 份檔名為論文拆解；兩者不等同獨立論文數。

完整論文／產業／報告／部署入口見 [來源索引](HANDBOOK_INDEX.md)，按需搜尋與讀取。
舊 [專家記憶](VLA_EXPERT_MEMORY.md) 是歷史快照，信念百分比與相變狀態未由本次同步重校準。

## DeepSeek 閱讀導覽

引用為上游節選；閱讀建議為模型建議，並非原論文結論。

### REKI：把记忆注册进 VLA（REKI: Registering Knowledge in VLAs）

來源：[theory/frontier/reki_registering_knowledge_in_vlas_dissection.md](https://github.com/sou350121/VLA-Handbook/blob/a972ac7178c3cf530c6bf1d44fac9059920895e0/theory/frontier/reki_registering_knowledge_in_vlas_dissection.md)

> REKI 要解决的是：VLA 只看当前帧，遇到两个看起来都像“该往对方走”的位姿时，会在 A、B 之间来回摆。它把每帧 VLM 上下文压成 32 个 register token，只把 K/V 留在 action expert 的 self-attention cache 里，让策略用极低开销看到最近约 2 秒。

閱讀建議（推斷）：閱讀時可先抓住作者如何定義短時記憶，再區分機制主張與基準結果，避免把效率宣稱直接當成部署結論。

### N₀-VTLA：把触觉变成“未来接触”的 latent 条件

來源：[theory/tactile/n0_vtla_latent_tactile_tokens_2026.md](https://github.com/sou350121/VLA-Handbook/blob/a972ac7178c3cf530c6bf1d44fac9059920895e0/theory/tactile/n0_vtla_latent_tactile_tokens_2026.md)

> 这篇论文的核心不是给 VLA 加一路“触觉相机”，而是把触觉从观测上下文移到动作专家的预测条件上：冻结 DINOv2 编码基线差分触觉图，轻量 predictor 估计未来 50 步的接触变化 latent z，z 不进入视觉语言 prefix，只条件 action expert。

閱讀建議（推斷）：閱讀時宜先確認觸覺表徵被放在哪個介面，再對照訓練階段與真機評測的界線，勿把版本差異當成確定結論。

### VLA-Touch：用双层触觉反馈增强 VLA / Enhancing Vision-Language-Action Models with Dual-Level Tactile Feedback

來源：[theory/tactile/vla_touch_dual_level_tactile_feedback_2025.md](https://github.com/sou350121/VLA-Handbook/blob/a972ac7178c3cf530c6bf1d44fac9059920895e0/theory/tactile/vla_touch_dual_level_tactile_feedback_2025.md)

> VLA-Touch 不是把触觉 token 塞进 VLA 继续预训练，而是把触觉拆成两个接口：高层用 Octopi 把 GelSight 序列读成语言，交给 GPT-4o 重规划；低层用 BRIDGeR 以 RDT-1B 动作为起点做触觉条件精炼。

閱讀建議（推斷）：閱讀時可先釐清高層與低層各自的輸入輸出，再檢查模組化設計帶來的延遲與評測限制，避免把外掛流程視為端到端訓練。

### VLA 双周前沿报告 | 2026-10-02 至 2026-10-15

來源：[reports/biweekly/2026-10-15.md](https://github.com/sou350121/VLA-Handbook/blob/a972ac7178c3cf530c6bf1d44fac9059920895e0/reports/biweekly/2026-10-15.md)

> 先说清数据边界：这 14 天里只有 **2026-10-15** 一天经核验为完整采集，其余 13 天属缺失或未核验，其中 10-11 无回执。因此以下内容只描述**已采集到的样本**，不足以支撑任何"领域级"判断；凡属推断处均已明确标注。

閱讀建議（推斷）：閱讀時宜把採集完整度與趨勢判斷分開，先看樣本邊界，再把摘要中的推論視為待驗證線索。

### 🏭 行业判断地图

來源：[companies/industry_mainline.md](https://github.com/sou350121/VLA-Handbook/blob/a972ac7178c3cf530c6bf1d44fac9059920895e0/companies/industry_mainline.md)

> 只依据公开官方来源；事件日期与补录日期分开标注。官方自报不等于独立验证；原文没有的数字不补，不把媒体转述当官方事实。

閱讀建議（推斷）：閱讀時可先區分官方自報與獨立驗證，並留意程序節點與完成狀態的差別，避免把公告規畫當成既成結果。
