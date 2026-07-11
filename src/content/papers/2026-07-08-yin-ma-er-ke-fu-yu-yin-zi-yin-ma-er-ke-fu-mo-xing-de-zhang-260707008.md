---
title: Tensorized algorithms and scalable filtering methods for hidden Markov and
  factorial hidden Markov models
title_zh: 隐马尔可夫与因子隐马尔可夫模型的张量算法及可扩展过滤方法
authors:
- Roxana Barrios
- Ioannis Sgouralis
arxiv_id: '2607.07008'
url: https://arxiv.org/abs/2607.07008
pdf_url: https://arxiv.org/pdf/2607.07008
published: '2026-07-08'
collected: '2026-07-11'
category: Other
direction: 时序建模 · fHMM 计算性能优化
tags:
- Hidden Markov Model
- Factorial HMM
- Tensor Algebra
- Forward Filtering
- Time Series
one_liner: 用张量代数直接利用fHMM多维结构，无需转换大状态HMM，大幅降低前向过滤计算开销
practical_value: '- 做用户行为时序建模时，可采用fHMM替代普通HMM，拆分兴趣、场景、周期等独立隐因子，提升建模精准度

  - 多隐变量序列模型推理时，可复用张量代数直接利用结构特性的思路，避免状态空间组合爆炸

  - 现有HMM相关的用户行为预测、序列召回模块，可引入该张量过滤方法降低推理延迟'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
因子隐马尔可夫模型（fHMM）可拟合受多独立隐因子影响的时序数据，比普通HMM对真实场景的建模能力更强，但传统实现需将fHMM转换为等价HMM，状态空间随隐链数量指数级膨胀，核心的前向过滤算法计算成本极高，无法适配大规模数据场景。
### 方法关键点
基于张量代数直接利用fHMM的原生多维结构特性，完全跳过构造中间大状态等价HMM的步骤，设计全新的可扩展前向过滤算法。
### 关键结果
计算性能相比传统方案实现数量级提升，可支撑大规模fHMM系统与大数据集的高效分析，拓展了fHMM在数据密集型业务场景的适用范围。
