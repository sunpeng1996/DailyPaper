---
title: 'PixelDiT2: Representation-Grounded Pixel Diffusion Transformers'
title_zh: PixelDiT2：基于表征锚定的像素空间扩散Transformer模型
authors:
- Yongsheng Yu
- Wei Xiong
- Yichen Sheng
- Shiqiu Liu
- Jiebo Luo
affiliations:
- NVIDIA
- University of Rochester
arxiv_id: '2609.24919'
url: https://arxiv.org/abs/2609.24919
pdf_url: https://arxiv.org/pdf/2609.24919
published: '2026-09-21'
collected: '2026-09-22'
category: Multimodal
direction: 多模态图像生成 · 像素空间扩散优化
tags:
- Diffusion Model
- Transformer
- Multimodal Generation
- Representation Learning
- Vision Foundation Model
one_liner: 引入冻结预训练视觉大模型的分块表征指导，大幅提升像素空间扩散模型的收敛速度与生成质量
practical_value: '- 电商商品图生成场景可复用「表征锚定」思路，用冻结的商品特征提取模型约束扩散生成过程，避免生成图偏离商品实际特征，降低人工审核成本

  - 多模态Agent的图像生成模块可直接复用该架构，无需额外训练VAE，减少端到端推理延迟，适配实时生成需求

  - 收敛速度提升4.25倍的训练优化思路可迁移至多模态生成类下游任务，降低大模型微调的算力成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有像素空间扩散模型虽缩小了与隐空间扩散的画质差距，但收敛速度慢、最终生成质量仍落后，核心原因是需要同时从原始RGB空间学习降噪友好表征和像素生成，缺乏显式表征先验。

### 方法关键点
1. 提出端到端PixelDiT2架构，无需引入自编码器或隐层重构瓶颈，解耦表征学习与像素生成任务；
2. 设计表征锚定机制，全程用冻结的预训练视觉大模型给扩散过程提供显式分块表征指导，让扩散Transformer专注于像素生成任务。

### 关键结果数字
- ImageNet-256×256数据集训练600 epoch后FID达1.46；
- 512×512分辨率下训练680 epoch后FID达1.48，收敛速度是初代PixelDiT的4.25倍，200 epoch即超过PixelDiT训练850 epoch的FID指标。
