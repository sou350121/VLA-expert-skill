# VLA 专家记忆 v1.6 | 2026-03-31

> **角色**：压缩索引 + 自足知识底座。无 repo 时独立运作；有 repo 时作为快速框架，深度分析由原始文件补充。
> **来源**：KW_VLA Handbook（328+ 篇 Markdown，70+ 论文拆解，产业分析，周报系统）。
> **维护**：定时任务每日 09:00 增量更新。
> **v1.6 变更摘要**：无信念节点置信度变更（B2/B5 下调弹药充足，保留给 03-31 hypothesis-review 正式执行）。**关键新论文**：DFM-VLA（Discrete Flow Matching，CALVIN 4.44/LIBERO 95.7%/真机 70.8%，全面击败 continuous FM+diffusion+AR——B5 强下行信号）；VLA-OPD（On-Policy Distillation，3× 样本效率但依赖 RL teacher）；Scaling Sim-to-Real RL（21.7%→75% 真机，3D generative worlds）；VLA-MBPO（WM+RL 第 4 个框架）；Realtime-VLA V2（真机达人类速度，0.2mm 精度）；Ruka-v2（开源灵巧手 v2）。**Phase 1 收敛度 82%→80%**（DFM-VLA = 第 5 条反相变信号）。**套利 #3 窗口确认 ≤1 月**。**B2 保守偏误 25/30 天，03-31 必须下调**。新潜在套利：RL→Distillation→Deploy 流水线、WM+RL 框架标准化。
> **v1.5 变更摘要**（03-29）：无信念节点变更（静默日）。产业信号更新：Unitree R1 Air $4,900、Amazon 收购 Fauna Robotics、ROBOTERA 100 亿 RMB。新论文：VLGOR、EquiBim、Fast-FoundationStereo。
> **v1.4 变更摘要**（03-25）：多 Phase 达临界/超临界。B4 65→70%，B9 65→70%，B3 raw 85→90%（PLD），B8 65→70%（TacVLA）。C2 20→15%（达下限）。Phase 1 85→82%，Phase 2 68→72%，Phase 3 35→42%🟡，Phase 4 54→60%，Phase 5 40→44%🟡。套利 #3 窗口即将关闭。

### Source Map（深度分析时按需读取原始文件）

| 本文 Section | 原始文件（KW_VLA/ 下） | 深度倍率 |
|---|---|---|
| §4 信念网络 | `docs/system/BELIEF_GRAPH.md` (468行) | 10× |
| §5 收敛地图 | `docs/system/CONVERGENCE_MAP.md` (296行) | 8× |
| §15 校准纪律 | `docs/system/EPISTEMICS.md` (191行) | 5× |
| §9 当前状态 | `reports/weekly/` 最新文件 + `reports/biweekly/` 最新文件 | 实时 |
| §6 触觉 | `theory/tactile/` + `theory/frontier/tactile_*` | 5× |
| §7 部署 | `deployment/` | 20× |
| §8 产业 | `companies/` + `memory/blog/archives/vla-social-intel/` 最新 | 10× |
| §10 深度专题 | `theory/frontier/` 对应论文 | 逐篇 |
| §14 面试 | `question-bank/` + `cheat-sheet/` | 5× |

---

## 0. VLA 是什么（30 秒版）

**Vision-Language-Action (VLA)** = 将视觉感知、语言理解、动作生成统一在一个模型里的具身智能范式。
输入：RGB 图像 + 语言指令（可选：深度、触觉、本体感觉）。
输出：机器人可执行的动作序列（关节角/末端位姿/夹爪）。
核心承诺：像 LLM 理解文字一样理解物理世界，并直接输出动作。

---

## 1. 模型族谱与关键架构

### 1.1 演化主线

```
RT-1(2022) → RT-2(2023) → OpenVLA(2024) → π0(2024) → π0.5(2025) → π0.6(2025)
                                              ↑ Flow Matching 引入点
```

| 模型 | 机构 | 参数 | 视觉 | 动作生成 | 控制频率 | 核心突破 |
|------|------|------|------|----------|----------|----------|
| RT-1 | Google | ~35M | EfficientNet | 离散 Token(256bin) + Softmax | 3Hz | 首个大规模真机验证 |
| RT-2 | DeepMind | 55B | ViT-22B(PaLI-X) | 离散 Token + Softmax | 1-3Hz | 语义泛化涌现（"抓灭绝动物"→抓恐龙玩具）|
| OpenVLA | Stanford | 7B | SigLIP(ViT-L) + Llama2 | 离散 Token + Softmax | 5-10Hz | 全开源 SOTA，LoRA 微调生态 |
| π0 | Physical Intelligence | 3B | PaliGemma(SigLIP+Gemma) | **Flow Matching**(ODE) | 10-50Hz | 首个 VLM × Flow Matching，高频精密控制 |
| π0.5 | PI | 3B+ | 同上 | Flow + FAST Token | ~50Hz | 开放世界泛化，co-training(机器人+互联网+仿真) |
| π0.6 | PI | 5B | 同上 + Action Expert | Flow + Recap(离线RL) | ~50Hz | 自我改进闭环，2× 吞吐 2× 低失败率 |

### 1.2 其他重要模型

- **Octo** (Berkeley)：Diffusion 动作头，连续动作，推理慢但平滑
- **Galaxea G0**：双系统（VLM 规划器 + VLA 执行器）
- **WALL-OSS**：Uni-CoT + 双分支(Flow + FAST)
- **GR-00T N1** (NVIDIA)：人形机器人基础模型
- **RDT-1B / RDT2**：Scalable Diffusion Transformer，跨具身零样本
- **LingBot-VLA**：务实型 VLA，语用接地
- **AR-VLA** (ETH)：自回归 Action Expert + DTR(Deep Token Routing)，SIMPLER 61.5% 超越 π0.5 51%

### 1.3 架构分类

```
单模型: RT-2 / OpenVLA / π0（一个模型端到端）
双系统: Galaxea G0 / π0.6（VLM 思考 + VLA 执行）
层级式: WALL-OSS（思维链规划 + 双动作头切换）
```

---

## 2. 三大动作生成范式

### 2.1 离散 Token 化（RT-1/RT-2/OpenVLA）
- 连续动作 → 量化为 N bins(通常 256)：`Token = round((a-min)/(max-min) × (N-1))`
- 优点：统一 Transformer 架构，支持多模态
- 致命缺点：量化误差导致精密操作失败（穿针、装配）

### 2.2 Diffusion Policy（Octo/RDT）
- 从高斯噪声迭代去噪生成动作轨迹
- 优点：连续高精度，天然多模态分布
- 缺点：需 50-100 步去噪，延迟高，不适合 >50Hz 控制

