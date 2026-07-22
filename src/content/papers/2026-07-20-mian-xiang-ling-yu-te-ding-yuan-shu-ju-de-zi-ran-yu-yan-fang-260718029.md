---
title: 'Natural Language Access to Domain-Specific Metadata: A Reusable Framework
  for LLM Query Generation'
title_zh: 面向领域特定元数据的自然语言访问：LLM查询生成可复用框架
authors:
- Blake G. Fitch
- Cato Elia Kurtz
affiliations:
- Max Planck Institute for Biological Cybernetics
arxiv_id: '2607.18029'
url: https://arxiv.org/abs/2607.18029
pdf_url: https://arxiv.org/pdf/2607.18029
published: '2026-07-20'
collected: '2026-07-22'
category: QueryRec
direction: 自然语言查询生成 · 知识图谱
tags:
- SPARQL
- Ontology
- Zero-shot
- Knowledge Graph
- Query Generation
one_liner: 基于OWL本体构建可复用NLKGQ框架，零样本实现自然语言转结构化查询，无需微调或RAG
practical_value: '- 搭建电商运营/商家侧自然语言数据分析工具时，优先给知识图谱实体补充可读名称与语义标注，收益远高于调优模型或prompt

  - 涉及用户隐私的内部数据查询场景，可基于OWL本体+本地LLM搭建自然语言转结构化查询链路，无需调用外部大模型API

  - 结构化查询生成场景优先选择OWL+SPARQL作为后端架构，相比SQL DDL可显著提升LLM生成查询的准确率'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
领域从业者需要查询专属档案的元数据，但大多不具备编写结构化查询的专业能力，现有方案依赖微调、RAG或多Agent架构，落地成本高且隐私性不足。

### 方法关键点
提出可复用NLKGQ框架：首先基于OWL本体沉淀领域词汇与语义，将档案元数据导入对应知识图谱；用户输入自然语言问题后，领域无关调度模块直接调用LLM零样本生成SPARQL查询，执行后返回结果，全程无需微调、RAG或多Agent编排。

### 关键结果
在神经影像档案专家构建的测试集上，最优配置准确率达100%；消融实验显示，实体可读名称与语义标注对准确率的影响远高于模型选择或prompt工程；OWL+SPARQL架构相比SQL后端，LLM查询生成准确率提升显著，支持本地部署满足隐私要求。
