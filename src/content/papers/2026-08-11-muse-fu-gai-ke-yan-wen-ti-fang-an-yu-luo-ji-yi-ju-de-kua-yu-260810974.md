---
title: 'MUSE: A Full-Text Cross-Domain Knowledge Base of Scientific Problems, Solutions,
  and Rationales'
title_zh: MUSE：覆盖科研问题、方案与逻辑依据的跨领域全文知识库
authors:
- Tsofia Cohen
- Tom Hope
affiliations:
- The Hebrew University of Jerusalem
- Allen Institute for AI (Ai2)
arxiv_id: '2608.10974'
url: https://arxiv.org/abs/2608.10974
pdf_url: https://arxiv.org/pdf/2608.10974
published: '2026-08-11'
collected: '2026-08-12'
category: RAG
direction: 科研知识抽取 · RAG知识库构建
tags:
- Knowledge Base
- Information Extraction
- Rationale Supervision
- Triplet Extraction
- Scientific NLP
one_liner: 构建含37K问题-方案-依据三元组的科研知识库，验证理由监督对LLM解题的效果差异
practical_value: '- 可复用「小批量专家标注+模块化抽取pipeline」范式，沉淀电商场景用户痛点、运营方案、优化逻辑的结构化三元组知识库，支撑Agent决策、策略迭代的RAG检索

  - 针对复杂多约束业务问题（如大促多目标资源分配、个性化文案生成），给LLM添加rationale监督训练可显著提升效果，简单任务无需添加避免负向影响

  - 结构化知识标注时加入来源溯源、共指关联的设计，可大幅提升业务知识库的检索准确率与可解释性'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有科研结构化知识库未覆盖细粒度的「问题-解决方案-选择依据」关联关系，无法支撑复杂科研问题的推理、方案检索需求，也缺少对应的标注与规模化抽取范式。
### 方法关键点
1. 设计包含问题/方案/依据文本span、关联关系、概念共指的完整标注schema，完成579段全文段落的专家标注；
2. 搭建模块化信息抽取pipeline，规模化扩展标注生成带来源溯源的三元组，构建MUSE知识库；
3. 开展rationale监督的LLM科学解题对比实验，验证监督信号的适用场景。
### 关键结果
1. 生成37K高质量跨领域P-S-R三元组知识库；
2. rationale监督可提升复杂多约束问题的LLM解题性能，但会降低简单问题的表现。