### 2.3 Flow Matching（π0 系列）⬅ 当前胜出者
- 学习确定性向量场（最优传输直线路径）
- ODE solver 仅需 1-10 步推理
- 优点：极速 + 高精度 + 支持 50Hz+
- 2026 年论文量 Flow:Diffusion ≈ 2:1，竞争基本结束
- **新进展 (03-17)**：OFP (One-Step Flow Policy) 实现 100× 加速，单步 flow 集成 π₀.5 后**超越**原始 10 步版本

### 2.4 FAST Token 化（折中方案）
- 对动作序列做 DCT（频域变换）+ BPE 合并，压缩 token 数量
- 类比 JPEG：保留高频平滑性，减少 token 爆炸(256^7 → 少量 token)
- OpenVLA 训练加速 5×；FAST+ 预训练 1M+ 轨迹实现跨具身泛化
- π0.5 同时使用 FAST(训练) + Flow(推理)

### 2.5 Discrete Diffusion（新兴第四范式，待验证）
- ICLR 2026 出现 4 篇并发 Discrete Diffusion VLA 论文
- 结合 AR 的 LLM 兼容性 + Diffusion 的多模态表达力
- **待验证**：推理速度数据 + 引用独立性。若推理延迟 ≈ FM 且训练效率更高，可能挑战 B5

### 2.6 Discrete Flow Matching（DFM-VLA，新兴第五范式）
- Token-level probability velocity field——Flow Matching 在离散空间的推广
- **DFM-VLA (2603.26320)**：CALVIN 4.44 / LIBERO 95.7% / 真机 70.8%，**全面击败** continuous FM(FlowVLA) + continuous diffusion(RDT) + discrete diffusion(Dream-VLA) + AR(OpenVLA)
- 推理 121 tokens/s vs AR 50.2 tokens/s（2.4× 加速），2-stage decoding: iterative + validation
- 关键争议：Bear 论点——"DFM 仍是 FM 框架内演化"；但 B5 原定义隐含 continuous FM，若 discrete FM > continuous FM 则定义需修订
- 真机验证规模有限（3 任务 ×40 试验 = 120 次），统计显著性待更大规模确认

**判断**：Action Head 收敛至 Flow Matching（置信度 74%，校准后 ↓自79%，5 条下行信号待合并处理）。范式空间比"FM vs AR"二元叙事更丰富：continuous FM + **discrete FM (DFM-VLA)** + AR-VLA + Discrete Diffusion + FAST + Hybrid 多轨并存。DFM-VLA (2603.26320) 在 CALVIN 4.44/LIBERO 95.7%/真机 70.8% 全面击败 continuous FM+diffusion+AR，是"discrete flow > continuous flow"首个全面对比证据。FM 仍领先但需重定义——"FM" vs "Flow-based methods"边界成为 B5 定义审查核心问题。

---

## 3. 训练范式

### 3.1 行为克隆 (BC) — 基线
- 监督学习：模仿专家示范 → MSE/CE/Diffusion Loss/Flow Loss
- 天花板：只能学到专家分布内的行为，分布外崩溃

### 3.2 Co-training — 数据扩展
- π0.5 路线：机器人数据 + 互联网视频 + 仿真数据联合训练
- 关键：loss masking（不同数据源用不同损失组合）
- 解决数据稀缺但引入域差异

### 3.3 RL Post-training — 突破 BC 天花板 ⬅ 当前唯一赢家
- π0.6 Recap：离线 RL 自我改进（VLM 自动打分 → 高分轨迹回训练）
- GR-RL：Mixture of Teachers 在线 RL
- GigaBrain RAMP：World Model 辅助 RL
- **2026-03 数据**：RL finetuning 加速比 1.82x（全场唯一 SURGE），Instruction Tuning 仅 0.06x（已死）
- 置信度：RL 后训练突破 BC 天花板 = 81%（校准后）。⚠️ 保守偏误预警：**25/30天无下调**，03-31 必须下调→预期 77%
- **PLD (CMU, ICLR 2026)**：残差RL+蒸馏闭环，第二独立团队验证。LIBERO 99% + 真机 100%
- **VLA-OPD (03-30)**：On-Policy Distillation，Reverse-KL 从 RL teacher 蒸馏到 student，1-traj init → LIBERO 93.4%，3× 样本效率。但依赖 RL teacher（不能替代 RL），暗示"RL→Distillation→Deploy"流水线新范式

### 3.4 数据飞轮（终极形态）
```
少量遥操作 → BC 基线 → 真机探索 → VLM 自动打分 → 高分轨迹回训练 → 更强模型 → 更多探索
                              ↑ Recap / Reward Discovery 核心机制
```
- RoboClaw (03-16)：Entangled Action Pairs 自重置飞轮，人工投入 -53.7%，长时域成功率 +25%

### 3.5 损失函数全景

| 阶段 | 损失类型 | 公式/方法 | 用途 |
|------|----------|-----------|------|
| BC-离散 | Cross-Entropy | -Σ y·log(ŷ) | RT-1/RT-2/OpenVLA token 分类 |
| BC-连续 | MSE/Huber | \|a-â\|² | 回归动作值 |
| BC-GMM | NLL | -log Σ wᵢ·N(a;μᵢ,σᵢ) | 多模态连续动作 |
| Diffusion | ε-prediction | \|ε-ε̂(xₜ,t)\|² | 去噪扩散 |
| Flow | velocity field | \|v-v̂(xₜ,t)\|² | 速度场匹配 |
| RL | PPO clip | min(rA, clip(r)A) + V_loss + entropy | 策略改进 |
| 对齐 | InfoNCE/CLIP | 视觉↔语言/视觉↔触觉对比学习 | 跨模态表示 |
| 安全 | barrier/jerk | 速度/加速度/力矩/工作空间约束 | 部署安全 |
| 抗遗忘 | Knowledge Insulation | 梯度隔离(动作头梯度不回传VLM) | 防灾难性遗忘 |

### 3.6 关键训练技巧
- **Knowledge Insulation**：双轨训练——VLM 学离散 token(保留语义)，Action Expert 学连续控制(独立优化)，梯度不互传。<1% 性能损失，2× 收敛加速
- **Co-training loss masking**：不同数据源用不同损失组合（机器人数据全损失，互联网视频只有视觉+语言损失）
- **Action Chunking**：一次前向生成 32-64 步动作序列，配合高频重规划实现闭环
- **Symmetry Equivariance (EquiBim)**：双臂任务训练时加对称等变正则化 L_sym，强制 π(S(O))=S(π(O))，模型无关、推理零开销，+2.7~9.5% 成功率
- **Reward Discovery**：双层元学习自动进化奖励函数，将稀疏"完成/失败"转化为平滑奖励地形

---

## 4. 核心信念网络（Belief Graph 精华）

> 置信度经过校准：>80% 原始值 ×0.9

