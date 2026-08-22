---
title: Point-Based 3D Reconstruction from Sparse Views under Known Illumination
title_zh: 已知光照条件下稀疏视角的基于点的3D重建方法
authors:
- Magnus Kaufmann Gjerde
- Joakim Bruslund Haurum
- Jeppe Revall Frisvad
- Markus Worchel
- J. Andreas Bærentzen
- Thomas B. Moeslund
affiliations:
- Aalborg University
- University of Southern Denmark
- Technical University of Denmark
- Technische Universität Berlin
- Pioneer Centre for Artificial Intelligence
arxiv_id: '2608.20000'
url: https://arxiv.org/abs/2608.20000
pdf_url: https://arxiv.org/pdf/2608.20000
published: '2026-08-20'
collected: '2026-08-22'
category: Other
direction: 3D稀疏视角重建 · 可微渲染优化
tags:
- Differentiable Rendering
- Point-based Reconstruction
- Inverse Rendering
- Adjoint Light Transport
- Gaussian Splatting
one_liner: 提出基于带透明度beta surfels的可微点渲染方法，用光传输约束提升稀疏视角3D重建精度并大幅降低基元数量
practical_value: '- 电商商品3D建模场景可借鉴beta surfels轻量表示思路，降低稀疏多角度商品图重建3D模型的存储与渲染成本

  - 可复用带透明度的伴随光传输梯度计算方法，优化商品3D重建的几何精度，降低对商品拍摄角度数量的要求

  - 轻量基元优化思路可迁移至AR试穿/试戴场景的3D商品实时渲染，降低端侧算力开销'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
稀疏视角3D重建现有方案（如Gaussian splatting）依赖十万级以上基元，图像保真度高但几何精度不足，基元数量多也带来较高的存储与渲染开销。

### 方法关键点
1. 提出带透明度的beta surfels作为轻量点基元表示；
2. 设计显式透明度伴随光传输公式，可输出surfel几何与外观参数的梯度，通过物理光传输约束重建过程，无需依赖海量基元即可保证几何精度。

### 关键结果
在10张视角图重建5个合成物体的任务上，相对最强点基线平均对称Chamfer距离降低28.5%；平均仅需267个surfel，基元数量较基线少161倍，同时几何准确率更优、表面补全效果具备竞争力。
