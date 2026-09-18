---
title: An Empirical Study of Harness Design for Coding Agents
title_zh: 代码Agent执行层Harness组件设计的大规模实证研究
authors:
- Run-Ze Fan
- Zihao Zhang
- Simin Ma
- Yebowen Hu
- Shouju Wang
- Kaiqiang Song
- Fei Liu
- Hamed Zamani
- Xiaoyang Wang
affiliations:
- UMass Amherst
- Emory University
- UNC Charlotte
- Zoom Video Communications
arxiv_id: '2609.20804'
url: https://arxiv.org/abs/2609.20804
pdf_url: https://arxiv.org/pdf/2609.20804
published: '2026-09-16'
collected: '2026-09-18'
category: Agent
direction: Agent 执行层架构优化
tags:
- Coding Agent
- Harness Design
- Context Management
- Planning
- Action Space
one_liner: 模块化拆解代码Agent Harness三大组件，给出不同场景下的最优设计选型规则
practical_value: '- 上下文管理可直接复用T4策略：先规则化过滤冗余工具返回结果，再按需做LLM总结，无需实现可召回外存模块（实测使用率<1%，无收益），适合电商导购Agent、推荐系统用户会话/行为序列压缩场景，可同时降本提效

  - 规划模块按需选型：7B/14B等小模型部署垂类Agent时必须开启规划，可显著提升任务完成率；70B以上大模型部署时可关闭规划，能降低30%左右推理成本，准确率损失不足2个百分点

  - 工具链分层设计：面向弱能力模型提供封装好的垂类专用工具（如电商查库存、领券、查物流工具），降低操作门槛；面向强能力模型仅提供底层通用接口，可减少交互次数，最多降本50%以上

  - 上下文窗口≥128k时无需开发复杂上下文管理逻辑，边际成功率收益不足3个百分点，可优先投入其他模块优化'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有代码Agent的Harness（执行层框架）通常作为整包系统被评估，无法明确规划、动作空间、上下文管理等单个组件的效果差异，也不清楚其收益随模型能力、上下文窗口预算、任务类型的变化规律，导致大量无效的复杂设计被盲目复用，既提升成本又无法优化效果。

### 方法关键点
- 构建模块化可消融的Harness框架，固定ReAct执行循环，单独控制三大核心组件的开关与策略：
  1. 规划模块：支持显式持久化任务计划/无规划两种配置
  2. 动作空间：支持预定义专用工具集/仅bash通用接口两种配置
  3. 上下文管理：实现5种策略（T0无管理、T1仅规则删冗余、T2删+可召回外存、T3仅LLM总结、T4先规则删冗余再LLM总结）
- 覆盖4个不同能力梯队的模型、4种上下文窗口预算（32k/64k/96k/128k），共176组对照实验，控制变量验证各组件的边际收益。

### 关键实验
- 测试数据集：SWE-Bench Verified（500个真实GitHub issue修复任务）、Terminal-Bench 2.1（89个端到端命令行任务）
- 核心结果：32k小窗口下上下文管理平均提成功率35.7pct，128k大窗口下仅提2.7pct；T4策略成本比纯LLM总结低30%，准确率无显著差异，可召回外存机制使用率不足1%，无任何准确率收益；30B小模型加规划提成功率11.6pct，550B以上大模型关闭规划降本30%+，准确率仅降<2pct；弱模型用预定义工具提成功率15pct，强模型用仅bash接口降本53%，提成功率3.6pct。

### 核心结论
Harness设计没有通用最优解，所有组件都需要匹配目标模型能力、资源预算、任务类型选型，不要盲目叠加复杂机制。
