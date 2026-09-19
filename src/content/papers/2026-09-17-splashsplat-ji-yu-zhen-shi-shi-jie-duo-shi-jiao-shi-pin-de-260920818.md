---
title: 'SplashSplat: Reconstructing Splashing Liquids from Real-World Multi-View Videos'
title_zh: SplashSplat：基于真实世界多视角视频的飞溅液体重建
authors:
- Peiyu Liu
- Dingxi Zhang
- Federico Tombari
- Marc Pollefeys
- Christina Tsalicoglou
- Daniel Barath
affiliations:
- EPFL
- ETH
- Google
- Microsoft
arxiv_id: '2609.20818'
url: https://arxiv.org/abs/2609.20818
pdf_url: https://arxiv.org/pdf/2609.20818
published: '2026-09-17'
collected: '2026-09-19'
category: Other
direction: 三维重建 · 动态流体高斯溅射
tags:
- 3D Reconstruction
- Gaussian Splatting
- Fluid Simulation
- Multi-view Dataset
- Dynamic Reconstruction
one_liner: 发布首个真实多视角飞溅液体基准，提出物理约束高斯溅射方法实现低开销高精度流体重建
practical_value: '- 涉及AR电商交互（如酒水、美妆液体特效展示）的业务，可借鉴物理约束+观测校正的动态高斯生成逻辑，大幅降低实时渲染开销

  - 多模态商品内容生成需制作动态流体特效时，可复用SDF+拉格朗日载体的时序对齐方法，避免逐帧重优化

  - 业务不涉及3D流体特效的搜索推荐/Agent从业者无直接可借鉴价值'
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有动态3D重建研究多聚焦烟雾、合成液体或缓变表面，尚无公开同步多视角真实飞溅液体数据集，高速无纹理飞溅液体重建存在精度低、训练开销高的痛点。
### 方法关键点
1. 发布包含20个真实飞溅场景的基准数据集，由7台同步校准4K相机以60fps采集，附带人工优化的液体/容器掩膜与固定评估拆分；
2. 提出SplashSplat框架，仅在观测可约束区域施加物理结构：多视角掩膜融合得到逐帧液体SDF作为几何基础，连续SDF的水平集传输生成粗速度场，沿流场平流的拉格朗日载体结合新观测校正、丢失覆盖时重播种，解码局部Gaussian实现可微渲染。
### 关键结果
在真实采集数据与合成基准上优于SOTA动态Gaussian splatting方法，运动物理合理性更高，训练成本更低，无需重优化即可支持时序插帧与风格迁移。
