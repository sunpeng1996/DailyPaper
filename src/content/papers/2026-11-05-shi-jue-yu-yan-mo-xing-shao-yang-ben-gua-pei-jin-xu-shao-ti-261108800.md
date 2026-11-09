---
title: 'On the Few-Shot Adaptation of Vision-Language Models: A Few Gradient Signs
  Are All You Need'
title_zh: 《视觉语言模型少样本适配：仅需少量梯度符号即可实现高效优化》
authors:
- Nairouz Mrabah
- Ismail Ben Ayed
- Mahdi S. Hosseini
- Eric Granger
affiliations:
- ETS Montreal, Canada
- Concordia University, Canada
arxiv_id: '2611.08800'
url: https://arxiv.org/abs/2611.08800
pdf_url: https://arxiv.org/pdf/2611.08800
published: '2026-11-05'
collected: '2026-11-09'
category: Training
direction: 多模态少样本训练 · 优化器设计
tags:
- Few-Shot Learning
- Vision-Language Model
- Optimizer
- Sparse Gradient
- PEFT
one_liner: 提出两款无状态稀疏梯度符号优化器，提升VLM少样本适配效果与长训练稳定性
practical_value: '- 电商多模态商品分类/召回场景的VLM少样本微调时，可复用高幅值梯度符号筛选思路，仅更新对应参数，降低少样本噪声影响，减少调参成本

  - 小样本任务微调阶段可替换现有Adam/SGD为SignSparseSGD，无需维护一二阶动量状态，节省训练显存，同时降低长训练周期过拟合风险

  - 跨品类商品识别等多模态迁移任务可直接复用统一超参配置，无需逐场景调优优化器超参数，降低落地成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
VLM少样本适配场景监督数据稀缺，梯度估计噪声大、幅值校准偏差严重，传统基于完整梯度的Adam/SGD等优化器易过拟合，且需针对不同场景单独调参，落地成本高。
### 方法关键点
1. 验证仅梯度幅值Top的小部分子集的符号具备有效信息，据此设计两款无状态优化器：静态SignSparseSGD在首个minibatch后固定更新参数子集，动态DynSignSparseSGD每步刷新更新子集
2. 仅用梯度幅值选择更新位置，用固定幅值的梯度符号执行更新，无一二阶动量状态，无需任务特定模块，全场景共用一套配置
### 关键结果
在11个数据集、3款CLIP backbone、5种少样本设置下，平均效果持平或优于现有PEFT及优化器基线，对长训练周期的敏感度显著降低
