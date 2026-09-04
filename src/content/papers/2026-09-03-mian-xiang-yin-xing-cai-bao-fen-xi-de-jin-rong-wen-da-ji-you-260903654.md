---
title: 'Enhancing Financial Question Answering: A Novel Benchmark Dataset of Banks''
  financial statements'
title_zh: 面向银行财报分析的金融问答基准FinRAG-QA及RAG系统优化
authors:
- Arianna Miola
- Bruno Spaccavento
- Lorenzo Silotto
- Marco Bianchetti
- Luca Cagliero
affiliations:
- Intesa Sanpaolo Innovation Center
- Università degli Studi di Milano-Bicocca
- Politecnico di Torino
- Intesa Sanpaolo IMI CIB
- University of Bologna
arxiv_id: '2609.03654'
url: https://arxiv.org/abs/2609.03654
pdf_url: https://arxiv.org/pdf/2609.03654
published: '2026-09-03'
collected: '2026-09-04'
category: RAG
direction: 金融领域RAG系统优化与基准构建
tags:
- RAG
- Financial QA
- Benchmark Dataset
- Embedding
- Reasoning LLM
one_liner: 推出覆盖24家欧美银行财报的FinRAG-QA基准，验证金融场景RAG系统各模块优化效果
practical_value: '- 垂直领域RAG落地时，优先选择检索优化的领域专用Embedding，搭配上下文Chunk enrichment（给每个Chunk补充所属文档的上下文摘要再索引），可大幅提升召回精度，本文中该组合将NDCG@10从0.322提升至0.710

  - 当首阶段检索精度已经较高时，不要盲目叠加Cross-encoder reranking，反而可能降低检索效果，可省略该步骤节省算力

  - 生成阶段优先选择单Top1召回Chunk作为上下文，比多Chunk输入的生成精度更高；推理优化的LLM虽然延迟高20倍，但精度可提升34.4个百分点，对精度要求高的场景可权衡使用

  - 构建垂直领域QA基准时，可参考本文结构化的query设计（固定模板+变量填充），同时覆盖跨实体、跨时间的对比查询需求，更贴合业务真实场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有金融QA基准多聚焦美股公开filings，缺少覆盖欧美银行巴塞尔协议Pillar 3监管报告的跨机构对比数据集，且通用RAG方案在平均长度达19.8万字的超长篇金融文档数值提取场景下召回、生成精度不足，无法满足分析师跨银行财报指标查询的规模化分析需求。
### 方法关键点
- 构建FinRAG-QA公开基准：覆盖24家欧美头部银行2019-2023年的209份年报+Pillar3监管报告，标注999条标准化金融指标查询及对应数值ground truth
- RAG pipeline分模块优化：文档预处理保留层级结构做语义分块，对每个Chunk生成所属文档上下文摘要前置后再做Embedding索引，对比不同Embedding、reranking、生成模型的效果
- 隔离评估机制：生成阶段仅在召回结果包含ground truth的样本上计算准确率，排除检索误差对生成效果评估的干扰
### 关键实验
检索端基线（OpenAI text-embedding-3-large）NDCG@10为0.322，搭配上下文Chunk enrichment+检索优化的VoyageAI voyage-3-large后NDCG@10提升至0.710，加Cross-encoder reranking后反而下降至0.498；生成端GPT-4o基线准确率44.6%，换成推理优化的GPT-o1-high后准确率提升至79.0%，但生成latency升高20倍，且单Top1召回Chunk输入的生成精度高于Top10/Top20输入。
### 核心结论
垂直领域RAG优化优先级是「检索专用Embedding+上下文Chunk enrichment」> 通用Embedding+reranking，生成阶段小而准的上下文效果远好于大而杂的上下文
