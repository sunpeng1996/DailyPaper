---
title: 'InfiniSplat: Implicit Gaussian Decoding for Large-Baseline Monocular View
  Synthesis'
title_zh: InfiniSplat：面向大基线单目视图合成的隐式高斯解码方法
authors:
- Jiawei Wang
- Hao Yu
- Yongzhen Hu
- Xinyi Yang
- Tao Ni
- Xin Zhan
- Junbo Chen
- Xiaowei Zhou
- Ruizhen Hu
- Sida Peng
affiliations:
- State Key Laboratory of CAD&CG, Zhejiang University
- Zhejiang University
- Udeer.ai
- Shenzhen University
arxiv_id: '2608.02437'
url: https://arxiv.org/abs/2608.02437
pdf_url: https://arxiv.org/pdf/2608.02437
published: '2026-08-02'
collected: '2026-08-06'
category: Other
direction: 单目3D重建 · 3D高斯溅射优化
tags:
- 3DGS
- Novel View Synthesis
- Implicit Decoding
- Single-image 3D Reconstruction
- Surface-aligned Representation
one_liner: 提出表面对齐的单图像前馈3DGS框架，提升大视角偏移下新视图合成质量
practical_value: '- 电商3D商品建模场景可直接复用该框架，仅用单张商品图即可快速生成可渲染3D资产，大幅降低多视角拍摄与逐场景优化成本

  - 几何引导采样+查询条件隐式解码器的对齐设计思路，可迁移至多模态内容生成任务，提升跨模态表征的一致性

  - 从固定网格对齐到任务相关结构对齐的表征优化逻辑，可用于优化生成式推荐中语义表征的跨场景泛化性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有单图像前馈3D Gaussian Splatting（3DGS）依赖像素对齐表征，高斯从固定图像网格位置预测，与真实场景表面耦合度低，大视角偏移下渲染结构一致性差，且传统方案需多视角采集、逐场景优化，落地成本高。

### 方法关键点
1. 提出表面对齐的单图像前馈3DGS框架InfiniSplat，摆脱固定像素网格约束；
2. 先通过几何引导采样，依据深度诱导的局部表面结构放置2D支撑点；
3. 引入查询条件隐式解码器，基于支撑点位置查询到的图像特征预测高斯属性，减少网格离散化导致的散碎基元。

### 关键结果
多跨数据集新视图合成评估中性能达到SOTA，基于Hypersim室内合成数据训练后可零样本泛化到复杂开放世界场景，大基线视角下渲染质量显著优于现有基线。
