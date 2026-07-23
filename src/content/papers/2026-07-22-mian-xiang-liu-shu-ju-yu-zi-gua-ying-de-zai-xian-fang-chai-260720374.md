---
title: Online Variance Reduction for Domain Adaptation on Streaming Data
title_zh: 面向流数据域自适应的在线方差削减方法
authors:
- Andrea Napoli
affiliations:
- Department of Electronics and Computer Science, University of Southampton
- University of Southampton, UK
arxiv_id: '2607.20374'
url: https://arxiv.org/abs/2607.20374
pdf_url: https://arxiv.org/pdf/2607.20374
published: '2026-07-22'
collected: '2026-07-23'
category: Training
direction: 流数据域自适应 · 训练方差优化
tags:
- Domain Adaptation
- Variance Reduction
- Online Learning
- Streaming Data
- MMD
- CORAL
one_liner: 提出首个面向流数据MMD、CORAL损失的在线方差削减算法ARROW，性能比肩离线SVR方案
practical_value: '- 跨域推荐场景遇到流数据域偏移时，可复用ARROW的滑动平均统计量对齐+minibatch重加权方案，替代离线SVR适配在线增量训练

  - 用MMD/CORAL做域对齐训练不稳定时，可引入文中的松弛重加权优化方案，降低权重求解复杂度同时削减训练方差

  - 分布式推荐模型训练的域对齐模块，可直接集成ARROW框架，无需全量数据即可实现与离线SVR相当的目标域精度'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有针对MMD、CORAL域对齐损失的离线随机方差削减（SVR）算法无法适配在线、分布式、增量学习场景，小batch场景下损失估计方差过高易导致训练不稳定，甚至出现域对齐效果劣于无对齐方案的问题。
### 方法关键点
1. 提出ARROW在线SVR框架，维护域对齐统计量的滑动平均参考值；
2. 自适应对输入minibatch样本重加权，实现minibatch统计量与参考值对齐；
3. 引入松弛重加权机制，将高复杂度权重优化问题转化为可高效求解的形式。
### 关键结果
实验验证ARROW在运行时长、方差削减幅度、目标域精度三个核心指标上，均达到与离线SVR算法相当的表现。
