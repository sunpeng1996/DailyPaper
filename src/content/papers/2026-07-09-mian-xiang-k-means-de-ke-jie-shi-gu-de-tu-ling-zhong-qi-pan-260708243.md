---
title: An interpretable Good--Turing restart criterion for k-means++
title_zh: 面向k-means++的可解释古德-图灵重启判定准则
authors:
- Renato Cordeiro de Amorim
affiliations:
- School of Computer Science and Electronic Engineering, University of Essex, UK
arxiv_id: '2607.08243'
url: https://arxiv.org/abs/2607.08243
pdf_url: https://arxiv.org/pdf/2607.08243
published: '2026-07-09'
collected: '2026-07-11'
category: Training
direction: 聚类算法优化 · 自适应重启策略
tags:
- k-means++
- Good-Turing Estimation
- Clustering
- Adaptive Criterion
- Unsupervised Learning
one_liner: 结合Good-Turing估计给出可解释k-means++自适应重启规则，替代固定重启次数策略
practical_value: '- 电商用户分层、召回端Embedding聚类等场景用k-means++时，可直接复用GTRC替代固定重启次数，适配不同数据集难度降本提效

  - 借鉴Good-Turing估计+置信边界的思路，设计其他迭代类算法（如向量检索聚类、粗排迭代优化）的自适应终止条件

  - 线上离线聚类任务的动态资源调度可参考「继续迭代收益低于阈值即停止」的逻辑，降低冗余计算的资源浪费'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
k-means++普遍采用固定次数重启规避局部最优，无法适配不同数据集难度，既造成简单数据集算力浪费，也可能在困难数据集上效果不足，且人工调参无统一标准，影响实验可比性。
### 方法关键点
提出GTRC重启判定准则，融合Good-Turing估计、无约束理论边界、置信度边界，计算下一次重启能带来效果提升的概率，当该概率低于用户指定的容忍阈值ε时自动停止重启。
### 关键结果
在36个公开数据集上测试，GTRC的聚类质量与人工最优固定重启次数方案持平，重启次数可随数据集难度自适应动态调整，无需提前指定超参数，可解释性强。