| ID | 信念 | 置信度 | 上次变更 | 最强反驳 |
|----|------|--------|----------|----------|
| B0 | 数据策略 > 模型架构 | 77% | 03-05 | C1：架构创新会回归(25%) |
| B1 | 数据飞轮是核心壁垒 | 77% | 03-05 | 开源数据集可能瓦解私有壁垒 |
| B2 | RL 后训练突破 BC 天花板 | 81% | 03-05 | ⚠️ **25/30天保守偏误**，5+条反方弹药(PI小actor/假探索/HIL-SERL/LRM仅+14pp/VLA-MBPO弱真机)，03-31必须下调→预期85%/77% |
| B3 | 自我改进闭环是终极形态 | 77%⚠️ | **03-24** | Reward 定义问题比想象的严重。**raw 90%**(PLD 第二独立团队), 受 B1_cal=77% 天花板约束 |
| B4 | World Model 作为闭环加速器 | **70%** ↑ | **03-25** | 物理幻觉在接触密集任务中致命；WM 分化三路线(pixel/latent/WAM) |
| B5 | Flow Matching 主导 Action Head | **74%** ↓ | 03-22 | **5条下行累积**(HybridVLA+A2A FM+Mean-Flow+FODMP+DFM-VLA)，DFM-VLA discrete FM全面超越continuous FM；定义需审查"FM" vs "Flow-based"；预期→78%/70%或更低 |
| B6 | 分层架构(S0/S1/S2)标准化 | 75% | 03-05 | 端到端可能重新胜出 |
| B7 | Action Expert 解耦语义与运动 | 75% | 03-15 | 解耦可能损失跨模态协同(WholeBodyVLA latent action) |
| B8 | 触觉从可选→必需 | **70%** ↑ | **03-17** | 硬件标准化遥遥无期；VFE 替代路线追踪中 |
| B9 | 小模型/边缘推理可行 | **70%** ↑ | **03-25** | GigaBrain-0-Small 80%/0.13s + AutoQVLA 30% VRAM + RoboECC 362ms + **Realtime-VLA V2 0.2mm 精度人类速度(累积中)** |

**逆共识（赌注）**：
- C1：架构创新会回归 (**25%** ↑) — Discrete Diffusion 4 并发论文 + Kairos 3.0 原生 WM 架构。不再信号饥饿
- C2：World Model 是死胡同 (**15%** ↓ 达下限) — 压倒性反面证据(Cosmos 3/NC AI WFM/GR00T N2 WAM)。下限规则：15% 不得再降，除非物理幻觉+因果保留双解决
- C3：VLA 不需要语言 (24%) — 纯视觉-动作路线有上升信号(VLM4VLA backbone无关性)

**风险标记**：
- B5 有 PI 锚定风险——去掉 PI 系列后 FM 独立收敛信号只剩 3 条。且 FM adoption 全量统计缺失（Moritz Reuss 博客无比例数据）
- B3 闭环实证来源风险**部分解除**——PLD(CMU, ICLR 2026) 是第二个独立团队验证残差RL+蒸馏闭环。但 B2+B3 双高置信度(90% raw)需 03-29 优先审查
- ⚠️ B2 保守偏误预警：**25/30 天无下调证据**(03-05→03-30)，距阈值仅 5 天。**5+条反方弹药充足，03-31 必须执行下调：90%→85%(校准 77%)**
- B4 定义扩展待办：行业"VLA+WM 混合"中的 WM 多指 learned dynamics model，非 full generative WM——概念需区分

---

## 5. 收敛地图（Phase Transitions）

### Phase 1: Action Head → Flow Matching 【80% 完成】 ↓
- 13/15 独立信号
- 判断：FM 仍领先但"唯一标准"叙事被多范式并存严重削弱，接近"反相变"
- **反相变信号（5条）**：FAST + AR-VLA(ETH) + ICLR 2026 Discrete Diffusion 4篇并发 + HybridVLA(AR+Diffusion 统一) + A2A FM 单步推理 + **DFM-VLA(discrete FM > continuous FM，首个全面对比证据)**
- OFP 单步 flow 100× 加速——FM 推理速度优势进一步扩大
- **双周数据**：flow_matching 0.89x（唯一 momentum stable），diffusion 0.70x，产出持平各24篇

### Phase 2: 训练范式 → RL 后训练 【72% 完成】 ↑ 🔴持续超临界
- 18/15 独立信号（PI RLT 工业级在线 RL 新增）
- RL finetuning 加速比 14d 1.77x → 7d 0.52x（momentum declining 但仍 dominant）
- rl_finetuning 对 instruction_tuning 形成 13:1 压倒性优势

### Phase 3: 触觉 → 标准化 【42% 完成】 ↑ 🟡达临界
- **11.5-12.5/10 独立信号**（+Tactile-VLA/VLA-Touch/Robotiq TSF-85）
- MoDE-VLA(03-14) 证明"触觉不可替代"(力觉去除-11%，触觉去除-8%)
- TacVLA(03-17) 证明"触觉可优雅集成"(gating 机制 +60%/2.1× 遮挡鲁棒性)
- **OmniVTA (03-25⚡)**：视触融合世界模型——触觉作为 WM 输入模态而非独立任务，可能是触觉方向存活路线
- 但学术端 tactile 加速比 0.26x（结构性衰退），被 dexterous_hand(0.62x) 以 4:1 碾压

### Phase 4: World Model → 闭环实用化 【60% 完成】 ↑ 🔴持续超临界
- **14/12 独立信号**（Cosmos 3 + NC AI WFM 新增；VLA-MBPO 与已有 WM+RL 框架相关不计独立信号）
- PlayWorld：自主探索→WM→RL 闭环，+65% 真机成功率
- WM 方法论持续分化：pixel WM → latent WM (CoWVLA) → structured planner (StructVLA) → WAM
- **新信号 (03-25)**：Cosmos 3（首个统一 WFM，NVIDIA 核心产品化）+ NC AI WFM（latent action 直接生成，25% GPU 成本达 80% 性能）
- **Fast-WAM (03-19)**：质疑 WM 是否需要测试时未来想象——WM 研究从"有没有用"转向"怎么用更高效"
- 关键障碍：接触密集任务的物理幻觉
- ⚠️ PI RLT 弱化 WM-as-RL-replacement 叙事但 WM-as-data-factory 加强

### Phase 5: 跨具身泛化 【44% 完成】 ↑ 🟡达临界
- **12.5/12 独立信号**（GR00T N1.7 商业化 + MEM 新增）
- RDT2 展示零样本跨具身迁移可能性
- 方法碎片化仍严重，但工业部署推动标准化

**约束松弛分析**：#1 约束 = 真机数据采集成本（几乎不可松弛，只能绕过：WM/互联网视频/Sim2Real）

