---
title: 'AsySplat: Efficient Asymmetric 3D Gaussian Splatting for Long-Sequence Scene
  Modeling'
title_zh: AsySplat：面向长序列场景建模的高效非对称3D高斯溅射方法
authors:
- Yingji Zhong
- Dave Zhenyu Chen
- Fuzhao Ou
- Youyu Chen
- Zhihao Li
- Lanqing Hong
- Dan Xu
affiliations:
- HKUST
- Huawei Noah’s Ark Lab
- CityU
arxiv_id: '2607.10995'
url: https://arxiv.org/abs/2607.10995
pdf_url: https://arxiv.org/pdf/2607.10995
published: '2026-07-12'
collected: '2026-07-18'
category: Other
direction: 3D高斯溅射 · 新视角合成效率优化
tags:
- 3D Gaussian Splatting
- Novel View Synthesis
- Asymmetric Architecture
- Long Sequence Modeling
- Efficient Inference
one_liner: 提出非对称解耦几何与外观建模的3DGS架构，大幅降低长序列新视角合成的计算与参数开销
practical_value: '- 若从事电商3D商品建模、虚拟展厅渲染、多视角商品展示相关业务，可借鉴几何/外观解耦的非对称架构思路，将算力优先分配给难度更高的几何重建任务，用低参数分支处理外观细节，大幅提升渲染效率

  - 若涉及长序列多视角3D内容生成落地，可复用该任务感知的算力分配策略，在保证效果的前提下减少模型参数量，降低训练与推理部署成本

  - 纯搜索推荐/Agent方向无3D内容业务的从业者，该论文无直接可迁移价值'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有泛化性3D Gaussian Splatting（3DGS）模型支撑长序列新视角合成（NVS）时存在大量冗余计算，算力开销高，难以适配高分辨率长序列输入的落地场景。

### 方法关键点
1. 基于两个核心观察设计非对称架构：高质量NVS不需要严格的高精度几何，且外观学习难度远低于几何重建；
2. 解耦几何与外观建模分支：几何分支分配大部分参数处理粗粒度token完成多视图重建，外观分支仅用少量参数处理细粒度token捕捉细节；
3. 两分支通过双向连接交互，互相引导优化各自任务，减少计算冗余，提升参数效率。

### 关键结果
在32视角960P输入场景下，效果对齐传统优化类方法的同时推理速度提升近800倍；参数量与训练/推理开销显著低于现有SOTA泛化模型，零样本性能超越SOTA。
