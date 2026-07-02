---
title: 'PointSplat: Compact Gaussian Splatting via Human-Centric Prediction'
title_zh: PointSplat：基于以人为中心预测的紧凑高斯溅射3D重建方法
authors:
- Yujie Guo
- Yudong Jin
- Lingteng Qiu
- Zehong Shen
- Zhen Xu
- Jing Zhang
- Xianchao Shen
- Hujun Bao
- Sida Peng
- Xiaowei Zhou
affiliations:
- State Key Lab of CAD&CG, Zhejiang University
- ByteDance
- The Chinese University of Hong Kong, Shenzhen
arxiv_id: '2606.32036'
url: https://arxiv.org/abs/2606.32036
pdf_url: https://arxiv.org/pdf/2606.32036
published: '2026-06-30'
collected: '2026-07-02'
category: Other
direction: 3D人体重建 · 紧凑高斯溅射表示
tags:
- 3D Reconstruction
- Gaussian Splatting
- Human-Centric
- Compact Representation
- Transformer
one_liner: 提出直接在3D空间预测高斯基元的PointSplat方法，实现更紧凑高效的高质量3D人体重建
practical_value: '- 电商AR试穿、3D商品展示业务可参考冗余点剪枝逻辑，降低3D模型的存储与传输带宽成本

  - 多模态2D-3D特征融合模块可复用Point-Image Transformer的架构设计，提升特征对齐效率

  - 实时沉浸式直播类3D内容生成场景，可借鉴单步前向预测高斯属性的端到端管线'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
沉浸式直播、全息通信等实时场景对3D人体重建的高保真、低算力、低传输带宽要求较高，现有视角中心的前馈重建方法会跨视角重复编码相同主体内容，存在严重的视角间冗余，难以兼顾效率与质量。
### 方法关键点
1. 核心思路转为直接在3D空间预测高斯基元，避免跨视角重复编码；
2. 先估计粗几何代理，通过光线投射剪枝冗余点，建立显式2D-3D对应关系；
3. 引入Point-Image Transformer融合外观与几何特征，单步前向即可预测高斯属性，预测范围限定在前景感兴趣区域，大幅减少高斯总量。
### 关键结果
在多数据集上验证，相比基线方法同时实现更高的重建效率与新视角渲染质量，对视角数量、输入图像分辨率变化的鲁棒性显著更强。
