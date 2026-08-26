---
title: SQLite is Enough. Lexical, Semantic, and Hybrid Search with scrydb
title_zh: 基于SQLite实现词法、语义及混合搜索的Python库scrydb
authors:
- Timo Breuer
affiliations:
- TH Köln – University of Applied Sciences
arxiv_id: '2608.24060'
url: https://arxiv.org/abs/2608.24060
pdf_url: https://arxiv.org/pdf/2608.24060
published: '2026-08-25'
collected: '2026-08-26'
category: RAG
direction: RAG/Agent 轻量级混合检索工具
tags:
- Hybrid Search
- SQLite
- Semantic Search
- Lexical Search
- RRF
- Retrieval
one_liner: 基于SQLite实现轻量无服务的词法、语义、混合搜索Python库scrydb，无需额外独立向量存储
practical_value: '- 中小规模业务场景（如商家端商品检索、私域问答召回）可直接复用scrydb，免去部署维护独立向量数据库的成本，所有检索数据存在单个SQLite文件易迁移同步

  - 混合检索可直接复用其RRF排序融合逻辑，平衡词法匹配精度和语义匹配泛化性，适配电商商品标题/SPU检索、用户Query理解等场景

  - 可参考其精度-时延权衡方案，低优先级请求用二进制向量召回降本，高优先级请求用全精度向量+重排保障效果，适合推荐系统多流量层级的召回优化'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
当前RAG、Agent搜索场景往往需要独立部署向量数据库、文本检索服务，架构重、多组件数据同步成本高，中小流量场景缺乏轻量开箱即用的混合检索方案。
### 方法关键点
1. 基于SQLite原生FTS5扩展实现词法检索，内置BM25排序；
2. 基于sqlite-vec扩展实现向量语义检索，支持二进制/全精度向量两种存储检索模式；
3. 内置Reciprocal Rank Fusion(RRF)实现词法+语义检索结果融合，可选全精度向量重排进一步优化效果；
所有索引、向量、文档存储在单个SQLite文件中，无外部服务依赖，开箱即用。
### 关键结果
在多个IR公开基准数据集上验证检索效果与独立部署的专业检索方案相当；二进制向量模式检索速度比全精度模式快2~3倍，磁盘占用降低70%，兼顾效果与成本，已基于MIT许可开源。
