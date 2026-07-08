---
title: Tuning-Free Latent Diffusion Models for Ultrahigh-Resolution Image Editing
title_zh: 无需微调的潜扩散模型超高清图像编辑框架
authors:
- Wanglong Lu
- Lingming Su
- Kaijie Shi
- Minglun Gong
- Xiaogang Jin
- Hanli Zhao
- Xianta Jiang
arxiv_id: '2607.06136'
url: https://arxiv.org/abs/2607.06136
pdf_url: https://arxiv.org/pdf/2607.06136
published: '2026-07-07'
collected: '2026-07-08'
category: Multimodal
direction: 多模态生成 · 超高清图像扩散编辑
tags:
- Latent Diffusion Model
- High-resolution Image Editing
- Tuning-free
- Multi-scale Processing
- Denoising
one_liner: 提出无需微调的UltraDiffEdit框架，单RTX 3090显卡即可实现最高8K分辨率图像编辑
practical_value: '- 电商商品图修图场景可直接复用开源UltraDiffEdit框架，无需微调预训练扩散模型即可实现8K级商品图局部编辑，大幅降低训练和算力成本

  - 多尺度渐进编辑+全局-局部一致性去噪思路可迁移到生成式推荐的高分辨率商品图生成场景，解决高分辨率生成时边界模糊、细节丢失问题

  - 分块混合采样策略可优化大尺寸图片生成的显存占用，单消费级GPU即可支撑高分辨率生成需求，降低业务部署门槛'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有扩散模型图像编辑能力受显存、高分辨率训练数据成本限制，最高仅支持1K以下分辨率输入，直接放大低分辨率编辑结果会出现模糊、细节丢失问题，无法匹配移动端8K素材的编辑需求。
### 方法关键点
无需微调预训练LDM的UltraDiffEdit框架核心设计：1）采用多尺度渐进编辑策略，由粗到细迭代融合高分辨率编辑内容与未编辑区域；2）多块编码保留隐空间内编辑/未编辑区域的视觉细节，搭配全局-局部一致性去噪消除编辑边界伪影；3）分块混合采样同时捕获局部、中间、全局特征，保证语义一致性的同时增强生成细节。
### 关键结果
仅需单张NVIDIA RTX 3090显卡即可支持最高8K分辨率图像编辑，编辑质量、细节保留度显著优于现有方案，代码已开源。
