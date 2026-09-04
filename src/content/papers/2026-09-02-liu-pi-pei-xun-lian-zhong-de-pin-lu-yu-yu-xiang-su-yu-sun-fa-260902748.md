---
title: Balancing Frequencies and Pixels in Flow Matching
title_zh: 流匹配训练中的频率域与像素域损失平衡优化方法
authors:
- Lucas Degeorge
- Paul Couairon
- Arijit Ghosh
- Alexei A. Efros
- David Picard
- Vicky Kalogeiton
affiliations:
- LIX, École Polytechnique, CNRS, IP Paris, France
- AMIAD
- LIGM, École Nationale des Ponts et Chaussées, IP Paris, UGE, CNRS, France
- UC Berkeley
arxiv_id: '2609.02748'
url: https://arxiv.org/abs/2609.02748
pdf_url: https://arxiv.org/pdf/2609.02748
published: '2026-09-02'
collected: '2026-09-04'
category: Training
direction: 生成式模型训练 · 损失函数优化
tags:
- Flow Matching
- Loss Function
- Frequency Domain
- Training Optimization
- Generative Model
one_liner: 提出频谱平衡损失与两阶段训练策略，无需改架构即可加速流匹配收敛、提升生成质量
practical_value: '- 电商商品图生成、AIGC营销素材训练场景可直接复用f-loss，无需改模型架构即可提升纹理、边缘等细节生成质量，缩短训练周期

  - 生成类任务的两阶段训练范式可迁移：早期加频域损失快速覆盖全频率特征，后期切像素域损失做空间细节优化，平衡收敛速度与生成精度

  - 多模态推荐中生成商品展示内容时，可引入频域损失权重调控，解决低分辨率模糊、细节丢失问题，提升用户对推荐内容的感知满意度'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
自然图像能量遵循1/f²频谱分布，多数能量集中在低频域，但纹理、边缘等感知关键结构位于稀疏高频带。像素空间重建损失对所有空间误差权重一致，导致优化被低频信号主导，高频特征学习滞后，是像素空间流模型训练效率低的核心原因。
### 方法关键点
1. 提出Focal Log-Frequency Loss（f-loss），通过频谱均衡机制让不同频率的学习信号权重对等，强化原本被抑制的高频分量学习；
2. 设计两阶段训练策略：前期侧重频域学习快速捕获全频率特征，后期切换为标准像素域损失做空间细节微调，适配模型不同训练阶段的需求，完全无需修改模型架构，可直接替换原有流匹配损失。
### 关键结果
多模型规模下训练收敛速度最高提升40%，同时FID、感知保真度均得到一致性优化。
