---
title: 'SciMARS: Multi-Agent Recursive Self-Improvement for Closed-Loop Scientific
  Discovery'
title_zh: SciMARS：面向闭环科学发现的多智能体递归自改进框架
authors:
- Weimin Wu
- Han Liu
affiliations:
- Northwestern University
arxiv_id: '2611.12552'
url: https://arxiv.org/abs/2611.12552
pdf_url: https://arxiv.org/pdf/2611.12552
published: '2026-11-09'
collected: '2026-11-10'
category: MultiAgent
direction: 多智能体协作 · 递归自改进与共享记忆
tags:
- Multi-Agent
- Recursive Self-Improvement
- Shared Memory
- Closed-Loop System
- Agent Workflow
one_liner: 提出带共享证据图与分组件编辑器的多智能体自适应框架，提升多类闭环任务完成率
practical_value: '- 多智能体分工场景可复用「共享证据图+独立记忆策略编辑器」设计，解决不同角色信息孤立、重复劳动问题，比如电商大促campaign策划多Agent团队（选品、文案、投放、核验）可通过该结构减少跨角色信息差

  - 可借鉴分组件独立编辑+探针验证的优化思路，无需整体改动Agent工作流，分别修改角色职责、协作规则、记忆策略，降低业务迭代风险，比如推荐系统多Agent召回、排序、重排链路优化可逐组件调整并做小流量验证

  - 递归自改进闭环设计可复用在电商冷启动场景，比如新品冷启动的选品Agent团队可基于每次投放反馈自动调整角色规则和信息流转逻辑，无需人工重写prompt'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有多智能体系统在闭环任务中存在两个核心痛点：一是无共享记忆导致不同Agent观测信息孤立，重复执行已验证的错误操作；二是固定的角色流程、交接规则和记忆策略，即便留存了错误证据也会重复犯错，无法自适应迭代，大幅降低复杂闭环任务的完成效率。

### 方法关键点
- 设计共享证据图，记录观测、结论、计划、待解决问题并附带来源，不同Agent可跨流程检索订阅信息，打通信息孤岛
- 采用分组件独立编辑器设计：基础版SciMARS设置角色编辑器、协作规则编辑器，分别修改单角色执行逻辑、单条协作交接契约，互不干扰；SciMARS + Memory新增独立记忆策略编辑器，调整各角色的记录规则、检索过滤条件、订阅信息类型，不改动证据图本身
- 引入探针验证+证据引导的组合选择机制：每个编辑器输出的候选配置先在隔离环境做探针测试，基于测试证据组合最优配置，避免盲目迭代导致的效果下降

### 关键实验
在3个基准测试集对比5个基线方法：Autonomous Science Bench（GPT-6-Astra 18次尝试）中，SciMARS + Memory完成率12/18，比基线多智能体的8/18提升50%；ScienceAgentBench 38个任务中完成14个，比基线的11个提升27%；AppWorld 20个交互任务中完成11个，比基线的5个提升120%。

### 核心结论
多智能体系统的自适应优化不需要整体重构工作流，将记忆留存、记忆使用、角色职责、协作规则解耦后逐组件迭代，可在低风险下实现大幅效果提升。
