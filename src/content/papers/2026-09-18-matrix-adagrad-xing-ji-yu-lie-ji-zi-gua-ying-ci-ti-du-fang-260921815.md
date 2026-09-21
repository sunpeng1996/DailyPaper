---
title: 'Matrix AdaGrad: Row-wise and Column-wise Adaptive Subgradient Methods'
title_zh: Matrix AdaGrad：行级与列级自适应次梯度方法
authors:
- Wenpeng Zhang
- Runsheng Yu
- Peilin Zhao
affiliations:
- Independent Researcher
- School of Artificial Intelligence, Shanghai Jiao Tong University
arxiv_id: '2609.21815'
url: https://arxiv.org/abs/2609.21815
pdf_url: https://arxiv.org/pdf/2609.21815
published: '2026-09-18'
collected: '2026-09-21'
category: Training
direction: 模型训练 · 自适应优化算法
tags:
- Optimization
- AdaGrad
- MatrixFactorization
- DNNTraining
- OnlineLearning
one_liner: 提出面向矩阵参数的行/列级自适应AdaGrad优化器，收敛边界更紧、训练稳定性更强
practical_value: '- 推荐系统矩阵分解类任务（如召回层MF、用户/物品Embedding预训练）可直接替换原有AdaGrad/Adam优化器，用Row/Column-AdaGrad提升训练稳定性，支持更大学习率加速收敛

  - 深度召回/排序模型的全连接层等矩阵参数训练场景，可替换该优化器缓解深层网络训练不稳定问题，支持堆叠更深层结构提升模型效果

  - 在线学习场景的用户/物品特征实时更新任务，采用行级自适应梯度缩放，适配业务数据的特征分布不均特性，降低长尾特征的更新噪声'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有AdaGrad、Adam等自适应优化器针对向量参数设计，未显式利用矩阵结构特性，已有的矩阵感知优化器缺乏类似AdaGrad的通用理论框架支撑，理论保证不完善。
### 方法关键点
基于带自适应近端函数的Online Mirror Descent框架，通过在线regret最小化推导矩阵感知的自适应优化策略；分别引入行级、列级矩阵近端函数，基于累积的行/列梯度范数做自适应缩放，得到Row-AdaGrad和Column-AdaGrad两个优化器，同时给出严格的regret理论保证。
### 关键结果
结构化梯度场景下，收敛边界比逐元素AdaGrad更紧；矩阵分解任务和DNN训练中，优化稳定性显著提升，支持更大学习率与更深网络训练，收敛速度和效果优于常规自适应优化器baseline。
