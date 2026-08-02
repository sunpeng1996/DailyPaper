---
title: Hierarchical Multilevel Monte Carlo for Order-Optimal Neural Actor-Critic in
  Average-Reward CMDPs
title_zh: 平均回报约束MDP中层级多级蒙特卡洛最优阶神经Actor-Critic方法
authors:
- Ankur Naskar
- Vaneet Aggarwal
affiliations:
- Indian Institute of Science
- Purdue University
arxiv_id: '2607.28390'
url: https://arxiv.org/abs/2607.28390
pdf_url: https://arxiv.org/pdf/2607.28390
published: '2026-07-30'
collected: '2026-08-02'
category: Agent
direction: 带约束强化学习 · 最优阶收敛保证
tags:
- CMDP
- Actor-Critic
- Multilevel Monte Carlo
- Neural Tangent Kernel
- Reinforcement Learning
one_liner: 提出层级MLMC神经critic解决偏差成本权衡，首次给出带神经critic的平均回报CMDP最优阶收敛保证
practical_value: '- 带约束的推荐Agent场景（如兼顾GMV提升与成本/合规约束）可借鉴层级MLMC思路，平衡critic估计偏差与采样成本

  - 无限 horizon 长期平均收益优化的推荐策略场景，可复用本文Primal-Dual自然Actor-Critic框架，无需提前估计混合时间

  - 采用深度网络做critic的RL推荐系统，可参考NTK视角下的偏差-成本权衡分析，优化critic训练效率'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有带线性critic的原对偶Actor-Critic方法理论性质成熟，但带神经critic的平均回报CMDP场景下一直缺乏最优阶收敛保证；核心瓶颈是神经critic估计存在固有偏差-成本权衡：降低偏差会大幅提升优化成本，无法在原对偶框架下实现最优阶收敛。

### 方法关键点
提出层级Multilevel Monte Carlo (MLMC) 神经critic，同时在轨迹采样和critic优化两个维度做去偏，仅需对数级期望采样成本即可达到长训练步的critic偏差水平；基于该估计器设计原对偶自然Actor-Critic算法。

### 关键结果
最优性间隙与约束违反度均达到$	ilde{O}(T^{-1/2})$阶，是首个针对无限 horizon 平均回报CMDP、通用策略参数化+神经critic的最优阶收敛证明，无需已知底层混合时间，无约束场景下结果同样具备创新性。
