---
title: 'NAE: Normalizing AutoEncoder'
title_zh: 《NAE：归一化自编码器》
authors:
- Muhammad Abdur Rafae
- Niels Landwehr
affiliations:
- University of Hildeshiem
arxiv_id: '2608.12084'
url: https://arxiv.org/abs/2608.12084
pdf_url: https://arxiv.org/pdf/2608.12084
published: '2026-08-12'
collected: '2026-08-13'
category: Training
direction: 生成模型训练 · 损失对齐优化
tags:
- Normalizing Flow
- AutoEncoder
- Loss Optimization
- Generative Model
- Gradient Alignment
one_liner: 通过对齐编解码器代理损失与重建损失梯度，提出性能达SOTA的归一化自编码器生成框架
practical_value: '- 推荐系统中用户/物品表征的VAE类生成模型训练，可借鉴损失对齐思路，将编解码器的代理损失梯度与重建损失对齐，提升表征质量

  - 生成式推荐的用户兴趣分布拟合、候选Item生成场景，可直接替换原有流自编码器的损失函数为NAE的条件损失，降低训练难度同时提升生成效果

  - 电商多模态商品内容（图、属性）生成任务中，可复用NAE框架兼顾似然估计与重建精度的优势，无需依赖严格可逆的流架构'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有带近似逆的归一化流（流自编码器）训练损失存在次优问题，编解码器代理损失未与重建损失对齐；同时严格可逆的归一化流架构灵活性差，训练采样阶段数值积分成本高。
### 方法关键点
1. 理论证明流自编码器现有损失的次优性，明确编解码器的优化梯度必须与重建损失梯度对齐；
2. 归一化自编码器NAE采用新型条件损失直接对齐代理损失与重建损失的梯度，无需依赖严格可逆架构，同时支持全维、瓶颈两种配置。
### 关键结果
在分子生成、表格数据、图像三类基准任务上全面达到SOTA性能，成为通用、高效的生成式建模框架。
