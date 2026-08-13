---
title: 'SAG: SQL-Retrieval Augmented Generation with Query-Time Dynamic Hyperedges'
title_zh: SAG：基于查询时动态超边的SQL检索增强生成架构
authors:
- Yuchao Wu
- Junqin Li
- XingCheng Liang
- Yongjie Chen
- Yinghao Liang
- Linyuan Mo
- Guanxian Li
affiliations:
- Zleap AI
arxiv_id: '2608.12129'
url: https://arxiv.org/abs/2608.12129
pdf_url: https://arxiv.org/pdf/2608.12129
published: '2026-08-12'
collected: '2026-08-13'
category: RAG
direction: 检索增强生成 · 多跳结构化召回
tags:
- RAG
- Multi-hop QA
- Hyperedge
- SQL Retrieval
- Event-Entity Index
one_liner: 无需全局知识图谱，通过事件-实体索引+SQL动态关联实现多跳RAG性能全面领先
practical_value: '- 电商多跳搜索/推荐场景（如用户搜「搭配连衣裙的透气防晒衫」）可复用事件-实体索引架构，无需构建全局知识图谱，将商品、评论、用户行为等chunk拆分为事件+关联实体，通过SQL
  join跨chunk关联证据，避免GraphRAG的高维护、高成本问题

  - RAG工程实现可参考双路召回设计：实体结构化召回+事件语义召回互补，返回结果采用结构路径最多选5个关联证据、语义路径补全剩余槽位的策略，兼顾多跳证据链关联性和内容直接相关性

  - Agent长时记忆存储可借鉴append-only索引设计，新增知识仅追加事件-实体行无需重构全局结构，同时方案对嵌入模型鲁棒性强，替换为低成本嵌入模型掉点极少，大幅降低部署成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
主流RAG的稠密检索难以处理结构化约束和多跳推理，离线构建知识图谱的方案存在语义碎片化、维护成本高、增量更新难的问题，尤其在企业级持续增长的非结构化知识库场景下，现有方案扩展性和成本平衡表现差。

### 方法关键点
- 离线索引：每个文档chunk拆分为1个语义完整的事件+关联实体集合，作为潜在超边存储为SQL的事件-实体多对多行记录，无需构建全局图谱，支持纯追加式增量更新
- 在线召回：双路并行生成初始种子集，一路提取查询实体后经SQL join召回关联事件，一路直接做事件向量语义召回，两路结果合并作为种子
- 查询时动态超边：通过SQL join用种子事件关联的实体做扩展，拉取关联未访问事件，1轮扩展即可覆盖绝大多数多跳需求
- 最终选块：结构路径用LLM从候选集中最多选5个关联证据，剩余槽位用语义召回结果补全，兼顾多跳证据链完整性和直接相关性

### 关键实验
在HotpotQA、2WikiMultiHopQA、MuSiQue三个多跳QA基准上测试，对比BM25、BGE、GraphRAG、HippoRAG 2等baseline，MuSiQue（最多4跳）上Recall@5达80.36%，领先最强基线11.52个百分点；QA F1达61.15，领先GraphRAG 7.01个点；替换不同嵌入模型性能仅下降1.35个点，远低于基线的9.42个点，对嵌入模型鲁棒性极强。

### 核心结论
多跳检索不需要依赖稠密相似度或者全局图谱，所需的关联结构已经隐含在段落描述的事件和跨段落共享的实体中，通过查询时动态激活即可低成本实现高性能多跳召回。
