---
title: 'PaaF: Raising the perceived quality of INR-Based Image Compression'
title_zh: PaaF：提升基于隐式神经表征(INR)的图像压缩感知质量
authors:
- Lorenzo Catania
- Dario Allegra
affiliations:
- University of Catania
arxiv_id: '2606.21655'
url: https://arxiv.org/abs/2606.21655
pdf_url: https://arxiv.org/pdf/2606.21655
published: '2026-06-19'
collected: '2026-06-27'
category: Multimodal
direction: 多模态 · INR图像压缩优化
tags:
- INR
- Image Compression
- Adaptive Quantization
- Entropy Coding
- Perceptual Quality
one_liner: 提出PaaF INR图像编解码器，通过架构优化、自适应量化、熵编码提升压缩性能与感知质量
practical_value: '- 电商商品图/短视频封面压缩场景可参考PaaF的自适应量化+高效熵编码组合，在不降低视觉感知质量的前提下减小码率，降低CDN成本

  - 可复用INR解码天然支持任意分辨率渲染的特性，实现商品图一次压缩、多端多分辨率适配输出，减少多尺寸素材存储开销

  - 自研业务侧图像编解码器时可参考PaaF的架构设计思路，平衡压缩效率与解码并行性，适配高并发分发场景'
score: 4
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有基于INR的图像压缩方法存在编码耗时长、PSNR等经典质量指标表现远低于成熟编解码器的问题，落地价值受限。
### 方法关键点
1. 优化INR编解码器架构设计，保留解码端简单易并行的原生特性；
2. 引入自适应量化策略，匹配INR参数的分布特性降低信息冗余；
3. 搭配高效熵编码方案进一步压缩码率，提升整体率失真表现。
### 关键结果数字
相比现有纯INR类图像压缩方法，在量化指标（PSNR等）和人眼感知质量上均实现一致提升，大幅缩小了INR压缩方案与成熟传统/学习型编解码器的性能差距。
