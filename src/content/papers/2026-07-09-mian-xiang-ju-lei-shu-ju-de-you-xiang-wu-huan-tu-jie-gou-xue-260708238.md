---
title: Structure Learning on Clustered Data
title_zh: 面向聚类数据的有向无环图结构学习方法
authors:
- Ryan Thompson
- Matt P. Wand
- Veerabhadran Baladandayuthapani
affiliations:
- University of Technology Sydney
- University of Michigan
arxiv_id: '2607.08238'
url: https://arxiv.org/abs/2607.08238
pdf_url: https://arxiv.org/pdf/2607.08238
published: '2026-07-09'
collected: '2026-07-12'
category: Other
direction: 因果发现 · 异质聚类数据结构学习
tags:
- DAG
- Causal Discovery
- Clustered Data
- Structure Learning
- Mixed Effects
one_liner: 将混合效应框架扩展到DAG结构学习，实现带集群异质性的因果关系发现
practical_value: '- 做用户/商品分群因果分析时，可复用该方法同时学习全局因果结构+分群特异效应，避免同质化假设导致的因果偏差

  - 可借鉴可微图耦合机制的设计思路，保证多场景/多群联合学习的DAG无环约束，无需复杂组合优化

  - 工程上可复用跨集群批量更新的一阶优化方法，降低多群因果结构学习的计算开销'
score: 4
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有DAG结构学习方法默认样本完全同质，无法适配聚类数据中普遍存在的集群特异变异（如不同用户群、不同场景的因果关系差异），限制了异质场景下的因果发现落地。
### 方法关键点
1. 将经典混合模型的固定/随机效应框架扩展到结构学习场景，同时估计全局通用因果结构与集群级局部特异效应；
2. 设计可微图耦合机制，严格保证固定效应与随机效应图的并集始终满足无环约束，大幅降低优化复杂度；
3. 提出可证明收敛的一阶优化方法，支持跨集群的高效批量更新，统计上证明了模型可识别性与渐近一致性。
### 关键结果
在真实与合成数据实验中，相比基线方法可检出其他估计器遗漏的依赖关系，聚类场景下结构学习准确率显著优于现有同质假设方法。
