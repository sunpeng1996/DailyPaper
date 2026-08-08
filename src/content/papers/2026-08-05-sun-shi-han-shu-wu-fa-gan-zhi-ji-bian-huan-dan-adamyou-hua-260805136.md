---
title: The Loss Does Not See the Basis, but Adam Does
title_zh: 损失函数无法感知基变换，但Adam优化器可以
authors:
- Devender Singh
affiliations:
- Memorial University of Newfoundland
arxiv_id: '2608.05136'
url: https://arxiv.org/abs/2608.05136
pdf_url: https://arxiv.org/pdf/2608.05136
published: '2026-08-05'
collected: '2026-08-08'
category: Training
direction: 深度学习训练 · 优化器低秩偏置研究
tags:
- Optimizer
- Adam
- Low-rank Bias
- Gauge Equivariance
- Transformer Training
one_liner: 揭示优化器规范等变特性决定低秩偏置，分类9种常见优化器的等变性与效果差异
practical_value: '- 训练矩阵分解类召回、用户建模模型时，优先选择GD、动量、shared-scalar Adam等规范等变优化器，可得到有效秩更低、泛化性更好的解

  - 训练多模态Embedding、Semantic ID生成模型时，避免使用普通Adam/RMSProp，减少基变换带来的Embedding空间不稳定问题

  - 推荐大模型LoRA微调场景可尝试用spectral schedule调整Muon优化器，平衡低秩拟合效果与长尾特征适配能力'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
过参数化矩阵分解训练中，梯度下降（GD）有天然低秩偏置但Adam没有，背后机制不明，优化器选择对解的泛化性影响长期被低估。
### 方法关键点
提出优化器需满足**规范等变（gauge-equivariant）**才能继承梯度流的低秩特性，证明无记忆等变规则等价于Gram确定的左预处理器，构建从逐坐标到共享标量预条件的单参数族，隔离各向异性对低秩偏置的影响。
### 关键结果数字
1. 9种常见优化器分类：GD、动量、shared-scalar Adam、Muon、Shampoo满足等变，普通Adam、RMSProp等逐坐标优化器不满足
2. 低采样密度下，等训练损失时GD比非等变优化器降低43~44%的留出误差，解的有效秩更低
3. Transformer训练中普通Adam会导致多头注意力的$W_Q^\top W_K$相对Frobenius距离差达56%，破坏头不变性
