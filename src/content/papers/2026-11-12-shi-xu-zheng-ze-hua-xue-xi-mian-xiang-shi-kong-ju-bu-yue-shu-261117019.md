---
title: 'Temporal Regularized Learning: Self-Supervised Learning Local in Space and
  Time'
title_zh: 时序正则化学习：面向时空局部约束的自监督学习方法
authors:
- Davide Wiest
affiliations:
- Department of Computer Science, TU Darmstadt
arxiv_id: '2611.17019'
url: https://arxiv.org/abs/2611.17019
pdf_url: https://arxiv.org/pdf/2611.17019
published: '2026-11-12'
collected: '2026-11-14'
category: Training
direction: 自监督训练 · 流式时序在线学习
tags:
- Self-Supervised-Learning
- Temporal-Learning
- Local-Training
- Online-Learning
- Hebbian-Updates
one_liner: 提出时空局部自监督学习规则TeReL，支持单样本流式训练与推理侧无标注持续学习
practical_value: '- 流式用户行为序列表征场景可复用TeReL的时序相邻正样本构造逻辑，无需batch即可做自监督预训练，降低训练内存开销

  - 推理侧实时学习场景可借鉴训练推理同计算的设计，基于用户实时行为无标注更新表征模型，无需全量重训

  - 端侧小模型推荐场景可尝试Hebbian/anti-Hebbian局部权重更新规则，省去层间反向传播开销，适配端侧算力约束'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有层局部自监督目标仅实现空间局部性，损失仍依赖跨样本batch计算，不支持时序流式输入的在线训练，无法实现推理侧无标注持续学习。

### 方法关键点
1. 提出TeReL时空局部学习规则，基于VICReg目标构造时序相邻样本为正样本，用非微分运行统计量替代batch统计，实现单样本粒度每神经元在线损失计算；
2. 梯度对应前馈权重Hebbian更新、层侧矩阵anti-Hebbian更新，无需层间反向传播，训练与推理计算逻辑完全一致。

### 关键结果数字
类别分块MNIST流式任务上，batch size=1的2层全连接网络线性探测准确率达96.48%，优于随机特征（95.09%）与经典SFA；放松局部约束的变体精度与监督反向传播相当，推理阶段无标注持续学习无精度损失。
