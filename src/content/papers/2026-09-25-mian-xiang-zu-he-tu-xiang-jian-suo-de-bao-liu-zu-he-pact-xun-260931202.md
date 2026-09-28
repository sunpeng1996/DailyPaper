---
title: Preserve-and-Compose Training for Composed Image Retrieval
title_zh: 面向组合图像检索的保留-组合（PACT）训练方法
authors:
- Sehyun Kwon
affiliations:
- Hanyang University ERICA
arxiv_id: '2609.31202'
url: https://arxiv.org/abs/2609.31202
pdf_url: https://arxiv.org/pdf/2609.31202
published: '2026-09-25'
collected: '2026-09-28'
category: Multimodal
direction: 多模态组合图像检索 · 零样本训练优化
tags:
- Composed-Image-Retrieval
- Zero-Shot-Learning
- Multimodal-Retrieval
- Training-Paradigm
- Cross-Modal-Alignment
one_liner: 提出无需目标图像的PACT训练范式与Chord打分策略，提升零样本组合图像检索性能
practical_value: '- 电商定制化以图搜图场景（如「同款红色、更大尺寸」检索需求）可复用PACT的图像-文本-文本三元组训练逻辑，无需采集大量目标图像样本，大幅降低标注成本

  - 多模态检索排序层可直接复用Chord打分策略，同时计算修改指令匹配度与源图核心属性保留度，减少检索结果偏离用户核心需求的问题

  - 零样本CIR落地时可复用冻结预训练多模态backbone加轻量微调的方案，无需更新检索库特征，降低工程迭代成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
组合图像检索（CIR）需结合参考图像+用户修改指令召回匹配目标图像，传统监督方案依赖高成本的源-修改-目标图像三元组标注；现有零样本CIR仅用目标caption做监督，易遗漏源图需保留的核心属性，导致检索结果不符合预期。

### 方法关键点
1. 提出PACT训练范式，仅用图像-文本-文本（ITT）三元组（源图、修改指令、目标caption）训练，无需目标图像，无需更新检索库特征，同时对齐组合查询与目标caption语义、通过源图视觉监督保留核心属性；
2. 提出Chord打分机制，在冻结的预训练图像特征空间内，融合目标相似度得分与源图相对方向一致性得分。

### 关键结果
在4个零样本CIR基准数据集上，跨不同规模backbone、外部检索库均取得SOTA级检索性能。
