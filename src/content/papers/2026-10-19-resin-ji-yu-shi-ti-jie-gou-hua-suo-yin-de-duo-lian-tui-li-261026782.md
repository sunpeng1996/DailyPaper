---
title: 'RESIN: Multi-Chain Reasoning with Entity-Structured Indexing'
title_zh: RESIN：基于实体结构化索引的多链推理框架
authors:
- Xuanyu Meng
- Jash Rajesh Parekh
- Jiawei Han
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2610.26782'
url: https://arxiv.org/abs/2610.26782
pdf_url: https://arxiv.org/pdf/2610.26782
published: '2026-10-19'
collected: '2026-10-20'
category: RAG
direction: RAG 多链推理性能优化
tags:
- RAG
- Multi-Chain Reasoning
- Entity Indexing
- Evidence Retrieval
- QA
one_liner: 通过实体结构化索引+延迟证据选择提升多链推理的召回与答案相关性
practical_value: '- 电商知识库RAG可复用其6类实体结构化推理单元（实体事实、因果边等）拆分知识，解决多约束商品查询（如「3000以内轻薄游戏本」）的漏召回问题

  - 多跳推理场景为每个单跳子查询分配独立top-k检索预算，保留所有候选到最终生成阶段，避免导购Agent做商品推荐时过早剪枝丢失关键证据

  - 离线索引保留原始文本溯源链接，最终生成直接基于原始文本而非结构化三元组，可降低抽取错误传播，适配商品参数、售后政策等高合规要求的回答场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有多链推理RAG存在两类核心缺陷：单次全局检索易引入大量无关上下文，挤占有效证据的上下文窗口；过早选定单条推理路径或剪枝知识图，易丢失后续推理需要的关键证据，无法满足需要整合多条独立证据链的复杂查询需求。
### 方法关键点
- 离线构建6类带溯源的实体结构化推理单元（实体事实、类型属性、实体类型、关系、因果边、规则），缓存单元向量，同时保留到原文本的完整链路，不依赖预构建知识图。
- 在线阶段将复杂查询拆分为最多4个独立的单跳子查询，每个子查询分配独立的top-k检索预算，互不干扰，默认k=10。
- 所有单跳检索到的单元映射回原文本构建推理缓冲，最终生成仅基于原始查询和缓冲内的原文本，不使用中间子查询的生成结果，避免错误传播。
### 关键实验
在跨医学、计算机、商业等5个领域的HolisQA基准上，对比SOTA基线CausalRAG2，整体context recall达82.92%、answer relevancy达76.70%，4个领域F1领先；在MS MARCO基准上context recall达91.65%，QASC上达84.51%，远超所有基线。
### 核心结论
精确的证据组织与延迟的决策承诺，是提升多链推理效果与可审计性的核心。
