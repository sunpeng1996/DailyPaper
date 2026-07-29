---
title: Soft-Constrained Optimization of Latent Space in Variational Autoencoders
title_zh: 变分自编码器隐空间的软约束优化方法
authors:
- Ye Shi
arxiv_id: '2607.23751'
url: https://arxiv.org/abs/2607.23751
pdf_url: https://arxiv.org/pdf/2607.23751
published: '2026-07-26'
collected: '2026-07-29'
category: Training
direction: VAE训练 · 隐空间优化
tags:
- VAE
- Latent Space
- Disentanglement
- Regularization
- Pruning
one_liner: 提出熵约束+权重过滤的VAE软约束训练框架，同时提升隐变量编码容量与解耦性
practical_value: '- 用VAE做用户/物品隐向量建模时，可新增熵约束平衡隐空间容量与解耦性，解决KL正则过强导致隐变量失效的问题

  - 下游召回/排序任务前，可复用权重过滤法自动裁剪低熵隐维度，降低特征规模的同时保留核心信息，加快模型收敛

  - 离散属性（如商品类目、用户性别）与连续属性（如价格、用户活跃度）的隐向量编码规律可直接复用，指导特征交叉设计'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
VAE隐空间的高编码容量和低维解耦特性难以兼得：削弱KL正则可提升容量但会降低解耦性，增强KL正则优化解耦性但会大量裁剪有效隐变量，存在明显trade-off。

### 方法关键点
1. 将VAE训练建模为软约束优化问题，对单个隐变量施加熵约束（EC）：隐编码熵是其与数据生成因子互信息的上界，提升熵即可直接提升编码容量。
2. 提出权重过滤法，利用软约束的松弛度在下游训练阶段裁剪低熵隐维度，得到可用隐空间维度的经验下界。

### 关键结果数字
- dSprites数据集上：相较vanilla VAE隐变量激活总分提升43-62%，FactorVAE得分达0.891（高于β-VAE的0.847），重构误差最高降低38%。
- MNIST数据集上：下游分类器输入隐维度从10裁剪到2仍保持90%以上精度，收敛epoch减少37%
