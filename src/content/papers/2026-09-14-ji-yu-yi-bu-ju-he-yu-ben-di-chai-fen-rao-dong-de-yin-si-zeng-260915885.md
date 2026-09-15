---
title: Privacy-enhanced federated learning via asynchronous aggregation and local
  differential perturbation
title_zh: 基于异步聚合与本地差分扰动的隐私增强联邦学习框架
authors:
- Zhen Zhong
- Shini Yang
- Liesheng Wei
affiliations:
- Georgetown University
- LinkedIn
- Shanghai Ocean University
arxiv_id: '2609.15885'
url: https://arxiv.org/abs/2609.15885
pdf_url: https://arxiv.org/pdf/2609.15885
published: '2026-09-14'
collected: '2026-09-15'
category: Training
direction: 联邦学习 · 隐私增强训练优化
tags:
- Federated Learning
- Differential Privacy
- Homomorphic Encryption
- Asynchronous Aggregation
- Privacy-Preserving Training
one_liner: 融合动态差分隐私、轻量同态加密与异步聚合策略，实现高隐私约束下低通信开销的联邦学习
practical_value: '- 电商跨端/跨商家联合建模场景可复用DDP+轻量HE+LDP组合隐私机制，在用户行为数据不出域的前提下降低隐私泄露风险，适配数据合规要求

  - 大流量推荐系统端云联合训练可借鉴带版本控制的异步聚合策略，相比传统FedAvg降低21.3%通信开销，适配异构节点训练节奏

  - 用户敏感标签建模等高隐私约束场景可参考其ε=0.1下仍保持82.6%精度的参数调优方案，平衡隐私合规与模型效果'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
分布式机器学习场景下，现有差分隐私、同态加密等隐私方案存在模型迭代追溯难、访问控制弱、数据流合规性难保障等问题，难以同时平衡隐私保护、模型精度与通信效率。

### 方法关键点
1. 融合Dynamic Differential Privacy (DDP)、轻量Homomorphic Encryption (HE)、Local Differential Privacy (LDP)三层机制，全链路保障训练过程数据隐私；
2. 采用带版本控制的异步聚合策略，适配异构分布式节点的异步训练需求，降低节点间通信依赖。

### 关键结果
在CIFAR-10、Purchase-100基准数据集验证：ε=0.1的严格隐私约束下分类精度最高达82.6%，相比FedAvg降低21.3%通信开销，可支撑大规模分布式协同计算场景。
