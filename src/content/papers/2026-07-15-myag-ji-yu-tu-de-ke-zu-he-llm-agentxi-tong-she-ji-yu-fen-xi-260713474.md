---
title: 'MyAG: A Graph-Based Framework for Designing and Analyzing Composable LLM Agent
  Systems'
title_zh: MyAG：基于图的可组合LLM Agent系统设计与分析框架
authors:
- Zhisong Zhang
affiliations:
- City University of Hong Kong
arxiv_id: '2607.13474'
url: https://arxiv.org/abs/2607.13474
pdf_url: https://arxiv.org/pdf/2607.13474
published: '2026-07-15'
collected: '2026-07-16'
category: Agent
direction: Agent 系统架构与效率分析
tags:
- LLM-Agent
- Graph-Framework
- Composable-Agent
- Efficiency-Analysis
- Open-Source
one_liner: 提出三层图抽象的轻量级开源Agent框架，支持组件复用、层级组合与性能-效率权衡分析
practical_value: '- 构建业务Agent系统时可参考三层图抽象设计，将组件定义、执行流程、运行时搜索解耦，大幅提升模块复用效率，比如电商导购Agent可快速切换不同决策流/搜索策略而无需重写组件

  - 落地多Agent系统时可复用系统节点的层级组合设计，将垂直场景Agent（如选品、售后、客服）封装为子系统，支持无状态/有状态两种调用模式适配不同业务需求

  - Agent性能优化时可复用其成本拆分方法，分别统计LLM推理成本（输入/输出token加权）、环境交互成本（各动作延迟加权），快速定位性能瓶颈，比如电商搜索Agent可优化高延迟的商品查询动作占比'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM Agent开发框架普遍存在组件、工作流、运行时搜索边界不清晰的问题，要么功能侧重单一、无法灵活切换不同策略做对比分析，要么代码臃肿，而轻量框架又普遍缺乏复杂流程控制与效率分析支持，难以快速迭代优化Agent系统的性能与效率权衡。

### 方法关键点
- 设计三层图抽象解耦Agent系统：组件图定义Agent、环境、工具等模块及交互关系；工作流图定义执行逻辑、控制流与终止条件；搜索图记录运行时状态与轨迹，支持贪心、最佳优先、回滚等不同搜索策略的快速切换
- 支持层级组合：通过系统节点将完整Agent系统封装为可复用组件，支持无状态（每次调用重置，适配独立子任务）、有状态（跨调用保留内存，适配多Agent协作）两种调用模式，实现模块化嵌套
- 内置效率分析工具：自动统计两类核心成本，LLM推理成本为输入/输出token的加权和（权重可按API定价/延迟自定义），环境交互成本为各动作的延迟加权和，支持性能-效率的量化对比

### 关键实验
在GAIA-text问答、Mind2Web-Live网页导航两个基准上测试，对比Greedy、Best-first、Rollback、Best-of-N四种策略：Greedy策略效率最高，Rollback在预算充足时准确率最高（GAIA上比Greedy高约3个百分点），Best-of-N、Best-first策略虽能提升准确率但整体延迟最高可达Greedy的2倍以上；同时验证了MoE模型在相同成本下相比同级别稠密模型可获得更好的性能-效率tradeoff。

### 核心结论
Agent系统选型没有通用最优解，策略、底层模型的选择需要结合推理预算、内存、延迟要求与目标性能综合判断，三层解耦的架构是快速迭代与对比优化的基础。
