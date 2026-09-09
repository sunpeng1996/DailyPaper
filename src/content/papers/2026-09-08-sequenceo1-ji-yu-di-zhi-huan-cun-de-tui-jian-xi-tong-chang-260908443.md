---
title: 'SequenceO1: End-to-End Ultra-Long (100K) Sequence Modeling in Recommendation
  with Low-Rank Caching'
title_zh: SequenceO1：基于低秩缓存的推荐系统100K超长序列端到端建模
authors:
- Lin Guan
- Jia-Qi Yang
- Zhishan Zhao
- Jiaqi Huang
- Hangyu Wang
- Longbin Li
- Beichuan Zhang
- Haonan Jiang
- Jinan Ni
- Xiangyu Fan
affiliations:
- ByteDance
arxiv_id: '2609.08443'
url: https://arxiv.org/abs/2609.08443
pdf_url: https://arxiv.org/pdf/2609.08443
published: '2026-09-08'
collected: '2026-09-09'
category: RecSys
direction: 推荐系统 · 超长用户行为序列建模
tags:
- Long-sequence Recommendation
- KV cache
- End-to-end Ranking
- Low-rank Compression
- Production System
one_liner: 提出端到端100K用户行为序列建模框架，已全量部署于抖音，性能优于两阶段长序列方案
practical_value: '- 模型设计可直接复用：借鉴Sketch Attention的prototype-wise归一化方案，将超长用户历史压缩为固定大小的target-agnostic
  sketch，替代传统离线聚类的两阶段长序列方案，兼顾长期信号保留与端到端优化能力

  - 工程落地可参考架构：训练与在线服务复用同一套用户sketch KV缓存，配合用户级多请求批处理（MRLB）、pipeline lift（将sketch计算前置与召回阶段并行），大幅降低长序列重复计算开销，适配电商/短视频高并发场景

  - 性能优化可复用trick：参考FlashSA fused kernel设计，避免存储超大的prototype-token亲和度中间矩阵，降低超长序列压缩阶段的HBM占用与计算延迟，满足线上低延迟要求'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前短视频/电商推荐场景单用户历史交互可突破10万条，传统截断方案丢失长期偏好信号，两阶段检索-压缩方案无法端到端优化，直接端到端长序列建模（如STCA）开销随序列长度线性增长，无法满足工业级延迟与吞吐要求。

### 方法关键点
- 模型侧：提出Sketch Attention（SA），采用全局可学习prototype与prototype-wise归一化，将100K用户历史压缩为512~1024长度的固定大小sketch，与候选无关可跨请求、跨候选复用；分双分支推理：最近10K序列用STCA建模时效性信号，压缩sketch用STCA建模长期信号，最后轻量融合
- 系统侧：训练与在线服务复用同一套本地KV缓存存储用户sketch，缓存命中时计算开销与原始序列长度无关（O(1)）；配合MRLB amortize压缩开销，pipeline lift将sketch计算前置与召回并行，FlashSA融合内核减少中间存储提升吞吐

### 关键结果
基于抖音全量生产数据评测，对比基线为生产环境STCA 10K + TWIN V2两阶段方案：离线Finish AUC提升0.29%，Dislike AUC提升1.29%；在线A/B测试抖音主站完播率+2.33%，评论+3.59%，点赞+2.36%，不喜欢率-6.98%；训练FLOPs比直接用STCA做100K序列低49.9×，推理低63.9×，仅损失17%的直接扩序列效果

### 最值得记住的一句话
工业级超长序列建模的核心不是单优化层计算效率，而是通过模型与系统协同设计，让长序列信号可压缩、可缓存、可复用，在效果损失可控的前提下大幅降低端到端开销
