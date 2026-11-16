---
title: 'MIRIX-2.0: Multi-Agent Memory System'
title_zh: MIRIX-2.0：面向LLM Agent的多智能体长时记忆系统
authors:
- Wei-Chieh Huang
- Weizhi Zhang
- Jiayan Nan
- Peng Xia
- Yu Wang
affiliations:
- MIRIX AI
- Tongji University
- University of North Carolina at Chapel Hill
- University of California San Diego
- University of Illinois Chicago
arxiv_id: '2611.12068'
url: https://arxiv.org/abs/2611.12068
pdf_url: https://arxiv.org/pdf/2611.12068
published: '2026-11-08'
collected: '2026-11-16'
category: Agent
direction: Agent 长时记忆系统优化
tags:
- Multi-Agent
- LLM Agent
- Memory System
- Hypergraph
- Procedural Memory
one_liner: 提出兼顾准确性、实用性、效率的多智能体记忆系统，支持用户与Agent双场景记忆存储检索
practical_value: '- 电商智能导购Agent可复用分层记忆设计：用户侧完整存储浏览、偏好、订单原始记录，用n-ary超图索引实体关系，既不丢失细节又保证检索效率，支撑个性化推荐和查询应答

  - Agent任务流程优化可借鉴AutoDream离线机制：离线合并重复实体、提炼电商选品/下单等场景的成功/失败经验为可复用技能，不影响线上写入路径性能，可提升任务成功率

  - 可直接复用检索预算控制逻辑：给超图遍历、原始记录召回分别设固定预算，不管历史数据量多大，检索耗时和Token成本都可控，适配高并发线上业务场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent长时记忆方案存在明显短板：参数记忆需要微调无法兼容闭源模型，全量原始记录检索效率随历史增长持续下降，结构化摘要/三元组存储容易丢失原始细节，且无法同时满足用户个性化记忆、Agent任务技能记忆两类场景需求，亟需兼顾准确、实用、高效的通用记忆系统。

### 方法关键点
- 分层保真架构：6类专用记忆Agent负责将完整原始记录写入向量库作为唯一可信数据源，永不修改；用溯源超图作为索引，以n-ary框架存储实体、关系、属性，所有索引节点均关联原始记录ID，索引写入失败不影响原始记录存储
- 可控检索机制：查询时先通过规划器设定超图遍历、原始记录召回的双预算，从匹配查询的锚点开始遍历超图，仅召回预算内的关联事实和对应原始记录，检索开销不随历史增长膨胀
- AutoDream离线合并：语义记忆侧离线合并同实体的重复锚点，仅修改索引不碰原始记录； procedural记忆侧从历史任务会话中提炼可复用技能和避坑规则，所有修改均可溯源

### 关键实验
在5个QA基准上4个准确率领先，LoCoMo达91.4%，LongMemEval-S达72.6%超最强基线14.3个点；单/多跳文档QA超HyperMem 31.0、22.0个点；作为任务记忆在电商交互基准WebShop上成功率达37.4%，MetaClaw-Bench达49.2%超原技能库5.2个点；关闭AutoDream时所有基准回答速度均快于HyperMem，无需微调支持闭源/开源模型。

**最值得记住的一句话**：记忆系统的核心设计原则是「存储层绝对保真，索引层按需组织，合并逻辑完全离线」，在不丢失原始信息的前提下平衡准确性和效率。
