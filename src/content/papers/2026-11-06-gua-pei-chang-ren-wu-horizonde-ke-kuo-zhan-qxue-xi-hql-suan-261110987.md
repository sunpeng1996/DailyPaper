---
title: Horizon-Scalable Q-Learning
title_zh: 适配长任务horizon的可扩展Q学习（HQL）算法
authors:
- Haoran Xu
- Pragya Srivastava
- Xinjie Liu
- Siddhant Agarwal
- Amy Zhang
affiliations:
- The University of Texas at Austin
arxiv_id: '2611.10987'
url: https://arxiv.org/abs/2611.10987
pdf_url: https://arxiv.org/pdf/2611.10987
published: '2026-11-06'
collected: '2026-11-10'
category: Training
direction: 离线强化学习 · 长horizon价值估计
tags:
- Offline RL
- Q-Learning
- Temporal Difference
- Long-Horizon
- Off-Policy Correction
one_liner: 自动平衡单步与多步TD回报，实现长horizon离线RL下的高精度Q值学习
practical_value: '- 电商全链路转化价值估计、长周期用户序列推荐场景，可借鉴HQL动态步长TD逻辑，平衡Q值估计的偏差与方差，避免长序列下的误差累积

  - 离线训练用户行为价值模型时，可复用HQL无动作密度的off-policy修正规则，兼容扩散模型、流模型等生成式策略的联合训练

  - 推荐系统多步决策Agent（如动态定价、智能营销触达）训练时，可替换原有固定步长多步TD，适配不同用户行为路径的步长需求'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
长horizon离线强化学习场景下，单步TD学习的每步小误差会沿轨迹累积，导致早期状态估值严重失准；固定步长多步TD会因行为策略次优引入额外偏差，无统一固定步长适配全轨迹。
### 方法关键点
提出Horizon-Scalable Q-Learning（HQL），自动平衡单步与多步回报：仅当critic对数据集动作的估值不低于BC策略采样的N个最优动作估值时，才扩展多步目标，否则回退到单步目标；该规则是无需动作密度的原则化off-policy修正，兼容流模型、扩散策略等高表达性策略。
### 关键结果
组合锁任务中跨不同horizon均规避了单步/多步TD的失效问题，在长horizon OGBench、OCBench任务上性能全面优于现有horizon缩减方法
