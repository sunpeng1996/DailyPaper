---
title: Offline Deep Q* Estimation with Diffusion Models
title_zh: 基于扩散模型的离线深度最优动作价值函数Q*估计
authors:
- Xiaohong Chen
- Yuling Jiao
- Lican Kang
- Jerry Zhijian Yang
- Chen Zhong
affiliations:
- Yale University
- Wuhan University
arxiv_id: '2608.14401'
url: https://arxiv.org/abs/2608.14401
pdf_url: https://arxiv.org/pdf/2608.14401
published: '2026-08-14'
collected: '2026-08-17'
category: Other
direction: 离线强化学习 · 扩散模型价值估计
tags:
- Offline-RL
- Diffusion-Model
- Q-Function-Estimation
- Bellman-Operator
- Deep-Learning
one_liner: 提出基于条件扩散模型近似贝尔曼最优算子、解耦算子与值函数学习的离线RL Q*估计框架
practical_value: '- 电商强化学习推荐、动态定价等场景，可借鉴扩散模型拟合未知环境的奖励与转移分布，降低离线交互成本

  - 解耦算子估计与值函数学习的思路可迁移到离线排序、多步决策类推荐场景，提升值函数估计稳定性

  - 无完备假设的理论结论可指导小样本离线RL场景的模型选型与效果边界预估'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
离线RL仅基于离线观测估计最优动作价值函数\(Q^*\)时，奖励函数、转移核未知导致最优贝尔曼算子无法直接从数据获取，是核心技术瓶颈。
### 方法关键点
1. 采用解耦算子估计与值函数学习的两段式框架：先用条件扩散模型估计奖励分布与转移核，实现最优贝尔曼算子的数据驱动近似
2. 将扩散模型输出的算子估计代入贝尔曼方程，在神经网络函数族上最小化经验贝尔曼残差得到\(Q^*\)深度估计器，理论分析不依赖深度RL常用的完备性假设
### 关键结果
理论上推导得到\(Q^*\)估计器的\(L^2\)收敛率为\(\widetilde{\mathcal O}\bigl(n^{-\fracβ{d_x+d_a+2β}}\bigr)\)，数值实验验证了方法的有效性与性能优势。
