---
title: Expressivity In Multimodal Contrastive Learning
title_zh: 多模态对比学习的表达能力研究
authors:
- Andrew Stuart
- Florian Wolf
affiliations:
- California Institute of Technology
arxiv_id: '2608.17203'
url: https://arxiv.org/abs/2608.17203
pdf_url: https://arxiv.org/pdf/2608.17203
published: '2026-08-17'
collected: '2026-08-19'
category: Multimodal
direction: 多模态对比学习 · 架构表达能力优化
tags:
- Contrastive Learning
- CLIP
- Multimodal
- Universal Approximation
- Representation Learning
one_liner: 从密度估计视角分析多模态对比学习架构表达边界，提出适配任意模态的通用近似Hadamard-CLIP
practical_value: '- 2模态多模态召回场景（如文本搜图）用原生双塔CLIP即可满足通用近似，无需额外冗余模块，降低训练推理开销

  - 3模态及以上（如文本+图像+商品属性）的多模态召回，可直接复用Hadamard-CLIP结构，仅加1组可学习权重向量就能实现联合分布通用近似，保留预计算embedding的快速检索能力

  - 多模态对比训练loss设计时，避免盲目用全pairwise求和loss，该结构理论上无法拟合任意联合分布，会损失跨模态关联表征精度'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
CLIP类多模态对比学习架构已成为生成、检索等任务的基础组件，但不同架构的理论表达能力边界尚未明确，3模态及以上常用泛化架构的性能缺陷缺乏量化论证。

### 方法关键点
从群体密度估计视角定义架构表达能力为参数化密度集合对模态联合分布的近似能力，分类验证不同结构的表达上限；设计Hadamard-CLIP，在原有编码器顶层新增单组可学习权重向量，全程保留预计算embedding的检索能力。

### 关键结果
- 2模态双塔CLIP为通用近似器，可拟合任意联合分布
- 业界常用的全pairwise求和多模态CLIP无法拟合任意联合分布，仅能匹配成对条件分布
- Hadamard-CLIP支持任意模态数的联合分布通用近似，完全保留CLIP的高速检索特性
