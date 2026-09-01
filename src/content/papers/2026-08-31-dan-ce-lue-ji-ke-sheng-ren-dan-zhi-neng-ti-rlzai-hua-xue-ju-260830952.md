---
title: 'One Policy Is Enough: Single-Agent Reinforcement Learning Outperforms Tree
  Search for Chemistry Tool Learning'
title_zh: 单策略即可胜任：单智能体RL在化学工具学习中超越树搜索
authors:
- Armin Dariani
- Sifan Wu
- Bang Liu
- Entao Yang
affiliations:
- Université de Montréal
- Mila - Quebec Artificial Intelligence Institute
- Air Liquide
arxiv_id: '2608.30952'
url: https://arxiv.org/abs/2608.30952
pdf_url: https://arxiv.org/pdf/2608.30952
published: '2026-08-31'
collected: '2026-09-01'
category: Agent
direction: 单智能体工具调用 · 强化学习优化
tags:
- Reinforcement Learning
- Tool Learning
- GRPO
- LLM Agent
- Single Agent
one_liner: 用单智能体RL训练的单工具调用策略，无需树搜索与奖励模型，性能超越化学工具学习SOTA
practical_value: '- 工具调用类 Agent 可放弃复杂MCTS多模型架构，改用单LLM端到端SFT+GRPO训练，推理仅需1次模型调用，大幅降低部署成本与延迟

  - 工具调用奖励设计优先选用程序式计算的带F1惩罚的列表级奖励，无需训练PRM/ORM等额外奖励模型，既避免工具滥发问题，又降低训练链路复杂度

  - 训练时实时调用真实工具执行请求，仅对模型生成的token计算损失，可让模型自动学会从工具错误返回中自我修复，提升长链路调用鲁棒性

  - 工具调用模型训练优先做SFT暖身（基于标注的黄金调用链）再做RL微调，SFT对效果的贡献高于直接RL，RL主要负责提升工具调用精度'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
化学领域问题需要调用大量专业工具完成计算、检索，现有SOTA方案CheMatAgent采用HE-MCTS架构，需同时训练策略、执行、PRM、ORM四个模型，推理时还需执行树搜索，调用成本随树大小线性增长，架构笨重部署门槛高。

### 方法关键点
- 单策略LLM端到端完成推理、工具选择、参数填充全流程，无需拆分不同功能模块，每轮直接读取真实工具返回结果后继续生成
- 训练链路：先基于标注的黄金调用链做SFT暖身，再用GRPO做RL微调，全程不需要训练额外奖励模型，奖励直接通过程序对比生成调用链与黄金链计算得到
- 奖励设计采用带F1惩罚的列表级指标，同时考核工具选择、参数匹配准确率，避免工具滥发、调用不终止的Reward Hacking问题
- 训练时真实执行工具调用，工具返回的token不参与损失计算，模型可自动学习从错误返回中自我修复

### 关键结果
在ChemToolBench多工具化学任务上对比SOTA的HE-MCTS：Qwen-2.5-7B上Tool F1提升5.5%，Return F1提升9.6%，Pass Rate领先；Llama-3.1-8B上Tool F1提升3.7%，Return F1提升3.9%；推理仅需1次模型调用，远低于树搜索方案的调用成本。

**最值得记住的一句话**：只要存在可验证的程序式奖励信号，无需复杂的树搜索与额外奖励模型，单智能体RL训练的端到端策略即可超过复杂多模型搜索方案的性能
