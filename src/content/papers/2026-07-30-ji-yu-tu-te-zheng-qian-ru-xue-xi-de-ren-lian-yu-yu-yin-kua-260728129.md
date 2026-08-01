---
title: Face and Voice Cross-modal Association with Learning Convex Feature Embedding
title_zh: 基于凸特征嵌入学习的人脸与语音跨模态关联方法
authors:
- Taewan Kim
- Jiwoo Kang
affiliations:
- Dongduk Women's University
- Sookmyung Women's University
arxiv_id: '2607.28129'
url: https://arxiv.org/abs/2607.28129
pdf_url: https://arxiv.org/pdf/2607.28129
published: '2026-07-30'
collected: '2026-08-01'
category: Multimodal
direction: 跨模态匹配 · 特征嵌入学习
tags:
- cross-modal-embedding
- multimodal-matching
- face-voice-association
- attention-mechanism
- convex-embedding
one_liner: 提出结合跨模态注意力的凸特征嵌入方案，解决人脸语音跨模态关联异质性问题，效果优于SOTA
practical_value: '- 多模态商品检索/召回场景可复用凸特征嵌入思路，约束同一商品的图文音视频特征落在同一凸包内，降低跨模态检索误召回率

  - 跨模态特征融合模块可借鉴「跨模态注意力+凸嵌入」组合方案，缓解不同模态特征异质性带来的正负样本误判问题

  - 直播场景主播身份核验、用户多模态身份认证等需求可直接迁移该方法框架，已在大规模公开数据集验证效果优于现有SOTA'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有跨模态人脸语音关联方法仅关注跨模态判别性，忽略音视频模态间的特征异质性，产生大量误报、漏报，匹配与检索效果受限。
### 方法关键点
1. 学习跨模态特征嵌入时，约束同一主体的人脸、语音特征嵌入到同一个凸包内，让两类特征互相落在对方的特征区间中
2. 结合跨模态注意力机制与凸嵌入技术，通过最小化类间差异降低正负样本误判率
### 关键结果数字
在大规模VoxCeleb数据集的跨模态核验、匹配、检索三类任务上，效果较现有SOTA方法获得显著提升
