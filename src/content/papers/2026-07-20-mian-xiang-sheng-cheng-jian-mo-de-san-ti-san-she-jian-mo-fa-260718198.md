---
title: Three-Body Scattering for Generative Modeling
title_zh: 面向生成建模的三体散射建模方法
authors:
- Peng Sun
- Zhenglin Cheng
- Deyuan Liu
- Jun Xie
- Xinyi Shang
- Tao Lin
affiliations:
- Westlake University
- Zhejiang University
- University College London
arxiv_id: '2607.18198'
url: https://arxiv.org/abs/2607.18198
pdf_url: https://arxiv.org/pdf/2607.18198
published: '2026-07-20'
collected: '2026-07-22'
category: Training
direction: 生成模型训练 · 单步生成性能优化
tags:
- Generative Modeling
- One-step Generation
- Energy Distance
- Wasserstein Gradient
- TBSM
one_liner: 提出三体散射建模TBSM，通过样本级交互监督训练高性能单步生成器
practical_value: '- 单步生成训练范式可迁移到生成式推荐场景，比如Semantic ID生成、推荐文案生成，大幅降低推理时延

  - 三元组（真实样本+2个生成样本）交互损失设计可替代GAN对抗损失，解决生成任务训练不稳定问题

  - 在线跟踪条件期望降噪声的trick可复用在大模型小批次微调场景，提升训练稳定性'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有生成模型依赖对抗训练、预定义扩散路径或自回归分解，存在训练不稳定、多步推理速度慢等问题，单步生成的性能天花板待突破。
### 方法关键点
提出三体散射建模（TBSM），将能量距离转化为每个生成样本的独立交互规则：每个生成样本（抛射体）朝向真实样本吸引、远离另一个独立生成的样本，其期望等价于$rac{1}{2}D_E^2(P_	heta,Q)$的2-Wasserstein梯度流速度；仅需O(B)样本级损失，避免小批次全对计算的噪声，可在线跟踪条件期望进一步降噪。
### 关键结果
在ImageNet-256数据集上，像素空间PixelDiT-XL单步生成FID达2.23，隐空间DiT-XL单步生成FID达1.63，为当前单步生成SOTA水平。
