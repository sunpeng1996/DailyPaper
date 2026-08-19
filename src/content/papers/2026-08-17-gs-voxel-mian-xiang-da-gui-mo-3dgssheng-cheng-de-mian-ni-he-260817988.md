---
title: 'GS-Voxel: Fitting-Free Structured Latents for Large-Scale 3DGS Generation'
title_zh: GS-Voxel：面向大规模3DGS生成的免拟合结构化隐空间框架
authors:
- Ming Qian
- Zijian Wang
- Minchao Sun
- Jincheng Xiong
- Hang Zhang
- Mu Xu
- Chi Wang
- Baoquan Chen
affiliations:
- Amap, Alibaba
- Zhejiang University
- Peking University
arxiv_id: '2608.17988'
url: https://arxiv.org/abs/2608.17988
pdf_url: https://arxiv.org/pdf/2608.17988
published: '2026-08-17'
collected: '2026-08-19'
category: Other
direction: 3D生成 · 3DGS隐空间建模
tags:
- 3DGS
- VAE
- Latent Representation
- Generative AI
- Large-Scale Generation
one_liner: 提出免拟合结构化隐空间框架GS-Voxel，实现大规模航空3DGS场景高效生成
practical_value: '- 若做电商3D商品生成/AR试穿场景，可借鉴免拟合结构化隐空间设计思路，降低3D内容生成的逐样本优化成本

  - 重叠感知分块推理方案可复用在电商线下商圈3D重建/虚拟逛街场景的大区域生成任务

  - 因子化VAE拆分几何与属性编码的思路可迁移至多模态内容生成的特征解耦任务'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有可扩展隐式3D生成器基于结构化张量实现，但预优化3D Gaussian Splatting（3DGS）重建结果无序、空间不规则、基元数量差异大，难以直接适配大规模3D场景生成需求。

### 方法关键点
1. 免拟合转换：无需逐场景额外优化，可将兼容的预优化3DGS重建结果确定性转换为稀疏激活体素，保留选中基元的亚体素位置与渲染属性；
2. 3DGS专属因子化VAE：分别编码体素几何与局部高斯属性为稀疏3D隐向量，隐向量规模随占用体素数量动态增长，不受固定全局基元数量限制；
3. 隐空间内训练图像条件流模型，结合重叠感知分块推理，支持基于卫星图像的超训练裁剪范围的大面积场景生成。

### 关键结果数字
可生成1400m×800m范围的高细节航空3DGS场景，隐空间容量随占用体素数量动态扩展，适配不同规模3D场景需求。
