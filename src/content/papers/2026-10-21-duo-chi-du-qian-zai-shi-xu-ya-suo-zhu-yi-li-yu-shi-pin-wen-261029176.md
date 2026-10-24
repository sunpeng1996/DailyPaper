---
title: Multi-Scale Latent Temporal Compression Attention and Video-Text Cross Attention
  Fusion for Video Action Detection
title_zh: 多尺度潜在时序压缩注意力与视频文本融合的视频动作检测方法
authors:
- Yicheng Qiu
- Keiji Yanai
affiliations:
- The University of Electro-Communications, Tokyo, Japan
arxiv_id: '2610.29176'
url: https://arxiv.org/abs/2610.29176
pdf_url: https://arxiv.org/pdf/2610.29176
published: '2026-10-21'
collected: '2026-10-24'
category: Multimodal
direction: 多模态理解 · 视频文本跨模态融合
tags:
- Multimodal
- Temporal Attention
- Video-Text Fusion
- Action Detection
- Attention Module
one_liner: 提出多尺度时序压缩注意力与双层级跨模态融合模块，提升视频动作检测性能与泛化能力
practical_value: '- 多尺度潜在压缩注意力可直接复用在短视频推荐的长序列用户行为建模场景，降低时序特征冗余，平衡全局长期兴趣与局部短期兴趣表达

  - 双层级（隐层+标准特征层）交叉注意力融合方案可迁移到短视频/直播带货场景的商品图文、口播文本与视频内容的语义对齐任务，提升内容匹配精度

  - 时序冗余压缩思路可优化长视频内容理解的推理延迟，适合短视频信息流推荐的端侧/云侧特征预处理环节'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
视频动作检测任务需建模连续视频流的时序依赖，现有方案存在帧信息冗余、全局与局部特征平衡困难、视觉与文本特征融合不充分三大痛点，难以精准捕获动态时序模式。
### 方法关键点
1. 多尺度潜在时序压缩注意力模块：在多时序尺度下聚合连续时序序列为统一特征表示，高效消除冗余信息，兼顾全局与局部时序特征表达
2. 视频文本交叉注意力融合模块：同时在隐特征层与标准特征层执行交叉注意力计算，实现视频与文本特征的细粒度融合，强化语义对齐与特征交互
### 关键结果
在多个公开视频识别基准数据集上性能全面优于现有方案，验证了模块的有效性与强泛化能力
