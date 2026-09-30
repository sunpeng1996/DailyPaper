---
title: 'ANTMAN: Adaptive Need Tracking for Multi-Agent Navigation in Large Information
  Spaces'
title_zh: ANTMAN：面向大信息空间多智能体导航的自适应需求追踪框架
authors:
- Jerry Wang
- Haibo Jin
- Xiaopeng Yuan
- Peng Kuang
- Haohan Wang
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2609.33326'
url: https://arxiv.org/abs/2609.33326
pdf_url: https://arxiv.org/pdf/2609.33326
published: '2026-09-26'
collected: '2026-09-30'
category: Agent
direction: 多智能体信息检索 · 动态协调
tags:
- MultiAgent
- NeedTracking
- InformationRetrieval
- LongContext
- Coordination
one_liner: 基于动态需求图的多智能体协调框架，解耦协调开销与信息空间规模
practical_value: '- 电商/搜索大规模库检索场景可复用需求驱动调度逻辑：替代按信息空间分块固定激活Worker的方案，仅激活匹配当前查询需求的Worker，信息空间扩16倍时协调开销仅涨1.23倍，大幅降低推理成本

  - Need Graph显式需求追踪结构可迁移至多轮搜索、导购Agent场景：动态记录未满足需求、已召回证据、尝试历史，支持需求修正、路由重试，提升长序列交互的需求满足率

  - WorkerCard轻量元数据路由方法可适配异构召回源调度：给商品、内容、广告等不同召回池生成对应范围摘要元数据，路由时先匹配元数据再决定调用对应召回源，避免全量召回浪费算力'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多Agent信息检索系统多采用静态信息空间分块分配Worker的架构，协调开销随信息空间规模线性增长，和查询实际需要的算力完全不匹配；同时长上下文下LLM存在lost in the middle问题，证据位置敏感度高，无法适配大规模异构信息空间的检索需求。

### 方法关键点
- 静态底物映射层：信息空间拆分为固定领地，每个领地对应轻量WorkerCard存储内容范围元数据，所有Worker共用统一检索接口
- 可更新Need Graph：作为运行时控制核心，追踪未解决需求、已积累证据、尝试历史、进度，每轮Worker返回结果后动态更新，支持需求解决、拆分、重构
- 需求驱动协调与恢复机制：根据Need Graph的未解决需求匹配WorkerCard完成路由，任务卡住时触发需求重构、换源路由、降级路径三种恢复策略，所有需求解决后汇总证据输出结果

### 关键实验
在多文档QA、长上下文缩放、结构化导航三类场景测试，对比LongAgent、CoA、S2G-RAG等基线：信息空间从32K扩到512K（16倍）时，活跃协调量仅涨1.23倍，基线涨超15倍，推理成本仅为基线的38%，同时F1保持0.84优于基线的0.75；结构化导航场景中，比最强基线分别高15.3%（RepoProbe）、18.4%（SWE-QA-Pro）、27.9%（GAIA）；用8B小模型做Worker的版本保留了全量版本89.2%~98.3%的性能，证据位置偏差仅0.015，远低于全上下文推理的0.181，大幅缓解lost in the middle问题。

### 核心结论
多智能体协调的核心单元应该是动态变化的未满足用户需求，而非静态的信息空间分区，算力分配应该和查询需求挂钩，而非和信息库规模绑定。
