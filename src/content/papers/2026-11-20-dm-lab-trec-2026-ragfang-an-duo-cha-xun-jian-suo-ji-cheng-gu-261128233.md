---
title: 'DM-Lab at TREC 2026 RAG: Multi-Query Retrieval, Ensemble Judging, and Claim-Pack
  Generation'
title_zh: DM-Lab TREC 2026 RAG方案：多查询检索、集成评估与声明生成
authors:
- Elyas Irankhah
- Muhammad Arif
- Sreeraj Ramachandran
- Samah Fodeh-Jarad
affiliations:
- Yale University School of Medicine
arxiv_id: '2611.28233'
url: https://arxiv.org/abs/2611.28233
pdf_url: https://arxiv.org/pdf/2611.28233
published: '2026-11-20'
collected: '2026-11-24'
category: RAG
direction: RAG系统优化 · 大规模语料检索生成
tags:
- RAG
- Multi-Query Retrieval
- Reciprocal Rank Fusion
- Ensemble Judging
- Claim-First Generation
one_liner: 面向5.53亿文档大规模语料提出高准确度、可复现的端到端RAG pipeline
practical_value: '- 多查询生成+RRF融合的检索trick可直接复用到电商搜索/导购Agent的召回层，无需训练稠密向量，适配已有BM25索引，大幅降低工程成本

  - 多模型集成relevance判优的思路可迁移到推荐系统粗排阶段，用小参数大模型+开源模型打分融合，在低算力开销下提升排序精准度

  - 声明优先的生成策略可用于电商商品问答/评价生成场景，强制每个生成内容绑定证据源，降低虚假宣传风险

  - 自适应检索深度的设计可复用在RAG类Agent的检索模块，动态控制召回文档数量，平衡效果和算力成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
TREC 2026 RAG赛道面向包含5.53亿文档的ClimbMix-400B大规模语料，要求RAG系统同时满足检索高相关性、生成内容事实覆盖、引用可靠三大要求，现有方案常存在检索召回不足、生成与证据脱节、引用不可靠的问题，亟需可落地、可复现的端到端RAG架构。

### 方法关键点
- 检索层：用GPT-4.1-mini生成7种BM25查询视图（含原query、关键词集合、子问题拼接串、HyDE风格伪文档），各视图召回200条文档，去重后用RRF（k=60）融合得到100条候选
- 打分层：融合RRF排序分、GPT-4.1-mini相关性分、Qwen3.5-9B+Ministral-3-14B双UMBRELA打分、覆盖度分5路信号，再用GPT-5.6-sol对Top30做listwise重排，动态控制检索深度在1-100之间
- 生成层：采用声明优先策略，先从Top40文档中提取绑定证据的原子声明，去重后转化为通顺句子，再用LLM做引用校验，删除无支持的引用

### 关键结果
在22个TREC2025开发集上检索nDCG@30达0.604；官方评测检索set precision 0.455，人工nugget gain 0.910；生成阶段引用校验将局部引用precision从0.725提升到0.926，召回保持0.731不变。

**最值得记住的一句话**：无需定制稠密索引的纯lexical多查询检索+多模型集成判优方案，在大规模语料RAG任务上可达到超过多数混合检索方案的效果，同时大幅降低工程部署成本。
