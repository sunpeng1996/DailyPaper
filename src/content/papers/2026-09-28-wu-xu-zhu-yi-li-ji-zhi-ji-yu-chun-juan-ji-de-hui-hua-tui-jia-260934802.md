---
title: 'No Attention, No Problem: Rethinking Session-based Recommendation with Pure
  Convolution'
title_zh: 无需注意力机制：基于纯卷积的会话推荐框架研究
authors:
- Tao Huang
- Wei Zhou
affiliations:
- School of Big Data and Software Engineering, Chongqing University
arxiv_id: '2609.34802'
url: https://arxiv.org/abs/2609.34802
pdf_url: https://arxiv.org/pdf/2609.34802
published: '2026-09-28'
collected: '2026-09-29'
category: RecSys
direction: 会话推荐 · 纯卷积架构优化
tags:
- Session-based Recommendation
- Convolutional Neural Network
- Efficient Recommendation
- Sequential Recommendation
- Effective Receptive Field
one_liner: 提出纯卷积会话推荐框架NextConvRec，性能追平Transformer基线，推理延迟降低16.7%
practical_value: '- 高并发电商推荐场景可将现有Transformer会话推荐模块替换为该纯卷积架构，在维持推荐效果基本不变的前提下降低推理延迟，适配首页猜你喜欢、购物车推荐等大流量场景

  - SPCE预处理模块可直接复用：会话图GCN提取结构信号+可学习位置残差的预训练方案，能提升纯卷积序列模型的全局建模能力，无需依赖注意力

  - 调参经验可直接落地：根据业务会话平均长度搭配大/小卷积核组合，FFN扩张比例选2~4可兼顾效果与推理速度，避免过拟合

  - 低算力边缘端推荐场景可直接迁移该架构，无需部署Transformer即可达到SOTA级效果，降低硬件成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前会话推荐领域Transformer类模型依赖自注意力实现全局建模，但推理延迟高、计算开销大，难以适配电商高并发推荐场景；传统卷积模型虽然效率高，但有效感受域（ERF）有限，全局建模能力弱，效果远低于Transformer，亟需兼顾效果和效率的会话推荐架构。

### 方法关键点
- 纯卷积架构NextConvRec完全弃用自注意力模块，通过优化卷积结构实现效果与效率的平衡
- 前置SPCE编码器：通过GCN层提取会话图、跨会话关联图的结构信号，搭配可学习位置残差模块，为卷积模块注入全局结构与位置信息
- 核心卷积模块：堆叠深度可分离卷积（DWConv+PWConv），通过大卷积核扩大有效感受域，解耦设计ConvFFN分别学习单会话内维度依赖、跨会话关联

### 关键实验
在Beauty、Sports、Toys、Yelp 4个公开会话推荐数据集上，对比SASRec、BERT4Rec、BSARec等SOTA基线：平均HR@20、NDCG@20相对最优基线提升1.73%，单会话平均推理速度提升16.7%，仅需22个epoch即可收敛，训练效率显著优于Transformer类模型。

### 核心结论
在会话推荐场景下，优化后的纯卷积架构完全可以达到Transformer级别的推荐效果，同时具备更优的推理与训练效率，是高并发工业场景的可行替代方案
