---
title: A Versioned Unified Graph Index for Dynamic Timestamp-Aware Nearest Neighbor
  Search
title_zh: 面向动态时间感知近邻搜索的版本化统一图索引
authors:
- Jun Woo Chung
- Weijie Zhao
affiliations:
- Rochester Institute of Technology
arxiv_id: '2608.27663'
url: https://arxiv.org/abs/2608.27663
pdf_url: https://arxiv.org/pdf/2608.27663
published: '2026-08-27'
collected: '2026-08-31'
category: RAG
direction: 向量检索 · 时间约束ANN优化
tags:
- ANN
- Graph-based Retrieval
- Temporal Filtering
- Dynamic Index
- Vector Search
one_liner: 提出TiGER版本化统一图索引，支持任意时间范围ANN搜索，QPS较基线最高提升5倍且精度无损
practical_value: '- 电商/推荐场景的时间感知召回（如近7天热销品、用户近期行为相关内容召回）可复用TiGER的节点/边时间有效性标注机制，替代现有HNSW+后过滤方案，在召回率不变的前提下提升QPS

  - 时间敏感RAG场景（如动态知识库检索、近期新闻检索）可借鉴其版本化统一图设计，无需维护多时间切片的独立索引，降低存储开销与动态数据更新成本

  - 对于高频连续时间范围查询场景，可复用其稀疏边数据库的预聚合设计，进一步降低查询时的边遍历开销，查询时间范围越大，性能提升越显著'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有图基近似最近邻（ANN）检索方案处理时间约束时，后过滤方案在高时间筛选度下会产生大量无效计算，预建多时间片子图的方案则存在极高的索引维护、多结果合并开销，且普遍难以支持动态数据更新与非连续时间范围查询，无法满足实时推荐、时间敏感RAG、动态内容召回等业务场景的性能需求。

### 方法关键点
- 构建统一版本化邻近图，每个节点标注活跃时间区间、每条边标注生效时间范围，无需为不同时间范围维护独立子图，避免前后置过滤开销
- 新增`prev(v)`动态前驱链机制，保证任意时间区间下从检索起点到所有活跃节点的连通性，支持向量动态增量插入，无需全量重建索引
- 设计稀疏边数据库预聚合连续时间范围的边信息，大幅降低连续时间查询时的边遍历计算开销，同时原生支持非连续时间范围查询

### 关键结果
在SIFT 1M、GloVe-100标准向量数据集上，对比HNSW后过滤、HNSW多时间片子图预过滤两个主流基线：相同召回率下，TiGER的QPS最高提升5倍；对连续、非连续时间范围查询均稳定优于基线，连续时间范围越大，稀疏边数据库带来的性能增益越明显。

### 核心结论
带属性约束的ANN检索的核心优化思路是将约束嵌入索引结构而非依赖前后置过滤，可在精度无损的前提下实现数量级的性能提升。
