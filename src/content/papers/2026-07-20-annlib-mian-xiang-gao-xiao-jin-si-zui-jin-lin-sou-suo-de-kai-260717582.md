---
title: 'ANNLib: A Development Framework for Efficient Approximate Nearest Neighbor
  Search'
title_zh: ANNLib：面向高效近似最近邻搜索的开发框架
authors:
- Zheqi Shen
- Jingbo Su
- Zijin Wan
- Yan Gu
- Yihan Sun
affiliations:
- UC Riverside
- William & Mary
arxiv_id: '2607.17582'
url: https://arxiv.org/abs/2607.17582
pdf_url: https://arxiv.org/pdf/2607.17582
published: '2026-07-20'
collected: '2026-07-21'
category: RecSys
direction: 推荐系统 · 向量召回ANNS开发框架
tags:
- ANNS
- Graph-based-ANNS
- Vector-Search
- Retrieval
- Framework
one_liner: 模块化解耦ANNS算法与数据结构组件，在降低开发成本的同时比肩专用实现的性能
practical_value: '- 可复用模块化设计思路，将现有向量召回服务的算法（HNSW/Vamana）与底层索引数据结构解耦，快速切换适配静态/动态/带过滤的业务场景，避免重复造轮子

  - 电商多维度商品检索场景可直接复用内置的Filtered-vamana/Stitched-vamana实现，比Milvus、Weaviate等通用向量数据库的QPS最高提升数倍

  - 需要支持向量索引多版本快照的业务（如A/B测试、历史数据回查），可借鉴chrono prefix array设计，相比naive快照方案内存占用最多降低70.4%

  - 实时上新商品的动态向量索引场景，可复用批量删除+状态数组快速校验liveness的优化，比纯重建索引成本低一个数量级'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前ANNS系统要么侧重功能丰富性牺牲性能，要么是高度优化的专用实现难以扩展新功能，开发者同时兼顾性能、功能、开发效率的成本极高，而ANNS是搜索推荐、RAG等场景的核心依赖，亟需一套兼顾灵活性和高性能的开发框架。

### 方法关键点
- 核心设计是将ANNS系统解耦为**算法**和**数据结构**两大独立模块，标准化接口实现组件可插拔
- 算法层内置Vamana、HNSW、HCNNG等主流图ANNS基算法，封装了并行beam search、剪枝、批量插入等通用原语，支持自定义扩展过滤、动态更新等模块
- 数据结构层抽象统一的图容器接口，内置静态场景用的CSR、快照场景用的功能树、动态更新优化的chrono前缀数组等多种实现，由edge agent屏蔽底层差异

### 关键结果
在BIGANN、DEEP、OpenAI、MS MARCO等多个公开向量数据集上测试，对比ParlayANN、DiskANN、Milvus、Weaviate等基线：
1. 批量插入性能比ParlayANN平均快1.58倍，最高达8.11倍
2. 常规向量搜索QPS与ParlayANN相当，是Milvus的数倍到一个数量级
3. 带属性过滤搜索场景下，所有数据集性能均超过DiskANN、Milvus、Weaviate
4. 快照功能的chrono前缀数组比naive方案内存占用最多降低70.4%

### 核心结论
ANNS系统开发不需要在功能灵活性和性能之间二选一，通过合理的模块化解耦和底层组件深度优化，可以同时兼顾两者，大幅降低定制开发成本。
