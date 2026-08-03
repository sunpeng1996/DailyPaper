---
title: 'Bridging the Question-Answer Gap in Retrieval-Augmented Generation: Hypothetical
  Prompt Embeddings'
title_zh: 弥合检索增强生成问答差距的假设提示嵌入HyPE框架
authors:
- Domen Vake
- Jernej Vičič
- Aleksandar Tošić
affiliations:
- University of Primorska
- InnoRenew CoE
- Research Centre of the Slovenian Academy of Sciences and Arts
arxiv_id: '2607.29402'
url: https://arxiv.org/abs/2607.29402
pdf_url: https://arxiv.org/pdf/2607.29402
published: '2026-07-31'
collected: '2026-08-03'
category: RAG
direction: RAG检索优化 · 假设提示预嵌入
tags:
- RAG
- Dense Retrieval
- Embedding
- HyDE
- Index Optimization
one_liner: 将假设内容生成从RAG推理端移至索引端，无额外延迟提升检索精度与召回
practical_value: '- 电商/客服类垂直领域RAG系统可直接复用HyPE思路，离线为商品详情、知识库chunk预生成用户可能的问题嵌入，替代原有chunk嵌入，在线链路零改造即可提升召回精度，无额外推理开销

  - 搜索query推荐/ autocomplete场景可把doc侧预生成的假设query直接作为候选suggestion池，同时提升语义匹配度和候选词覆盖度

  - Agent系统的知识库检索模块可接入HyPE，优化用户自然语言query与垂直知识库的语义gap，尤其适配法律、美妆等专业术语多、用户表述与知识库风格差异大的场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG系统存在用户query（疑问句式）与知识库chunk（陈述句式）的风格语义gap，主流优化方案HyDE需要在推理侧调用LLM生成假设答案再做检索，额外增加推理延迟和调用成本，无法适配高并发线上业务场景，亟需无在线额外开销的gap弥合方案。

### 方法关键点
- 索引阶段离线为每个知识库chunk调用LLM生成3~5个对应用户可能提问的问题，将这些问题的embedding而非原chunk的embedding存入向量库，每个chunk对应多组嵌入
- 在线检索直接对用户query做embedding后与预存的问题嵌入做ANN检索，匹配逻辑从「问句-陈述句」变为「问句-问句」，完全消除在线侧额外LLM调用开销
- 框架可与重排序、多向量检索、query分解等现有RAG优化方案兼容，可作为drop-in组件替换现有chunk嵌入逻辑

### 关键实验
在6个公开RAG数据集（MS MARCO、RAGBench、MultiHopRAG等）上对比朴素RAG、HyDE两个基线，平均context precision提升21.2pp，平均claim recall提升17.9pp，单领域场景下最高precision提升42pp、recall提升45pp，推理端 latency与朴素RAG完全一致，相比HyDE降低70%以上。

**最值得记住的一句话**：把语义对齐成本从高并发的在线端转移到一次性的离线端，是工业级RAG优化的核心性价比思路
