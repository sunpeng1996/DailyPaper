---
title: 'Seeing, Maintaining, and Learning: The Evolution of Multimodal Agent Memory'
title_zh: 《多模态智能体记忆的演化框架：感知、维护与学习》
authors:
- Minghao Guo
- Qingyue Jiao
- Xiujin Liu
- Jianhong Pang
- Ruimeng Yang
- Naihao Xu
- Liwei Che
- Haochen Xue
- Ziqi Wang
- Xinying Cai
affiliations:
- Rutgers
- Notre Dame
- Fudan
- UC San Diego
- UIUC
arxiv_id: '2610.19366'
url: https://arxiv.org/abs/2610.19366
pdf_url: https://arxiv.org/pdf/2610.19366
published: '2026-10-13'
collected: '2026-10-15'
category: Agent
direction: 多模态智能体 · 记忆机制框架
tags:
- Multimodal Agent
- Memory Mechanism
- Agent Framework
- Memory Management
- Survey
one_liner: 提出双轴多模态智能体记忆分析框架，覆盖297种现有架构与82项基准并总结设计原则
practical_value: '- 多模态用户行为记忆设计可直接复用双轴框架：Axis I选择存储形式（源素材/模态特征/文本结构化/参数），Axis II选择管理等级（静态/动态/自演进），快速适配不同业务的成本与精度需求

  - 电商多模态Agent（如导购、直播内容理解）可优先采用混合记忆架构：用文本/结构化记录做检索索引，关联原始多模态素材（商品图/视频/直播片段），平衡检索效率与信息保真度

  - 长周期用户个性化记忆可参考T3自演进策略：基于用户交互反馈自动优化记忆的写入、遗忘、检索规则，减少人工迭代策略的成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多模态Agent落地长周期任务（如长会话导购、用户长期兴趣建模）时，无法有效从异构多模态数据中持续沉淀有用信息，记忆机制缺乏统一分析框架，设计时难以平衡保真度、效率、演进能力的 trade-off，业务落地无通用参考标准。

### 方法关键点
- 提出双轴分析框架：Axis I为记忆形成与表示，分为4类：源模态原生表示、跨模态显式表示、隐式参数化表示、混合表示，明确不同表示的保真度、存储成本、可编辑性 trade-off
- Axis II为记忆管理，分为3个层级：T1静态记忆（仅复用固定内容不修改）、T2动态记忆（基于固定策略更新记忆内容）、T3自演进记忆（基于反馈自动更新记忆管理策略）
- 梳理297种现有多模态记忆架构、82项基准数据集，总结出4项核心设计原则：平衡源数据保真度与抽象效率、维护时间有效性与来源可追溯、记忆使用需关联可复现证据、记忆策略需随时间迭代

### 关键结果数字
统计显示2023-2026年具身、视频类多模态记忆架构增长最快；当前已落地方案中80%以上采用T1/T2级记忆管理，T3自演进记忆落地占比不足10%；混合表示架构相比纯源模态存储可降低70%以上的检索与存储成本，同时保留92%的任务精度。

### 最值得记住的一句话
多模态记忆设计没有最优解，需根据下游任务对保真度、效率、个性化程度的需求，在表示类型与管理等级间做适配性选择。
