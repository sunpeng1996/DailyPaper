---
title: 'Beyond the Hard Budget: Sparsity Regularizers for More Interpretable Top-k
  Sparse Autoencoders'
title_zh: 超越硬预算：面向高可解释性Top-k稀疏自编码器的稀疏正则方法
authors:
- Nathanaël Jacquier
- Maria Vakalopoulou
- Mahdi S. Hosseini
affiliations:
- Université Paris-Saclay, CentraleSupélec
- Concordia University
- Mila–Quebec AI Institute
- Gustave Roussy (INSERM/IHU PRISM)
- MICS Laboratory
arxiv_id: '2606.27321'
url: https://arxiv.org/abs/2606.27321
pdf_url: https://arxiv.org/pdf/2606.27321
published: '2026-06-25'
collected: '2026-06-27'
category: Training
direction: Top-k稀疏自编码器训练 · 稀疏正则优化
tags:
- Sparse Autoencoder
- Top-k SAE
- Sparsity Regularization
- Model Interpretability
- Representation Learning
one_liner: 为Top-k稀疏自编码器设计两种适配稀疏正则器，兼顾重构质量与特征单语义性
practical_value: '- 电商推荐做用户/物品Embedding稀疏化时，可组合Top-k硬截断与软稀疏正则，兼顾推理时延控制与特征可解释性

  - 训练稀疏召回模型时，可复用ℓ1/ℓ2比例正则设计，让信息更集中在少数隐变量，提升小算力预算下的召回精度

  - 多场景推荐的特征适配场景，可参考仅对batch内激活单元加正则的trick，降低正则计算开销同时避免过拟合到固定k值'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
Top-k SAE通过架构层面硬截断实现稀疏，规避了传统SAE的ℓ1惩罚缺陷，但存在固定k值无法适配输入复杂度、易过拟合训练阶段k值的问题，此前未被尝试结合显式稀疏正则优化。

### 方法关键点
设计两种适配Top-k架构的稀疏正则器，均作用于Top-k选择前的激活层：① 对未被选中的非支持单元施加ℓ1惩罚；② 施加尺度不变的ℓ1/ℓ2比例正则，将编码集中到更少有效单元；两种正则仅作用于batch内至少被Top-k选中过一次的激活单元，降低额外计算开销。

### 关键结果
在2个数据集、3个视觉基础模型、多组k值配置下，两种正则均在无重构质量损失的前提下稳定提升特征单语义性；ℓ1/ℓ2正则可将信息集中到更少隐变量，使重构对推理阶段k值选择更鲁棒，小预算下线性探针性能明显提升。
