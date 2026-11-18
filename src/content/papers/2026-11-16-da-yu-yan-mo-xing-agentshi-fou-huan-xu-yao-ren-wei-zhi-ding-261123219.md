---
title: Do LLM Agents Still Need to Be Told How to Self-Improve?
title_zh: 大语言模型Agent是否还需要人为指定自我改进流程？
authors:
- Shobhita Sundaram
- Cansu Sancaktar
- Phillip Isola
affiliations:
- MIT CSAIL
- University of Tübingen
arxiv_id: '2611.23219'
url: https://arxiv.org/abs/2611.23219
pdf_url: https://arxiv.org/pdf/2611.23219
published: '2026-11-16'
collected: '2026-11-18'
category: Agent
direction: Agent 自主自改进机制研究
tags:
- LLM Agent
- Self-Improvement
- Self-Regulated Learning
- Context Optimization
- Transfer Learning
one_liner: 验证能力达标LLM可自主构建自我改进流程，生成的知识可跨任务跨模型迁移
practical_value: '- 业务Agent冷启动优化时，无需完整预置学习流程，仅提供基础工具（读写、执行、评估）和泛化目标，强LLM可自主生成任务、做A/B测试迭代策略，适配无标注数据的场景比如电商导购Agent话术优化

  - 可直接复用文中验证有效的自改进策略：优先选择中等难度任务迭代、小步更新上下文、做A/B测试验证效果，可套用到推荐系统prompt优化、用户意图理解Agent迭代等场景

  - 自优化生成的文本知识（策略、规则）支持跨模型迁移，无需为不同基座单独做优化，降低多基座部署的Agent迭代成本，比如搜索query改写Agent的规则可直接在不同LLM上复用

  - 做业务Agent优化时，平衡目标场景信息注入，过多注入特定场景细节会导致过拟合泛化性下降，无需给过细的场景约束，可保障知识跨场景复用性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM自改进方法大多需要人为预置学习流程、任务分布、更新规则，随着模型能力提升，是否还需要人为指定自改进逻辑尚未明确，该问题既关乎Agent能力上限，也对AI安全有重要参考价值。

### 方法关键点
- 采用师生同模型架构：冻结的LLM同时作为教师（负责优化上下文）和玩家（执行任务），仅给教师提供Read/Write、Bash、Gameplay三个基础工具，以及「优化文本提升玩家在未知游戏的表现」的通用目标，不预置任何学习流程、外部数据、任务规则
- 测试对象覆盖Claude Opus、GPT、GLM三个系列的6款不同能力等级的模型，用游戏玩法作为多步推理能力测试场景
- 从量化行为、自调节学习（SRL）框架对齐度、任务选择策略三个维度分析成功自改进的Agent的行为特征

### 关键结果
- 能力足够的新模型（Claude Opus-5、GPT 6-Astra、GLM 5.3）可实现自改进：Claude Opus-5在PuzzleScript-t20数据集胜率提升20%，和基于真实数据、预置流程的GEPA方法效果相当
- 生成的上下文可跨任务迁移：在PuzzleScript-t30胜率提升9%，ARC-AGI-L1提升21%，MazeBench SPL提升0.15；同时支持跨模型迁移，GPT-6生成的知识可让Claude Opus-5胜率提升22.1%
- 给教师注入过多目标场景细节会提升域内表现但降低泛化性，例如限定20轮游戏预算后，t20表现提升但t30迁移表现下降

### 最值得记住的一句话
随着LLM能力提升，人为指定的自改进流程等 inductive bias 会逐渐失去必要性，仅需提供基础工具和通用目标，强LLM即可自主构建有效学习策略。
