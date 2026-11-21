---
title: 'ProtoDiffusion: Token-per-Layer Generative Modeling of Multi-Layer Images'
title_zh: ProtoDiffusion：面向多层图像的逐层Token式生成建模
authors:
- Adrià Ciurana Lanau
- Harleen Hanspal
- Lusine Abrahamyan
- Emilio Tylson Baixauli
- Yu Cao
- Danai Triantafyllidou
- Stefano Zorzi
- Gustavo Zanoni Felipe
- Peter Griger
- Stefan Sietzen
affiliations:
- Canva
- Queen Mary University of London
- Universidade Estadual de Maringá
arxiv_id: '2611.26586'
url: https://arxiv.org/abs/2611.26586
pdf_url: https://arxiv.org/pdf/2611.26586
published: '2026-11-19'
collected: '2026-11-21'
category: Multimodal
direction: 多模态分层图像生成 · 扩散模型优化
tags:
- Diffusion Model
- Latent Representation
- Multimodal Generation
- Text-to-Design
- Image Decomposition
one_liner: 提出ProtoDiffusion框架，用共享原型+每层向量压缩多层图像表征，支持文生/图生分层设计
practical_value: '- 电商海报/活动页自动化生成场景可复用「共享全局原型+每层独立向量」的表征方案，大幅降低分层设计生成的算力开销，生成速度较级联方案高19倍

  - 支持可选布局约束的生成范式可直接迁移到商品素材生成场景，既支持指定元素位置的可控生成，也支持全自动分层生成

  - 原生分层输出可直接支持后续元素编辑、替换，适配电商个性化素材快速迭代、批量调优的需求'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有多层图像生成模型每层采用全画布潜空间网格，表征规模随层数线性增长，算力开销高，分层生成效率低，且难以同时适配可控与全自动生成需求。
### 方法关键点
1. 基于ProtoVAE变分自编码器，将整幅分层设计编码为1个共享空间原型+每层1个候选向量，N层表征仅需HW+N个token，远低于传统方案的NHW规模
2. ProtoDiffusion联合对原型和固定候选槽去噪，支持文本/图像作为生成条件，bounding box可作为可选布局引导，自动判断所需层数与布局
3. 同一架构同时支持图转分层设计、文生分层设计两类任务
### 关键结果
- ProtoVAE层裁剪重建PSNR达40.43dB
- 图转设计任务带框约束下RGB L1为0.040、alpha soft IoU达0.850，接近最优微调基线的0.871
- 文生设计任务FID达66.41，远优于FLUX.2的86.84，文本匹配度0.860，生成速度较同骨干先生成再拆分的级联方案快19.1倍
