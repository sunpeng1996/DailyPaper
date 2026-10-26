---
title: 'Reinforcement Learning with Multi-Step Transition Predictions: A Bellman Theory'
title_zh: 多步转移预测增强强化学习：贝尔曼理论框架
authors:
- Chenbei Lu
- Zaiwei Chen
- Tongxin Li
- Chenye Wu
- Adam Wierman
affiliations:
- Cornell University
- Purdue University
- The Chinese University of Hong Kong (Shenzhen)
- Caltech
arxiv_id: '2610.32887'
url: https://arxiv.org/abs/2610.32887
pdf_url: https://arxiv.org/pdf/2610.32887
published: '2026-10-23'
collected: '2026-10-26'
category: Other
direction: 强化学习 · 多步转移预测理论
tags:
- Reinforcement-Learning
- MDP
- Bellman-Equation
- Sample-Complexity
- Offline-RL
one_liner: 推导含多步转移预测MDP的贝尔曼方程，提出BF-BOLA算法并给出匹配样本复杂度界
practical_value: '- 电商/广告场景的RL序列决策任务（如长周期用户留存优化、动态出价）可复用块反馈协议，每K步更新一次转移预测，避免状态空间爆炸

  - 基于RL的策略优化可借鉴贝尔曼-詹森分析框架，量化预测误差、动作覆盖度对最终策略收益的影响，降低预测模块迭代成本

  - BF-BOLA的离线预训练+在线适配范式可直接迁移到样本受限的个性化推荐策略迭代场景，减少在线试错成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
多步转移预测可提升强化学习效果，但直接将预测纳入状态会导致状态空间指数增长，动态规划计算成本极高，且预测带来的价值难以量化。
### 方法关键点
针对折扣有限MDP提出块反馈协议：每K周期块起始阶段仅观测部分动作的K步概率转移预测，块内根据观测状态调整决策；推导得到原始状态空间下的贝叶斯贝尔曼方程，通过贝尔曼-詹森分析量化预测horizon、误差、动作覆盖度、块内反馈的影响；提出BF-BOLA基于模型的离线学习+在线适配算法，推导样本复杂度上下界。
### 关键结果
样本复杂度上下界仅差对数因子，学习近最优策略所需的预测样本量少于贝叶斯价值函数估计所需样本量。
