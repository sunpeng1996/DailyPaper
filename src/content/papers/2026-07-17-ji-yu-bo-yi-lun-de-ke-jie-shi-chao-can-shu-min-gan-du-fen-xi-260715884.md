---
title: Which Hyperparameters Matter? A Game-Theoretic Framework for Interpretable
  Hyperparameter Sensitivity Analysis
title_zh: 基于博弈论的可解释超参数敏感度分析框架
authors:
- Nyi Nyi Aung
- Heepeom Shin
- Abigail Lawlor
- Adrian Stein
affiliations:
- Louisiana State University
arxiv_id: '2607.15884'
url: https://arxiv.org/abs/2607.15884
pdf_url: https://arxiv.org/pdf/2607.15884
published: '2026-07-17'
collected: '2026-07-21'
category: Training
direction: 模型训练 · 超参数敏感度分析
tags:
- Hyperparameter Optimization
- Game Theory
- Shapley Value
- Pareto Front
- Interpretability
one_liner: 用Shapley效应和帕累托前沿实现目标感知的可解释超参数敏感度分析
practical_value: '- 推荐/LLM Agent模型调参前，可先用该框架分析核心影响超参数，大幅缩小HPO搜索空间，降低调参算力开销

  - 针对多目标权衡场景（如推荐的准确率、推理时延、资源占用多目标优化），可复用帕累托前沿筛选高效超参数配置，加速早期模型选型

  - LLM微调、LoRA训练场景下，可通过该框架快速定位对业务目标（如点击率、生成准确率）影响最大的超参数，针对性优化'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有超参数优化（HPO）多为黑盒方案，无法区分不同超参数对业务目标的实际影响，易产生冗余搜索、浪费训练算力，尤其对训练成本高的大模型、推荐系统来说开销不可接受。
### 方法关键点
1. 基于博弈论框架，将超参数作为博弈玩家、业务目标作为收益，用Shapley Effects做全局敏感度分析，量化每个超参数对不同目标的贡献度
2. 结合帕累托前沿集筛选高性价比超参数配置，支持多目标场景下的早期模型评估
### 关键结果
跨3类不同领域神经网络、多目标设置下验证有效，可有效缩小超参数搜索空间、降低调参成本，提前完成早期模型性能预判
