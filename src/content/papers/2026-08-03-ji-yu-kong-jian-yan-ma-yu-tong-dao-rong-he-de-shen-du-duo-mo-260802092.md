---
title: Deep Multimodal Fusion Detection through Spatial Mask and Channel Fusion
title_zh: 基于空间掩码与通道融合的深度多模态融合检测
authors:
- Guandi Wang
- Ming Li
- Yunsen Xing
- Junle Liu
affiliations:
- KTH Royal Institute of Technology
- University of Maryland, College Park
arxiv_id: '2608.02092'
url: https://arxiv.org/abs/2608.02092
pdf_url: https://arxiv.org/pdf/2608.02092
published: '2026-08-03'
collected: '2026-08-07'
category: Other
direction: 跨模态目标检测 · 多模态特征融合
tags:
- Multimodal Fusion
- Object Detection
- Spatial Attention
- Channel Fusion
- Cross-Modality Learning
one_liner: 提出注意力驱动的互补重采样框架，解决跨模态检测单模态过拟合问题，性能达SOTA水平
practical_value: '- 多模态推荐场景可借鉴语义掩码交换训练策略，避免模型过度依赖文本/图像任一单模态特征，提升泛化性

  - 可学习通道竞争机制可迁移到多模态召回/排序层的特征聚合，替代固定的concat/加权求和策略

  - 共享通道空间注意力模块可复用在多模态特征对齐环节，降低跨模态特征融合的计算开销'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有双骨干架构的跨模态特征级融合方法仅对双模态加权后映射到统一表征空间，易出现单模态统计特性过拟合/过适配问题，限制跨模态检测的鲁棒性。
### 方法关键点
基于共享通道空间注意力机制搭建框架，训练阶段引入语义掩码交换主动混合模态边界，强制骨干网络学习不依赖固定模态标签的通用特征；设计可学习通道竞争机制，按通道维度自适应采样、聚合多模态特征，替代固定加权融合逻辑。
### 关键结果
在多个公开跨模态目标检测数据集上性能优于现有SOTA方案，相关源码已开源。
