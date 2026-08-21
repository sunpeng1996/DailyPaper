---
title: Rule-Compliant Visual Spatial Planning for Multimodal Large Language Models
title_zh: 面向多模态大模型的规则合规视觉空间规划方法
authors:
- Yu Chen
- Ting Lei
- Yaoyi Li
- Jia Cai
- Zhecen Wu
- Yang Liu
affiliations:
- 北京大学王选计算机研究所
- Yinwang Intelligent Technology Co., Ltd.
arxiv_id: '2608.20237'
url: https://arxiv.org/abs/2608.20237
pdf_url: https://arxiv.org/pdf/2608.20237
published: '2026-08-20'
collected: '2026-08-21'
category: Agent
direction: 多模态Agent · 规则约束空间规划
tags:
- MLLM
- Spatial Planning
- Rule Compliance
- Embodied Agent
- Benchmark
one_liner: 提出RuleMaze基准与拆解式多模态规划框架，提升MLLM规则约束下空间规划能力
practical_value: '- 做规则约束的导购/履约Agent时，可复用Language-Logic-Function Hybridization流水线，将自然语言业务规则（如优惠券使用、履约路径限制）自动转换为逻辑表达式与可执行验证器，降低人工规则开发成本

  - 多模态Agent决策模块可参考DMP的模块化设计，将感知、动作执行、规则校验拆分为独立可替换工具，仅训练控制器的工具调度逻辑，新规则上线无需重训核心模型，大幅降低迭代成本

  - 构建多步决策任务的评测集时，可借鉴RuleMaze的规则-场景匹配策略，自动生成带唯一合规解、含干扰项的测试用例，提升评测的可控性与覆盖度'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

## 动机
现有多模态大模型（MLLM）的空间规划能力大多面向无约束场景，无法适配需动态遵守自然语言规则的真实业务场景（如履约调度、线下导购导航、自动驾驶等）；同时现有基准缺乏对规则复杂度的可控构造，端到端训练的模型泛化性差，规则变更需全量重训，效率极低。

## 方法关键点
1. 提出RuleMaze可控基准，通过**Language-Logic-Function Hybridization**流水线，自动生成自然语言规则、转换为结构化逻辑表示、生成可执行规则验证器，无需人工规则开发；
2. 采用规则-迷宫启发式匹配策略，确保每个测试用例存在唯一合规解，规则按逻辑连接符数量分为易/中/难三档，覆盖静态约束、动态状态依赖两类场景；
3. 提出**Disentangled Multimodal Planning (DMP)** 框架，将规划任务拆解为感知、执行、校验三类可调用工具，仅训练控制器的工具调度逻辑，规则校验工具可独立替换，新规则接入无需重训核心模型。

## 关键实验结果
在RegularMaze、QuestMaze两个数据集上，基于Qwen2.5-VL 3B微调的DMP相比端到端SFT基线，unseen规则下的Exact Match分别从70.3%提升至90.0%、从56.3%提升至88.0%；硬规则下的优势更显著，QuestMaze难例上EM从40.0%提升至84.0%，即使是GPT-5搭配工具提示也仅达到81.4% EM，低于DMP的90.0%。

## 核心结论
将规则校验、感知、执行拆解为独立可替换工具，仅训练控制器的调度逻辑，能同时提升多模态Agent的规则合规性与新规则泛化能力，大幅降低规则迭代成本。
