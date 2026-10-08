---
title: Does Document Structure Help Dense Retrieval? A Placebo-Controlled Ablation
  of Four Mechanisms Across Two Corpora
title_zh: 文档结构对稠密检索的作用验证：四种机制的安慰剂对照消融研究
authors:
- Andrey Kuehlkamp
- Priscila Correa Saboia Moreira
- Samuel Rund
affiliations:
- Center for Research Computing, University of Notre Dame
arxiv_id: '2610.10170'
url: https://arxiv.org/abs/2610.10170
pdf_url: https://arxiv.org/pdf/2610.10170
published: '2026-10-07'
collected: '2026-10-08'
category: RAG
direction: RAG稠密检索 · 文档结构处理优化
tags:
- Dense Retrieval
- RAG
- Document Chunking
- Placebo Control
- Hierarchical Retrieval
one_liner: 通过严格对照消融明确四类文档结构处理对稠密检索的增益及生效逻辑
practical_value: '- 电商/知识库RAG系统优先采用结构对齐分块，效果优于固定窗口+LLM生成上下文的组合，还能节省LLM推理成本

  - 给分块拼接真实的标题/层级路径前缀可稳定提升检索效果，不要拼接无意义文本，会引入噪声甚至降低表现

  - 不要上线朴素两级分层检索（先召回section再排chunk），除非搭配跨编码器重排补全被剪枝的候选，否则会因一级召回不足跌点

  - 26B级模型诱导的文档结构在学术、商品说明等浅层级长文本上效果和原生结构无显著差异，可放心落地'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
RAG系统广泛使用四类文档结构处理方法（结构对齐分块、LLM生成chunk上下文、层级路径元数据注入、分层检索），但过往研究在不同语料、模型下结果冲突，且无法区分增益是结构内容生效还是单纯的token注入带来的embedding偏移，从业者无法判断哪种方法真正值得落地。

### 方法关键点
- 设计11组变量严格受控的消融实验，固定所有组的分块大小匹配基线，排除分块长度差异的干扰
- 新增语义安慰剂组：给chunk拼接格式、长度完全匹配但跨文档打乱的层级路径，分离token注入效应和结构内容效应
- 采用coverage-nDCG@10作为主指标，支持多证据片段的 novelty 加权，避免小分块重复计分导致的评估偏差
- 预注册4组核心对比，采用文档聚类bootstrap+Holm校正统计显著性，避免指标作弊

### 关键实验
在200篇维基百科精选文章（951条控制泄露的合成查询）、1585篇QASPER学术论文（4303条真实读者查询）上测试：
- 结构对齐分块+真实层级路径比固定窗口+LLM生成上下文分别高+0.022/+0.012 cov-nDCG@10
- 真实层级路径比安慰剂组高+0.010/+0.016，安慰剂组无额外增益甚至在学术语料上负向
- 朴素两级分层检索比平检索分别低-0.033/-0.015，核心原因是一级section召回率仅0.17~0.68
- LLM诱导结构在学术语料上和原生黄金结构效果无显著差异（+0.001，统计不显著）

### 核心结论
分块边界的合理性是文档结构处理的第一增益来源，其余方法增益远小于此甚至负向。
