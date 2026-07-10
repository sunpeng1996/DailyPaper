---
title: Conversational Retrieval and On-the-Fly Knowledge Modeling of Historical Penitentiary
  Repression Records
title_zh: 对话式检索与历史监狱镇压记录的动态知识建模
authors:
- Paula Font Solà
- Adrià Molina Rodríguez
- Josep Lladós
affiliations:
- Computer Vision Center
- Universitat Autònoma de Barcelona
arxiv_id: '2607.08459'
url: https://arxiv.org/abs/2607.08459
pdf_url: https://arxiv.org/pdf/2607.08459
published: '2026-07-09'
collected: '2026-07-10'
category: RAG
direction: RAG增强 · 图结构动态知识建模
tags:
- RAG
- Knowledge Graph
- Conversational Retrieval
- Dynamic Knowledge Modeling
- Document Analysis
one_liner: 提出融合图结构记忆的RAG系统，支持历史文档库动态知识注入与跨文档关联查询
practical_value: '- 可复用「RAG+图结构记忆库」架构，将用户跨会话行为、运营专家规则、多触点业务数据关联为可查询图记忆，解决普通RAG仅能单文档片段检索的短板，适配电商客服Agent、长期用户兴趣建模场景

  - 动态知识注入机制可直接迁移，支持业务方实时新增规则、事实数据，无需重训模型或重构全量索引，适配大促、活动期间业务规则频繁迭代的需求

  - 跨文档关联推理思路可用于全场景用户行为序列建模，挖掘不同行为、不同触点间的隐含关联，提升推荐系统对长序列依赖的捕捉能力'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有RAG方案仅能基于单份文档片段完成抽取类任务，缺乏对文档集合的全局理解能力，也无法动态融入专家新增的知识，难以处理跨文档长依赖查询、隐含关联挖掘、隐式知识推理类需求。
### 方法关键点
1. 面向历史数字图书馆场景，搭建支持动态知识建模的对话式文档分析系统
2. 采用图结构存储两类事实：专家档案管理员输入的领域知识、文档检索过程中自动挖掘的关联事实，作为LLM可直接访问的外置记忆
3. 检索阶段同时从原始文档库、已构建的图记忆索引中召回相关信息，供给LLM生成回复
### 关键结果
可支持跨文档长依赖复杂查询、隐含关联发现、原始文档未明确标注的专家知识融合，生成内容的丰富度与全面性显著优于普通RAG方案
