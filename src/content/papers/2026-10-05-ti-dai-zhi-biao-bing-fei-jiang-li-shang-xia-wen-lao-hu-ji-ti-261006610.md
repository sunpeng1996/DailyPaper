---
title: 'The Surrogate Is Not the Reward: Post-Surrogate Primary-Outcome Acquisition
  in Contextual Bandits'
title_zh: 替代指标并非奖励：上下文老虎机中替代观测后的主结果采集
authors:
- Kyungbok Lee
- Michael R. Kosorok
affiliations:
- University of North Carolina at Chapel Hill, Department of Biostatistics
arxiv_id: '2610.06610'
url: https://arxiv.org/abs/2610.06610
pdf_url: https://arxiv.org/pdf/2610.06610
published: '2026-10-05'
collected: '2026-10-06'
category: RecSys
direction: 上下文老虎机 · 在线采样效率优化
tags:
- Contextual Bandit
- Online Learning
- Sample Efficiency
- Surrogate Outcome
- Regret Minimization
one_liner: 提出ASB算法，结合决策相关性与残差不确定性分配主结果采集预算，降低上下文老虎机后悔值
practical_value: '- 电商/短视频推荐的在线学习、AB测试场景，可复用ASB双因子采样逻辑：先按策略评估重要性分配主指标采样预算，再结合点击、停留等替代指标的残差不确定性动态调整，大幅降低复购、GMV、完播率等高成本核心指标的采集成本

  - 新策略冷启动、小流量测试等预算有限场景，无需全量采集核心业务指标，通过ASB动态采样机制即可保证策略学习的regret最优，平衡替代指标偏差与采样成本

  - 在线策略评估时可参考论文的regret边界推导，量化替代指标偏差与采样预算的权衡关系，合理制定核心指标的采样比例，避免不必要的成本浪费'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
上下文老虎机在线学习场景中，主收益（如GMV、用户长期价值）采集成本高，低成本替代指标（如点击、停留）无法完全代表主收益，现有采样方法要么全量采集主收益成本过高，要么仅依赖替代指标会导致策略学习偏差，预算分配效率低。

### 方法关键点
提出Audited Surrogate Bandit（ASB）框架，分两步分配主收益采集预算：
1. 先基于当前策略的决策相关性预设总采集配额；
2. 观测替代指标后，根据替代指标的残差不确定性动态调整配额，优先采集对策略迭代价值更高的样本。

### 关键结果
1. 理论上ASB的regret上界为$	ilde{O}[\sqrt{KT\log\N}\\{1+ackslashackslashackslashackslashackslashackslashsqrt{T/B}\}]$；
2. 二行动场景下ASB可实现有界regret，而替代观测前决策的方法最坏case regret为$ackslashackslashOmega(T/B)$；
3. 合成实验中ASB regret显著低于仅用单因子的基线方法，KuaiRec短视频推荐基准上，相比仅考虑决策相关性的采样方法，ASB的regret优势随预算提升先扩大后缩小
