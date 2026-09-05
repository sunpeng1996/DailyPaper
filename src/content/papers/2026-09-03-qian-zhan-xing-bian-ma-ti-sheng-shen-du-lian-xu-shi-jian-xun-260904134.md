---
title: Prospective Coding Improves Learning in Deep Continuous-Time Recurrent Networks
title_zh: 前瞻性编码提升深度连续时间循环网络的学习性能
authors:
- Shivang Rawat
- Mirko Morello
- Flaviano Morone
- David J. Heeger
affiliations:
- Telepath
- New York University
arxiv_id: '2609.04134'
url: https://arxiv.org/abs/2609.04134
pdf_url: https://arxiv.org/pdf/2609.04134
published: '2026-09-03'
collected: '2026-09-05'
category: Training
direction: 深度连续时间循环网络训练优化
tags:
- State Space Models
- Recurrent Neural Networks
- Temporal Modeling
- Gradient Optimization
- Prospective Coding
one_liner: 提出递归正交滤波器RQF与无参数前瞻性输入编码，缓解深度连续时间循环网络梯度衰减
practical_value: '- 时序用户行为建模可借鉴无参数两阶前瞻性输入编码trick，不增加推理开销的前提下缓解深层时序模型梯度衰减，适配长序列用户行为召回/排序场景

  - 轻量时序建模需求可复用RQF结构，参数量远小于常规SSM/Mamba类模型，适合端侧/低延时推荐推理场景

  - 长序列训练时可尝试截断时间梯度仅做空间反向传播，搭配前瞻性编码修正，大幅降低训练算力开销的同时保障模型效果'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
连续时间循环网络/SSM堆叠到深层时，时序积分会导致自底向上信号延迟、自顶向下梯度衰减，限制深层时序模型性能，同时全时间反向传播训练算力开销极高。

### 方法关键点
1. 提出生物启发的复值时序滤波器RQF，是对角SSM的特例，可学习参数控制带通滤波的频率和带宽，参数量极低；
2. 提出无参数两阶前瞻性输入修正方案，不改变原有循环转移与并行扫描逻辑，适配所有对角SSM与RNN结构，可缓解截断时间梯度（仅空间反向传播）下的深度相关梯度衰减。

### 关键结果
全BPTT训练下所有模型的前瞻性变体均优于基线；31.9k参数量的6层非残差RQF在Speech Commands raw音频任务上准确率达96.09%；6层RQF在16384步长Path-X任务上准确率达83.56%
