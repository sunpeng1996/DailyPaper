---
title: 'ZeroRAG: Adaptive Semantic Peer Routing for Decentralized Retrieval-Augmented
  Generation'
title_zh: ZeroRAG：面向去中心化检索增强生成的自适应语义对等路由
authors:
- Petru Neague
- Quinten Stokkink
- Martijn de Vos
- Rafael Pires
- Mathis Randl
- Anne-Marie Kermarrec
- Johan Pouwelse
affiliations:
- Delft University of Technology
- EPFL
arxiv_id: '2611.07928'
url: https://arxiv.org/abs/2611.07928
pdf_url: https://arxiv.org/pdf/2611.07928
published: '2026-11-05'
collected: '2026-11-06'
category: RAG
direction: 去中心化RAG · 语义路由优化
tags:
- RAG
- Decentralized Retrieval
- Semantic Routing
- P2P
- ANN Search
one_liner: 提出无全局结构与中心化协调的去中心化RAG路由层，性能接近中心化方案且可扩展至10万节点
practical_value: '- 跨机构/多商家联邦RAG场景（如电商多商家私域商品检索、跨品牌知识库问答）可复用其架构，无需构建全局索引，规避数据合规与版权风险

  - 多Agent分布式知识检索场景，可借鉴「历史查询缓存+邻接节点自适应重连」机制，在无全局协调的前提下提升跨Agent检索召回率、降低通信开销

  - 大规模分布式召回系统优化可参考其轻量本地状态设计（邻居语义广告+近期查询缓存），降低全局索引的存储与维护成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG系统依赖中心化文档存储与索引，无法满足数据主权、隐私合规、避免单点故障等场景需求；现有去中心化检索方案要么需要协调中心，要么依赖DHT等全局数据结构，需全网持续同步，开销高、灵活性差。

### 方法关键点
- 文档完全留存于持有节点，无全局索引与中心化协调，每个节点仅维护两个轻量本地状态：邻居节点的语义广告（节点持有文档的嵌入摘要）、近期路由的查询缓存
- 查询采用最佳优先遍历：节点收到查询后，基于本地文档、邻居广告、历史查询缓存返回匹配结果与高相关邻居推荐，查询发起方逐步扩展检索范围
- 网络自组织优化：每次查询完成后，发起方将返回最优结果的节点加入邻接表，超出容量则淘汰最早邻居，随查询量增加网络拓扑逐步向语义对齐方向演化，召回率持续提升

### 关键实验
基于AOL-IA、Amazon Electronics、PubMedQA三个真实数据集，对比Semantica、DHT-LSH两个去中心化基线与中心化HNSW基线：1. 召回率比最优去中心化基线高11~17pp，消息开销仅为DHT-LSH的1/10；2. 端到端RAG准确率达77%，仅比中心化HNSW低2pp；3. 可扩展至10万节点，50%节点同时宕机后可快速自恢复到95.5%的召回率；4. 99%的查询最多仅需13次节点交互即可找到最优匹配文档。

### 核心结论
完全去中心化的语义检索不需要全局索引，仅通过局部语义路由与网络自组织，就能达到接近中心化方案的性能，同时满足数据主权与合规要求。
