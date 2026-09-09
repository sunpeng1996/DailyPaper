---
title: 'Beyond One-Shot Expansion: Contrastive Evidence Exploration for Multi-Hop
  Retrieval'
title_zh: 超越单次扩展：面向多跳检索的对比证据探索框架
authors:
- JungMin Yun
- YoungBin Kim
affiliations:
- Chung-Ang University
arxiv_id: '2609.07050'
url: https://arxiv.org/abs/2609.07050
pdf_url: https://arxiv.org/pdf/2609.07050
published: '2026-09-07'
collected: '2026-09-09'
category: RAG
direction: RAG优化 · 多跳检索
tags:
- Multi-Hop Retrieval
- Query Expansion
- RAG
- Training-Free
- Contrastive Index
one_liner: 提出训练免费的多跳检索框架，融合对比索引、迭代探索和覆盖度排序，显著提升多跳QA效果
practical_value: '- 电商导购Agent、售后咨询等多轮复杂查询场景可直接复用「迭代证据探索+覆盖度排序」的pipeline，无需额外训练即可适配现有RAG底座，提升复杂问题的解答准确率

  - 离线阶段可借鉴passage-specific对比facet构建方法，为商品/内容知识库的每个片段生成唯一区分性query，提升相似内容的检索区分度，解决电商同款/相似商品检索混淆问题

  - 候选排序阶段的覆盖度增益计算逻辑可直接迁移到推荐系统的多样性排序模块，平衡相关性和互补性，减少推荐结果冗余，提升多意图query的召回覆盖'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多跳RAG检索依赖固定意图或单次query扩展，无法适配迭代发现的新证据，易引入噪声、遗漏推理链所需的互补证据，导致多跳复杂问题的召回率和下游QA效果不佳，无法满足需要跨多段信息关联推理的场景需求。

### 方法关键点
- 离线阶段：为每个语块召回Top10语义相似邻居，用LLM生成仅能从目标语块回答、无法从邻居回答的对比facet query，构建专属对比索引，无额外训练成本
- 在线推理：迭代执行多轮检索，每轮基于已召回证据生成摘要，再生成针对未解决信息需求的新检索探针，逐步补全推理链所需证据
- 相关性精排：用语块的对比facet加权修正原语义相似度得分，区分语义相似但承载不同推理信息的候选
- 最终选排：采用覆盖度感知的贪心策略选TopK，优先选择能覆盖未被满足的探针需求的候选，平衡相关性和证据互补性

### 关键实验
在MuSiQue、HotpotQA、2WikiMultihopQA三个多跳QA数据集上，对比BM25、e5-large-v2、bge-reranker、HyDE、IRCoT等基线，MuSiQue数据集FSR@10（全支持证据召回率）从39.2提升至57.0，2WikiMultihopQA FSR@10从75.6提升至91.5，下游QA的EM得分平均提升3~4个点，所有指标均领先基线。

### 核心结论
多跳检索的核心不是单次召回最相关的内容，而是迭代探索覆盖推理链全环节的互补证据，训练免费的轻量优化就能带来显著收益。
