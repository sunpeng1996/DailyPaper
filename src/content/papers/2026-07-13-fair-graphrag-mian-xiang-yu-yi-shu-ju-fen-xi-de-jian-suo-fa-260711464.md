---
title: 'FAIR GraphRAG: A Retrieval-Augmented Generation Approach for Semantic Data
  Analysis'
title_zh: FAIR GraphRAG：面向语义数据分析的检索增强生成方法
authors:
- Marlena Flüh
- Soo-Yon Kim
- Carolin Victoria Schneider
- Sandra Geisler
affiliations:
- RWTH Aachen University
- University Hospital RWTH Aachen
arxiv_id: '2607.11464'
url: https://arxiv.org/abs/2607.11464
pdf_url: https://arxiv.org/pdf/2607.11464
published: '2026-07-13'
collected: '2026-07-14'
category: RAG
direction: GraphRAG · FAIR知识图谱构建
tags:
- GraphRAG
- FAIR Principle
- Knowledge Graph
- RAG
- LLM for KG Construction
one_liner: 将FAIR数字对象作为图节点融入GraphRAG，提升领域问答准确率与可解释性
practical_value: '- 搭建电商/广告领域知识库RAG时，可将每个知识单元（商品、品牌、售后规则等）封装为带唯一Semantic ID、标准化元数据、类目映射的结构，大幅提升异构数据互操作性和复杂查询准确率

  - 构建业务知识图谱时，可复用LLM自动生成schema、提取实体元数据并映射到业务标准类目（如电商商品分类、广告定向标签体系）的pipeline，降低多源数据整合成本

  - 面向需要可解释性的业务场景（如合规广告推送、客诉智能回复），GraphRAG返回结果时可附知识来源ID、元数据和查询语句，方便结果溯源和人工校验'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有GraphRAG的底层知识资源缺乏标准化的FAIR（可发现、可访问、可互操作、可复用）治理，异构数据难以关联，尤其在专业领域会导致问答准确率低、结果不可追溯，无法支撑涉及元数据、语义关联的复杂查询。

### 方法关键点
- 提出以FAIR Digital Object（FDO）为图节点的KG模型，每个节点包含唯一Persistent Identifier（PID）、元数据、核心数据、领域本体链接四层结构，单节点本身满足FAIR标准。
- 端到端FAIR KG构建pipeline：先用LLM基于输入数据集自动生成适配业务的schema，再按schema提取实体信息，封装为FDO后自动生成PID、匹配领域本体，最后关联实体语义关系生成完整KG。
- 问答阶段基于KG schema和用户query让LLM自动生成图查询语句（如Cypher），返回自然语言答案同时附上原始查询语句、关联FDO的PID和元数据，完全支持结果溯源。

### 关键实验
在生物医学胆管癌RNA测序数据集上验证，对比未做FAIR治理的GraphRAG基线：gpt-4o-mini驱动的FAIR GraphRAG整体问答准确率达92.86%，较基线提升50个百分点；元数据、本体相关问题准确率从基线的0%提升至90%，可解释性达100%；基线完全无法回答元数据、本体类复杂查询。

### 核心结论
对知识资源做标准化可追溯封装，比单纯优化检索算法更能大幅提升领域RAG的复杂查询能力和可靠性。
