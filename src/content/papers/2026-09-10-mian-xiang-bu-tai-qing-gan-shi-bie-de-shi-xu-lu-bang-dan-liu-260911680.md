---
title: Single-Stream Multi-Feature Fusion with Temporal Robustness for Gait Emotion
  Recognition
title_zh: 面向步态情感识别的时序鲁棒单流多特征融合框架
authors:
- Shirong Lyu
- Silu Quan
- Yixuan Ding
- Chengpeng Wang
affiliations:
- Southwest University
- Wisesoft Inc.
arxiv_id: '2609.11680'
url: https://arxiv.org/abs/2609.11680
pdf_url: https://arxiv.org/pdf/2609.11680
published: '2026-09-10'
collected: '2026-09-14'
category: Other
direction: 步态情感识别 · 时空图卷积优化
tags:
- GCN
- Feature Fusion
- Temporal Robustness
- Skeleton Recognition
- Emotion Recognition
one_liner: 提出具备帧率不敏感特性的单流多特征融合SV-GCN框架，提升异构步态情感数据泛化能力
practical_value: '- 线下智慧零售场景可复用帧无关特征提取思路，基于用户步态判断情绪偏好，优化线下导购、商品推荐策略

  - 处理异构时序用户行为数据时，可借鉴全局掩码引导的有效帧卷积模块，适配不同采样率的浏览/点击序列

  - 小样本标注场景下可复用浅层特征早融合策略，避免多流架构复杂度的同时提升模型泛化能力'
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
3D skeleton-based步态情感识别存在标注成本高、数据稀缺问题，现有模型对异构数据泛化性差，多流架构复杂度高，且对帧率、序列长度波动敏感。
### 方法关键点
1. 单流多特征融合SV-GCN框架引入帧内相对运动特征消除帧率敏感性，浅层嵌入异构特征实现早融合，无多流架构额外开销
2. 全局掩码引导的有效帧时空图卷积模块，首次在该领域实现帧率不敏感，原生支持可变长序列输入
### 关键结果
在E-Gait数据集上性能比肩SOTA，跨不同序列长度、帧率的泛化表现显著优于基线，可直接在大规模骨架动作识别数据集上预训练。
