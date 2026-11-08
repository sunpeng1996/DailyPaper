---
title: Risk-Sensitive Non-Parametric and Kernel Bandits
title_zh: 风险敏感的非参数与核老虎机算法研究
authors:
- Devdan Dey
- Sujoy Bhore
- Avishek Ghosh
arxiv_id: '2611.06489'
url: https://arxiv.org/abs/2611.06489
pdf_url: https://arxiv.org/pdf/2611.06489
published: '2026-11-04'
collected: '2026-11-08'
category: Other
direction: 风险敏感老虎机 · 序贯决策优化
tags:
- Bandit
- Cumulative Prospect Theory
- Regret Bound
- Kernel Method
- Non-Parametric
one_liner: 提出基于累积前景理论的非参数核老虎机算法，风险敏感引入无额外阶数regret损失
practical_value: '- 可将CPT风险敏感评估逻辑引入推荐/广告在线学习链路，替换传统仅用期望收益的目标，适配平台对补贴超支、负反馈风险的管控需求

  - NPCB的均值估计与决策解耦的模块化设计可直接复用，无需重构现有推荐序贯决策的在线训练模块即可快速接入风险控制逻辑

  - 核版本的信息增益regret界结论可指导电商冷启动场景的核函数选型，平衡探索效率与效果损失'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
传统多臂老虎机仅优化期望奖励，无法适配电商、金融等需考虑风险、匹配人类决策偏好的场景，现有风险敏感老虎机多为参数化设定，泛用性差。
### 方法关键点
1. 提出非参数CPT老虎机算法NPCB，将均值估计与基于累积前景理论（CPT）的决策逻辑解耦，支持连续动作空间与臂依赖噪声
2. 拓展支持未知噪声CDF场景，新增分布Eluder维度控制的CDF学习成本
3. 适配核函数场景，给出Kernel-CPT老虎机实现
### 关键结果
- NPCB的CPT regret阶为$	ilde{igcirc}igl(igl(igl(igr)igr)igr)igr)$，与经典非参数老虎机完全对齐，证明引入风险敏感无额外阶数的regret损失
- 核版本regret界与风险中性核老虎机仅差对数因子，性能损失可忽略
