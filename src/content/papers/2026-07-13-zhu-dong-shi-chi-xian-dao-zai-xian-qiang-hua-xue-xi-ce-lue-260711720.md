---
title: Active Offline-to-Online Reinforcement Learning
title_zh: 主动式离线到在线强化学习策略选择框架
authors:
- Alper Kamil Bozkurt
- Shangtong Zhang
- Yuichi Motai
affiliations:
- Virginia Commonwealth University
- University of Virginia
arxiv_id: '2607.11720'
url: https://arxiv.org/abs/2607.11720
pdf_url: https://arxiv.org/pdf/2607.11720
published: '2026-07-13'
collected: '2026-07-14'
category: Training
direction: O2O强化学习 · 主动策略选择优化
tags:
- Reinforcement-Learning
- Offline-to-Online-RL
- Policy-Selection
- UCB
- Active-Learning
one_liner: 基于UCB的主动策略选择方法，提升有限在线交互预算下O2O-RL调优效率
practical_value: '- 推荐系统离线训练多版本召回/排序策略后，可借鉴UCB主动选择机制分配线上流量，平衡策略评估和效果调优的流量占用，降低单策略全量上线的风险

  - 电商Agent（如智能定价、流量分配Agent）在线交互成本高的场景，可复用基于局部线性预测的性能上界计算方法，用有限流量快速筛选最优策略

  - 小流量AB测试场景可参考该框架的资源分配逻辑，替代固定流量均分或单策略放量的传统方案，提升测试效率'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有离线到在线RL（O2O-RL）流程通常选单个离线最优策略上线调优，调优效果对算法、超参敏感，单策略上线风险高，且未解决有限在线交互预算下，资源分配给策略评估还是调优的权衡问题。
### 方法关键点
1. 首次形式化O2O-RL下有限交互预算的主动调优策略选择问题，明确评估-调优的资源权衡关系；
2. 基于未来性能上置信界（UCB）的主动选择框架，通过在线评估得到的观测拟合局部线性性能预测，推导UCB边界，动态分配交互资源给潜力最高的策略。
### 关键结果
在多组实验中，该方法效果持续优于现有O2O-RL基线，相比单策略全量上线、策略均分预算的方案，有限交互预算的利用率显著提升。
