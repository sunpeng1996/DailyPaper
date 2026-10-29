---
title: Repurposing Video Diffusion Transformers for Cross-View Temporal Object Correspondence
title_zh: 复用视频扩散Transformer实现跨视角时序物体匹配
authors:
- Siyoon Jin
- Dahyun Chung
- Honggyu An
- Sangbeom Lim
- Wonjin Nam
- Jaewoo Jung
- WonJun Moon
- Seungryong Kim
affiliations:
- KAIST AI
- Korea University
arxiv_id: '2610.37633'
url: https://arxiv.org/abs/2610.37633
pdf_url: https://arxiv.org/pdf/2610.37633
published: '2026-10-27'
collected: '2026-10-29'
category: Other
direction: 跨视角时序物体匹配 · 视频DiT复用
tags:
- Video DiT
- Object Correspondence
- Multi-View Perception
- Temporal Tracking
- Diffusion Model
one_liner: 提出XTrack框架复用预训练视频DiT，实现鲁棒跨视角时序物体身份匹配与跟踪
practical_value: '- 复用预训练大模型做下游任务时，可借鉴focal注意力对齐、难负例构造、局部上下文裁剪的优化思路，解决预训练先验与下游任务不适配问题

  - 标注资源不足的视频类任务，可复用稀疏标注转稠密伪标签的Pipeline，大幅降低标注成本

  - 电商直播多视角商品跟踪、短内容同款商品跨镜头匹配场景可直接适配XTrack框架做ID对齐'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有跨视角物体匹配方法多依赖逐帧匹配或序列跟踪逻辑，在物体外观变化、遮挡等场景下容易出现匹配误差传播，无法同时保障跨视角、时序两个维度的物体ID一致性。
### 方法关键点
1. 提出XTrack统一框架，复用带语义与时序先验的预训练视频DiT实现RGB到掩码的隐空间传输，联合建模跨视角匹配与时序跟踪两类任务
2. 针对原生视频DiT跨视角落地不准、易匹配语义相似但错误物体的缺陷，引入focal跨视角注意力对齐、难负例约束、局部上下文裁剪三类优化策略
3. 设计伪标签构造Pipeline，将Ego-Exo4D数据集的稀疏标注转换为稠密监督，解决视频级训练标注不足的痛点
### 关键结果
在跨视角时序物体匹配任务上实现SOTA效果，具备优异的时序一致性与物体身份保留能力
