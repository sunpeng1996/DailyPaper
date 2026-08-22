---
title: An Inclusive and Lightweight Approach to Federated Continual Learning for Cultural
  Heritage
title_zh: 面向文化遗产的普惠轻量化联邦持续学习方法
authors:
- Ioannis Theologitis
- Debin Meng
- Stylianos Eleftheriadis
- Vasileios Lolis
- Konstantinos Votis
affiliations:
- Information Technologies Institute, Centre for Research and Technology Hellas
- Queen Mary University of London
arxiv_id: '2608.20038'
url: https://arxiv.org/abs/2608.20038
pdf_url: https://arxiv.org/pdf/2608.20038
published: '2026-08-20'
collected: '2026-08-22'
category: Other
direction: 联邦持续学习 · 隐私保护分布式训练
tags:
- Federated Continual Learning
- Regularization
- Privacy-preserving
- Energy Efficiency
- Fairness
one_liner: 提出基于正则化的轻量化联邦持续学习策略FedCurv-DR，平衡性能、公平性与能效
practical_value: '- 跨多商家/区域的隐私受限推荐建模场景，可借鉴基于参数重要性估计的正则化思路，缓解旧用户/冷门品类特征的灾难性遗忘问题

  - 分布式联邦推荐架构中，固定间隔更新全局正则化参数的策略可降低跨节点通信 overhead，适合边缘端参与的轻量化推荐部署

  - 核心方案针对文化遗产图像分类场景设计，无直接适配电商推荐的实验结论，落地需额外做场景适配'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
文化遗产数据分散在不同机构，受所有权、访问权限限制无法共享，且数据随时间持续演化，现有联邦持续学习方案通信与计算开销过高，难以落地。
### 方法关键点
1. 基于正则化设计轻量化FCL策略FedCurv-DR，跨客户端、跨任务累积参数重要性估计，保护已学习的旧知识，缓解灾难性遗忘
2. 仅按固定间隔更新全局参数重要性估计，大幅降低跨节点通信量与计算开销
### 关键结果
在WikiArt图像风格演化的持续分类任务上测试，FedCurv-DR有效降低遗忘，同时在分类性能、多机构公平性、计算能效三个维度实现均衡，适配文化遗产领域可持续AI需求。
