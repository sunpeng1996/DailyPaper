---
title: Beyond Worst-Case Coreset Bounds for $k$-Clustering via Determinantal Sampling
title_zh: 基于行列式采样的k聚类超最坏情况核心集边界优化
authors:
- Diptarka Chakraborty
- Satyaki Mukherjee
- Gaurav Vallabhdas Revankar
- Hoang-Son Tran
affiliations:
- School of Computing, National University of Singapore
- Department of Mathematics, National University of Singapore
- Department of Mathematics, Indian Institute of Technology Bombay
arxiv_id: '2609.06394'
url: https://arxiv.org/abs/2609.06394
pdf_url: https://arxiv.org/pdf/2609.06394
published: '2026-09-06'
collected: '2026-09-09'
category: Other
direction: k聚类 · 核心集构建 · 数据降采样
tags:
- k-clustering
- coreset
- determinantal point process
- data sampling
- data reduction
one_liner: 基于行列式采样的k聚类ε-核心集构建框架，突破现有最坏情况ε⁻²的大小下界
practical_value: '- 大规模用户/物品聚类场景可引入行列式采样构建coreset，降低内存占用与计算耗时，比传统采样得到的子集更小且聚类损失偏差可控

  - 推荐系统召回/粗排阶段的海量样本采样环节，可参考本方法的相关性采样思路，在保留数据分布特征的前提下压缩样本量

  - 分布式训练的海量数据分片预处理阶段，可复用本采样框架降低跨节点数据传输量，同时保证下游任务精度'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
大规模聚类任务受内存、算力约束需构建ε-coreset（可近似保留所有聚类中心损失的加权小子集），现有最坏场景下coreset大小的ε⁻²下界已达理论紧界，但最坏样本不符合真实数据分布，无法满足实际场景对更小coreset的需求。
### 方法关键点
基于行列式点过程设计相关采样框架（行列式采样），在温和自然的数据分布假设下构建coreset，固定维度d时coreset大小对1/ε的依赖指数严格小于2。
### 关键结果
首个理论上可证明突破最坏情况ε⁻²下界的coreset方法，在合成与真实基准数据集上coreset大小一致优于现有SOTA方法，即使未显式满足理论假设仍保持效果。
