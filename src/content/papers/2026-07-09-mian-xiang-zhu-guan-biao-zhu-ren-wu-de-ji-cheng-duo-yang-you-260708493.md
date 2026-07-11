---
title: Ensemble Diversity Optimization for Subjective Supervision
title_zh: 面向主观标注任务的集成多样性优化框架EDO
authors:
- Xia Cui
- Ziyi Huang
- N. R. Abeynayake
affiliations:
- Manchester Metropolitan University
- Hubei University
arxiv_id: '2607.08493'
url: https://arxiv.org/abs/2607.08493
pdf_url: https://arxiv.org/pdf/2607.08493
published: '2026-07-09'
collected: '2026-07-11'
category: Training
direction: 主观标注任务·集成模型训练优化
tags:
- Ensemble Learning
- Model Calibration
- Subjective NLP
- Diversity Regularization
- Gumbel-Softmax
one_liner: 提出端到端可训练的集成多样性优化框架EDO，提升主观NLP任务校准性与标注分布对齐度
practical_value: '- 电商内容审核、用户评论情感分类等存在标注分歧的场景，可引入EDO的带符号多样性正则器，避免模型坍缩到主流标注，提升输出校准性

  - 多模型融合排序/召回场景，可复用EDO基于Gumbel-Softmax端到端优化集成权重与有效基数的方法，替代人工调权，平衡效果与推理成本

  - 处理样本不平衡的分类任务时，可直接复用EDO的软F1代理损失+类别加权交叉熵的组合损失设计，提升小类识别精度'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
主观NLP任务（如内容审核、情感分析）普遍存在系统性标注分歧，传统监督学习聚合为单一标签会丢失分布信息，易过拟合主流标注，现有集成方法易发生坍缩，难以平衡效用与校准性。

### 方法关键点
1. 提出统一可微目标的EDO框架，基于Gumbel-Softmax松弛端到端学习集成的组成与规模，联合优化集成权重、有效基数、校准性；
2. 引入可在验证集上调优的带符号多样性正则器，可按需保留/抑制标注分歧，避免集成坍缩；
3. 融合软F1代理损失、类别加权交叉熵、可靠性加权多样性约束，适配不平衡样本与集成内变率调控。

### 关键结果数字
在4个主观文本分类基准上，相比Soft-CE、Top-5 Voting等基线，交叉熵降低40%-78%，Brier分数显著下降，同时保持有竞争力的F1，与标注分布对齐度更优。
