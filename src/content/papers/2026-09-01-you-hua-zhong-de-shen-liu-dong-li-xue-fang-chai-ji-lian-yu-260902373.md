---
title: 'Percolation Dynamics in Optimization : Variance Cascades and Discrete Scale
  Invariance'
title_zh: 优化中的渗流动力学：方差级联与离散尺度不变性
authors:
- Sai Niranjan Ramachandran
- Suvrit Sra
arxiv_id: '2609.02373'
url: https://arxiv.org/abs/2609.02373
pdf_url: https://arxiv.org/pdf/2609.02373
published: '2026-09-01'
collected: '2026-09-06'
category: Training
direction: 深度学习优化 · 训练动力学机制
tags:
- SGD
- Adam
- Optimization
- Training Dynamics
- Percolation Model
one_liner: 用渗流过程建模随机梯度流，揭示SGD/Adam/AdamW训练隐式偏置的动力学机制
practical_value: '- 训练电商推荐/广告大模型时，可监控梯度方差尖峰判断子网络合并阶段，预判grokking拐点，动态调整学习率调度策略

  - 基于子网络离散批量合并的规律，优化LoRA微调的参数解冻策略，分阶段释放参数，提升垂域推荐模型微调效率

  - 针对AdamW优化的重尾噪声特性，在大尺寸商品Embedding训练时加入梯度截断，抑制方差级联带来的训练不稳定'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
当前对SGD等优化器引导深度网络向简单子网络收敛的演化动力学机制认知不足，无法解释grokking等非平滑训练现象，制约训练稳定性与效率优化。
### 方法关键点
1. 将随机梯度流（SGF）建模为渗流过程，发现架构对称性会驱动子网络以离散批量方式合并，而非逐次迭代演化
2. 该结构相变可通过宏观序参数的方差尖峰表征，与物理相变规律一致
3. 证明在明确的重尾噪声模型下，该捕获机制及对应的缩放级联效应同样适用于Adam、AdamW优化器
### 关键结果
揭示了SGD/Adam/AdamW训练过程中网络向稀疏低秩表征坍缩的内在规律，解释了训练过程中非平滑跃迁的底层成因
