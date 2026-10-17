---
title: 'AdaFrame: Hierarchical Multimodal Deduplication with Adaptive Information
  Budgeting for Cost-Efficient Video Advertisement Analysis'
title_zh: AdaFrame：面向低成本视频广告分析的自适应分层多模态去重方法
authors:
- Abdul Basit Tonmoy
- Arman Luthra
- Guang Lin
- Qixin Deng
affiliations:
- Wabash College
- Purdue University
arxiv_id: '2610.19127'
url: https://arxiv.org/abs/2610.19127
pdf_url: https://arxiv.org/pdf/2610.19127
published: '2026-10-13'
collected: '2026-10-17'
category: Multimodal
direction: 多模态广告分析 · 推理成本优化
tags:
- VLM
- Video Deduplication
- Advertisement Analysis
- Cost Optimization
- Frame Selection
one_liner: 提出分层自适应帧去重方案AdaFrame，大幅降低VLM视频广告分析成本同时提升提取精度
practical_value: '- 电商短视频广告/素材的标签萃取、合规审核场景，可直接复用三级轻量去重pipeline，在VLM推理前过滤冗余帧，大幅降本

  - 可借鉴Intrinsic Semantic Dimensionality(ISD)方法，通过帧嵌入SVD计算内容语义复杂度，动态分配采样预算，替代固定采样率

  - 落地时可根据业务精度要求调整三级过滤的阈值，在推理成本和准确率之间做tradeoff，实测可降低75%左右VLM推理成本'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
基于VLM的视频广告分析若采用均匀帧采样会引入大量冗余内容，推高推理成本；现有关键帧选择方法面向人类观看优化，无法匹配下游内容提取的精度需求。
### 方法关键点
1. 设计三级渐进式去重流水线：依次通过感知哈希、LPIPS、CLIP语义聚类做低成本冗余帧过滤，避免无效内容进入高开销的跨模态推理环节
2. 提出Intrinsic Semantic Dimensionality(ISD)指标，通过对帧嵌入做SVD计算单视频语义复杂度，自适应分配帧采样预算，无需全局固定采样率
### 关键结果
在Pitt Ads数据集500条视频广告上测试，相比均匀采样：帧数量降低48%，VLM推理成本降低75%；主题准确率达86.0%（+1.6pp），情感准确率达79.4%（+7.5pp）
