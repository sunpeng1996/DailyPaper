---
title: 'The User Asks, Platforms Compete: How Agentic Recommendation Markets Take
  Shape'
title_zh: 用户需求驱动下跨平台竞争的智能体推荐市场机制研究
authors:
- Deyao Hong
- Kehan Zheng
- Qian Li
- Jun Zhang
- Jie Jiang
- Hongning Wang
affiliations:
- Tsinghua University
- Tencent Inc.
arxiv_id: '2607.25253'
url: https://arxiv.org/abs/2607.25253
pdf_url: https://arxiv.org/pdf/2607.25253
published: '2026-07-28'
collected: '2026-07-29'
category: Agent
direction: 智能体推荐 · 跨平台市场机制设计
tags:
- Agentic Recommendation
- Cross-Platform Recommendation
- Market Mechanism
- LLM Simulation
- Reputation System
one_liner: 通过可控LLM模拟实验揭示智能体推荐市场访问、注意力与问责的协同设计规律
practical_value: '- 做跨平台聚合类推荐Agent的团队可直接复用LocalRep机制：通过记录平台过往推荐解释与用户实际反馈的匹配度校准排序，可将夸大解释的Top1占比从73-78%降至36-41%，同时提升目标商品购买率

  - 电商平台应对跨平台Agent竞争时需平衡解释的客观性与吸引力：纯夸大解释短期能提升转化率，但长期会被用户Agent的声誉机制降权；过于保守的解释则会在无声誉机制的场景下丢失流量

  - 跨端推荐产品设计需注意：盲目扩大候选池（接入更多平台）无法直接提升用户效用，固定短名单容量下接入平台从6个升到24个时，目标商品购买率反而下降13pp，需同步优化注意力分配机制'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统推荐模式下用户先选定平台再接收推荐，平台完全掌控候选池与排序权。LLM驱动的用户Agent打破了这一范式：用户先通过Agent明确需求，Agent跨平台发起推荐请求，各平台竞争用户注意力，形成了全新的智能体推荐市场。但该模式下平台会策略性操纵推荐解释抢占曝光，跨平台候选池扩张也会引发注意力分配瓶颈，缺乏系统性实证研究支撑机制设计。

### 方法关键点
- 基于亚马逊真实用户交互数据构建可控LLM模拟环境，还原用户请求、平台检索与解释生成、Agent排序、用户决策全流程
- 设定三类平台展示策略：严格客观（披露证据与局限性）、平衡、夸大（选择性正向表述，不虚构属性）
- 对比两种用户Agent模式：NoRep（无平台历史记录，仅基于当前信息排序）、LocalRep（维护用户侧本地平台声誉，记录过往解释与用户反馈的匹配度用于校准排序）
- 全链路追踪目标商品（用户真实购买的高评分商品）的流转路径，拆解访问、注意力、问责三个环节的独立影响

### 关键实验结果
- 跨平台查询相比单平台推荐，目标商品进入候选池比例从~20%升至近90%，目标购买率提升4.2-4.8倍
- 接入平台从6个增至24个时，目标商品候选池出现率提升8pp，但短名单入围率、购买率分别下降13.6pp、13pp
- NoRep模式下，夸大解释占据73-78%的Top1位置；引入LocalRep后该比例降至36-41%，目标购买率提升2.3-5.8pp

### 核心结论
用户Agent不是简单的大候选池排序器，其查询、展示、反馈规则共同决定了谁能参与竞争、哪些推荐能获得稀缺注意力，智能体推荐需要将访问、注意力、问责作为联合设计问题。
