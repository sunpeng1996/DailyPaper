---
title: 'Beyond Residual Connections: Manifold-Constrained Hyper-Connections for Robust
  Speaker Representation Learning'
title_zh: 超越残差连接：用于鲁棒说话人表征学习的流形约束超连接
authors:
- Zezhong Jin
- Xiaoyu Wang
- Zhe Li
- Chong-Xin Gan
- Zilong Huang
- Man-Wai Mak
- Kong Aik Lee
affiliations:
- The Hong Kong Polytechnic University
- Baidu Inc.
- The University of Hong Kong
arxiv_id: '2608.05549'
url: https://arxiv.org/abs/2608.05549
pdf_url: https://arxiv.org/pdf/2608.05549
published: '2026-08-06'
collected: '2026-08-08'
category: Training
direction: 深度网络训练 · 残差连接优化
tags:
- Residual Connection
- Manifold Constraint
- Sinkhorn-Knopp
- Backbone Optimization
- Representation Learning
one_liner: 提出流形约束超连接mHC，即插即用替换传统残差连接，提升多类骨干网络表征学习性能
practical_value: '- 推荐/多模态模型的残差连接可参考mHC改造思路，引入多流信息混合机制提升表征容量，缓解深层模型梯度消失

  - 跨模态特征融合场景可复用Sinkhorn-Knopp迭代做能量守恒约束，稳定训练过程，减少特征退化

  - 语音交互类Agent的说话人识别模块可直接替换现有骨干的残差连接为mHC，低侵入式提升识别准确率'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
传统残差连接依赖单路径恒等映射，限制了深层网络的信息流动与表征容量，无法满足复杂场景下鲁棒表征学习需求。

### 方法关键点
1. 提出Manifold-Constrained Hyper-Connections (mHC)，将单路径残差重构为多流演化结构，通过双随机矩阵实现跨流信息混合；
2. 引入Sinkhorn-Knopp迭代约束，保障信号强度与特征均值的能量守恒，稳定梯度同时缓解深层网络信号退化；
3. 可即插即用替换各类骨干网络的标准残差连接，无额外结构依赖。

### 关键结果数字
在VoxCeleb1数据集上，替换ECAPA-TDNN、ResNet-34、Res2Net、E-Res2Net四类骨干的残差连接后，所有架构的说话人识别性能均获得一致提升，无性能退化案例。
