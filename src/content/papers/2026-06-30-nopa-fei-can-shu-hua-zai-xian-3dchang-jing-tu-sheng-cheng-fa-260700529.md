---
title: 'NoPA: Non-Parametric Online 3D Scene Graph Generation'
title_zh: NoPA：非参数化在线3D场景图生成方法
authors:
- Qi Xun Yeo
- Seungjun Lee
- Yan Li
- Gim Hee Lee
affiliations:
- National University of Singapore
arxiv_id: '2607.00529'
url: https://arxiv.org/abs/2607.00529
pdf_url: https://arxiv.org/pdf/2607.00529
published: '2026-06-30'
collected: '2026-07-04'
category: Other
direction: 3D场景图生成 · 非参数化表征
tags:
- 3D Scene Graph
- Non-Parametric
- Kernel Density Estimation
- Online Inference
- Embodied AI
one_liner: 提出非参数化物体表征的NoPA框架，兼顾实时性与精度实现高性能在线3D场景图生成
practical_value: '- 布局AR试穿、3D商品建模的电商业务，可借鉴非参数化物体表征方案平衡几何精度与推理时延，降低端侧算力消耗

  - 做家居场景智能推荐、Embodied Agent导购的业务，可复用基于最大平均差异的候选物体合并策略，提升3D场景理解鲁棒性

  - 无3D/AR/机器人相关场景的纯线上搜索推荐业务，可迁移价值较低'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
传统3D场景图生成依赖点云表征计算开销极高，无法满足实时推理要求；近期基于单3D高斯近似物体的方案虽大幅提速，但存在几何细节丢失严重、在线推理时物体候选合并误差高的缺陷。
### 方法关键点
1. 提出NoPA框架，将每个物体表征为独立非参数化分布，在保留3D几何信息的同时维持原参数化高斯方案的实时推理能力
2. 设计定制化物体合并策略，基于核密度估计的最大平均差异实现鲁棒的候选物体合并，每个物体维护固定粒子集控制额外计算开销
3. 新增高亲和度物体间关系传播机制，修正物体误分类导致的关系丢失问题
### 关键结果
实验验证NoPA在不牺牲实时推理速度的前提下，性能显著优于当前SOTA方法
