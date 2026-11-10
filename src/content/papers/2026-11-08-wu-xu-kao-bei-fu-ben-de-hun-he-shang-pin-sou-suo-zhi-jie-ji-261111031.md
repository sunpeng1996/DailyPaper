---
title: 'Hybrid Product Search Without the Copy: Lexical, Semantic and Filtered Retrieval
  Served Directly from a Data Lake'
title_zh: 无需拷贝副本的混合商品搜索：直接基于数据湖的词法/语义/过滤检索
authors:
- Raghvendra Yadav
- Xiang Fu
- Chinmay Soman
affiliations:
- StarTree Inc.
arxiv_id: '2611.11031'
url: https://arxiv.org/abs/2611.11031
pdf_url: https://arxiv.org/pdf/2611.11031
published: '2026-11-08'
collected: '2026-11-10'
category: RecSys
direction: 湖原生混合检索 · 电商商品搜索
tags:
- HybridRetrieval
- BM25
- VectorSearch
- DataLake
- ProductSearch
- ApachePinot
one_liner: 扩展Apache Pinot实现无数据副本的湖原生混合商品搜索，效果、延迟匹配专用检索引擎
practical_value: '- 可直接复用BM25+ANN+RRF全SQL实现的混合检索逻辑，无需额外开发多引擎结果拼接模块，降低检索层运维复杂度

  - 分块索引下的BM25全局统计量按快照预计算缓存的trick，可解决分片/文件粒度索引的分数不可比问题，实测能提升BM25吞吐量10倍以上

  - 电商商品数据湖表可按品牌、品类等高频过滤字段做聚类存储，配合文件级统计剪枝，能把带筛选的检索p50延迟压到10ms级，满足大促高并发要求

  - 湖原生检索架构省去多副本同步 pipeline，新品从入湖到可搜索延迟可压到4s内，接近专用搜索引擎，适合快消、上新频繁的电商场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前电商商品 catalog 普遍存储在Iceberg格式的数据湖表中，但传统混合商品搜索需要将数据分别拷贝到词法搜索引擎、向量数据库，存在多套 ingestion pipeline 维护成本高、schema 修改同步慢、数据一致性差、新鲜度低的痛点，且额外存储多份副本大幅提升了存储和运维成本。
### 方法关键点
- 扩展Apache Pinot的外部表能力，仅在计算层构建Lucene词法索引、HNSW向量索引，原始数据完全存放在数据湖Iceberg表中，无任何二次拷贝
- 新增双阶段BM25打分机制：先拉取全表所有文件的词频、文档数等全局统计量，再生成跨文件可比的BM25分数，解决分块索引下的分数漂移问题，统计量可按快照预计算缓存提升吞吐量
- 原生支持SQL化的全链路混合检索：词法匹配、向量ANN、结构化过滤下推、RRF结果融合全部在单条SQL中完成，还支持流批一体的统一查询视图
- 按Iceberg快照做查询一致性路由，配合文件级统计量剪枝，大幅降低带过滤查询的扫描范围
### 关键实验
基于Amazon ESCI基准数据集（1.2M美国商品，22458条测试query），对比Elasticsearch、OpenSearch、精确检索基线：
- 混合检索nDCG@10达0.361，与精确检索完全一致，比纯BM25高17.2%，比纯向量检索高3.1%
- 277M商品（0.8TB）单16vCPU节点下，带品牌过滤的检索p50延迟6.5-9ms，可支撑1100 QPS向量搜索、635 QPS BM25搜索，p99均低于180ms
- 新数据入湖到可检索延迟仅3.8s，与专用搜索引擎持平，全表上线仅需149s，比ES快66%
- 1.2M商品场景整体成本比传统多副本方案低9%，复用现有湖计算集群时可降本54%
> 最值得记住的结论：按高频过滤维度聚类的湖原生混合检索，效果和性能完全匹配专用检索引擎，还能省去多副本同步的所有存储和运维成本。
