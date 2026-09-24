---
title: 'Limiting-Kernel Q($λ$): Bridging Short and Long Horizons'
title_zh: Limiting-Kernel Q(λ)：衔接长短时序的强化学习值估计算法
authors:
- Tolga Ok
- Arman Sharifi Kolarijani
- Peyman Mohajerin Esfahani
- Mohamad Amin Sharifi Kolarijani
affiliations:
- Delft University of Technology
- Alpha Brain Technologies
- University of Toronto
arxiv_id: '2609.27741'
url: https://arxiv.org/abs/2609.27741
pdf_url: https://arxiv.org/pdf/2609.27741
published: '2026-09-23'
collected: '2026-09-24'
category: Training
direction: 强化学习值估计 · 长序列任务优化
tags:
- Reinforcement Learning
- Value Estimation
- Long Horizon
- Actor-Critic
- Off-policy
one_liner: 推出复杂度与n步估计相当的LKQL值估计器，兼顾长短时序，提升长序列任务策略优化效果
practical_value: '- 做推荐系统时序决策（如多步流量分发、长周期用户留存优化）时，可参考LKQL思路，在n步截断值估计基础上增加长时域近似模块，保持计算复杂度不变的前提下提升长序列任务效果

  - 基于Actor-Critic框架的电商营销Agent、动态定价Agent训练时，可直接替换原有的n步值估计器为LKQL，无需大幅修改架构即可提升策略收敛速度与最终性能

  - 连续状态空间的RL任务（如动态排序、实时出价）可复用LKQL的收敛性证明思路，降低长时序值估计的方差与偏差权衡成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
价值类强化学习中，n步截断值估计计算高效但仅适配短时域，利用转移动力学全局结构的方法能加速策略评估，但内存、计算开销大，难以扩展到大/连续状态空间场景，长短时域能力难以兼顾。
### 方法关键点
Limiting-Kernel Q(λ)（LKQL）是一种离策略值估计器，结合n步截断与基于限域核的长时域近似，复杂度与n步估计器相当，可直接嵌入On-policy、Off-policy的Actor-Critic算法；理论证明非周期性、近On-policy场景下，n足够大时LKQL算子的策略评估收敛速率优于截断版本，固定行为策略下有限MDP中LKQL几乎必然收敛到最优值。
### 关键结果
在MuJoCo连续控制基准上，多数场景下性能优于n步基线，长时域任务提升尤为显著。
