---
title: 'ATSplat: Compact Feed-forward 3D Gaussian Splatting with Adaptive Token Expansion'
title_zh: ATSplat：带自适应Token扩展的紧凑前馈3D高斯溅射框架
authors:
- Cho In
- Jeonghwan Cho
- Mijin Yoo
- Gim Hee Lee
- Seon Joo Kim
affiliations:
- Yonsei University, South Korea
- National University of Singapore, Singapore
arxiv_id: '2607.20417'
url: https://arxiv.org/abs/2607.20417
pdf_url: https://arxiv.org/pdf/2607.20417
published: '2026-07-21'
collected: '2026-07-24'
category: Other
direction: 3D内容生成 · 3D高斯溅射性能优化
tags:
- 3D Gaussian Splatting
- Novel View Synthesis
- Adaptive Token
- Feed-forward Network
- Efficient Rendering
one_liner: 通过自适应3D Token实现前馈3D高斯溅射容量按需分配，降本同时保持SOTA渲染性能
practical_value: '- 电商3D商品建模场景可复用自适应Token扩容逻辑：先构建稀疏3D锚点，仅对纹理、褶皱等细节丰富区域动态提升建模精度，平衡渲染质量和存储成本

  - 多视图3D重建管线可参考像素网格解耦设计：通过可学习3D偏移生成本地高斯基元，摆脱输入图像分辨率对重建精度的约束，降低高分辨率输入下的冗余计算

  - AR实时场景渲染需求下可复用其性能优化方案：单GPU秒级重建+千FPS渲染的能力可支撑移动端AR商品预览、虚拟试穿等低延迟交互场景'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有前馈3D Gaussian Splatting（3DGS）采用像素对齐架构，高斯基元的数量和位置受输入图像分辨率、视角约束而非场景复杂度，生成大量冗余高斯，存储和渲染成本高。

### 方法关键点
1. 先将粗粒度patch级深度和相机特征升维为稀疏3D锚点Token，构建场景紧凑骨架；
2. 每个Token通过可学习3D偏移回归为本地高斯，解耦基元位置与输入图像网格；
3. 新增Adaptive Token Expansion模块，用渲染误差图监督预测Token级不确定性，仅对高不确定性Token扩容，把算力集中在难重建区域。

### 关键结果
在RealEstate10K、DL3DV数据集上达到SOTA渲染质量，相比稠密前馈3DGS方法高斯数量减少5.7×以上；单商用GPU上输入12张512×960图像可1秒内完成重建，仅用311K高斯即可实现1136 FPS的512×960新视角渲染。
