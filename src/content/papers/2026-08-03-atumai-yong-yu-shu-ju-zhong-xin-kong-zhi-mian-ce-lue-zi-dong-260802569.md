---
title: 'AtumAI: A Principled Framework for Agentic Generation of Datacenter Control-Plane
  Policies'
title_zh: AtumAI：用于数据中心控制面策略自动生成的Agent框架
authors:
- Qiushi Lin
- Chaojie Zhang
- Íñigo Goiri
- Aditya Akella
- Ricardo Bianchini
- Jovan Stojkovic
affiliations:
- The University of Texas at Austin
- Microsoft Azure
arxiv_id: '2608.02569'
url: https://arxiv.org/abs/2608.02569
pdf_url: https://arxiv.org/pdf/2608.02569
published: '2026-08-03'
collected: '2026-08-05'
category: Agent
direction: Agent 控制面策略自动化生成
tags:
- Agentic AI
- Policy Generation
- Datacenter Optimization
- Evolutionary Search
- Surrogate Model
one_liner: 基于Agent实现自然语言需求到优于专家设计的数据中心控制面策略的自动化生成
practical_value: '- 自然语言需求转标准化可搜索IR的思路可直接迁移到推荐/广告策略迭代场景：自动把运营侧模糊需求（如"不降点击率前提下提升客单价"）拆解为明确的目标、约束、决策变量、评估逻辑，减少人工对齐和编码成本

  - 扩散模型扩结构+进化算法调参+Surrogate预筛的搜索框架，可用于优化推荐排序/广告出价策略：既突破LLM生成策略的局部最优局限，又能提前过滤劣质候选，降低高成本线上AB实验的频次

  - 可复用优化Pass库的设计，适合沉淀业务场景的历史策略经验，新业务/新场景策略生成可直接复用已有成熟逻辑，无需从零搭建pipeline，大幅提升迭代效率'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
数据中心控制面策略直接决定硬件利用率、成本与可靠性，但人工设计依赖深度领域经验，迭代周期长达数月，赶不上硬件、workload快速迭代的节奏。现有Agent方案存在三大缺陷：无形式化问题定义导致硬约束无法保障、跨任务知识无法复用、仅靠LLM生成候选易陷入局部最优，探索范围极窄。
### 方法关键点
- 核心由两个组件构成：数据中心任务编译器、进化设计发现环
- 任务编译器将自然语言需求编译为标准化、机器可校验的中间表示（IR），自动对齐目标、约束、决策变量、评估方法，结合可复用的优化Pass库实现跨任务知识迁移，新任务接入仅需写需求描述
- 进化设计发现环用扩散模型做策略结构探索、进化算法做参数调优，大幅扩展搜索空间，引入Surrogate模型预筛候选，提前过滤低质量方案，降低高成本仿真/实测的开销
- 全程闭环反馈，每轮搜索结果回传优化Pass库置信度与下一轮搜索方向，持续沉淀知识
### 关键实验
基于Azure、阿里等生产环境真实trace测试，对比专家手写的基线策略，三大场景均实现显著提升：1. 工作负载放置：放置成功率提升17%，调度吞吐量提升8%；2. 资源伸缩：成本效率提升24%，SLO违反率维持在1.3%；3. 功率管理：功耗降低21%，吞吐量提升17%，所有服务精度满足要求。
### 核心洞察
Agent落地复杂业务优化场景的核心不依赖大模型能力上限，而是把形式化问题定义、跨任务知识复用、结构化搜索三者结合，才能稳定产出优于人工设计的方案
