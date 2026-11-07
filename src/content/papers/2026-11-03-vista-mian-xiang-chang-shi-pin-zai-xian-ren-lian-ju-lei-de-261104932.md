---
title: 'VISTA: Vision-Language Integrated Semantic Triage Architecture for Online
  Face Clustering in Long Videos'
title_zh: VISTA：面向长视频在线人脸聚类的视语言融合语义分流架构
authors:
- Jiashu Liao
- Joanne Garde-Hansen
- Sanjay Sharma
- Tanaya Guha
affiliations:
- University of Glasgow
- University of Leeds
- The University of Warwick
arxiv_id: '2611.04932'
url: https://arxiv.org/abs/2611.04932
pdf_url: https://arxiv.org/pdf/2611.04932
published: '2026-11-03'
collected: '2026-11-07'
category: Multimodal
direction: 长视频理解 · 多模态在线人脸聚类
tags:
- Face Clustering
- Online Clustering
- Vision Language Models
- Multimodal Learning
- Long Videos
one_liner: 首个视语言融合的长视频在线人脸聚类框架，在VPCD基准上性能优于现有最强无监督在线基线
practical_value: '- 长序列内容/用户行为聚类任务中，可复用「不确定性感知的语义推理+多模态特征融合」思路，解决特征漂移导致的聚类精度下降问题

  - 在线实时聚类场景下，可参考VISTA的语义分流架构，在保证聚类纯度的同时维持长程ID连续性，适配电商直播人脸标签、用户实时兴趣分群等场景

  - 多模态特征融合的轻量落地可借鉴「视觉特征基础匹配+语义特征歧义修正」的两阶段策略，避免全链路多模态推理的算力浪费'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有长视频人脸聚类方案以离线为主，依赖全量数据输入无法适配实时流场景；少量在线方法仅用视觉特征与简单阈值判定，对长视频中人脸光照、姿态、服饰变化的鲁棒性差，聚类精度大幅下降。
### 方法关键点
首个面向长视频在线人脸聚类的视语言融合框架VISTA，采用「视觉特征初筛+不确定性感知语义推理修正」的分流架构，同时保障高聚类纯度与长程身份ID连续性，对长视频中人脸外观变化具备强鲁棒性。
### 关键结果
在含15集影视剧的VPCD基准数据集上，相同检测器、embedding、评估协议配置下，性能全面优于最强在线无监督基线COFC，实现精度与召回的稳健平衡，代码已开源。
