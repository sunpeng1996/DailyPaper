---
title: 'EAGR: Evidence-Guided Adaptive Graph Retrieval'
title_zh: EAGR：证据引导的自适应图检索框架
authors:
- Sonam Gupta
- Vignesh P
- Vishwajeet Kumar
- Adnan Qidwai
- Anand Eswaran
- Jaydeep Sen
- Sachindra Joshi
affiliations:
- IBM
arxiv_id: '2611.01910'
url: https://arxiv.org/abs/2611.01910
pdf_url: https://arxiv.org/pdf/2611.01910
published: '2026-11-01'
collected: '2026-11-03'
category: RAG
direction: 多跳RAG · 无显式图自适应检索
tags:
- RAG
- Multi-hop Reasoning
- GraphRAG
- VectorDB
- Adaptive Retrieval
one_liner: 无需显式构建存储图，基于向量库元数据实现证据引导多跳RAG检索，效果超现有基线3.9pp
practical_value: '- 电商商品/内容多跳检索场景可复用该方案：无需额外搭建图数据库，仅通过VectorDB存储商品/内容的实体、属性元数据即可实现GraphRAG能力，大幅降低工程落地成本

  - 多轮检索终止策略可直接迁移：基于已收集证据的推理链完备性做终止判断，无需固定检索k值，能平衡效果和latency，适配推荐/搜索实时场景

  - 检索结果重排序逻辑可复用：根据证据链关联度而非仅查询相似度排序，可提升多跳关联商品/内容的排序权重，适配跨品类推荐、关联搜索等场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多跳RAG方案要么依赖显式图存储，需额外构建运维GraphDB、成本高昂；要么靠迭代改写查询实现多跳，易偏离原始需求、推理latency高，无法适配企业现有标准VectorDB架构下的多跳推理需求，难以落地到电商、搜索等对成本和实时性要求高的场景。

### 方法关键点
- 离线阶段：仅为每个段落/内容单元生成语义描述符（实体、核心概念），作为元数据存储在标准VectorDB中，共享描述符的单元自动构成隐式关联，无需显式构建图边或图索引
- 在线阶段：先以DPR召回种子单元，迭代执行节点评估与证据积累、关联方向选择、证据充足性校验、证据引导的方向重排、邻域检索5步，全程不改写原始查询，仅基于已收集证据决定下一步检索方向
- 终止逻辑：仅当LLM判断已收集证据能形成完整推理链回答查询，或达到检索预算时终止，最后按证据链关联度重排检索结果

### 关键实验
在HotPotQA、2WikiMultiHopQA、MuSiQue三个主流多跳QA基准上测试，对比Vanilla RAG、HippoRAG2、LinearRAG等基线，平均LLM准确率达67.1%，比Vanilla RAG高7.3pp，比最强GraphRAG基线高3.9pp；HotPotQA和2WikiMultiHopQA上Recall@5分别达95.4%、95.5%，81%的简单查询检索量不超过10个单元，大幅降低无效检索成本。

### 核心结论
多跳检索的核心是基于已收集证据自适应调整检索方向，而非依赖预先构建的固定图结构或反复改写查询。
