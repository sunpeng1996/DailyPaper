---
title: 'Make It Flow: Animating Water in 3D Gaussian Splatting Scenes'
title_zh: 在3D高斯溅射场景中实现流水动画效果
authors:
- Kjell Keune
- Florian Hahlbohm
- Jannis Möller
- Susana Castillo
- Martin Eisemann
- Marcus Magnor
affiliations:
- Computer Graphics Lab, TU Braunschweig, Germany
arxiv_id: '2610.13860'
url: https://arxiv.org/abs/2610.13860
pdf_url: https://arxiv.org/pdf/2610.13860
published: '2026-10-09'
collected: '2026-10-13'
category: Other
direction: 3DGS动态场景 · 流体动画生成
tags:
- 3D Gaussian Splatting
- Optical Flow
- Dynamic Scene Synthesis
- Novel View Synthesis
- Fluid Animation
one_liner: 无需动态采集或物理模拟，为静态3DGS场景生成合理的无缝循环流水动画，保留实时渲染能力
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
3D Gaussian Splatting（3DGS）可实现高质量实时新视图合成，但原生仅支持静态场景，现有动态重建方案无法在 casual 采集条件下生成流水这类高频动态效果，且依赖多视角高速采集或物理模拟，落地成本高。
### 方法关键点
1. 从参考图像或模型渲染结果估计2D光流，升维得到全局一致的3D欧拉运动场；
2. 借鉴cinemagraph算法将运动场作用于高斯基元变形，生成时间连续的无缝循环动画；
3. 全程无需动态采集数据或物理仿真计算，额外开销极低。
### 关键结果
在自建野外瀑布数据集上验证，相比现有动态3DGS、3D cinemagraph方案，视觉质量与计算效率均有明显提升，生成的场景表示完全保留实时渲染性能与自由视角导航能力。
