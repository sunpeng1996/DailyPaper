---
title: 'SVF-CR: Synchronized Visual-Facial Cross-Refinement for Multimodal Ambivalence
  and Hesitancy Recognition'
title_zh: SVF-CR：面向多模态矛盾犹豫识别的同步视觉-面部交叉优化框架
authors:
- Hyein Park
- Namho Kim
- Junhwa Kim
affiliations:
- Konyang University
- Korean Broadcasting System (KBS)
arxiv_id: '2607.09417'
url: https://arxiv.org/abs/2607.09417
pdf_url: https://arxiv.org/pdf/2607.09417
published: '2026-07-10'
collected: '2026-07-14'
category: Multimodal
direction: 多模态行为识别 · 跨模态交叉注意力融合
tags:
- Multimodal Fusion
- Cross-Attention
- Behavior Recognition
- Visual Feature
- Facial Feature
one_liner: 提出同步视觉-面部交叉优化框架，通过多模态证据融合提升矛盾犹豫行为识别效果
practical_value: '- 直播电商用户下单犹豫/主播专业度识别场景，可复用同步时序切分的全局视觉+局部面部特征双向交叉注意力优化方案，提升细粒度行为识别准确率

  - 多模态特征融合场景下，可借鉴先做局部跨模态特征增强、再做全局多模态证据配对融合的两阶段架构，降低特征噪声干扰

  - 跨模态特征建模时，可新增一致性与差异度建模模块，挖掘不同模态信息的互补价值，提升分类/识别任务效果'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
矛盾与犹豫是融合了语言、面部、视觉、声学信号的细粒度行为状态，现有识别方法未有效建模时序对齐的跨模态信号交互关系，单模态表征利用率低。

### 方法关键点
1. 按相同时序窗口切分提取全局视频段token与局部面部段token，通过模态内自注意力+双向视觉-面部交叉注意力实现两类特征互优化
2. 基于一致性与差异度建模构建段级视觉-面部证据，经时序自注意力与注意力池化增强
3. 文本、声学特征经轻量上下文自注意力优化后，在最终决策层与增强后的视觉-面部证据做配对融合

### 关键结果
在BAH公开数据集上macro-F1达0.7156，优于全局视觉-面部token融合、同步证据两类基线方案。
