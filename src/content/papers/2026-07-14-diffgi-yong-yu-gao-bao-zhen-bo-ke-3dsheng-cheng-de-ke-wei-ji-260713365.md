---
title: 'DiffGI: Differentiable Geometry Images for High-Fidelity Thin-Shell 3D Generation'
title_zh: DiffGI：用于高保真薄壳3D生成的可微分几何图像
authors:
- Eungjune Shim
- Hansol Lee
- Eunjung Ju
affiliations:
- CLO Virtual Fashion Inc., South Korea
arxiv_id: '2607.13365'
url: https://arxiv.org/abs/2607.13365
pdf_url: https://arxiv.org/pdf/2607.13365
published: '2026-07-14'
collected: '2026-07-22'
category: Other
direction: 3D生成 · 可微分表示学习
tags:
- 3D Generation
- Differentiable Rendering
- Latent Diffusion
- TSDF
- VAE
one_liner: 提出可微分几何图像框架DiffGI，实现低算力开销的高保真薄壳3D生成
practical_value: '- 电商虚拟服饰3D建模/虚拟试穿业务可复用连续TSDF表示，降低薄布料重建的楼梯伪影，提升边界精度

  - 3D内容生成场景可借鉴可微分Marching Squares设计，将3D重建损失端到端传导到2D latent空间，简化训练pipeline

  - 3D商品生成落地可复用32×32超紧凑latent空间设计，大幅降低生成模型的推理、训练算力开销'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有3D生成模型多依赖隐式体积表示，强制watertight拓扑，难以表达服饰这类薄壳非流形几何；几何图像类方案用离散二值占用图，存在分辨率依赖的楼梯伪影、下采样信息损失，且表面重建为不可微后处理，与训练pipeline割裂。
### 方法关键点
1. 提出端到端3D转2D映射框架DiffGI，用连续2D TSDF替代二值图，亚像素精度编码边界，消除分辨率相关楼梯伪影；
2. 设计基于解析线性插值的可微分Marching Squares算法，支持3D表面损失梯度回传到2D latent空间；
3. 训练带几何感知法线渲染损失的DiffGI-VAE，将3D表面压缩到32×32超紧凑latent空间，叠加Transformer结构latent diffusion模型实现条件3D生成。
### 关键结果
在服饰、物体数据集上，相比现有几何图像、体素方案，重建保真度、边界精度更优，算力需求显著降低。
