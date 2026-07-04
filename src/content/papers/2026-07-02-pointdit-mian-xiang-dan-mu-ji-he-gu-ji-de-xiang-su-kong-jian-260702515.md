---
title: 'PointDiT: Pixel-Space Diffusion for Monocular Geometry Estimation'
title_zh: PointDiT：面向单目几何估计的像素空间扩散模型
authors:
- Haofei Xu
- Rundi Wu
- Philipp Henzler
- Nikolai Kalischek
- Michael Oechsle
- Fabian Manhardt
- Marc Pollefeys
- Andreas Geiger
- Federico Tombari
- Michael Niemeyer
affiliations:
- Google
- ETH Zurich
- University of Tübingen
- Microsoft
- Technical University of Munich
arxiv_id: '2607.02515'
url: https://arxiv.org/abs/2607.02515
pdf_url: https://arxiv.org/pdf/2607.02515
published: '2026-07-02'
collected: '2026-07-04'
category: Other
direction: 单目3D重建 · 像素空间扩散Transformer
tags:
- Diffusion Transformer
- 3D Reconstruction
- Vision Transformer
- DINOv3
- Pixel Space Diffusion
one_liner: 基于纯ViT构建极简像素空间扩散Transformer，实现性能超SOTA的单目3D重建
practical_value: '- 电商3D商品库构建场景可复用该思路，仅用单张商品RGB图即可快速生成3D模型，替代传统多视角拍摄建模方案，大幅降低内容生产成本

  - 透明/反光等特殊材质商品的3D建模可参考该方案的鲁棒性设计，提升异形、高歧义商品的几何结构还原精度

  - 涉及AR试穿、AR逛店等3D交互功能的业务可基于该极简架构做轻量化改造，降低端侧推理的部署复杂度

  - 中小团队做3D内容生成时可参考该方案的训练流程，无需复杂的tokenizer与隐空间适配设计，大幅简化训练链路'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有单图像3D重建方案存在两个核心痛点：要么依赖复杂混合架构与定制化损失函数，落地门槛高；要么需将几何信息压缩至隐空间适配预训练隐扩散模型，引入额外编码解码开销。

### 方法关键点
1. 提出极简像素空间Diffusion Transformer架构PointDiT，基于纯ViT搭建，直接对原始3D点图块做运算，省去隐空间压缩步骤
2. 以预训练DINOv3输出的图像token为条件信号，扩散骨干网络完全从零训练，无需额外设计点图tokenizer

### 关键结果
性能超越现有复杂隐空间扩散模型，架构复杂度远低于同类混合方案；输出的几何结构更清晰，对透明物体等高歧义区域的重建鲁棒性显著提升。
