---
title: A Graph-Native Bitemporal Memory Store for Conversational AI Agents
title_zh: 面向对话AI Agent的图原生双时态记忆存储系统
authors:
- Alp Niksarli
- Gopesh Baheti
affiliations:
- Davidson College
arxiv_id: '2607.26520'
url: https://arxiv.org/abs/2607.26520
pdf_url: https://arxiv.org/pdf/2607.26520
published: '2026-07-29'
collected: '2026-07-30'
category: Agent
direction: Agent对话记忆 · 双时态图存储
tags:
- AgentMemory
- BitemporalDatabase
- GraphRAG
- SemanticRetrieval
- Neo4j
one_liner: 基于Neo4j实现图原生双时态对话Agent记忆存储，兼顾隐私、长时记忆留存与检索效率
practical_value: '- 电商客服Agent可复用双时态记忆架构：区分事实生效时间与系统记录时间，精准回溯用户历史偏好变更（如不同时期的尺码、地址变化），避免用旧信息错误响应

  - 隐私敏感类推荐场景（如医疗、金融电商）可落地本地图数据库+向量索引架构：无需调用第三方记忆服务，用户对话数据全程不出自有集群，同时支持语义关联检索

  - 记忆写入阶段自动构建语义关联边的技巧可复用：写时基于cosine相似度≥0.75阈值关联相似记忆节点，读时无需重排即可快速获取相关记忆，降低检索时延

  - 双索引设计可直接迁移：分别维护当前最新版记忆索引、全历史版本索引，兼顾日常检索效率与历史回溯需求，避免冗余存储'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有对话Agent跨会话记忆方案存在三类痛点：全量注入对话历史会消耗大量token、超出上下文窗口容量；依赖第三方记忆服务会泄露用户隐私，不适合金融、医疗等敏感场景；普通向量存储仅保留最新状态，无法区分不同时间生效的事实（如用户前后变更的收货地址、饮食禁忌），满足不了长周期交互需求。

### 方法关键点
- 数据模型拆分身份与版本节点：`:Memory`节点作为不变的身份锚点关联所有版本，`:MemoryVersion`节点存储具体内容、1024维embedding、双时态时间区间（valid time为事实生效时间，transaction time为系统记录时间），更新时仅新增版本节点不删除历史数据
- 双HNSW向量索引设计：`current_version_embedding`仅索引带`:CurrentVersion`标签的最新版本，支撑低延迟常规检索；`memory_version_embedding`索引全量版本，配合10倍过取+时态条件过滤支撑历史回溯检索
- 写时自动构建语义关联：每写入新记忆时，召回top5相似度≥0.75的记忆添加`RELATED_TO`边，降低后续关联记忆检索成本

### 关键实验
基于LongMemEval基准的60个抽样问题（覆盖6类记忆任务）测试，整体R@10为46.7%；其中单会话用户事实类任务R@10达90%，知识更新类任务R@10达80%；纯检索方案对跨会话聚合、偏好推理类任务表现较差，R@10仅为30%、10%。

### 核心结论
纯向量检索只能解决直接事实召回需求，涉及跨信息聚合、时态推理的记忆任务必须在存储层配套结构化建模与后处理逻辑才能达标。
