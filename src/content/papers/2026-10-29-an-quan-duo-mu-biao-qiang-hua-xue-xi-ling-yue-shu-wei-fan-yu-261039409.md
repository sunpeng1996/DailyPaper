---
title: 'Safe Multi-Objective Reinforcement Learning: Zero Constraint Violation and
  Primal-Averaging Convergence'
title_zh: 安全多目标强化学习：零约束违反与原平均收敛
authors:
- Chenxi Li
- Yao Shu
- Siyang Gao
- Shuang Qiu
- Guangxin Jiang
affiliations:
- Harbin Institute of Technology
- The Hong Kong University of Science and Technology (Guangzhou)
- City University of Hong Kong
arxiv_id: '2610.39409'
url: https://arxiv.org/abs/2610.39409
pdf_url: https://arxiv.org/pdf/2610.39409
published: '2026-10-29'
collected: '2026-10-31'
category: Other
direction: 安全多目标强化学习 · 零约束违反算法
tags:
- Multi-Objective RL
- Safe RL
- Constrained MDP
- Pareto Optimality
- Sample Efficiency
one_liner: 提出两类样本高效的安全多目标强化学习算法，保障训练全阶段零约束违反
practical_value: '- 电商多目标RL排序/流量分配场景可复用「乐观奖励估计+悲观成本边界」思路，平衡GMV、转化目标的同时严格控制资损、超售等硬约束

  - 推荐Agent动态策略调优可参考无预设偏好的先探索后适配框架，无需反复线上交互即可快速适配不同业务目标偏好，降低试错成本

  - 广告投放、营销预算控制等零违规要求场景，可复用算法的零约束违反保障逻辑，替代现有软约束惩罚方案，避免线上事故'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
多目标强化学习（MORL）落地时需平衡冲突目标同时满足安全约束，现有算法无法在未知动态探索过程中保证全程无约束违反，易引发资损、合规等业务风险

### 方法关键点
1. 针对给定目标偏好场景，结合乐观奖励估计与悲观成本边界学习安全帕累托最优策略，保证训练全程每一步执行策略都满足约束
2. 针对无预设偏好场景，提出先安全探索、后适配任意偏好的框架，无需后续交互即可生成适配目标的安全策略
3. 进一步放松对初始严格安全策略的要求，仅产生最多常数级累计约束违反

### 关键结果数字
两类算法均以高概率保证T轮训练全程零约束违反，给定偏好算法次优gap为$	ilde{O}(1/ead{T})$，无偏好算法次优gap为$	ilde{O}(1/ead{T}+1/ead{K})$，是首个样本高效且执行策略全程安全的MORL算法
