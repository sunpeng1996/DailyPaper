---
title: 'Hi-Q: Hierarchical Evidence-guided Query Refinement for Multi-Hop Question
  Answering'
title_zh: Hi-Q：面向多跳问答的分层证据引导查询细化方法
authors:
- Jueun Kim
- Sungho Park
- Wook-Shin Han
affiliations:
- Department of Computer Science and Engineering, POSTECH
- Graduate School of Artificial Intelligence, POSTECH
arxiv_id: '2608.30468'
url: https://arxiv.org/abs/2608.30468
pdf_url: https://arxiv.org/pdf/2608.30468
published: '2026-08-31'
collected: '2026-09-02'
category: QueryRec
direction: 多跳查询细化 · 证据引导检索
tags:
- Query Refinement
- Multi-hop QA
- RAG
- Hierarchical Reasoning
- Evidence-guided
one_liner: 提出证据驱动的分层查询细化框架，无需预建语料图即可大幅提升多跳QA的检索与回答效果
practical_value: '- 电商搜索多跳query改写场景可复用分层证据判断逻辑：先校验当前query召回结果是否满足需求，不满足再做依赖保留的拆分细化，避免无效改写

  - 多跳RAG系统无需预建全局语料图，可通过动态生成的查询树拓扑适配语料粒度，大幅降低图构建的工程与计算成本

  - 搜索query rewrite、商品多属性检索场景可引入语义覆盖校验模块，保证拆分后的子query覆盖原query完整语义，避免信息丢失'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
多跳QA核心瓶颈是用户查询的表述粒度与语料可检索粒度不匹配，现有方法要么依赖固定语料图、要么用固定模板拆分query，无法动态判断当前查询单元是否已匹配到足够证据，检索精度低且额外开销大。
### 方法关键点
提出Hi-Q分层证据引导的查询细化框架，核心包含三个模块：1）解析算子：针对每个查询节点校验召回证据是否支持当前查询单元，已支持则终止细化；2）依赖保留二元拆分算子：对未解析的查询节点做语义拆分，保证子节点间依赖关系不丢失；3）语义覆盖校验器：校验拆分后的子节点是否完整覆盖父节点语义，避免信息损失。整体查询树拓扑完全由语料的支持信号动态生成，无需预建全局语料图或固定拆分模板。
### 关键结果
全语料检索场景下，三个多跳QA基准平均EM达52.3、F1达64.0，较IRCoT基线高15.1 EM、18.2 F1，较PropRAG基线在MuSiQue-full数据集上高11.5 EM、12.0 F1；受限语料场景下平均EM达57.9、F1达69.3，同样优于现有基线。
