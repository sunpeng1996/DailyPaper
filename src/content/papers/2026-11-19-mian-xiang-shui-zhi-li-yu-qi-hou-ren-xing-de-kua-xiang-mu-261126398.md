---
title: 'Democratizing Cross-Project Knowledge for Transforming Water Governance and
  Climate Resilience: an Agentic AI Ecosystem'
title_zh: 面向水治理与气候韧性的跨项目知识共享Agentic AI生态
authors:
- Oriol Alàs
- Ian Palacín
- Iván Cester
- Edgar Rubión
affiliations:
- Eurecat, Centre Tecnològic de Catalunya, Barcelona, Spain
arxiv_id: '2611.26398'
url: https://arxiv.org/abs/2611.26398
pdf_url: https://arxiv.org/pdf/2611.26398
published: '2026-11-19'
collected: '2026-11-20'
category: Agent
direction: Agent 跨域知识库检索编排
tags:
- Agentic AI
- RAG
- Embedding Fine-tuning
- ReAct
- Retrieval Orchestration
one_liner: 提出整合异构跨项目文档的Agentic RAG生态，相对单embedding基线MRR升26.7%
practical_value: '- 处理多来源异构业务文档（如多品类商品介绍、多项目运营报告）时，可先重构为层级章节树+结构化元数据索引，降低后续检索噪声

  - 多垂直域检索场景可拆分领域微调专属embedding，对比单通用embedding基线能获得显著效果提升，可复用在电商品类/内容垂类检索

  - 多源召回场景可采用ReAct风格控制器动态分配不同召回池的检索配额，直到满足停止条件，降低无效检索开销的同时提升召回准确率'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
欧盟水治理、气候领域的资助项目产出大量报告、案例、交付物，知识分散在不同项目且文档结构异构，决策阶段难以快速定位上下文相关的有效信息。
### 方法关键点
1. 异构项目文档重构为层级章节树，绑定结构化元数据索引，构建领域感知知识库；
2. 微调水、气候两个垂直域专属embedding模型支撑底层检索；
3. 上层部署ReAct风格控制器迭代编排检索动作，跨领域集合动态分配检索预算，持续积累证据直到触发停止条件。
### 关键结果
在目标语料的检索基准测试中，相对单领域embedding基线，MRR相对提升26.7%，可稳定支撑跨项目知识合成与气候韧性决策。
