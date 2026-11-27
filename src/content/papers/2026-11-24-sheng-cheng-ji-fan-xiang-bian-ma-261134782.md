---
title: Generation as Reverse Encoding
title_zh: 生成即反向编码
authors:
- Cheng Shi
- Sibei Yang
- Hanzhong Guo
- Yipeng Qin
- Pietro Lio
- Yizhou Yu
affiliations:
- University of Hong Kong
- Sun Yat-sen University
- Cardiff University
- University of Cambridge
arxiv_id: '2611.34782'
url: https://arxiv.org/abs/2611.34782
pdf_url: https://arxiv.org/pdf/2611.34782
published: '2026-11-24'
collected: '2026-11-27'
category: Multimodal
direction: 多模态生成 · 反向编码框架
tags:
- Multimodal Generation
- DiT
- Reverse Encoding
- Efficient Sampling
- Generative Model
one_liner: 提出基于反向编码原理的RevFlow视觉生成框架，显著降低训练成本、提升采样效率
practical_value: '- 可复用「冻结预训练编码器+分阶段反向生成浅层/深层表征」的思路，优化电商商品图、广告物料的生成效率，降低训练成本

  - 统一主干+分阶段条件注入的HyC-DiT架构可迁移至多模态生成场景，避免多阶段生成需要独立训练多个模型的冗余

  - 语义表征空间原生匹配的少步采样技巧，可用于落地低延迟的实时图像生成需求，比如AI生成商品主图的实时预览场景'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
预训练视觉编码器的抽象表征虽能加速生成学习，但表征转像素的解码路径独立训练成本高、Decoder参数负担重，未复用编码器已学习的像素到语义的映射关系。

### 方法关键点
1. 提出RevFlow框架，遵循生成即反向编码原理，以冻结编码器的中间表征为逐阶段生成目标，先生成深层语义表征，再生成带外观空间细节的浅层表征，最终解码为像素
2. 设计HyC-DiT统一生成模型，跨阶段共享标准DiT主干，仅注入阶段特定条件，无需为每个阶段训练独立生成器
3. 引入语义表征空间原生匹配机制，实现少步生成

### 关键结果
- ImageNet 256×256任务上仅训练5轮，690M参数版本FID达1.96，1.55B参数版本FID达1.74
- 89M小解码器实现30.25dB重建PSNR
- 短时间原生匹配适配后，RevFlow-XL每阶段仅需1次采样，总FID达2.85
