---
title: 'PhotoQuilt: Training-Free Arbitrary-Resolution Photomosaics via Bootstrapped
  Tiled Denoising'
title_zh: PhotoQuilt：基于自举分块去噪的无训练任意分辨率照片马赛克生成框架
authors:
- Koorosh Roohi
- Javad Rajabi
- Andrew Fleet
- Babak Taati
affiliations:
- University of Toronto
- Vector Institute
- Samsung Research
- KITE Research Institute
- Queen's University
arxiv_id: '2606.30968'
url: https://arxiv.org/abs/2606.30968
pdf_url: https://arxiv.org/pdf/2606.30968
published: '2026-06-28'
collected: '2026-07-01'
category: Other
direction: 生成式图像 · 高分辨率分块生成
tags:
- Diffusion Model
- Training-Free
- High-Resolution Generation
- Tiled Denoising
- Photomosaic
one_liner: 提出无需训练的自举分块去噪框架，可生成兼顾全局结构与局部真实感的任意分辨率照片马赛克
practical_value: '- 分块生成+全局先验的思路可迁移到电商大尺寸营销海报/长图生成场景，兼顾整体品牌调性与局部商品细节

  - 无需训练的流程改造思路可复用，基于现有预训练扩散模型仅调整推理逻辑即可落地，大幅降低二次开发成本

  - 分块去噪避免全局attention二次开销的工程技巧，可优化高分辨率生成任务的推理速度与显存占用'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有高分辨率照片马赛克生成计算成本高，扩散模型直接生成易出现全局顺滑无马赛克效果，分块拼接法则丢失全局结构，无法同时满足全局布局一致性与局部tile真实感要求。

### 方法关键点
1. 先低分辨率生成全局构图固定整体布局，避免分块生成的全局结构丢失问题
2. 隐空间上采样后重新注入噪声恢复生成能力，保留局部生成的自由度
3. 固定tile范围内独立去噪，无需全局attention，无二次计算开销，可扩展到任意分辨率

### 关键结果
无需额外训练，在全局结构一致性、局部tile真实感两个维度均优于现有基线方法，可支持任意画布尺寸生成
