---
title: Let Vision-Language Models Generate Images through Their Representations
title_zh: 基于视觉语言模型自有表征的统一多模态图像生成方法
authors:
- JB Kim
- Byungwoo Jeon
- Kyungmin Lee
- Hyeonmo Kang
- Cheonbok Park
- Shinyoung Joo
- Jinwoo Shin
- Jeonghoon Kim
affiliations:
- NAVER Cloud
- Korea Advanced Institute of Science and Technology
arxiv_id: '2611.31237'
url: https://arxiv.org/abs/2611.31237
pdf_url: https://arxiv.org/pdf/2611.31237
published: '2026-11-22'
collected: '2026-11-26'
category: Multimodal
direction: 多模态大模型 · VLM理解生成能力统一
tags:
- Multimodal-LLM
- Vision-Language-Model
- Image-Generation
- Representation-Sharing
- Parameter-Efficient-FineTuning
one_liner: 构建理解与生成共享的视觉表征空间，将预训练VLM扩展为兼具双能力的统一多模态模型
practical_value: '- 电商商品素材生成场景可复用「共享表征空间」思路，复用预训练VLM的语义理解能力，避免生成图与文本语义 mismatch，收敛速度远高于单独训练生成模型

  - 冻结预训练主干+仅加轻量旁路的架构可直接迁移，Block-wise交互方式可大幅降低多模态任务微调成本，适合中小算力场景落地

  - 分层表征聚合方法可复用在多模态召回的表征对齐环节，提升商品图文表征的语义一致性，优化跨模态召回效果'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有统一多模态模型无法高效融合视觉理解与生成能力，预训练VLM习得的多模态知识难以被生成任务复用，核心瓶颈是理解与生成模块采用异构视觉表征，语义信息无法打通。
### 方法关键点
提出Integral框架：1）Abstraction Fusion模块聚合冻结VLM视觉编码器的分层表征，构造跨理解、生成任务的共享视觉token；2）Block-wise MoT模块引入轻量生成流，仅在VLM块边界与主干交互，无需微调预训练VLM主干。
### 关键结果
对比独立表征空间方案，共享表征方案的生成学习效率提升30%+，生成结果语义余弦相似度提升4pct，同时完整保留预训练VLM的原有理解能力，GenEval指标优于FLUX.1 VAE基线。
