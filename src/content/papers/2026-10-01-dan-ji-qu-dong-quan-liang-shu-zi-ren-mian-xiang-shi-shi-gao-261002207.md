---
title: 'One Basis to Animate Them All: Gaussian Blendshape Distillation for Real-Time
  Avatars'
title_zh: 单基驱动全量数字人：面向实时Avatar的高斯混合形状蒸馏方法
authors:
- Ramazan Fazylov
- Stamatis Lefkimmiatis
- Ivan Laptev
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
- MWS AI
arxiv_id: '2610.02207'
url: https://arxiv.org/abs/2610.02207
pdf_url: https://arxiv.org/pdf/2610.02207
published: '2026-10-01'
collected: '2026-10-03'
category: Other
direction: 3D高斯Avatar 实时推理轻量化
tags:
- 3D Gaussian Splatting
- Avatar
- Knowledge Distillation
- Real-time Rendering
- Model Compression
one_liner: 提出GALA蒸馏框架，用共享线性混合形状替代重神经解码，实现3D高斯Avatar端侧实时运行
practical_value: '- 电商虚拟主播、AR试穿等场景可复用该蒸馏思路，将高算力3D Avatar推理优化到移动端60fps水平，大幅降低端侧部署门槛

  - 可迁移「预训练大模型+浅层MLP预测线性组合系数」的蒸馏框架，适配其他大模型端侧部署的轻量化需求

  - 渲染感知的块局部PCA基构建方法可复用，在固定内存预算约束下有效提升轻量化模型的输出保真度'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
3D Gaussian Avatar渲染效率高，但动画生成依赖重度神经网络推理，算力开销大，难以在端侧实现实时部署。
### 方法关键点
1. 发现预训练Avatar的动画效果可通过身份无关的blendshape线性组合近似拟合，提出GALA蒸馏框架，用浅层MLP预测混合系数+线性组合替代逐帧重神经解码
2. 采用渲染感知度量下的块局部PCA构建基向量，在控制内存开销的同时提升生成保真度
3. 无需重训练原始预训练模型，可直接适配多种不同架构的Avatar模型
### 关键结果
在人脸、带服饰全身等三类Avatar模型上验证，CPU推理速度最高提升3个数量级，泛化到未见过的身份时仍保留绝大部分渲染质量，移动端运行帧率可达60fps
