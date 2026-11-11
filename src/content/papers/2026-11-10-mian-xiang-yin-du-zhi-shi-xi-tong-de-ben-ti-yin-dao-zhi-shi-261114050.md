---
title: Ontology-Guided Knowledge Graph Construction and Robust Evidence Retrieval
  for Indian Knowledge Systems
title_zh: 面向印度知识系统的本体引导知识图谱构建与鲁棒证据检索
authors:
- Anand Kaniyaar Sriranga Prasad
- Avinash Holenarasipur Nagendra
- Mohan Raghavan
affiliations:
- Indian Institute of Technology Hyderabad
- HTSR Institute
- Central Sanskrit University
- Bheri Technology Foundation
arxiv_id: '2611.14050'
url: https://arxiv.org/abs/2611.14050
pdf_url: https://arxiv.org/pdf/2611.14050
published: '2026-11-10'
collected: '2026-11-11'
category: RAG
direction: RAG · KG增强多跳证据检索
tags:
- KnowledgeGraph
- OntologyGuided
- EvidenceRetrieval
- MultiHopRetrieval
- RAG
one_liner: 提出本体引导的KG构建与检索pipeline，在多跳等复杂查询上优于纯向量检索的早期排序精度
practical_value: '- 电商/内容领域的业务知识图谱构建可复用两阶段LLM抽取流程：先基于业务领域本体约束抽取实体、类型及摘要，再逐实体提取合法范围内的关系，可大幅降低无效三元组占比

  - 多跳类用户查询（如「适合跑步的防水平价运动鞋」）的召回可借鉴KG+向量检索融合策略：优先用KG保证前几结果的相关性，合并向量检索结果提升整体召回覆盖率

  - RAG/智能客服系统的结果融合可根据业务目标选择策略：重视首条结果正确性用单独KG输出，重视证据全面性用KG+向量+多源结果全重排，多跳场景可将多通路交集结果置顶提升首中率

  - 可复用检索效果-延迟权衡框架：提前按查询类型路由到不同通路，简单查询用纯向量检索降低latency，复杂多跳查询用KG+向量融合保证效果'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
印度知识系统的文本存在大量音译变体、名称歧义、关系跨段落分布等问题，传统稠密检索仅依赖语义相似性无法显式建模实体间的关联逻辑，容易召回同名异义实体、漏选跨段落关联证据，无法满足多跳、计数、复合类复杂查询的证据检索需求。

### 方法关键点
- KG构建：基于分领域本体约束，用Qwen3-32B做两阶段抽取，先提取实体及对应类型、语义摘要，再逐实体提取符合本体规则的关系，通过名称正则+语义相似度阈值合并同义实体，存储时所有三元组关联原始文本片段做溯源
- 检索流程：先做查询实体消歧，结合有界2跳图遍历、词法锚点匹配、关系向量搜索获取候选三元组，经RRF分数融合后映射回原始文本片段，可选合并单向量检索（SV）、实体笔记（EN）的候选集后重排
- 融合策略：支持全量候选统一重排、多通路交集结果优先置顶两种模式，适配不同业务目标

### 关键实验结果
实验基于Dhara Bench的320条专家标注查询，对比4种检索配置，重排器用BGE和Qwen：
- 单独KG在Qwen重排下多跳查询MRR@20达0.8722，较纯SV高14.4%，完整证据CE-MRR@20达0.4651，较SV高37.9%
- KG+SV+EN融合配置在Qwen重排下整体Recall@20达0.5134，较单独KG高18.1%
- 单独KG平均检索耗时20.37s，是SV的31.6倍，Qwen重排耗时是BGE的7.3倍

### 核心结论
KG更擅长提升复杂查询的早期排序精度，纯向量检索更擅长提升召回覆盖度，两者融合可根据业务对首条相关性、召回率、延迟的要求灵活选型
