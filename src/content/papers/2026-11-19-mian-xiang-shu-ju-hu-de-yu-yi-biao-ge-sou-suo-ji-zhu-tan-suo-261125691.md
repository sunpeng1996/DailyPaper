---
title: Exploring Semantic Table Search in Data Lakes
title_zh: 面向数据湖的语义表格搜索技术探索
authors:
- Martin Pekár Christensen
- Matteo Lissandrini
- Katja Hose
affiliations:
- Aalborg University
- University of Verona
- Technische Universität Wien
arxiv_id: '2611.25691'
url: https://arxiv.org/abs/2611.25691
pdf_url: https://arxiv.org/pdf/2611.25691
published: '2026-11-19'
collected: '2026-11-21'
category: Other
direction: 数据湖语义表格搜索 · 多信号融合排序
tags:
- Table_Search
- Data_Lake
- HNSW
- Multi_Signal_Ranking
- Semantic_Search
one_liner: 推出融合关键词与语义信号的Thetis++表格搜索框架，验证HNSW索引可提速语义搜索4.7倍且精度无损
practical_value: '- 多信号排序融合思路可迁移到电商搜索召回排序场景，将关键词精确匹配、语义相似度信号结合，兼顾召回准确性和相关性

  - 语义检索索引选型可直接参考结论：HNSW相比LSH平均提速4.7倍且精度无损，适合大规模商品库/语料库的语义召回前置过滤

  - 业务侧需要搭建内部数据表/特征库快速检索工具时，可直接复用Thetis++的关键词+实体语义匹配框架，降低数据查找成本'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
数据湖中异构数据集检索效率低、相关性差，单独使用关键词精确匹配或实体语义搜索均存在召回范围窄、匹配灵活性不足的缺陷，无法满足探索式检索需求。
### 方法
1. Thetis++框架融合关键词匹配信号与表格实体语义相似度信号做联合排序，测试覆盖无监督（TOPSIS等）、监督学习排序两类多信号融合方案；
2. 对比LSH与HNSW两种语义预过滤索引的性能差异，优化语义搜索的可扩展性。
### 关键结果
1. 学习类排序方案相比传统单一检索范式效果更优；
2. HNSW索引相较LSH平均将语义表格搜索速度提升4.7倍，同时完全保留检索结果质量。
