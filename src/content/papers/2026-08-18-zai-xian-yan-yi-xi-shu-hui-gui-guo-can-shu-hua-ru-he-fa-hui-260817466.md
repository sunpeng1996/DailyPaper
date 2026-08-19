---
title: 'Online Generalized Sparse Regression: How Does Overparametrization Help?'
title_zh: 在线广义稀疏回归：过参数化如何发挥作用？
authors:
- Shuoguang Yang
- Qiang Sun
affiliations:
- HKUST
- University of Toronto
- MBZUAI
arxiv_id: '2608.17466'
url: https://arxiv.org/abs/2608.17466
pdf_url: https://arxiv.org/pdf/2608.17466
published: '2026-08-18'
collected: '2026-08-19'
category: Training
direction: 在线稀疏回归 · 过参数化优化算法
tags:
- sparse regression
- online learning
- hard thresholding
- overparameterization
- streaming data
one_liner: 设计无需动态调参的过参数化在线硬阈值稀疏回归框架，效率与精度均优于现有SOTA
practical_value: '- 在线特征选择场景可复用带基数约束的稀疏回归框架，省去正则参数动态调优的开销，适配流数据实时更新需求

  - CTR预估等在线训练任务可替换原迭代优化逻辑为闭形式硬阈值更新，仅存统计量即可，大幅降低存储与计算成本

  - 低秩用户/物品矩阵的在线补全任务可参考过参数化投影设置，在非凸约束下仍能保证最优收敛速率'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
离线稀疏正则回归研究成熟，但在线场景存在四大核心痛点：逐轮动态调整正则参数不可行、存储与内存复杂度高、无法通过闭形式更新实现实时计算、缺乏真实假设下的最优统计保证。

### 方法关键点
设计带广义稀疏约束的在线回归框架，覆盖基数约束线性回归、低秩矩阵感知两大场景，用硬约束替代正则项省去动态调参流程；实现高效在线硬阈值算法，仅需存储汇总统计量即可完成闭形式更新，同时通过合理设置过参数化投影集，解决非凸组合优化的收敛难题。

### 关键结果
真实假设下可达到最优统计速率的全局收敛，数值实验显示效果稳定优于现有SOTA方案。
