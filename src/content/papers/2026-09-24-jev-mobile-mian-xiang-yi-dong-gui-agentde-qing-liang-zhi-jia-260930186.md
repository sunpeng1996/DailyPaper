---
title: 'Jev-Mobile: Jev as an Executor for Mobile GUI Agents'
title_zh: Jev-Mobile：面向移动GUI Agent的轻量执行框架
authors:
- Linghua Zhang
affiliations:
- Rice University
arxiv_id: '2609.30186'
url: https://arxiv.org/abs/2609.30186
pdf_url: https://arxiv.org/pdf/2609.30186
published: '2026-09-24'
collected: '2026-09-25'
category: Agent
direction: 移动GUI Agent 规划执行分层优化
tags:
- GUI Agent
- VLM
- Execution Optimization
- Mobile Agent
- Cost Efficiency
one_liner: 解耦VLM低频规划与轻量Jev高频执行，实现移动GUI Agent降本提效同时保持竞争性能
practical_value: '- 电商APP自动化操作Agent（如自动上新、商品信息爬取、客服自动操作场景）可复用「大模型低频做规划+轻量模型高频执行动作」的分层架构，大幅降低大模型调用成本和延迟

  - 端侧交互Agent可优先基于系统原生accessibility tree/DOM树生成可执行动作候选集，无需每次调用VLM做视觉grounding，减少多模态推理开销

  - 交互类Agent的动作历史可仅保留实际执行成功的结构化记录，无需存储全量截图或模型生成总结，既能降低上下文长度消耗，又能保证规划信息足够'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有移动GUI Agent多依赖VLM每步同步完成规划和动作grounding，推理延迟高、API成本昂贵，难以落地到高频交互的实际场景，亟需兼顾任务性能和落地效率的架构方案。

### 方法关键点
- 分层控制流：VLM仅低频读取任务、当前屏幕/accessibility树、已执行动作历史，输出局部目标和可选输入文本，不生成执行后总结，将动作执行权委托给Jev轻量决策模型
- 动态候选集生成：每次执行动作后重新从最新accessibility树提取可见、可交互节点，生成带唯一ID的可执行动作候选（点击、长按、输入、返回等），避免界面变化导致的动作绑定错误
- 明确控制权切换机制：Jev在局部目标完成、遇到树中不存在的目标、无法继续执行时返回DONE/BLOCKED，将控制权交还给VLM重新规划

### 关键实验
在全量AndroidWorld任务集上测试，对比Step-wise VLM（每步调用通用VLM）、SeeAct-V（VLM+UI-TARS视觉grounding）两个基线：任务成功率79%，接近SeeAct-V的78%，略低于Step-wise VLM的84%；成功轨迹的端到端平均执行时间132.67s，较Step-wise VLM降32.7%，较SeeAct-V降18.4%；成功轨迹的平均模型API成本0.0727美元，较Step-wise VLM降73.4%，较SeeAct-V降62.3%。

### 核心结论
交互类Agent的规划与执行解耦是兼顾性能和落地成本的核心路径，不需要每个动作都调用强大的大模型，轻量决策模型在结构化动作空间下的执行效果足以满足大部分场景需求。
