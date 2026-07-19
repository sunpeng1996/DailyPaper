---
title: 'Event Stream based Multi-Modal Video Anomaly Detection: A Benchmark Dataset
  and Algorithms'
title_zh: 基于事件流的多模态视频异常检测：基准数据集与算法
authors:
- Peipei Zhu
- Yueqing Niu
- Lin Zhu
- Guanchong Niu
- Yang Yu
- Zheng Li
affiliations:
- Tianjin University of Traditional Chinese Medicine
arxiv_id: '2607.09114'
url: https://arxiv.org/abs/2607.09114
pdf_url: https://arxiv.org/pdf/2607.09114
published: '2026-07-10'
collected: '2026-07-19'
category: Multimodal
direction: 多模态视频异常检测 · 跨模态表征融合
tags:
- Multimodal Learning
- Video Anomaly Detection
- Event Camera
- Contrastive Pre-training
- Feature Fusion
one_liner: 构建大规模可见光-事件流VAD基准数据集，提出跨模态对齐+自适应融合的事件增强VAD框架
practical_value: '- 跨多模态信号的对比预训练对齐思路可复用在多模态推荐表征学习阶段，对齐用户行为、商品图文、评论等不同模态语义

  - 自适应动态融合多模态特征的模块可迁移至多模态召回/排序场景，解决不同场景下各模态信号有效性差异问题

  - 极端场景下补充互补信号的思路可借鉴，可用于暗光/高动态场景下的商品内容识别、直播异常行为检测等业务'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有仅依赖可见光视频的Video Anomaly Detection（VAD）在光照波动、快速运动、复杂背景场景下鲁棒性差，且缺乏真实场景下大规模事件流-可见光多模态VAD基准数据集，限制相关技术落地。
### 方法关键点
1. 构建覆盖多样光照、运动模式、背景复杂度的多模态VAD基准，包含63亿事件、376368帧视频，填补事件驱动VAD的真实场景数据集空白；
2. 设计跨事件流、可见光视频、文本描述的对比预训练框架，通过对齐跨模态语义嵌入学习高区分度事件表征；
3. 引入自适应融合模块，动态整合事件流时序运动线索与视频空间语义，提升环境干扰下的鲁棒性。
### 关键结果
在公开基准及自建TJUTCM Pha数据集上，所提E-VAD框架性能持续优于现有基线方法，验证了事件传感信号在真实场景VAD任务中的有效性。
