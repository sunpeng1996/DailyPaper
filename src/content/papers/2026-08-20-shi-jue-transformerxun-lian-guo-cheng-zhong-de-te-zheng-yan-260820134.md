---
title: Feature Evolution and Migration during Vision Transformer Training
title_zh: 视觉Transformer训练过程中的特征演化与迁移
authors:
- Joonas Järve
- Halil Ibrahim Aysel
- Tarun Khajuria
- Meelis Kull
affiliations:
- University of Tartu
arxiv_id: '2608.20134'
url: https://arxiv.org/abs/2608.20134
pdf_url: https://arxiv.org/pdf/2608.20134
published: '2026-08-20'
collected: '2026-08-21'
category: Training
direction: Transformer训练 · 特征动态分析
tags:
- ViT
- Sparse Autoencoder
- Feature Evolution
- Training Dynamics
- CLS Token
one_liner: 基于稀疏自编码器分析ViT训练跨层跨epoch特征动态，揭示特征迁移规律与分层收敛特性
practical_value: '- 多模态推荐ViT预训练/微调时，可利用深层先稳定的结论，冻结深层参数仅微调浅层，降低训练算力开销

  - 模型训练质量监控可采用Sparse Autoencoders提取CLS token稀疏特征，比表征相似度更易捕捉细粒度特征变化

  - ViT预训练可适配特征演化规律：训练早期采用大学习率加速特征迁移，后期调低学习率巩固稳定特征'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
ViT已成为视觉、多模态任务主流骨干网络，但训练过程中内部特征的演化规律尚不清晰，传统表征相似度度量无法捕捉细粒度的特征层面动态。
### 方法关键点
提出跨「网络层深度」「训练epoch」两个维度的特征演化分析框架，采用Sparse Autoencoders（SAEs）从CLS token表征中提取稀疏候选特征，对比不同epoch-层对的特征激活分布，定义特征迁移为训练过程中特征最易检测的层位置变化。
### 关键结果
1. 特征迁移集中在训练早期，向浅层迁移的频率显著高于向深层迁移，随特征组织稳定后迁移行为快速下降
2. ViT深层比浅层更早、更稳定地完成特征收敛
