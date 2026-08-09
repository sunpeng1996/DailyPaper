---
title: 'From Passive Mirrors to Active Agents: Holonic Digital Twins for Physical
  AI over Networks'
title_zh: 从被动镜像到主动Agent：面向网络物理AI的合弄数字孪生框架
authors:
- Christo Kurisummoottil Thomas
- Omar Hashash
- Walid Saad
arxiv_id: '2608.06227'
url: https://arxiv.org/abs/2608.06227
pdf_url: https://arxiv.org/pdf/2608.06227
published: '2026-08-06'
collected: '2026-08-09'
category: Agent
direction: 多Agent协同 · 数字孪生推理架构
tags:
- Digital Twin
- Multi-Agent
- Active Inference
- Causal Reasoning
- Edge AI
one_liner: 提出合弄数字孪生网络HDT-Nets框架，支持异构物理Agent跨网络实时协同推理
practical_value: '- 多Agent跨节点协同可借鉴HDT分层推理架构：本地侧做低延迟自主决策，边缘侧做全局协同，平衡算力开销与一致性，适配推荐/广告端边云协同场景

  - 范畴论支撑的跨异构Agent语义一致性保障方法，可复用在多模态推荐、RAG跨模块信息对齐场景，解决不同模块表示不兼容问题

  - 基于认知价值筛选待传输信息的思路，可优化推荐系统多模块通信开销，仅传递对下游高价值的用户/物品特征，降低带宽占用'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有AI嵌入机器人、自动驾驶等物理实体系统时，无法在不确定性场景下维护可靠世界模型支撑长周期规划，泛化性差；现有无线网络仅优化吞吐、延迟等QoS指标，无法支撑多Agent需共享时空上下文的实时协同需求。

### 方法关键点
1. 提出HDT-Nets框架，每个合弄数字孪生为跨物理Agent与网络边缘的分层结构，本地自主推理+相邻节点协同形成全局智能单元；
2. 基于因果马尔可夫毯确定Agent协同范围，支持多域干预的反事实推理；
3. 基于主动推理统一感知、动作、学习流程，根据接收方认知价值筛选待传输信息；
4. 用范畴论保障异构Agent间信息传递的语义一致性，用整合信息论量化集体智能收益。

### 关键结果
为纯理论架构设计，暂未公布面向具体落地场景的量化性能数据，核心价值在多Agent协同的系统设计范式创新。
