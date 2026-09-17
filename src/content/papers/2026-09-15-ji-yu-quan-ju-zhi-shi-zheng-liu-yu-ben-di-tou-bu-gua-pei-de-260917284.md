---
title: Personalized Federated Learning through Global Knowledge Distillation and Local
  Head Adaptation
title_zh: 基于全局知识蒸馏与本地头部适配的个性化联邦学习
authors:
- Polycarpo Souza Neto
- José Mairton Barros da Silva Júnior
- Charles Casimiro Cavalcante
affiliations:
- Universidade Federal do Ceará
- Uppsala University
arxiv_id: '2609.17284'
url: https://arxiv.org/abs/2609.17284
pdf_url: https://arxiv.org/pdf/2609.17284
published: '2026-09-15'
collected: '2026-09-17'
category: Training
direction: 联邦学习训练 · 非IID数据适配
tags:
- Federated Learning
- Knowledge Distillation
- Non-IID Data
- Model Personalization
- Distributed Training
one_liner: 提出pFedKDH个性化联邦学习框架，仅聚合共享backbone，保留客户端本地头部，用校准全局头做训练教师
practical_value: '- 跨端隐私合规推荐场景可复用「仅聚合公共backbone、保留端侧个性化头部」的架构，既利用全局数据信息，又适配不同用户/商家的分布差异

  - 非IID数据下的模型训练可引入全局校准teacher做知识蒸馏，能降低分布偏移带来的精度损失，同时提升模型稳定性

  - 多租户广告推荐场景可借鉴该思路，不用聚合租户私有数据就能联合训练，满足隐私合规要求的同时提升个性化效果'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
联邦学习可在不迁移用户原始数据的前提下实现分布式协同训练，是隐私合规场景的核心训练范式，但客户端数据非IID（尤其是标签偏斜）导致全局分类器无法适配各客户端分布，严重制约模型效果。
### 方法关键点
提出pFedKDH个性化联邦学习框架：1）仅聚合各客户端的共享backbone参数，本地保留持久化的客户端专属分类头，适配本地分布；2）训练阶段引入服务端重新校准的全局头作为teacher模型，通过知识蒸馏引导本地优化。
### 关键结果
在MNIST、Fashion-MNIST、CIFAR10、CIFAR100四个数据集的类Dirichlet划分设置下，大部分场景精度均为最优，较最弱基线精度最高提升37.67%，重复实验的标准差始终保持较低水平，验证了持久化头部与蒸馏引导优化的有效性
