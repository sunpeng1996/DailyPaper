---
title: 'AVTok: 1D Unified Tokenization for Holistic Audio-Video Generation'
title_zh: AVTok：面向全量音视频生成的一维统一Tokenization方法
authors:
- Kien T. Pham
- I Chieh Chen
- Qifeng Chen
- Long Chen
affiliations:
- The Hong Kong University of Science and Technology
arxiv_id: '2606.30811'
url: https://arxiv.org/abs/2606.30811
pdf_url: https://arxiv.org/pdf/2606.30811
published: '2026-06-28'
collected: '2026-07-01'
category: Multimodal
direction: 多模态生成 · 音视频统一Tokenization
tags:
- Tokenizer
- Multimodal Generation
- Unified Codebook
- Audio-Video Generation
- Transformer
one_liner: 提出共享编解码、统一码本的音视频1D Tokenizer AVTok，实现跨模态高效对齐并降低训练成本
practical_value: '- 电商多模态商品素材生成场景可复用「共享编解码+模态专属可学习查询」架构，降低图文/音视频多模态素材生成的训练与推理成本

  - 跨模态内容对齐任务可借鉴分层训练策略，渐进式完成不同模态的重建能力学习，解决模态信息不平衡导致的对齐效果差问题

  - 统一码本设计可迁移至多模态商品召回系统，将图文/音视频商品映射至同一向量空间，提升跨模态检索召回准确率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有音视频生成方案多采用双分支独立Tokenization设计，存在模态表征gap，且训练算力开销极高，缺乏统一的跨模态Tokenization方案支撑全链路音视频生成。
### 方法关键点
1. 架构上采用双流Transformer结构，共享编解码层、搭配模态专属可学习查询，可将音视频对编码为带统一码本的1D紧凑隐层表示
2. 训练侧设计分层训练策略，渐进式实现不同模态的重建能力，解决模态间信息不平衡阻碍跨模态信息对齐的问题
### 关键结果
音视频重建效果优于单模态SOTA Tokenizer，可直接嵌入下游生成pipeline，支持音频转视频、视频转音频、类别条件联合音视频生成三类下游任务
