---
title: A Finite Sample Analysis for Quantile Temporal Difference Learning in Distributional
  Reinforcement Learning
title_zh: 分布强化学习中分位数时序差分学习的有限样本分析
authors:
- Zijie Cheng
- Xiang Li
- Yang Peng
- Zhihua Zhang
affiliations:
- 北京大学数学科学学院
- 宾夕法尼亚大学
- 清华大学丘成桐数学科学中心
arxiv_id: '2608.27313'
url: https://arxiv.org/abs/2608.27313
pdf_url: https://arxiv.org/pdf/2608.27313
published: '2026-08-27'
collected: '2026-08-29'
category: Other
direction: 分布强化学习 有限样本理论分析
tags:
- Distributional RL
- Quantile TD
- Finite Sample Analysis
- Temporal Difference Learning
- Reinforcement Learning
one_liner: 证明表格型分位数时序差分学习的全局有限样本上界，区分局部波动与全局样本复杂度
practical_value: '- 若业务中采用QR-DQN等基于QTD的分布RL做动态出价、流量分配等收益分布估计场景，可参考结论：适当增加分位数数量不会带来多项式级收敛波动，可按需提升分布估计精度

  - 步长调优可参考：采用a∈(1/2,1)的幂律衰减步长可获得最优收敛阶，降低迭代波动

  - 非RL驱动的推荐、搜索、广告业务无直接可借鉴价值，仅适合RL决策类场景参考'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
分位数时序差分学习（QTD）是QR-DQN、隐式分位数网络等主流分布强化学习算法的核心基础，但现有研究缺乏其全局有限样本收敛性的严格证明，收敛速度与分位数数量、步长等超参数的定量关系不明确。
### 方法关键点
证明拆解为两个稳定性机制：
1. 基于奖励累积分布函数的序单调性、分布Bellman算子的$W_\infty$压缩性，证明任意初始化的迭代都会收敛到局部邻域
2. 邻域内对QTD平均场线性化，利用雅可比矩阵的非奇异M矩阵性质开展方差敏感的鞅分析
### 关键结果
- 步长取$α_t=c(t+1)^{-a}$（$a∈(1/2,1)$）时，最终迭代波动阶为$\widetilde O(T^{-a/2}/\sqrt{1-\gamma})$，且与分位数数量无多项式依赖
- 全局burn-in阶段仅在最坏情况下与分位数数量成反比，明确区分局部随机波动与全局样本复杂度的差异
