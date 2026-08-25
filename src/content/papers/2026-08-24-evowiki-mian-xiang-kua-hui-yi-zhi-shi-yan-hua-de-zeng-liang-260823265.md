---
title: 'EvoWiki: Incremental State Overwriting and Traceable Question Answering for
  Cross-Meeting Knowledge Evolution'
title_zh: EvoWiki：面向跨会议知识演化的增量覆写可追溯问答系统
authors:
- Dongsheng Chen
- Tianyu Wang
- Wenhui Que
affiliations:
- WeChat, Tencent Inc.
arxiv_id: '2608.23265'
url: https://arxiv.org/abs/2608.23265
pdf_url: https://arxiv.org/pdf/2608.23265
published: '2026-08-24'
collected: '2026-08-25'
category: Agent
direction: Agent动态记忆 · 可追溯知识QA
tags:
- RAG
- Long-Context QA
- Knowledge Evolution
- Agent Memory
- Temporal Reasoning
one_liner: 提出带实体版本链与状态覆写协议的EvoWiki架构，解决跨会议动态知识QA的冲突与溯源问题
practical_value: '- 做电商商家/运营多会话知识沉淀Agent时，可复用状态覆写协议：对同一实体的多轮更新保留版本链，标记Active/Overturned状态，避免RAG召回过期活动规则、商品价格、运营策略等信息，大幅降低事实错误。

  - 电商活动规则/价格动态更新的客服QA场景，可借鉴Build-Read分离架构：将冲突消解、实体对齐、新旧状态区分移到写入时离线完成，在线读直接走确定性实体寻址，绕过语义Top-k召回容易返回过时结果的问题。

  - 可复用版本溯源机制：每个状态绑定来源会话/证据span，客服回答用户活动规则、售后政策疑问时可自动附上来源文件/会议纪要片段，降低客诉举证成本，提升合规性。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
跨多轮会议/会话的动态知识QA场景中，现有长上下文直接读取、传统RAG、静态结构化记忆方案均未建模知识生命周期与替换关系，容易同时召回新旧冲突状态，要么丢失历史溯源信息，要么返回过期结果，无法满足企业级知识管理的事实一致性与可审计需求。

### 方法关键点
- 采用Build-Read不对称架构：离线Build阶段处理增量会议流，依次做时间对齐、会内演化解析（区分提案/讨论/最终决议）、写时共指消解、事实抽取、实体路由，最终通过State-Overwrite协议更新知识库
- 结构化Wiki核心维护实体版本链：同一实体属性的更新不删除旧状态，仅将旧状态标记为Overturned，新状态标记为Active，每个状态绑定来源会议、证据span与生效时间，保留完整溯源路径
- 在线Read阶段无需访问原始会议，直接对结构化Wiki做确定性实体寻址、时间解析、跨实体多跳聚合，生成带溯源信息的答案

### 关键结果
在自建双语CrossMeet基准（中英各100个项目、500场会议、2000条QA对）+4个公开QA数据集上，对比9种基线（Direct LLM、各类RAG、GraphRAG、LogicRAG等），使用DeepSeek-V4-Flash时EvoWiki宏观Judge Accuracy达60.09%，领先最强基线9.72个百分点；使用Qwen3.5-397B时达63.02%，领先最强基线10.00个百分点；状态翻转4次时准确率仅下降4.13个百分点，远优于基线的20+百分点下降，同时缓解长上下文Lost-in-the-Middle效应。

### 核心结论
把实体消歧、冲突消解的复杂逻辑移到离线写入阶段完成，是解决动态演化知识QA事实一致性问题的性价比最高的路径。