**收敛交叉检测**：
- Phase 2×4（RL in imagination）：最危险交叉——World Model 生成合成 rollout 做 RL，成功则颠覆真机数据需求
- Phase 3×2（触觉奖励 for 精细 RL）：被低估——触觉信号可作为精细操作的天然稠密奖励
- **时间套利窗口**：
  - #1 WM 作为数据工厂（~4月，重定义中）
  - #2 VLM-as-Universal-Reward（~9月，早期）
  - #3 🔴🔴仿真规模化 > 真实数据（**≤1月，窗口即将关闭**——Cosmos 3 + NC AI WFM + Scaling Sim-to-Real(2603.18532) = 第三个验证，学术界已跟进工业界，共识快速形成）
  - #4 触觉×RL 交叉（6-12月，早期）
  - #5 工业数据飞轮（10-14月，窗口微缩——ABB/FANUC/YASKAWA/KUKA 整合 NVIDIA 栈）
- **新增跨Phase监测**：Phase 3×5（触觉跨具身）、Phase 2×6（RL+灵巧操作）
- **新潜在套利（观察中）**：
  - RL→Distillation→Deploy 流水线（VLA-OPD 提示，训练一次 + 蒸馏部署多次 = 成本摊销，窗口 ~8-12月）
  - WM+RL 框架标准化（4 个框架竞争中，率先整合端到端方案获先发优势，窗口 ~3-6月）
  - 单步推理商业化（Mean-Flow + FODMP + A2A FM 三条路线，窗口 ~4-6月）

---

## 6. 触觉专题

### 6.1 为什么不可替代
- 视觉给坐标，语言给意图，**触觉给接触相位的真反馈**
- 三联仪表盘：力(抓稳没)、形(局部几何)、质(软硬粗糙)
- 视觉先天缺陷：遮挡 + 不可观测物理量(摩擦/应力) + 接触事件太快

### 6.2 技术栈四层
1. **硬件**：e-skin(电阻/电容/压电) vs 光学触觉(GelSight/DIGIT)
2. **表示**：异构信号→统一空间(UV map/手坐标系锚定)
3. **融合**：高层(触觉→语言→VLM) or 低层(FiLM/cross-attention 注入 policy)
4. **仿真**：接触动力学建模复杂，Sim2Real gap 大，是 scaling 瓶颈

### 6.3 前沿工作
- **MoDE-VLA** (03-14)：残差力觉注入，量化消融——力觉去除-11%，触觉去除-8%，证明触觉不可替代
- **TacVLA** (03-17)：contact-aware gating 机制，选择性激活触觉 token，拆卸+20%/盒内取物+60%/遮挡鲁棒2.1×
- TaF-VLA：触觉力对齐
- TacMamba：快慢双通路触觉压缩
- TacRefineNet：纯触觉抓取精炼
- GenForce：触觉力迁移
- SuperTac/DOVE：仿生多模态电子皮肤
- UniVTAC：统一视触觉仿真平台

---

## 7. 部署与工程

### 7.1 边缘部署策略
- 量化：INT8/INT4（QVLA 专门做 action-centric 量化）
- 蒸馏：Shallow-π 从大 Flow VLA 蒸馏到小模型
- Thin Client：本地轻量推理 + 云端重模型（延迟 vs 成本 trade-off）
- 小模型趋势：<3B 参数占领边缘（B9 置信度 **70%** ↑）
- **GigaBrain-0-Small**：840 GFLOPs, 0.13s 推理, 80% 成功率——小模型实用性重要验证
- **AutoQVLA (ICLR 2026)**：自动量化 VLA，30% VRAM 节省
- **RoboECC**：边缘云协同，1274→362ms 延迟
- **Realtime-VLA V2 (03-30)**：真机 VLA 达人类操作速度，0.2mm 精度 PCB 插件，3-4× 快于 demo。关键发现：感知管线延迟（camera 33ms + exposure 55ms + proprioception 50ms + motion lag 150ms ≈ 288ms）是真实瓶颈，非 action decoding——印证推理加速价值有限的判断
- **Fast-FoundationStereo (CVPR 2026)**：零样本双目深度实时化（蒸馏+blockwise NAS+structured pruning），证明 foundation perception 不必牺牲实时性

### 7.2 数据采集方案
- **遥操作**：GELLO/ALOHA（双臂镜像）、数据手套+振触反馈、VR 控制
- **互联网视频**：VITRA 从 Ego4D/Epic 等自动解析 1.2M 人手操作 episodes (26M 帧) → VLA 预训练
- **仿真生成**：RoboGene 用 agentic 方式多样化生成仿真数据
- **真机 RL**：带安全约束的在线探索（最危险但最有效）
- **合成数据引擎**：World Model 生成 → 过滤 → 训练闭环
- **自重置飞轮**：RoboClaw EAP(前向+逆恢复配对)，人工投入-54%
- 核心矛盾：1 小时遥操作 = 数百元，且无法覆盖长尾场景

### 7.3 仿真环境
- **Isaac Sim/Lab** (NVIDIA)：GPU 并行物理 + RTX 渲染，大规模 RL 首选
- **MuJoCo** (DeepMind)：软接触精度高 + 速度快，精细操作仿真
- **SAPIEN/ManiSkill** (UCSD)：零件级交互，灵巧操作
- **PyBullet**：轻量入门
- **Gazebo**：ROS 集成

### 7.4 Sim-to-Real
- Domain Randomization：视觉/动力学参数随机化
- Domain Adaptation：对抗训练对齐仿真/真实分布
- System Identification：用真实数据校准仿真器参数
- 加速比 0.28x（结构性衰退）— 学术界在逃"硬件依赖"

### 7.5 评估体系
- **指标**：Success Rate (SR)、Mean Steps to Success、Intervention Rate、Executable Rate
- **基准**：CALVIN (5 步链式)、LIBERO (**已饱和** 99.2%，ICLR 2026 确认)、SIMPLER (sim↔real 相关性，70-80% SOTA)、ManiSkill、RoboChallenge
- **ICLR 2026 基准校准**：LIBERO 不再是有效信号源（95-98% 区间无区分度）。以后评估论文时 LIBERO 高分需打折。SIMPLER 和真实零样本才是有效基准。
- **统计纪律**：Wilson 区间置信度、EMA checkpoint 选择、A/B 测试协议
- **产业 KPI**（学术不追踪但更重要）：任务成功率、吞吐量、干预率、连续运行时长、部署成本

### 7.6 RL 训练基础设施（RLinf 视角）
- 关键6点：控制频率对齐(10-30Hz vs 125-500Hz)、评估协议固定、KL-to-base 必备、奖励防欺骗、失败当一等数据、先跑通数据面再谈算法
- 最稳路径：BC warmstart → 仿真 RL 大规模改进 → 真机小步安全迭代
- 训练三层：策略学习(BC/RL loss) → 表示对齐(CLIP/InfoNCE) → 安全约束(barrier/jerk)

---

## 8. 产业格局

### 8.1 三大流派
1. **全栈整合派**（Tesla/Figure）：模型+数据+硬件+制造一步打通
2. **垂直突破派**（DYNA/Amazon）：单场景极强→再泛化
3. **生态平台派**（NVIDIA/Google/Meta）：工具链+标准化接口建生态

