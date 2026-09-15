---
title: Thought without systematicity? Evaluating reasoning models on rule induction
  tasks
title_zh: 《无系统性的思考？规则归纳任务下推理模型的系统性评估》
authors:
- Simon Schug
- Brenden M. Lake
affiliations:
- Princeton University
arxiv_id: '2609.13948'
url: https://arxiv.org/abs/2609.13948
pdf_url: https://arxiv.org/pdf/2609.13948
published: '2026-09-12'
collected: '2026-09-15'
category: Reasoning
direction: 推理模型认知系统性评估
tags:
- systematicity
- rule induction
- reasoning evaluation
- cognitive science
- LLM benchmark
one_liner: 通过认知科学规则归纳同构任务评估，验证主流推理模型普遍缺乏认知系统性
practical_value: '- 电商/导购Agent的推理能力验证可复用本文的同构任务变体生成方法，避免单测试集过拟合导致的模型能力高估

  - 落地依赖规则泛化的业务场景（如大促规则理解、优惠券匹配Agent）时，必须用结构等价的多变体测试集验证鲁棒性

  - 做推理模型微调或prompt优化时，可加入同构任务变体做训练增强，提升规则归纳的跨场景泛化能力'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
人类认知具备系统性核心特征：掌握某概念后可直接泛化到结构等价的变体场景，但当前主流推理模型是否具备该能力缺乏严谨验证，现有评估常因测试场景单一高估模型真实推理水平。
### 方法关键点
引入认知科学领域4类规则归纳任务族（布尔类别学习、符号瑞文推理、整数序列程序归纳、语法驱动指令学习），通过重组、替换等任务同构变换，为每个基础任务生成K=5个结构完全等价的变体，从三个维度评估系统性：是否解决任意变体、变体平均解决率、是否解决全部变体。
### 关键结果数字
仅布尔类别学习任务上几乎所有模型表现出完全系统性；其余3类任务中，即使模型能解决某单个任务变体，同构变体平均解决率最高仅约70%，GPT-5.5全任务的全变体解决率仅30%左右，多数模型存在显著泛化缺口。
