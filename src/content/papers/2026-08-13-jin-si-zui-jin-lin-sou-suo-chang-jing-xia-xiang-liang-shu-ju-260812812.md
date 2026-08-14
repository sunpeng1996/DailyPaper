---
title: 'A Comprehensive Empirical Evaluation of Vector Database Systems for Approximate
  Nearest Neighbor Search: Performance, Quality, and Resource Trade-offs'
title_zh: 近似最近邻搜索场景下向量数据库性能、质量与资源权衡综合评估
authors:
- Ashen Rashmiks
- Tiroshan Madushanka
affiliations:
- University of Kelaniya, Sri Lanka
arxiv_id: '2608.12812'
url: https://arxiv.org/abs/2608.12812
pdf_url: https://arxiv.org/pdf/2608.12812
published: '2026-08-13'
collected: '2026-08-14'
category: Eval
direction: 向量数据库基准测试 · 检索性能评估
tags:
- VectorDB
- Benchmark
- ANN Search
- RAG Infrastructure
- Retrieval Performance
one_liner: 针对7款主流向量数据库开展多维度基准测试，给出选型指南并开源测试框架
practical_value: '- 选型参考：高吞吐离线召回场景优先选FAISS；在线低延迟召回选Qdrant；对召回精度要求高的RAG/语义搜索场景选Weaviate；快速迭代需快速建索引的场景选LanceDB

  - 可直接复用本次开源的15项指标测试框架，针对自有业务的向量检索组件做定制化压测，适配业务特有的向量维度、数据量场景

  - 做混合检索方案时可参考不同向量库的召回率-延迟权衡特性，搭配调优索引参数，平衡业务的QPS、资源占用和推荐/搜索效果'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
向量数据库是RAG、语义搜索、推荐系统的核心基础设施，但行业缺乏同时覆盖检索质量、查询性能、资源消耗的可复现综合基准，选型无统一参考依据。
### 方法关键点
覆盖FAISS、Qdrant、Milvus、Weaviate、Chroma、pgvector、LanceDB共7款主流向量数据库，采用CV、文本领域共6个公开数据集（总规模超400万向量，维度覆盖96~960），从检索质量、查询性能、资源消耗3个维度共15项指标开展系统性测试。
### 关键结果数字
SIFT1M数据集下：FAISS单节点吞吐量最高达866 QPS，但无完整数据库运维能力；Weaviate开箱召回率>99%；全功能向量库中Qdrant中位数延迟最优（4.55ms）；LanceDB可牺牲部分召回质量换取极快的索引构建速度。
