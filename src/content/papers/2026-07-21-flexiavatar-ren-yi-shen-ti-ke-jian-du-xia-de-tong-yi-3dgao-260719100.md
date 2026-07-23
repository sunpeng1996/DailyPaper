---
title: 'FlexiAvatar: Unified 3D Gaussian Human Avatars Under Arbitrary Body Visibility'
title_zh: FlexiAvatar：任意身体可见度下的统一3D高斯人体化身
authors:
- Yihalem Yimolal Tiruneh
- Muhammad Salman Ali
- Uyoung Jeong
- Muneeb A. Khan
- MD Khalequzzaman Chowdhury Sayem
- Allanur Bayramgeldiyev
- Binod Bhattarai
- Seungryul Baek
affiliations:
- UNIST (South Korea)
- University of Aberdeen (UK)
- University College London (UK)
- Fogsphere (UK)
arxiv_id: '2607.19100'
url: https://arxiv.org/abs/2607.19100
pdf_url: https://arxiv.org/pdf/2607.19100
published: '2026-07-21'
collected: '2026-07-23'
category: Other
direction: 3D高斯人体重建 · 可见度感知优化
tags:
- 3D Gaussian Splatting
- Human Avatar Reconstruction
- SMPL-X
- Visibility-Aware Optimization
- Diffusion Model
one_liner: 提出仅优化可见区域的统一3D高斯人体重建框架，兼顾更高重建精度与更低运行内存开销
practical_value: '- 电商3D数字人直播、商品3D展示场景可借鉴仅优化可见区域的思路，大幅降低渲染算力开销，适配端侧/轻量设备部署

  - 数字人局部细节补全场景可复用扩散模型生成与观测一致纹理的方案，提升未观测区域（如背部）的纹理一致性与保真度

  - 部分可见场景（如上半身直播、虚拟头像生成）的3D重建可参考分部位残差优化的trick，避免不可见区域引入的重建伪影'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
单目视频重建可驱动3D人体化身是AR/VR、数字内容创作的核心问题，现有方案联合优化所有身体区域，会降低可见区域的重建保真度，同时算力开销较高。
### 方法关键点
1. 可见度感知优化策略：仅对观测到的身体区域做优化，消除未观测肢体带来的伪影；
2. 融合抗遮挡SMPL-X跟踪与分部位残差优化，捕捉高频几何与外观细节；
3. 引入扩散模型生成与观测区域一致的纹理，补全完全不可见区域（如背部）。
### 关键结果
在全身体、上半身、仅头部等多数据集上，PSNR平均比SOTA方法高约3%；部分可见场景下需优化渲染的高斯数量显著减少，运行时与内存开销明显降低。
