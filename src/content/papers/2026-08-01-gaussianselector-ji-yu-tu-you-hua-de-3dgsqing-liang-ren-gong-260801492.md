---
title: 'GaussianSelector: Lightweight Human-Guided Object Selection in 3D Gaussian
  Splatting with Graph Optimization'
title_zh: GaussianSelector：基于图优化的3DGS轻量人工引导物体选择框架
authors:
- Baihan Yang
- Tiexin Li
- Yuheng Liu
- Xin Lin
- Xinke Li
- Xiaohui Xie
- Truong Nguyen
affiliations:
- UC San Diego
- City University of Hong Kong
- UC Irvine
arxiv_id: '2608.01492'
url: https://arxiv.org/abs/2608.01492
pdf_url: https://arxiv.org/pdf/2608.01492
published: '2026-08-01'
collected: '2026-08-07'
category: Other
direction: 3D场景交互 · 3DGS物体选择
tags:
- 3D Gaussian Splatting
- Graph Optimization
- Interactive Segmentation
- Training-free
- 3D Object Selection
one_liner: 提出免训练3DGS交互式物体选择框架，仅需稀疏视图与少量用户涂鸦即可实现低开销高精度3D物体提取
practical_value: '- 电商3D商品素材生产环节可复用该框架，仅需少量人工标注即可从3D重建场景中快速提取完整3D商品资产，降低素材制作成本

  - 虚拟导购/AR互动场景的3D交互功能可借鉴其稀疏涂鸦+图优化的免训练交互范式，降低用户操作成本与端侧计算开销

  - 需批量生产3D商品库的业务可参考其少视图、低算力要求的设计，适配普通消费级设备的3D素材处理需求'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有3DGS场景物体选择方法要么需重训高斯表征嵌入物体标签，要么依赖密集多视图SAM观测，算力要求高、需密集视角覆盖，落地难度大。

### 方法关键点
1. 免训练直接基于原生高斯基元运行，将密集高斯粗聚类为几何一致的超点，融合外观与空间特征构建连续性加权图
2. 稀疏用户涂鸦通过可见性感知的透射率覆盖映射到3D空间，将选择问题转化为全局图割能量最小化问题，传播稀疏标注得到完整3D物体
3. 天然支持多轮迭代优化，用户可在额外视角补充标注逐步提升选择效果

### 关键结果
效果与SOTA多视图SAM基方法相当，所需交互视图数量显著减少，计算开销大幅降低，适配真实部署场景的人在回路3D场景编辑与3D资产提取需求