### 8.2 关键玩家
- **Physical Intelligence (PI)**：π0 系列，Flow Matching 先驱，Robot API 平台化
- **Figure**：Helix 02 全身自主，$2.6B 估值
- **Tesla Optimus**：全栈+数据飞轮。Gen 3 新手部(22-DoF, 50执行器)；**Terafab 量产线 03-21 启动**
- **NVIDIA**：GR00T N1.7 商业部署（LG/NEURA 采纳）+ N2 预告（"新环境 2x+ 成功率"）+ Isaac Lab + Cosmos — 做机器人的 CUDA（生态锁定 52% 置信度）
- **ACE Robotics (商汤旗下)**：Kairos 3.0-4B 开源实时生成式 WM，72x>Cosmos 2.5，跨 embodiment（Agilex PIPER/Unitree G1/Galaxy G1）
- **1X (1X Technologies)**：World Model 路线，EVE/NEO（GTC 2026 展示视频学习新 WM 能力）
- **Amazon**：收购 Fauna Robotics（儿童尺寸社交人形机器人初创，03-24）——巨头入场信号
- **中国阵营**：智元(Agibot)/宇树(Unitree, 2026前两月出货5500+, **R1 Air $4,900 大众市场基准**)/灵初(LimX)/银河通用(Galaxea)/智在无界(Boundless)/XGSynBot(Z1人形发布)/ROBOTERA(100亿RMB估值, 03-23)

### 8.3 产业信号（2026-03，含 GTC 2026）
- 产业融资超 50 亿美元（AI²/Apptronik/Spirit 等）
- Agility×Toyota 签产线部署协议
- **NVIDIA GTC 2026 (03/16-19) 密集信号**：GR00T N1.7 商业部署 + N2 预告、Kairos 3.0 开源、UR AI Trainer、多家人形机器人展示（IntBot/Techman/Noble Machines Moby3）
- **UR AI Trainer × Scale AI**：首个工业级 VLA 数据飞轮产品（力反馈 + 直接扭矩控制 + 结构化训练数据）
- **Noble Machines Moby3**：18 月隐身→商业收入，已部署至财富 500 强客户
- **北京亦庄人形机器人半马** 04-19 正式开赛，03-14/15 完成试跑（20+ 团队）
- **Tesla Terafab** (03-21)：Optimus Gen 3 量产线启动宣言
- **Unitree** 2026 前两月出货 5,500+，全年目标 10,000-20,000
- **Ubtech** 签署 10,000 台产能框架协议；深圳机器人租赁价降至数百元/天
- **Rhoda AI** 获 $4.5 亿 A 轮（03-11），基于数百万公开视频训练机器人智能平台——资本赌"视频数据+端到端"
- **StarVLA** 开源完整 Franka 实机部署案例（03-19）
- **产业量产加速 vs 学术硬件逃逸**：Tesla 2026年底量产、Ubtech 10,000 台、深圳租赁数百元/天 → 产业冲刺；但学术端 tactile(0.26x)/sim_to_real(0.31x)/cross_embodiment(0.26x) 全线衰退
- 学术与产业分道扬镳：学术刷 LIBERO 99.2%→99.5%，产业谈量产落地
- 工具链收敛：LeRobot 成事实标准，v0.5.0 集成 X-VLA backbone
- **VLA+WM 混合架构成行业共识**：Li Auto(MindVLA-o1)/Tesla/XPeng 均采用（36kr 分析）
- 产业从"原型演示"向"量产准备+商业部署+公开场景验证"阶段加速过渡
- **03-24 信号密集**：Unitree R1 Air $4,900（价格下探至消费级）+ Amazon 收购 Fauna Robotics（巨头布局人形）+ ROBOTERA 100 亿 RMB 估值——"高价演示→大众市场+商业化验证"加速
- **NVIDIA Physical AI × AV**：自动驾驶是 NVIDIA Physical AI 最先跑通的主战场（标准化车体+成熟数据闭环+安全工程），GM/Uber/Mercedes 产线整合进行中；对机器人的启示：车是"标准化身体"模板，机器人 Physical AI 路径可能复刻 AV 闭环模式

---

## 9. 领域当前状态（截至 2026-03-31）

### 9.1 核心判断
- **执行层收敛**：Action Head(Flow Matching 胜) + 后训练(RL 胜)
- **认知层发散**：World Model 多路径探索（pixel→latent→structured planner 三条路线）
- **领域处于"修 bug 阶段"**：174 篇论文仅 3 篇突破性(1.7%)，无架构创新
- **方法论讨论热度首次超过实验室动态** — 从"谁在做"转向"怎么做"
- **ICLR 2026 全景**：164 篇 VLA 提交(vs ICLR 2025 的 9 篇, 18× 增长)；VLM backbone 与下游 VLA 性能**无相关性**(VLM4VLA)；零样本差距巨大(开源 VLA << π0.5/Gemini-Robotics)；数据质量研究极少(OXE "大部分低质量数据")
- **GTC 2026 产业信号**：GR00T N1.7→N2（研究品→商业部署）、Kairos 3.0（WM 延迟瓶颈被解决）、UR AI Trainer（数据飞轮产品化）——产业加速度明显快于学术

### 9.2 速度异常（双周报 03-25 更新）
| 方法族 | 14d加速比 | 7d加速比 | 趋势 |
|--------|-----------|----------|------|
| language_grounding | 2.53x | 0.46x | ⚠️ 爆发后衰退——"推理时修复"红利3周内吃完 |
| rl_finetuning | 1.77x | 0.52x | 仍dominant但momentum declining |
| world_model | — | 0.75x | momentum cooling，社区耐心耗尽 |
| flow_matching | — | 0.89x | **唯一 stable**，静默胜出（工程选择非理论胜利） |
| diffusion_policy | — | 0.70x | 与FM产出持平(各24篇)但momentum更弱 |
| dexterous_hand | — | 0.62x | 碾压 tactile 4:1 |
| tactile | — | 0.26x | 结构性衰退（学术逃"硬件依赖"） |
| sim_to_real | — | 0.31x | 结构性衰退 |
| cross_embodiment | — | 0.26x | 结构性衰退 |
| instruction_tuning | — | 0.05x | 已死 |

### 9.3 基准状态
- LIBERO：**已饱和**（开源 99.2%，闭源 98.6%）— ICLR 2026 Blog 确认"基本已解决"
- SIMPLER：当前最有效学术基准(70-80% SOTA)
- RLBench：VLA"远落后于 3D SOTA"——开放世界仍难
- RoboChallenge：差异化赛道（仅 2 次 SOTA 变动/5%）——唯一未饱和基准，但可能是"低关注度陷阱"
- CALVIN：**已饱和**——与 LIBERO 合计承包 75% 的 SOTA 更新(40次中30次)
- **零样本差距**：开源 VLA 在 benchmark 上接近天花板，但真实零样本远落后 π0.5/Gemini-Robotics

