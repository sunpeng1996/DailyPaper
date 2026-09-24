---
title: 'DeltaS: Reading the Gated Linear Attention State for KV Cache Eviction in
  Streaming Video'
title_zh: DeltaS：基于门控线性注意力状态的流式视频KV缓存淘汰方法
authors:
- Taeyoun Kwon
- Seungjin Kim
- Hyeonyu Kim
- Moon Hwan Kim
affiliations:
- Maum AI Inc.
- Seoul National University
- Yonsei University
arxiv_id: '2609.27470'
url: https://arxiv.org/abs/2609.27470
pdf_url: https://arxiv.org/pdf/2609.27470
published: '2026-09-23'
collected: '2026-09-24'
category: LLM
direction: LLM推理优化 · KV缓存淘汰
tags:
- KV Cache
- Linear Attention
- Streaming Video
- Multimodal LLM
- Inference Optimization
one_liner: 提出无Query依赖、免训练的DeltaS方法，利用线性注意力状态漂移实现流式视频KV缓存高效淘汰
practical_value: '- 电商短视频理解、直播内容分析等长流式多模态处理场景，可直接复用DeltaS的KV缓存淘汰策略，在有限显存下支持更长输入，无需额外训练

  - 混合线性+全注意力架构的LLM推理优化，可借鉴「复用线性注意力状态变化作为新信息度量信号」的思路，比传统淘汰方案计算开销更低

  - Agent流式感知模块可参考该无Query预淘汰思路，在用户请求到达前提前过滤冗余信息，降低端到端响应延迟'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
混合线性+全注意力的多模态大模型处理流式视频时，全注意力层KV缓存随输入持续膨胀，受限显存下必须做淘汰；且流式场景下Query未提前到达，现有基于位置/注意力/KV表征的淘汰方法要么效果差要么额外计算开销高。
### 方法关键点
利用门控delta线性注意力的循环状态更新特性：状态变化量直接对应输入片段的新信息规模，提出无Query依赖、免训练的DeltaS策略，仅保留归一化状态漂移（状态变化量）更大的视频片段。
### 关键结果
信号计算开销仅为前向传播的1.9%；在6个长视频基准上平均比最优无Query限显存基线高2.1个点，最长视频基准上高5.6个点，效果优于位置、注意力、KV表征类淘汰信号。
