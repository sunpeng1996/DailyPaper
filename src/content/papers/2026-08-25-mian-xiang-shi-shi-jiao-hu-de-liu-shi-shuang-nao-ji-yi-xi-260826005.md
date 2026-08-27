---
title: 'VoiceMem: Streaming Dual-Brain Memory for Real-Time Interaction'
title_zh: 面向实时交互的流式双脑记忆系统VoiceMem
authors:
- Zhifei Xie
- Jiaqi Lang
- Ze An
- Yifan Zhao
- Dongchao Yang
- Kai Li
- Ziyang Ma
- Mingbao Lin
- Chunyan Miao
- Shuicheng Yan
affiliations:
- Nanyang Technological University
- National University of Singapore
- Tsinghua University
- The Chinese University of Hong Kong
- Open Interaction Lab
arxiv_id: '2608.26005'
url: https://arxiv.org/abs/2608.26005
pdf_url: https://arxiv.org/pdf/2608.26005
published: '2026-08-25'
collected: '2026-08-27'
category: Agent
direction: Agent 实时交互记忆优化
tags:
- Agent Memory
- Streaming Retrieval
- Low-Latency
- Emotion Modeling
- Conversational Agent
one_liner: 提出并行事实+情感双脑架构的低延迟流式记忆系统，适配实时语音交互场景
practical_value: '- 记忆架构可复用：将事实记忆与用户偏好/情感记忆分库存储检索，能同时提升电商对话Agent的信息准确性和情感适配性，降低top-K检索的候选池噪声

  - 低延迟优化技巧可迁移：采用流式四阶段检索（监听/语音尾/预判/搜索），将检索逻辑嵌入VAD等待窗口，可直接用于直播实时助理、客服机器人等对延迟敏感的场景

  - 上层路由与底层引擎解耦的架构设计，可在不改动上层业务逻辑的前提下升级向量数据库等底层存储，适配业务迭代需求

  - top-K压缩方案：通过schema-entity两层索引压缩检索候选池，在top-5下即可达到普通系统top-200的效果，大幅节省LLM上下文token成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有对话Agent记忆系统普遍存在三个核心缺陷：仅关注事实检索，忽略用户情感、长期人格建模；检索延迟高达2-3s，超出实时语音交互500ms的延迟阈值；动辄返回top-100检索结果浪费LLM上下文，且架构与底层存储强绑定，迭代灵活性差。
### 方法关键点
- 双脑并行架构：左脑负责事实记忆，采用schema-entity两层索引+查询驱动的聚类涌现机制，大幅压缩检索候选池；右脑负责情感与人格建模，区分用户固有属性的独立节点、与实体绑定的跨实体节点，通过长短周期情感归因更新用户画像
- 流式四阶段检索：将检索流程拆分为监听、语音尾、预判、搜索4步，完全嵌入VAD的500ms等待窗口，无额外交互延迟
- 解耦部署架构：上层双脑路由与底层记忆引擎完全解耦，支持灵活切换Mem0等不同后端存储；配套提出黑盒在线蒸馏训练流水线，构建了400K规模的记忆依赖对话数据集与多维度评测基准
### 关键实验
对比Mem0、A-MEM、EverMemOS等10个主流记忆系统，在信息记忆基准平均得分76.39，较Mem0提升24.12分；在人格记忆基准平均得分74.16，较之前SOTA提升1.89分；CHATMEM-BENCH平均得分68.73，在声学相关任务上领先基线20+分；检索延迟仅134ms，top-5下用430个token即可达到基线top-100的精度，token成本降低4.4倍。

双脑分治+流式预处理不仅能在严格的低延迟约束下实现记忆能力的跃升，还能通过分层索引让小检索预算达到大候选池的效果，是实时交互Agent记忆系统的可行落地方向。
