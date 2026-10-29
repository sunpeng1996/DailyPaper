---
title: 'Honeycomb-Surfels: Compact Hexagonal Primitives for Efficient Scene Rendering
  and Reconstruction'
title_zh: 蜂窝表面元：面向高效场景渲染与重建的紧凑六边形基元
authors:
- Prakhar Kaushik
- Soumava Paul
- Alan Yuille
affiliations:
- Johns Hopkins University
arxiv_id: '2610.37668'
url: https://arxiv.org/abs/2610.37668
pdf_url: https://arxiv.org/pdf/2610.37668
published: '2026-10-27'
collected: '2026-10-29'
category: Other
direction: 3D场景渲染重建 · 高效基元设计
tags:
- 3D Reconstruction
- Novel View Synthesis
- Efficient Rendering
- Splatting
- Hexagonal Primitive
one_liner: 提出新型六边形表面元Hexels，大幅提升3D渲染重建、2D表示的质量-效率权衡表现
practical_value: '- 电商3D商品建模、AR试穿/试戴场景可复用Hexels基元设计，在保持渲染画质的前提下降低模型存储开销与推理显存占用，提升端侧渲染帧率

  - 商品高清图压缩场景可借鉴Hexels的「大基元+局部颜色场」设计思路，在相同压缩比下降低图像失真

  - 资源受限的端侧3D交互场景可参考Hexels的帕累托优化逻辑，平衡用户体验与硬件性能要求'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有基于辐射场、splatting的3D渲染与重建方案内存、计算开销过高，无法落地资源受限场景。
### 方法关键点
提出新型平面六边形表面元Hexels，搭配一阶空间颜色场，利用局部平面区域的外观平滑性，以更少更大的基元完成表示；六边形结构兼顾面积与边界效率，局部颜色场可捕捉基元内的外观变化，同时适配3D场景与2D图像表示。
### 关键结果
- 34个场景测试：同内存下PSNR较2DGS提升4.53~7.38dB，训练显存更低；单基元较2DGS PSNR最高高4.74dB，帧率快2.31倍
- 3D重建任务：15组DTU扫描数据同内存下较2DGS误差降低28.9%；6个Tanks and Temples场景平均F1达34.38%，优于2DGS的31.72%
- 2D图像表示效果优于同基元数量的Image-GS，整体推高了表面对齐基元的质量-效率帕累托边界
