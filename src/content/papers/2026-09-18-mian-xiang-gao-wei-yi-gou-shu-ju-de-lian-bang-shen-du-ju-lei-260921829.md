---
title: Federated Deep Clustering Networks for High-Dimensional and Heterogeneous Data
title_zh: 面向高维异构数据的联邦深度聚类网络
authors:
- Morris Stallmann
- Charalampos S. Kouzinopoulos
- Marcin Pietrasik
- Anna Wilbik
affiliations:
- Maastricht University
arxiv_id: '2609.21829'
url: https://arxiv.org/abs/2609.21829
pdf_url: https://arxiv.org/pdf/2609.21829
published: '2026-09-18'
collected: '2026-09-21'
category: Other
direction: 联邦学习 · 非IID数据无监督聚类
tags:
- Federated Learning
- Deep Clustering
- Non-IID
- Representation Learning
- Data Augmentation
one_liner: 提出适配非IID数据的联邦深度聚类框架FedDCN，通过数据增强和几何正则保证隐空间对齐
practical_value: '- 跨域/跨端用户分群场景可参考FedDCN架构，在不泄露各方用户隐私的前提下完成高维用户特征的聚类对齐

  - 非IID数据下的特征对齐需求可复用几何正则+合成数据增强的组合策略，降低分布差异带来的效果衰减

  - 联邦场景下的无监督任务可借鉴双损失优化思路，同时保证特征重构质量与下游分群、聚类任务效果'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有联邦深度聚类方法在客户端数据为非IID分布时效果稳定性差，而大量真实场景下数据天然分布式存储，跨方聚合存在隐私合规障碍，无监督聚类需求无法得到满足。

### 方法关键点
- 构造联邦场景下的深度聚类框架FedDCN，同时优化特征重构损失与聚类损失，兼顾表征质量与聚类效果
- 引入合成数据增强提升模型鲁棒性，新增几何正则项约束不同客户端的隐空间分布对齐，适配非IID数据场景

### 关键结果
在IID与非IID数据假设下的多组实验均验证了方案有效性，非IID场景下相比现有联邦聚类方法的聚类指标提升更显著，鲁棒性表现更好。
