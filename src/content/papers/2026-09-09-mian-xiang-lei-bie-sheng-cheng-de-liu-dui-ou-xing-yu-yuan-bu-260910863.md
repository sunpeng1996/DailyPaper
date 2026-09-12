---
title: Flow Duality and Source Geometry for Categorical Generation
title_zh: 面向类别生成的流对偶性与源分布几何特性研究
authors:
- Etrit Haxholli
arxiv_id: '2609.10863'
url: https://arxiv.org/abs/2609.10863
pdf_url: https://arxiv.org/pdf/2609.10863
published: '2026-09-09'
collected: '2026-09-12'
category: Training
direction: 离散类别生成 · 流匹配对偶性优化
tags:
- Flow Matching
- Categorical Generation
- Discrete Generation
- Source Distribution
- Duality
one_liner: 揭示连续与离散流匹配的对偶关系，证明源几何特性影响类别生成效果
practical_value: '- 做生成式推荐的离散token生成（如Semantic ID序列生成、推荐文案生成）时，可参考流对偶方法将连续流匹配优化迁移到离散生成任务，降低离散建模难度

  - 可测试高斯、有界均匀、中心负指数三类源分布对业务生成效果的影响，根据场景（短文案/长序列生成）选择最优源几何，提升生成质量

  - 对早期生成质量要求高的场景（如搜索query联想、实时推荐文案生成），可参考本文源分布设计准则，优化冷启动阶段的生成效果'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
连续、离散流匹配此前被视为完全独立的两类构造，离散类别生成（如文本、Semantic ID、推荐文案）的流建模无法复用连续域成熟的优化工具与可解释性分析方法，亟需打通两者的关联机制。
### 方法关键点
1. 证明带one-hot目标的连续凸插值路径经逐位置argmax投影后，可直接得到等价的离散凸插值路径，仅要求源分布满足坐标对称性与边界正则性条件；
2. 推导高斯、有界均匀、中心负指数三类常见源分布对应的离散插值行为，明确不同源几何对转换时序、词表大小依赖的差异化影响。
### 关键结果
小样本视觉诊断和语言建模预实验验证：源分布几何特性可直接作用于学习后的传输过程与早期生成质量，不同源设计的生成效果差异显著。
