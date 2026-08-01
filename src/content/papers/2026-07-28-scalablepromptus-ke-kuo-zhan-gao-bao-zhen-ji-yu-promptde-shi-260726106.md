---
title: 'ScalablePromptus: Scalable and High-Fidelity Prompt-Based Video Streaming'
title_zh: ScalablePromptus：可扩展高保真基于Prompt的视频流传输
authors:
- Zehao Cao
- Bowei Xu
- Xun Cao
- Zhan Ma
- Hao Chen
affiliations:
- Nanjing University
arxiv_id: '2607.26106'
url: https://arxiv.org/abs/2607.26106
pdf_url: https://arxiv.org/pdf/2607.26106
published: '2026-07-28'
collected: '2026-08-01'
category: Multimodal
direction: 多模态生成 · 低码率视频流传输
tags:
- Prompt Optimization
- Video Reconstruction
- Low-Bitrate Streaming
- Dropout Training
- Generative AI
one_liner: 针对prompt视频流丢包质量崩溃问题，通过排序dropout训练实现任意截断prompt下的稳健视频重构
practical_value: '- 可复用排序dropout训练策略，用于RAG语义向量截断、弱网轻量化prompt传输场景，解决部分信息丢失导致的效果暴跌问题

  - 语义&颜色感知的prompt逆优化方法可迁移到生成式商品短视频的prompt压缩场景，用更小维度保留核心展示信息

  - 球面线性插值补全中间帧的思路可用于电商直播/商品短视频低带宽传输场景，降流量成本同时保持观感'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有基于prompt的视频流方案Promptus传输语义prompt替代像素内容，可实现超低码率通信，但存在两大缺陷：仅用像素级损失优化prompt导致生成质量不佳，网络波动下prompt部分接收会触发灾难性质量崩溃，无法落地。
### 方法关键点
1. 引入语义+颜色感知的prompt逆优化，提升重构视频的语义一致性和色彩准确性；
2. 采用球面线性插值补全中间帧，提升时序连贯性；
3. 核心创新为排序dropout训练策略，生成带优先级的有序prompt表征，接收端无需额外适配即可从任意截断的prompt中重构有效内容。
### 关键结果
稳定网络下相比基准方案有小幅质量提升；丢包/截断场景下，相比基准降低82%~95%的性能衰减，满足实际部署要求。
