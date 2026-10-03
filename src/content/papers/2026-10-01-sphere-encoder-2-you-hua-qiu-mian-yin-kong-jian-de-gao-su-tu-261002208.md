---
title: Sphere Encoder 2
title_zh: Sphere Encoder 2：优化球面隐空间的高速高画质图像自编码器
authors:
- Kaiyu Yue
- Sean McLeish
- Ruchit Rawal
- Brian Bartoldson
- Menglin Jia
- Tom Goldstein
affiliations:
- University of Maryland
- Lawrence Livermore National Laboratory
- Cornell University
arxiv_id: '2610.02208'
url: https://arxiv.org/abs/2610.02208
pdf_url: https://arxiv.org/pdf/2610.02208
published: '2026-10-01'
collected: '2026-10-03'
category: Other
direction: 球面自编码器 · 高速图像生成优化
tags:
- Autoencoder
- Latent Sphere
- Image Generation
- Low Latency Inference
- High Resolution
one_liner: 针对初代球面自编码器两项缺陷优化，保留高速特性的同时大幅提升图像生成质量
practical_value: '- 可复用球面隐空间均匀分布设计思路，优化电商商品图批量生成的采样效率与输出一致性

  - 针对像素级重建损失导致生成模糊的问题，可迁移到商品主图/营销图生成的损失函数设计中，提升高清细节还原度

  - 单步无CFG生成方案可落地到电商实时图生图（如用户定制商品预览）需求，大幅降低推理延迟'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
初代Sphere Encoder存在两个核心缺陷限制生成质量：1）隐空间随机采样点集中在赤道区域，训练旋转未覆盖该区域，单步生成效果存在明显天花板；2）像素级重建损失引导解码器对多组合理图像取平均，生成结果模糊，缺失高频细节。
### 方法关键点
针对性优化两项缺陷：1）调整训练旋转策略覆盖隐空间赤道采样区域，消除分布gap；2）优化损失函数设计避免平均化输出，保留图像高频细节；全程保留自编码器的轻量架构，无需引入扩散类多步推理逻辑。
### 关键结果
支持ImageNet 512×512分辨率无CFG单步高清生成；256×256分辨率下无筛选生成效果显著优于初代，无需多步迭代即可输出清晰图像，推理延迟与初代持平