### 9.4 关键预测（可追踪）
1. RL finetuning 8 周内出现"稳定性"子赛道（截止 2026-05-06）
2. LeRobot v0.6.0 将 Flow Matching 设为默认 Action Head（截止 2026-04-23）
3. 首个产线场景 VLA 基准由产业联盟发布（截止 2026-06-01）
4. Instruction Tuning 论文 8 周内跌破 1%/月（截止 2026-05-06）
5. **[新]** flow_matching 4 周内跨域信号突破 3 条（截止 2026-04-22）
6. **[新]** CALVIN/LIBERO 新 SOTA 更新频率 3 周内下降 50%（截止 2026-04-15）
7. **[新]** 6 周内至少 1 个新基准发布（截止 2026-05-06）
8. **[新]** 触觉方向 3 周内再出⚡论文（OmniVTA 跟进，截止 2026-04-15）

### 9.5 新兴趋势：记忆 VLA
- MEM (DeepMind/Stanford, 03-16)：双尺度记忆(video短期+language长期)，15分钟长时域任务
- ReMem-VLA (TU Munich, 03-17)：双层递归记忆查询，超越 π0.5/OpenVLA-OFT
- MemoryVLA (作为 baseline 被引用)
- **初步判断**：长时域记忆(>5分钟任务)是 VLA 从 demo 级→实用级的关键瓶颈。3 个独立团队在 2 天内出现 = 赛道形成早期信号。2026-04 前再出现 2+ 个独立工作则考虑创建新 Phase

---

## 10. 深度专题

### 10.1 π0 系列架构详解

**π0 (2024)**：PaliGemma 3B (SigLIP 视觉编码 + Gemma 2B 语言) + Flow Matching 动作头。学习速度场 v(x,t) 将噪声分布映射到动作分布，沿直线路径（rectified flow）。ODE solver 1-10 步推理 → 50Hz+ 控制。核心创新：首次证明大 VLM 可以高频输出精密动作。

**π0.5 (2025)**：分层推理——高层 VLM 异步语义推理 + 低层同步 50Hz 动作输出。训练用 FAST token 化（DCT+BPE 压缩），推理用 Flow Matching。Co-training：机器人 + 互联网视频 + 仿真，loss masking 分数据源。实现开放世界"做任何家务"的泛化。

**π0.6 / π*0.6 (2025)**：5B VLM + 10M 参数 Action Expert（轻量独立模块）。π0.6 = 监督学习基线；π*0.6 = Recap 算法（离线 RL 自我改进）。Recap 流程：收集 on-policy rollout → VLM 自动打分 → 筛选高分轨迹 → 重新训练。Knowledge Insulation 防止动作训练破坏语义能力。成果：2× 吞吐提升，2× 失败率下降。

### 10.2 World Model 演进路线

```
阶段 1: 评估器 (WorldEval) — 能否不用真机就评估策略优劣？
阶段 2: 标准化评估 (WorldArena/Ctrl-World) — 如何统一 WM 基准？
阶段 3: 数据引擎 (VLAW) — WM 生成合成轨迹喂给策略训练
阶段 4: 动作生成基底 (DreamZero/WAM) — WM 直接取代 action model？
```

关键进展：
- **VLAW**：on-policy rollout 微调 WM → 生成合成轨迹 → 过滤式 BC 训练，+39.2% 成功率
- **DreamZero/WAM**：World Model 即零样本策略，比较三条路线(解耦/端到端/统一多任务)
- **PlayWorld**：自主探索→WM→RL 全闭环，+65% 真机成功率
- **AtomVLA**：LLM 分解任务为原子子任务 + 预测性潜在 WM + 离线 GRPO，LIBERO 97%
- **StructVLA** (03-17)：WM 重构为 structured planner(预测稀疏运动学里程碑帧)，SimplerEnv 75.0%，LIBERO 94.8%。第三种 WM 范式
- **ACE Kairos 3.0-4B** (03-17)：商汤旗下开源实时生成式 WM，4B 参数 Jetson Thor 实时运行，72x>Cosmos 2.5（但对比基准不公平：4B vs 14B+），跨 embodiment 部署宣称（待同行评审）。解决 WM 延迟瓶颈的首个工程证据
- **Cosmos 3 (03-25)**：NVIDIA 首个统一 World Foundation Model，核心产品化信号
- **NC AI WFM (03-25)**：latent action 直接生成，25% GPU 成本达 80% 性能，低成本路线验证
- **Fast-WAM (03-19)**：质疑 WM 是否需要测试时未来想象——与 Chain of World + Simulation Distillation 形成对话，WM 使用范式在分化
- **VLA+WM 混合架构行业趋势**：Li Auto(MindVLA-o1 内嵌 Predictive Latent WM)/Tesla(Neural World Simulator)/XPeng 均采用——WM 从可选组件→标准配置演进中
- 核心张力：好视频 ≠ 好评估器，好评估器 ≠ 好规划器；WM 从侧模块→系统工具→核心基底
- **VLA-MBPO (03-30)**：UMM 做 WM + multi-view consistency + chunk-level branched rollout——2 月来第 4 个 WM+RL 框架（+ GigaBrain/WoVR/World-VLA-Loop），方法论子问题逐个被解决但碎片化风险
- **Scaling Sim-to-Real (03-30)**：3D generative worlds + RL，真机 21.7%→75%（+53.3pp），WM-as-data-factory 维度的新验证——但任务复杂度和 RL-specific ablation 待确认
- ⚠️ 概念区分待办："full generative WM" vs "learned dynamics model/predictive latent model"——行业混用，**B4 四子类需正式区分**：feature-extractor (DiT4DiT) / simulator (VLA-MBPO/WoVR) / data-factory (Scaling Sim-to-Real) / causal-reasoner (尚无验证)

### 10.3 小模型路线 (<3B)

| 模型 | 参数 | LIBERO | 核心技巧 |
|------|------|--------|----------|
| Evo-1 | 450M | 94.8% | RT-2 参数的 1.4%，证明模型大小≠控制能力 |
| SmolVLA | 500M | ~92% | 极致压缩 VLM |
| ControlVLA | 770M | ~93% | 控制专精设计 |
| Eva-VLA | 700M | ~91% | 高效视觉编码 |

启示：边缘部署不需要 7B；但小模型在开放世界泛化上仍有明显差距。

### 10.4 推理与规划

- **Chain of Thought 四种模式**：显式文本 / 结构化 JSON / 隐式潜在 / 交错逐步
- **OneTwoVLA**：单模型自适应 System 2(深度推理)/System 1(快速执行) 切换，用 [BOR]/[BOA] token
- **Thinker VLM**：UBTech 具身规划模型（不直接输出动作），4B/7B，处理 ego-view 混淆
- **ReconVLA**：通过注视区域重建辅助损失防止注意力漂移，隐式空间接地

### 10.5 跨模态迁移与数据规模化

