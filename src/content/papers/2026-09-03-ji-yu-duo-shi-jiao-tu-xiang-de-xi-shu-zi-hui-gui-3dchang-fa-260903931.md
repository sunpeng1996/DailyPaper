---
title: Sparse auto-regressive modeling for scene generation from multi-view images
title_zh: 基于多视角图像的稀疏自回归3D场景生成方法
authors:
- Thomas Lucas
- Maxime Pietrantoni
- Philippe Weinzaepfel
- Wonjune Cho
- Bardienus Pieter Duisterhof
- Vincent Leroy
- Jerome Revaud
affiliations:
- NAVER LABS Europe, France
- NAVER LABS, South Korea
- Carnegie Mellon University, USA
arxiv_id: '2609.03931'
url: https://arxiv.org/abs/2609.03931
pdf_url: https://arxiv.org/pdf/2609.03931
published: '2026-09-03'
collected: '2026-09-05'
category: Other
direction: 3D视觉·多视角图像场景生成
tags:
- 3D Scene Generation
- Sparse Voxel
- Autoregressive Transformer
- 3D Gaussian Splatting
- Multi-view Reconstruction
one_liner: 提出SPAR3S稀疏3D隐式生成模型，无需3D真值监督即可完成多视角输入的场景补全
practical_value: '- 可复用稀疏体素仅保留占用位的压缩思路，用于3D商品/场景建模时降低显存占用、提升推理速度

  - 无需3D真值监督、仅用多视角图像光度监督的训练范式，可迁移到电商3D商品素材自动生成场景，降低标注成本

  - 掩码自回归Transformer联合预测空间占用+隐向量的架构，可借鉴到AR看房/家装场景的3D空间补全任务'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
多视角稀疏输入生成完整3D场景是3D视觉核心难题，现有前馈重建方法仅能还原输入可见内容，稠密3D生成方法计算成本高、依赖大量3D真值标注，落地难度大。
### 方法关键点
1. SPAR3S稀疏体素对齐3D隐式生成模型仅对占用体素建模，大幅压缩隐空间规模
2. 基于可微3D Gaussian Splatting的光度监督，直接从多视角图像学习稀疏隐空间，无需3D真值标注
3. 掩码自回归Transformer联合建模体素占用率和隐式token值，从输入视角编码的部分体素预测缺失区域内容
### 关键结果
在合成室内场景数据集上生成新视角质量优于现有SOTA，在RealEstate10k真实场景数据集上验证了良好泛化性
