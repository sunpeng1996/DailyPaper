---
title: 'Beyond Retrieval: Analytic Memory for Multimodal Agents'
title_zh: 面向多模态Agent的分析型内存架构：超越传统检索范式
authors:
- Zhoujin Tian
- Yao Tian
- Hao Zhang
- Cheng Chen
- Yakun Li
- Lei Zhang
- Xiaofang Zhou
affiliations:
- HKUST
- ByteDance
arxiv_id: '2607.29440'
url: https://arxiv.org/abs/2607.29440
pdf_url: https://arxiv.org/pdf/2607.29440
published: '2026-07-31'
collected: '2026-08-03'
category: Agent
direction: 多模态Agent · 长时记忆架构优化
tags:
- Multimodal Agent
- Long-term Memory
- Analytic Memory
- Schema Induction
- Query Planning
one_liner: 提出融合检索内存与自动schema归纳分析内存的ADAMM框架，提升多模态Agent长时记忆查询准确率
practical_value: '- 电商用户长时行为分析场景可复用ADAMM的自动schema归纳逻辑：从多模态交互（直播浏览、对话、订单截图）中自动抽取高频属性生成结构化表，替代人工定义用户画像标签体系，降低维护成本

  - 导购Agent的记忆系统可采用双内存设计：检索内存处理语义召回类查询（如「我之前看过的蓝色连衣裙」），分析内存处理统计类查询（如「我这个月花了多少钱在美妆上」），同时支持两类用户需求

  - 可复用渐进式工具执行的规划逻辑：先生成高层面执行计划，再根据前序工具返回结果动态填充后续工具参数，避免多步查询的参数绑定错误，提升复杂query的处理准确率

  - 多模态记忆提取的provenance关联设计值得借鉴：每个抽取的属性值都绑定源对话片段或图像，当结果出错时可快速溯源定位提取错误，方便问题排查'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有多模态Agent长时记忆系统普遍基于检索范式，仅能返回与查询语义相关的片段信息，无法可靠处理需要全量过滤、聚合、时序对比的分析类查询（如统计用户过去1个月的平均消费额），存在检索-分析不匹配问题：检索结果过少会遗漏必要数据导致统计偏差，检索结果过多会占用有限的上下文窗口引入冗余信息，严重降低复杂查询的准确率。

### 方法关键点
- 双内存互补架构：同时维护检索内存与分析内存，检索内存采用topic→episode→event三级层级组织多模态交互信息，支持灵活的语义召回；分析内存自动从对话、图像等多模态数据中抽取带溯源信息的属性值对，基于频繁项集挖掘自动归纳高频schema，将重复出现的结构化观测实体化为可直接查询的关系表
- 自适应查询规划：将两类内存的能力封装为专用工具（分析内存支持LOOKUP、FILTER、COMPUTE、RANK操作，检索内存支持SEMANTICMATCH、EVENTLOCATE操作），查询时先召回与query相关的内存元数据生成高层执行计划，再渐进式实例化工具调用参数，后续工具可复用前序工具的返回结果，避免参数绑定错误

### 关键结果
在MemEye、MemGallery两个多模态长时记忆基准上测试，对比A-Mem、MIRIX、MM-RAG等8个强基线：使用GPT-4.1-nano作为底座时，MemEye准确率最高提升7.3%，MemGallery F1提升4.2%、LLM-judge得分提升7.0%；使用GPT-5.4-mini作为底座时，MemEye LLM-judge得分最高提升11.3%，MemGallery LLM-judge得分提升5.2%；其中需要统计分析的健康、卡券日志类任务提升幅度最高达18.8%。

### 核心结论
长时记忆系统不能仅依赖语义检索，面向重复出现的结构化观测自动构建可计算的分析内存，能大幅提升Agent处理复杂统计类查询的能力。