- **VITRA**：自动从人类活动视频(Ego4D/Epic)提取 1.2M 机器人式 episodes，逐帧 3D 手部运动恢复
- **跨模态映射逻辑**：互联网视频学"语义动作规范"（开门先握把手）→ 精细力控交给底层算法/少量真机微调
- **ABot-M0 UniACT**：统一 6 个数据集(6M 轨迹, 20+ 具身)，EEF-delta + rotation-vector 标准化
- **RoboGene**：Agentic 多样化仿真数据生成，提升 VLA 预训练质量

### 10.6 分层控制架构（以 Figure Helix 02 为例）

```
S2 (语义层): VLM 输出语义 latent — 低频（~2-5Hz）
  ↓
S1 (运动层): 200Hz 全身目标生成（locomotion + manipulation）
  ↓
S0 (执行层): 1kHz 学习式先验控制（接触/平衡/稳定性）
```

Helix 02 训练数据：>1000h 人类运动 + >200k 仿真环境。无状态机，统一处理行走+操作。
此分层模式(B6 置信度 75%)正在成为人形机器人标准架构。

---

## 11. 关键论文速查（按影响力排序）

| 论文 | 核心贡献 | 影响 |
|------|----------|------|
| **里程碑** | | |
| π0 (2024) | Flow Matching + VLM = 高频精密控制 | 定义 Action Head 新范式 |
| π0.5 (2025) | 分层推理 + co-training 开放世界 | 泛化路线验证 |
| π0.6 Recap (2025) | 离线 RL 自我改进闭环 | 定义后训练新范式 |
| RT-2 (2023) | VLM → VLA 语义泛化涌现 | 证明大模型路线可行 |
| OpenVLA (2024) | 开源 7B VLA + LoRA 生态 | 民主化 VLA 研究 |
| Diffusion Policy (2023) | 去噪生成连续动作 | 建立连续动作基线 |
| **World Model** | | |
| DreamZero / WAM (2026) | World Model = 零样本策略 | WM 功能角色跃迁 |
| PlayWorld (2026) | 自主探索→WM→RL 闭环 | +65% 真机成功率 |
| VLAW (2026) | VLA × WM 迭代共进化 | on-policy WM 校准 +39.2% |
| AtomVLA (2026) | 原子子任务 + 潜在 WM + 离线 GRPO | 无需在线试错 |
| StructVLA (2026) | WM→稀疏运动学里程碑 planner | 第三种 WM 范式 |
| ACE Kairos 3.0 (2026) | 4B 实时生成式 WM，72x>Cosmos | WM 延迟瓶颈首次工程解决 |
| Cosmos 3 (2026) | 首个统一 WFM，NVIDIA 产品化 | WM 工业级基础设施 |
| NC AI WFM (2026) | Latent action 生成，25% GPU 成本 | 低成本 WM 路线 |
| Fast-WAM (2026) | 质疑 WM 测试时想象必要性 | WM 使用范式分化 |
| PLD (CMU, 2026) | 残差RL+蒸馏闭环，ICLR 2026 | B3 第二独立验证 |
| **触觉** | | |
| MoDE-VLA (2026) | 残差力觉注入，量化消融-11%/-8% | 触觉不可替代性实证 |
| TacVLA (2026) | Contact-aware gating 触觉 VLA | 触觉优雅集成方案，+60%/2.1× |
| TaF-VLA (2026) | 触觉力对齐注入 VLA | 触觉融合新范式 |
| TacMamba (2026) | 快慢双通路触觉压缩 | 触觉反射层架构 |
| OmniVTA (2026) | 视触融合世界模型 | 触觉作为 WM 输入模态新路线⚡ |
| UniVTAC (2026) | 统一视触觉仿真平台 | 仿真标准化 |
| **数据与效率** | | |
| VITRA (2026) | 人类视频→1.2M 机器人 episodes | 数据规模化路线 |
| SimVLA (2026) | 0.5B 达 98.6% LIBERO | 训练 recipe > 架构复杂度 |
| FAST (2024) | DCT+BPE 动作 token 压缩 | 5× 训练加速 |
| Shallow-π (2026) | Flow VLA 知识蒸馏 18→6 层 | 边缘部署 <1% 性能损失 |
| QVLA (2026) | 动作敏感性量化 | 部署优化 |
| OFP (2026) | 单步 flow 100× 加速 | FM 推理速度再飞跃 |
| RoboClaw (2026) | EAP 自重置飞轮 -54% 人工 | 数据收集效率 |
| **语言与推理** | | |
| LangGap (2026) | 语言理解缺口四维诊断 | 语言接地修复框架 |
| ReViP (2026) | 视觉一致性验证修正错误补全 | 推理时闭环修复 |
| OneTwoVLA (2026) | 自适应 S1/S2 推理切换 | 统一快慢思维 |
| ReconVLA (2026) | 隐式空间接地(注视重建) | 防注意力漂移 |
| **记忆** | | |
| MEM (2026) | 双尺度VLA记忆(video+language) | 15分钟长时域 |
| ReMem-VLA (2026) | 双层递归记忆查询 | 超越 π0.5/OpenVLA-OFT |
| **其他** | | |
| GR00T N1.7 (2026) | 开源 VLA 商业部署(LG/NEURA) | NVIDIA 生态锁定信号 |
| Helix 02 (2026) | S2→S1→S0 分层全身自主 | 人形架构标杆 |
| ABot-M0 (2026) | UniACT 6M 轨迹统一 | 跨具身基础 |
| RDT2 (2026) | 零样本跨具身迁移 | 泛化验证 |
| AR-VLA (2026) | 自回归 Action Expert, SIMPLER 61.5% | FM 挑战者 |
| GigaBrain-0-Small (2026) | 840 GFLOPs, 0.13s, 80% 成功率 | 小模型边缘可行性 |
| AutoQVLA (2026) | 30% VRAM, ICLR 2026 | 自动量化 VLA |
| Golden Ticket (2026) | 单样本 No 改进策略 | 资源有限团队切入点 |
| **新增 03-26~29** | | |
| VLGOR (2026) | VLM 生成物理一致虚拟轨迹 + 离线 RL | VLM 替代 LLM 做 RL 数据增强（仅仿真） |
| EquiBim (2026) | 双臂对称等变正则化，模型无关 | 即插即用训练技巧，无架构修改 |
| Fast-FoundationStereo (CVPR 2026) | 零样本立体匹配压到实时（蒸馏+NAS+剪枝） | 证明 foundation perception 可实时部署 |
| **新增 03-30** | | |
| DFM-VLA (2026) | Discrete Flow Matching，CALVIN 4.44/LIBERO 95.7%/真机 70.8%，2.4× 推理加速 | **B5 强下行信号**——discrete FM 全面击败 continuous FM+diffusion+AR |
| VLA-OPD (2026) | On-Policy Distillation 桥接 SFT↔RL，1-traj init → 93.4%，3× 样本效率 | RL→Distillation→Deploy 流水线新范式（依赖 RL teacher） |
| Scaling Sim-to-Real (2026) | 3D generative worlds + RL，真机 21.7%→75%（+53.3pp） | 套利 #3 第三个验证，WM-as-data-factory 又一维度 |
| VLA-MBPO (2026) | UMM 做 WM + multi-view consistency + chunk-level branched rollout | WM+RL 第 4 个框架（+ GigaBrain/WoVR/World-VLA-Loop），方法论成熟度 |
| Realtime-VLA V2 (2026) | 真机达人类速度，0.2mm 精度 PCB 插件，3-4× 快于 demo | 部署工程成熟度；感知管线延迟 ~288ms 是真实瓶颈 |
| Ruka-v2 (2026) | 开源灵巧手 v2，+2 DOF，51.3% 完成时间减少 | Phase 6 基础设施层面积极信号 |

