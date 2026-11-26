---
title: Reliable User Simulation in Complex Multi-Step Workflows
title_zh: 复杂多步工作流场景下的高可靠LLM用户模拟器实现
authors:
- Pusala Pavan Teja
- Jayasimha Talur
- Saab Mansour
- Marcello Federico
affiliations:
- IIT Palakkad
- Amazon
arxiv_id: '2611.34044'
url: https://arxiv.org/abs/2611.34044
pdf_url: https://arxiv.org/pdf/2611.34044
published: '2026-11-25'
collected: '2026-11-26'
category: Agent
direction: Agent 用户模拟 多步工作流目标对齐
tags:
- User Simulation
- LLM Agent
- Prompt Engineering
- Goal Alignment
- Multi-step Task
one_liner: 提出ReUST提示策略，大幅提升多步工作流下LLM用户模拟器的目标对齐率，降低对助手回复风格的依赖
practical_value: '- 电商客服/导购Agent离线评测场景，可复用ReUST的结构化状态跟踪提示，让模拟用户严格遵循预设测试流程，避免goal drift导致的评测结果失真

  - 多步任务类Agent（比如电商售后退货、差旅预订全流程）开发中，可借鉴每轮输出「推理+状态块」的模式，减少长流程下的参数遗忘、步骤跳转错误

  - 评估用户模拟器性能时，需测试多类助手回复风格，避免仅在友好回复下的性能高估，保证评测结果的鲁棒性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM用户模拟器多用于单任务对话评测，在含顺序任务、回退逻辑、跨任务依赖的多步工作流场景下极易出现目标漂移，导致评测误差被错误归因为对话助手的能力缺陷；且现有评估未考虑助手回复风格对模拟器保真度的干扰，评测结果可信度不足。

### 方法关键点
- 构建基于HTN（层次任务网络）的500个多步工作流评测集，覆盖酒店、交通、景点等预订场景，设计任务、方法、步骤三级结构，包含跨任务参数传递、分支逻辑等复杂约束
- 提出ReUST（Reasoning + User State Tracking）无偏提示策略：每轮对话要求模拟器输出结构化JSON状态块，记录当前任务、已尝试选项及结果、下一步动作，再生成用户utterance
- 核心评估指标为Goal Success Rate（GSR，全流程完全符合预设要求的比例），辅助工具准确率、参数准确率、存活率定位错误类型

### 关键实验
基于500个分层采样的多步工作流，对比无状态提示、目标重复、自由文本摘要、仅状态跟踪四种策略，跨5种不同回复风格的助手测试：
- ReUST在中大型模型（70B~671B参数）上GSR提升12+百分点，最高从84.6%提升至97.4%
- 模拟器GSR在不同回复风格的助手上差异可达30个百分点，ReUST将跨风格GSR的标准差从12.4降至2.0，几乎消除回复风格干扰
- ReUST将目标漂移错误降低85.5%，跨任务依赖错误降低81.2%

### 核心结论
用户模拟器的保真度不是独立属性，会显著受对话助手回复风格影响，基于自维护结构化状态的提示策略可大幅提升长流程多步任务的目标对齐率
