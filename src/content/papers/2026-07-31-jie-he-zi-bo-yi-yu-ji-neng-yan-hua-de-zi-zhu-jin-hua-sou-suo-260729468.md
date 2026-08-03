---
title: 'Self-Play Meets Skill Evolution: Self-Evolving Search Agents that Pose, Solve,
  and Remember'
title_zh: 结合自博弈与技能演化的自主进化搜索智能体框架
authors:
- Zenghuang Fu
- Zhaoyang Li
- Qiuyuan Ai
- Haoyu Wu
- Minghui Wu
- Chenxu Zhao
- Ante Wang
- Guannan He
- Changwei Wang
affiliations:
- Peking University
- University of Chinese Academy of Sciences
- Tsinghua University
- Mininglamp Technology
- Qilu University of Technology
arxiv_id: '2607.29468'
url: https://arxiv.org/abs/2607.29468
pdf_url: https://arxiv.org/pdf/2607.29468
published: '2026-07-31'
collected: '2026-08-03'
category: Agent
direction: Agent 自博弈与技能演化优化
tags:
- Self-Play
- Skill Evolution
- Search Agent
- GRPO
- Procedural Memory
one_liner: 耦合自博弈与在线技能演化，实现无监督进化的搜索Agent，精度优于现有基线
practical_value: '- 搜索/推荐Agent自训练可复用非对称自博弈+钟型难度奖励设计，问题生成方看不到解题方技能库避免泄露，引导生成刚好在能力边界的训练样本，适配电商搜索query理解、多轮导购Agent的无标注训练场景

  - 可复用bad case自动蒸馏技能的流程，将搜索/推荐场景的错误案例抽象为可检索的技能卡片（如query改写规则、歧义规避策略、多跳查询模板），既可以在训练时注入让模型内化能力，也可作为推理时RAG外挂库，适配搜索冷启动、大模型导购优化

  - 双路径部署逻辑可复用：训练时加入技能增强，部署时可选择不带技能库的轻量化方案（大部分收益已内化到参数），或带技能库的增强方案，平衡推理性能与效果，适合高QPS的电商搜索/推荐场景'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有自博弈Agent的训练经验是瞬态的，失败案例仅用于梯度更新，不会留存为可复用的结构化经验；而技能增强RL的技能库通常基于固定数据集构建，无法适配自博弈动态演化的任务分布，两者无法形成正向闭环。

### 方法关键点
- 非对称自博弈架构：分离出题的proposer和解题的solver，仅solver可访问技能库避免技能泄露，两者均采用GRPO做无critic的策略优化
- 边界塑造奖励：为proposer设计钟型奖励，惩罚全对（太简单）和全错（太无解）的问题，引导生成刚好落在solver能力边界的训练样本
- 在线失败蒸馏：将solver的有效失败案例自动抽象为包含触发条件、规避规则、查询模板的技能卡片，去重后写入可动态维护的技能库，低效用技能自动淘汰
- 双路径能力复用：训练时技能库注入会改变on-policy训练轨迹，让能力内化到solver参数，支持无技能库的轻量化部署；也可在推理时保留技能库做RAG外挂增强

### 关键实验结果
在7个公开开放域/多跳搜索基准（共3125道题）上测试，对比SSP（无技能库自博弈）、SkillRL（固定数据集技能增强）基线：
- 跨不同模型规模、模型族平均精度比SSP高1.2~3.2个百分点，比SkillRL高0.9个百分点
- 关闭技能库的SESA-Off版本仍比SSP高1.8~2.2个百分点，说明大部分收益已内化到模型参数，外挂技能库可额外提升0.5~1.0个百分点
- 去掉失败蒸馏模块精度下降2.7个点，是最核心的组件

### 核心结论
技能增强不是推理时的临时补丁，而是可以改变自训练分布、让能力内化到模型参数的训练机制。