---

## 12. 开源基础设施与工具链

| 工具 | 类别 | 最新版本 | 定位 |
|------|------|----------|------|
| LeRobot | 训练框架 | v0.5.0 (2026-03) | 事实标准，集成 X-VLA backbone |
| Isaac Lab | 仿真+RL | - | GPU 并行训练首选 |
| MuJoCo | 物理引擎 | v3.6.0 (2026-03) | 精细接触仿真 |
| SAPIEN | 仿真 | v3.0.3 (2026-03) | 零件级交互 |
| Genesis | 仿真 | v0.4.3 (2026-03-16) | 新兴综合仿真 |
| GELLO/ALOHA | 数据采集 | - | 遥操作硬件方案 |

**开源分级**：展示型(算法 demo) < 生态锁定型(厂商工具) < 基础设施型(全 CAD+栈+know-how 透明)
工具链正在快速收敛，继续维护独立训练代码库的团队将面临"无人复用"困境。

---

## 13. 产品与市场

- **PMF 真标准**：持续用户留存 + 可量化 ROI + 可靠性验证（非 demo 级别）
- **人形机器人**：Figure/Tesla/1X/Agility 领跑，中国 Unitree/LimX/银河通用追赶；2026 年进入小批量产线部署但距大规模量产仍有 2-3 年
- **产业与学术脱节**：学术卷 LIBERO 99.2%→99.5%，产业谈"产线部署""量产基地"——当基准分数与客户付费标准脱钩，学术研究合法性基础正在松动

---

## 14. 高频面试要点

**Q: VLA 和传统机器人学习有什么本质区别？**
A: 传统方法是模块化流水线(感知→规划→控制)，VLA 是端到端：视觉+语言直接映射到动作。优势是涌现泛化能力，代价是可解释性和安全保障。

**Q: 为什么 Flow Matching 胜出？**
A: Diffusion 走随机路径需 50-100 步去噪，Flow 走最优传输直线仅需 1-10 步。同等精度下推理快 10 倍+，首次让大模型支持 50Hz+ 实时控制。OFP 进一步证明单步 flow 可超越多步版本。

**Q: VLA 最大瓶颈是什么？**
A: 数据。真机数据采集成本是 #1 约束（1 小时数百元，无法覆盖长尾）。三条绕过路径：互联网视频跨模态迁移、World Model 生成合成数据、Sim2Real。

**Q: RL 后训练为什么是突破口？**
A: BC 只能学到专家分布内行为，分布外崩溃。RL 通过在线探索收集分布外数据 + 自动奖励(VLM 打分) → 突破 BC 天花板。π0.6 Recap 是典型代表。

**Q: 触觉为什么重要？**
A: 视觉给坐标，语言给意图，触觉给接触相位真反馈。遮挡下力/形/质不可视觉观测，精密操作的最后 1cm 靠触觉闭环。MoDE-VLA 量化证明：去除力觉-11%，去除触觉-8%。

**Q: World Model 当前状态？**
A: 从 nice-to-have 预测器 → 评估器 → 规划器 → 动作生成基底 演进中。PlayWorld 已证明 WM→RL 闭环可行(+65%)，但接触密集任务的物理幻觉是致命障碍。方法论分化为 pixel/latent/structured/WAM 四条路线。Cosmos 3（NVIDIA 产品化）+ NC AI WFM（25% GPU 成本达 80%性能）= 双工业级信号。置信度 70%↑，Phase 4 持续超临界(60%)。

**Q: 小模型能替代大模型吗？**
A: 在受限场景可以。Evo-1 (450M) 达 LIBERO 94.8%，仅 RT-2 参数的 1.4%。GigaBrain-0-Small(840 GFLOPs, 0.13s, 80%)进一步验证。AutoQVLA(ICLR 2026)节省30% VRAM。RoboECC 边缘云协同将延迟从 1274→362ms。置信度已升至 70%。但开放世界泛化仍需大模型。

**Q: SimVLA 的启示？**
A: 0.5B 模型通过正确训练 recipe（数据 shuffling、归一化、LR schedule）达 98.6% LIBERO。关键："沉默旋钮"(shuffling off = 9.9% vs on = 98.6%) 比花哨模块重要得多。数据策略 > 架构创新(B0)的直接证据。

**Q: Knowledge Insulation 是什么？**
A: 双轨训练防灾难性遗忘：VLM backbone 只学离散 token（保留语义能力），Action Expert 独立学连续控制，梯度隔离不互传。π0.6 核心技巧之一。

**Q: 当前领域最大风险？**
A: 学术与产业脱节。学术在 LIBERO 上刷 0.3% 提升，产业需要"产线任务成功率""维护周期"。工具链(LeRobot)收敛加速了实验民主化，但 54 篇 RL 论文中多数是调参报告而非方法创新——"工具易得≠方法成熟"。

**Q: ICLR 2026 揭示了什么？**
A: 164 篇 VLA 提交(18× 年增长)。关键发现：VLM backbone 大小与 VLA 性能无关(VLM4VLA)；LIBERO 已饱和；Discrete Diffusion VLA 是新兴趋势(4篇并发)；零样本差距依然巨大——开源 VLA 远落后 π0.5/Gemini-Robotics。

---

## 15. 校准纪律（使用本记忆时的注意事项）

1. **谦逊折扣**：所有 >80% 置信度已乘 0.9（LLM 在此区间系统性过度自信）
2. **保守偏误修正**：强证据最小更新 ±5%，Bull+Bear 共识最小 ±10%。**禁止 2-3% 安慰性微调**——要么 ≥5% 要么不调整(记录为观察中)
3. **逆共识保护**：逆共识信号的筛选阈值为正常的 1/3（防止系统性杀死异见）
4. **高确定性 = 高风险**：你最确定的判断，恰恰是最需要被挑战的
5. **生存者偏误警告 🔴**：系统零失败案例记录。每次分析需主动搜索失败/无法复现/部署失败信号
6. **本文档截止日期**：2026-03-29，VLA 领域每周都有重大变化

---

*生成自 KW_VLA Handbook v3 | 330+ 篇源文件 → ~16K tokens 压缩索引 | 定时任务每日 09:00 增量更新*
