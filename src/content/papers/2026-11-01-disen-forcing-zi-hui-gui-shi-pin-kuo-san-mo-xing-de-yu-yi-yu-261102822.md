---
title: 'Disen-Forcing: Disentangling Semantic Anchoring from Motion for Autoregressive
  Video Diffusion'
title_zh: Disen-Forcing：自回归视频扩散模型的语义锚定与运动解耦
authors:
- Zhengyang Yu
- Akio Hayakawa
- Masato Ishii
- Qingtao Yu
- Xuesong Li
- Takashi Shibuya
- Yuki Mitsufuji
- Jing Zhang
affiliations:
- Australian National University
- Sony AI
- CSIRO
- Sony Group Corporation
arxiv_id: '2611.02822'
url: https://arxiv.org/abs/2611.02822
pdf_url: https://arxiv.org/pdf/2611.02822
published: '2026-11-01'
collected: '2026-11-16'
category: Multimodal
direction: 多模态生成 · 注意力头功能解耦
tags:
- Autoregressive Diffusion
- Attention Head
- Knowledge Distillation
- Video Generation
- Long Context
one_liner: 提出蒸馏插件Disen-Forcing，解耦AR-VDM注意力头分工，平衡长视频一致性与动态性
practical_value: '- 注意力头分功能专用的思路可迁移到LLM4Rec/多模态推荐优化，拆分语义一致性、动态兴趣建模两类头，提升长序列推荐效果

  - 解耦上下文路由方法可复用在长序列推荐的KV cache优化，避免全局上下文强制注入带来的用户兴趣动态性损失

  - 过条件导致的模式坍缩结论可借鉴到生成式推荐蒸馏阶段，针对性调整正则策略，提升生成结果多样性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
自回归视频扩散模型（AR-VDM）生成长视频时，一旦推理时长超过训练时长，性能会因暴露偏差快速衰减；现有基于帧锚定（Frame Sink）的优化方法强制所有注意力头接入初始帧上下文，会导致生成运动动态性坍缩。
### 方法关键点
1. 核心发现：AR-VDM的注意力头天然分工，稀疏子集负责长程语义锚定，多数头负责捕获局部时序动态，并非LLM式的全局注意力锚点机制
2. 提出蒸馏阶段可插拔的Disen-Forcing框架，通过解耦上下文路由、运动解耦正则强化头的专用分工，避免全头过条件问题
### 关键结果
长程视频生成基准上，相比Frame Sink基线，动态度提升20%，30s生成成像质量提升5个百分点，同时兼顾语义一致性与运动动态性，解决了原有方法的 trade-off 问题。
