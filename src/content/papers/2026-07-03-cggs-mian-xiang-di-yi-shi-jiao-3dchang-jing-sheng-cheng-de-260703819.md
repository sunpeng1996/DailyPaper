---
title: 'CGGS: Consistency-Augmented Geometric Gaussian Splatting for Ego-centric 3D
  Scene Generation'
title_zh: CGGS：面向第一视角3D场景生成的一致性增强几何高斯溅射方法
authors:
- Zhenyu Sun
- Xiaohan Zhang
- Qi Liu
- Huan Wang
arxiv_id: '2607.03819'
url: https://arxiv.org/abs/2607.03819
pdf_url: https://arxiv.org/pdf/2607.03819
published: '2026-07-03'
collected: '2026-07-08'
category: Other
direction: 文本驱动3D场景生成 · 高斯溅射优化
tags:
- 3D Gaussian Splatting
- Text-to-3D
- Ego-centric Generation
- Diffusion Model
- Depth Estimation
one_liner: 提出一致性增强的文本转第一视角3D场景生成框架，解决视角不一致与几何畸变问题
practical_value: '- 电商AR/VR虚拟卖场搭建可复用多视角一致性损失设计，提升场景不同视角下的视觉连贯性

  - 3D商品建模流程可借鉴光流+点迹对应估计深度的方案，低成本从多视角2D商品图生成粗点云

  - 3D高斯重建阶段的互信息深度损失+分层优化策略可直接复用，降低3D模型几何畸变'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
第一视角3D场景生成存在视角重叠少、单视角主导场景理解的问题，导致生成内容视角一致性差、语义对齐度低、几何结构不准确，无法满足AR/VR等场景的落地要求。
### 方法关键点
1. 设计第一视角生成器，对多视角潜扩散模型做微调，加入一致性增强损失，生成对齐文本描述的高保真一致2D内容
2. 布局装饰器利用光流与点迹对应关系估计深度，从第一视角2D先验生成稠密点云作为粗布局
3. 几何优化器引入基于熵的互信息深度损失（MID），结合分层优化策略增强3D高斯重建效果，提升视觉质量与几何结构准确性
### 关键结果
在文本驱动第一视角3D场景生成任务上，CGGS的生成连贯性、结构准确性、语义对齐度均优于现有SOTA方法
