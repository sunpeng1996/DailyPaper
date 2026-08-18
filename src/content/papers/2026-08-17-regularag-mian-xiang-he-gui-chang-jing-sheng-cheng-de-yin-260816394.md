---
title: 'Think Inside the Chunk: RegulaRAG for Regulation-Compliant Scenario Generation
  using LLMs: A Case Study of UN Regulation No. 152'
title_zh: RegulaRAG：面向合规场景生成的引用增强RAG管道
authors:
- Vahid Zolfaghari
- Nenad Petrovic
- AndrÉ Schamschurko
- Alois Knoll
affiliations:
- Technical University of Munich
arxiv_id: '2608.16394'
url: https://arxiv.org/abs/2608.16394
pdf_url: https://arxiv.org/pdf/2608.16394
published: '2026-08-17'
collected: '2026-08-18'
category: RAG
direction: 检索增强生成 · 合规文档处理
tags:
- RAG
- Compliance
- Chunking
- Information Retrieval
- LLM Application
one_liner: 提出融合引用感知智能分块与重排的RAG管道，大幅提升法规类文档驱动场景生成的合规性与效率
practical_value: '- 处理带大量交叉引用、表格的业务文档（如电商平台规则、广告合规条款、促销活动规则）时，可复用规则化引用识别+BFS遍历的方法补全关联上下文，避免检索到孤立片段导致生成内容不符合规则

  - 检索优化可复用「基础chunk+关联引用内容」的富集检索单元设计，相比仅检索原始chunk，能大幅提升分散关联信息的召回率，尤其适合合规类、规则类RAG场景

  - 生成内容需校验关键数值、枚举类标签（如电商满减数值、广告合规禁用标识）时，可复用「语义相似度+关键属性正则匹配惩罚」的评估框架，比单纯语义匹配准确率高30%以上

  - 处理PDF解析的跨页表格碎片时，可复用规则化的连续<table>标签合并heuristic，避免表格信息断裂导致的参数错误'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM生成高合规性要求内容时，易因长文档上下文超限、跨章节/表格引用分散、检索片段孤立等问题出现幻觉，直接输入全量文档token成本高、长上下文利用率低；现有RAG系统的通用分块、检索逻辑无法覆盖跨引用关联信息，在汽车法规、电商规则等对参数准确度要求极高的场景下，生成内容合规性不足。

### 方法关键点
- SmartChunking：将PDF转结构化Markdown，识别文档内标题引用、表格引用，构建引用有向图，通过BFS遍历为每个基础chunk补全所有关联引用内容，形成自包含的富集chunk，同时通过BFS深度限制、去重、元数据压缩控制token量
- 智能检索重排：直接对富集chunk做语义检索，检索后对选中chunk的引用内容二次去重，再按照原文档的层级编号排序，为LLM提供逻辑连贯的上下文
- 定制化评估指标：在语义相似度基础上，加入数值、关键枚举属性的匹配惩罚项，避免因语义模板一致但参数错误导致的评估虚高

### 关键结果
在UN R152法规的AEBS测试场景生成手动标注数据集上，对比5种基线RAG系统，RegulaRAG平均Meta-Score达82.99，比次优方案高出43%；单查询token消耗仅14k~25k，远低于图基线的最高500k；且在语料库规模扩大时性能无明显衰减，而基线系统性能大幅下降。

### 核心结论
处理结构明确、交叉引用多的规则类文档时，先基于文档原生结构做引用感知的chunk富集，比盲目优化检索模型或扩大上下文窗口的投入产出比高得多
