---
title: 'LP-NAS: Linear Programming-based Neural Architecture Search'
title_zh: 基于线性规划的神经网络架构搜索方法LP-NAS
authors:
- Abhishek Shukla
- Ankur Sinha
- Faiz Hamid
affiliations:
- IIT Kanpur, India
- IIM Ahmedabad, India
arxiv_id: '2608.14472'
url: https://arxiv.org/abs/2608.14472
pdf_url: https://arxiv.org/pdf/2608.14472
published: '2026-08-14'
collected: '2026-08-17'
category: Training
direction: 神经网络架构搜索 · 可微NAS优化
tags:
- NAS
- Linear Programming
- Differentiable NAS
- DARTS
- Bilevel Optimization
one_liner: 基于线性规划优化可微NAS架构更新方向，实现更快收敛与更优泛化性能
practical_value: '- 优化召回/排序模型的NAS流程时，可参考用验证集损失梯度+训练集损失Hessian构造线性规划求解架构更新方向，提升搜索效率

  - 可复用S-LP-NAS/R-LP-NAS两个轻量变体，在DARTS搜索空间下快速迭代模型架构，降低NAS算力开销

  - 针对跨场景迁移的模型架构需求，可参考本文架构迁移验证逻辑，减少新业务场景下模型调优成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
可微NAS效率优于传统NAS，但现有方案的架构更新方向未同时兼顾泛化性与模型参数最优性，存在搜索收敛慢、效果不稳定问题。
### 方法关键点
LP-NAS基于验证损失梯度、训练损失Hessian构造线性规划，求解可同时提升泛化性、保留模型参数最优性的架构更新方向，高效遍历搜索空间；推出S-LP-NAS、R-LP-NAS两个低算力消耗变体，适配DARTS搜索空间得到对应算法版本。
### 关键结果数字
CIFAR-10、CIFAR-100数据集上，LP-DARTS搜索与评估阶段效果均优于标准DARTS；相比P-DARTS、PC-DARTS等主流变体，CIFAR-10上效果更优；搜索得到的架构可直接迁移至ImageNet数据集生效，早期迭代验证性能显著高于标准DARTS。
