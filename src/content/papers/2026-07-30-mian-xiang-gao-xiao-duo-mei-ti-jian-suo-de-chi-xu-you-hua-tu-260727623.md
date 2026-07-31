---
title: An Exploration Graph with Continuous Refinement for Efficient Multimedia Retrieval
title_zh: 面向高效多媒体检索的持续优化探索图
authors:
- Nico Hezel
- Kai Uwe Barthel
- Konstantin Schall
- Klaus Jung
affiliations:
- HTW Berlin
arxiv_id: '2607.27623'
url: https://arxiv.org/abs/2607.27623
pdf_url: https://arxiv.org/pdf/2607.27623
published: '2026-07-30'
collected: '2026-07-31'
category: RecSys
direction: 向量检索 · 图结构ANNS优化
tags:
- ANNS
- Proximity Graph
- Multimedia Retrieval
- Exploratory Search
- Recommendation System
one_liner: 提出快速构建的持续优化探索图crEG，兼顾检索精度速度，适配推荐系统常用探索式搜索场景
practical_value: '- 电商商品向量召回场景可参考crEG的快速构建+边优化思路，降低大规模商品库的图索引更新成本，适配高实时性需求

  - 探索式推荐（如相似商品推荐、瀑布流续推）场景可借鉴crEG的全时段图连通性设计，避免搜索路径断裂降低召回覆盖率

  - 验证向量检索方案时不能仅测通用ANNS指标，需补充业务场景下的探索式搜索专项评测，避免指标与业务效果脱节'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
大规模多媒体数据集与特征维度持续扩张，现有图结构近似最近邻搜索（ANNS）方案存在构建速度慢、内存占用高的缺陷；同时现有ANNS优化极少针对推荐/探索系统常用的探索式搜索（查询本身属于库内元素）场景设计，通用ANNS的高性能无法直接迁移到该场景。
### 方法关键点
1. 提出持续优化探索图crEG，可快速构建紧凑的无向均匀度图结构，检索精度与速度达到SOTA水平
2. 支持可选边优化算法，可根据业务需求进一步提升检索效果
3. 所有算法设计保证任意时段图连通性，完美适配探索式搜索的路径遍历需求
### 关键结果
实验证实通用ANNS的高效性不能直接转化为探索式搜索的良好性能；crEG在ANNS场景下达到SOTA的精度-速度权衡，构建速度显著优于同类图方案，内存占用更低，在探索式搜索场景下表现远优于通用ANNS基线。
