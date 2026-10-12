---
title: 'PRIME: Pre-Retrieval Index Modeling Enhancement for Structured Document Retrieval-Real'
title_zh: PRIME：面向结构化文档检索的检索前索引建模增强
authors:
- Cheuk Hei Chung
- Li Liu
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2610.13296'
url: https://arxiv.org/abs/2610.13296
pdf_url: https://arxiv.org/pdf/2610.13296
published: '2026-10-09'
collected: '2026-10-12'
category: RAG
direction: RAG 索引侧优化 · 结构化文档检索
tags:
- RAG
- Index Optimization
- Structured Document Retrieval
- Hierarchical Retrieval
- Semantic Restructuring
one_liner: 提出不修改现有检索器的索引侧RAG优化框架，兼顾检索效率与下游QA效果
practical_value: '- 电商商品详情页、平台规则知识库这类结构化文档的RAG索引，可复用MS+HR方案，仅嵌入标题+高区分度TF-IDF关键词+章节结构，大幅降低embedding计算量和索引向量数，检索效果损失极小

  - 对知识问答类Agent的RAG pipeline，若下游对答案准确率要求高，可在冷启动阶段对高频访问的结构化文档做LLM语义重构，实测能提13.7%的Answer-F1，查询量足够大时可覆盖预计算成本

  - 做RAG优化前先判断语料属性：API文档、商品参数这类结构清晰、预训练语料覆盖少的场景优先做索引侧优化；短文本、无结构的用户评论、晒单等场景索引侧优化收益低甚至负向

  - 现有RAG pipeline加了强cross-encoder reranker后，文档级检索的索引侧优化收益会被抹平，此时可重点优化section级的内容密度，提升下游生成效果'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG优化多聚焦查询侧检索器、生成器迭代，语料侧仅做简单分块处理，索引侧质量是长期被低估的优化杠杆；同时已有研究证实强reranker会抵消大部分检索增强的收益，亟需探索无需修改现有检索组件的索引侧优化方案。
### 方法关键点
- 双轨互补架构：1）LLM驱动的语义重构(SR)：按H2章节拆分长文档，显式化隐式逻辑、压缩冗余描述，提升知识密度，保留原有章节结构；2）确定性元数据合成(MS)+分层检索(HR)：提取top5高区分度TF-IDF关键词和章节树作为元数据，用小模型嵌入做粗排召回，再用cross-encoder做章节级精排，双路结果用RRF融合。
- 两种部署模式：离线模式仅跑MS+HR，无LLM推理开销；全模式叠加SR，优先适配高频访问的结构化知识库场景。
### 关键结果
在QASPER、BRIGHT、NFCorpus三类结构差异的数据集上测试，对比结构感知分块、RAPTOR-lite等基线：
1. 离线模式检索效果与结构感知分块持平，embedding计算量降低45.8×，索引向量数减少22.4×；
2. 全模式叠加SR后，Answer-F1提升13.7%，语料语义密度提升127.3%，事实矛盾率仅4.3%；
3. 强cross-encoder会抹平文档级索引优化的收益，但section级内容密度提升仍能带来下游QA效果增长；
4. 语料特性决定收益：API类结构清晰、预训练覆盖少的文档NDCG@5提升175.6%，无结构短文本场景最多下降19.5%。
> 最值得记住：RAG优化不要只盯着查询侧，索引侧的结构优化和密度提升在结构化文档场景能拿到「降本+提效」的双重收益，且无需修改现有检索组件。
