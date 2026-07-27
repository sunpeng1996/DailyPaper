---
title: 'TRACE-ROUTER: Task-Consistent and Adaptive Online Routing for Agentic AI'
title_zh: TRACE-Router：面向Agent系统的任务一致性自适应在线路由框架
authors:
- Ritik Raj
- Souvik Kundu
- Sarbartha Banerjee
- Dheemanth Joshi
- Ishita Vohra
- Tushar Krishna
affiliations:
- Georgia Institute of Technology
- Intel
- Texas A&M University
arxiv_id: '2607.22465'
url: https://arxiv.org/abs/2607.22465
pdf_url: https://arxiv.org/pdf/2607.22465
published: '2026-07-24'
collected: '2026-07-27'
category: Agent
direction: Agent系统 · LLM在线路由优化
tags:
- LLM Routing
- Contextual Bandit
- Agent Serving
- Online Learning
- Latency Optimization
one_liner: 提出任务级上下文老虎机路由框架，对齐反馈单元，优化Agent场景LLM推理精度延迟 tradeoff
practical_value: '- 搭建电商Agent导购/智能客服系统时，可复用任务级sticky路由逻辑：同一任务的所有LLM调用绑定同一个模型，避免跨模型状态失效和信用分配问题，同时降低路由决策overhead

  - 多LLM异构部署场景可直接套用冷启动上下文UCB路由方案，无需离线标注训练数据，仅靠任务级终端反馈（用户下单/问题解决率、响应延迟）就能自适应学习最优路由策略

  - 任务上下文分类不需要复杂模型，用极简正则/关键词/长度规则即可获得明显收益，适合工程快速落地，平衡精度和额外开销

  - 多模型选型可参考其reward设计思路，将精度、延迟、成本加权整合为单指标优化，适配不同业务优先级（大促期优先降延迟，日常优先提解决率）'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM路由器均为单请求粒度独立决策，和Agent工作流长周期、任务级延迟反馈的特性完全不匹配，无法将最终任务成败归因到单次路由决策，还会导致跨模型状态失效，严重浪费算力、降低任务成功率。

### 方法关键点
- 路由粒度对齐反馈单元：任务接入时仅做一次路由决策，同一任务的所有LLM调用绑定选中的后端模型，避免中间切换模型的状态损失和信用分配混乱
- 上下文感知在线学习：用极简规则（关键词、长度）将任务粗分类为易/中/难3个上下文，每个上下文对应独立的UCB老虎机，无需离线训练，在线探索不同模型的精度延迟表现
- 延迟反馈更新机制：任务结束后，将最终精度和端到端延迟加权为单值reward，仅更新对应上下文老虎机的参数，支持高并发任务流的异步更新
- 轻量冷启动设计：每个上下文的每个模型先强制拉取k次做初始化，无需先验知识就能快速收敛

### 关键结果
在τ2-Bench、LiveCodeBench、Terminal-Bench共4个Agent基准测试集上对比单模型、语义路由、复杂度路由等基线：
- τ2-Bench上比同延迟的随机模型混合精度高7-8个百分点
- Terminal-Bench上比最强单模型多解决7.1%的任务，同时延迟降低36%
- 所有场景下的路由结果都占据精度-延迟帕累托前沿，没有被任何基线支配

**最值得记住的一句话**：Agent场景下路由决策的粒度必须和反馈的粒度对齐，基于任务级反馈的在线自适应路由，收益远高于单请求的静态路由策略。
