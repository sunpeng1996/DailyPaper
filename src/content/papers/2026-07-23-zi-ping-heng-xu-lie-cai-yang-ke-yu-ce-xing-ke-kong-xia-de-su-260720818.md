---
title: 'Self-Balancing Sequential Sampling: Fast Convergence with Controlled Predictability'
title_zh: 自平衡序列采样：可预测性可控下的快速收敛方法
authors:
- Zachary McNulty
- Daniel Raban
affiliations:
- Department of Mathematics, University of California, Berkeley
- Department of Statistics, University of California, Berkeley
arxiv_id: '2607.20818'
url: https://arxiv.org/abs/2607.20818
pdf_url: https://arxiv.org/pdf/2607.20818
published: '2026-07-23'
collected: '2026-07-25'
category: Other
direction: 序列采样优化 · 收敛与可预测性平衡
tags:
- Sequential Sampling
- Entropy Regularization
- Stochastic Process
- Convergence Optimization
one_liner: 提出兼顾采样收敛速度与不可预测性的自平衡序列采样方法，收敛速率O(n⁻¹)优于IID采样的O(n⁻¹/2)
practical_value: '- 推荐系统负采样、召回池动态采样场景可直接复用该方法，在保证采样分布快速拟合目标分布的同时，避免采样规律被黑灰产破解

  - 电商内容/广告流量分配、A/B测试分组场景可替代传统IID采样，降低重复曝光/长周期未覆盖问题，同时避免分组规则可预测导致的实验偏差

  - Agent多轮决策的场景采样模块可引入该熵正则化优化思路，平衡探索效率与决策行为的不可预测性'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
序列采样场景（如审计调度、代表性采样、实验分组）普遍存在双重需求：既要采样经验分布快速收敛到目标分布，又要避免采样规则可预测被利用；传统IID采样收敛速率仅O(n⁻¹/²)，确定性采样可预测性过高，二者均无法兼顾需求。

### 方法关键点
基于马尔可夫采样器的不变性构造自平衡采样器，通过自适应调整采样概率偏差实现双目标平衡，可通过熵正则化优化框架求解，具备随机镜像下降的理论解释，实现逻辑简单轻量化。

### 关键结果
1. 收敛速率达最优O(n⁻¹)，显著优于IID采样的O(n⁻¹/²)，收敛速度与偏差参数显式相关；
2. 是平衡收敛速度与采样不可预测性的熵正则化优化问题的唯一解；
3. 弱偏差场景下，标准化后的计数过程在扩散极限下收敛到Ornstein-Uhlenbeck过程。
