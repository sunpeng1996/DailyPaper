---
title: Module-Aware Optimization for Graph Neural Networks
title_zh: 面向图神经网络的模块感知优化方法
authors:
- Guy Hadad
- Haggai Roitman
- Moshe Eliasof
- Bracha Shapira
affiliations:
- Ben-Gurion University of the Negev
arxiv_id: '2611.08379'
url: https://arxiv.org/abs/2611.08379
pdf_url: https://arxiv.org/pdf/2611.08379
published: '2026-11-05'
collected: '2026-11-07'
category: Training
direction: GNN训练优化 · 自适应优化器
tags:
- GNN
- Optimizer
- Training Efficiency
- Graph Representation
- Muon
one_liner: 提出适配图传播输入协方差结构的GraphMuon优化器，大幅提速GNN训练且精度持平或更优
practical_value: '- 业务中若使用GNN建模用户-商品交互、商品关联、用户社交关系图，可直接替换AdamW为GraphMuon，最高获2.42倍训练收敛提速，降低训练成本

  - 优化器设计思路可迁移：针对图输入传播的协方差特征做更新正交化与步长归一化的逻辑，可复用至自研图推荐模型的定制优化器开发

  - 训练收敛提速后可支持更大规模电商交互图训练、更频繁的模型迭代，适配实时性要求高的推荐场景'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有AdamW等坐标级自适应优化器、Muon等矩阵感知优化器，均未考虑GNN中参数更新效果会被图传播特征放大，导致更新不稳定、收敛速度慢。
### 方法关键点
1. 提出图感知优化器GraphMuon，适配GNN层输入的图传播表征协方差结构定义正交化度量
2. 基于更新对层表征的诱导效应动态归一化步长，从理论上缓解图带来的更新放大问题
### 关键结果
1. 在3个大规模OGB基准数据集上，相较AdamW获得1.32×~2.42×的验证损失达标时间提速
2. 覆盖节点分类、归纳式图分类、图回归的15组数据集-架构配置中，13组实现收敛提速，同时预测精度持平或更优
