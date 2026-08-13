---
title: Constructing Dynamic Master Logic Models as Knowledge Graphs for Complex System
  Diagnostics Using Retrieval-Augmented Large Language Models
title_zh: 基于RAG大模型构建用于复杂系统诊断的知识图谱型动态主逻辑模型
authors:
- Saman Marandi
- Yu-Shu Hu
- Mohammad Modarres
affiliations:
- Center for Risk and Reliability, University of Maryland
- DML Inc., Hsinchu, Taiwan
arxiv_id: '2608.12304'
url: https://arxiv.org/abs/2608.12304
pdf_url: https://arxiv.org/pdf/2608.12304
published: '2026-08-12'
collected: '2026-08-13'
category: RAG
direction: RAG+LLM 结构化知识图谱自动构建
tags:
- RAG
- Knowledge Graph
- LLM
- System Diagnostics
- Knowledge Construction
one_liner: 结合RAG与LLM自动从复杂系统技术文档构建知识图谱形式动态主逻辑模型支撑诊断与可靠性分析
practical_value: '- 分层定向检索+层级依赖校验的思路可直接复用在电商品类知识图谱、用户行为因果图谱的自动化构建场景，大幅降低人工标注成本

  - 多层级质量校验框架可迁移到RAG结构化输出的质量评估环节，同时覆盖元素准确率、层级结构一致性、整体完整性三个维度，减少人工质检工作量

  - 长文档定向关联检索的设计可复用在电商售后知识库、工单系统的RAG落地中，解决跨模块信息关联抽取准确率低的问题'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
动态主逻辑（DML）是连接系统功能目标与底层结构元素的层级化系统行为刻画框架，传统构建依赖专家人工解读技术文档，在复杂系统场景下扩展性极差，无法支撑规模化诊断、可靠性分析需求。

### 方法关键点
提出RAG+LLM的自动化KG-DML构建框架，沿DML层级做定向检索，完整保留功能依赖与显式逻辑关系；配套多层级验证方法，覆盖层间Precision/Recall、逻辑门一致性、整体结构完整性三个维度的校验。

### 关键结果
在退役沸水反应堆低压冷却剂注入系统场景验证，重复运行构建结果一致性高，可直接将技术文档转化为可执行功能模型，支撑诊断推理、安全评估、故障传播分析、依赖溯源等任务。
