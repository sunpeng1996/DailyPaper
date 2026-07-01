---
title: 'RaysUp: Ultra-light Universal Feature Upsampling via Geometry-Aware Ray Representation'
title_zh: RaysUp：基于几何感知射线表征的超轻量通用特征上采样方法
authors:
- Yuchuan Ding
- Linfei Li
- Lin Zhang
- Ying Shen
affiliations:
- School of Computer Science and Technology, Tongji University
arxiv_id: '2606.22749'
url: https://arxiv.org/abs/2606.22749
pdf_url: https://arxiv.org/pdf/2606.22749
published: '2026-06-21'
collected: '2026-07-01'
category: Other
direction: 视觉基础模型 · 特征上采样
tags:
- Vision Foundation Model
- Feature Upsampling
- Cross Attention
- Positional Encoding
- Dense Prediction
one_liner: 提出跨任务、跨视觉基础模型的超轻量几何感知射线域特征上采样框架，精度效率大幅优于现有方案
practical_value: '- 电商多模态推荐中需要对CLIP等VFM输出的低分辨率视觉特征上采样时，可复用RaysUp的轻量架构，在不额外微调VFM的前提下提升细粒度视觉特征质量，降低推理开销

  - 做商品图细粒度识别（比如瑕疵检测、款式属性识别）的CV Agent模块，可引入RayPE的3D几何先验注入方法，提升像素级推理的几何一致性

  - 需要任意分辨率特征输出的多模态生成场景（比如商品图生成、文案配图的特征对齐），可复用Any-Resolution Cross-Attention机制，避免不同分辨率场景下的重复建模'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
预训练视觉基础模型（VFM）的补丁化/池化输出天然为低分辨率，无法满足像素级细粒度推理需求；现有上采样方案要么语义保真度差，要么需针对特定VFM重训、架构冗余，效率和可扩展性不足。

### 方法关键点
将特征重构从2D域提升到几何感知射线域，核心包含4个模块：
1. 空间解耦引导编码器做方向感知引导编码
2. 任意分辨率交叉注意力实现灵活分辨率重构
3. 基于6D Plucker射线坐标的Ray Positional Encoding（RayPE）注入隐式3D几何先验
4. 几何感知邻域注意力模块实现内容自适应聚合，同时保留几何一致性
框架对任务、VFM均无依赖，可生成任意分辨率的高分辨率特征图。

### 关键结果
在多类密集预测任务上达到SOTA，参数量仅为AnyUp的16%，推理速度提升约7倍，精度效率trade-off显著优化。
