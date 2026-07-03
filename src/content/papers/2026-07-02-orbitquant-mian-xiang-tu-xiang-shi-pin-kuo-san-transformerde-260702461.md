---
title: 'OrbitQuant: Data-Agnostic Quantization for Image and Video Diffusion Transformers'
title_zh: OrbitQuant：面向图像视频扩散Transformer的无数据量化方法
authors:
- Donghyun Lee
- Jitesh Chavan
- Duy Nguyen
- Sam Huang
- Liming Jiang
- Priyadarshini Panda
- Timo Mertens
- Saurabh Shukla
affiliations:
- Cantina Labs
- University of Southern California
- University of Illinois Urbana-Champaign
arxiv_id: '2607.02461'
url: https://arxiv.org/abs/2607.02461
pdf_url: https://arxiv.org/pdf/2607.02461
published: '2026-07-02'
collected: '2026-07-03'
category: Training
direction: 多模态生成 · DiT低比特量化
tags:
- PTQ
- Diffusion-Transformer
- Quantization
- Low-bit-Inference
- Multimodal-Generation
one_liner: 提出无需校准数据的DiT无感知量化方案，跨模态通用，低比特下生成效果达SOTA
practical_value: '- 电商AI海报、商品短视频生成场景可直接复用该无数据PTQ方案，无需针对不同商品品类、prompt重新校准，大幅降低DiT类生成模型部署成本

  - 离线量化阶段可参考权重旋转抵消逻辑，仅保留推理侧激活层轻量旋转操作，几乎无额外推理 overhead 即可实现低比特压缩

  - 多模态生成服务（图像/视频素材生成）可复用同一套量化框架，无需分模态调整参数，降低多模态素材生产服务的运维复杂度'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
Diffusion Transformer（DiT）在图像、视频生成领域效果达SOTA，但多步采样+大参量导致推理成本极高；现有PTQ方案存在激活跨时间步、prompt、引导分支偏移问题，需针对每个checkpoint、模态重新校准数据，落地门槛高。
### 方法关键点
1. 提出OrbitQuant无数据权重-激活量化方案，在归一化旋转基下做量化，跳过范围估计步骤
2. 采用随机置换块哈达玛（RPBH）旋转将坐标集中到固定边缘分布，单一Lloyd-Max码本即可覆盖所有时间步、prompt、同维度层
3. 离线将旋转吸收进权重，线性层内部旋转抵消，推理侧仅需保留激活前向旋转操作，无需分模态调参
### 关键结果
在FLUX.1、Z-Image-Turbo、Wan 2.1、CogVideoX等多个主流DiT模型上，多个低比特设置下PTQ效果达SOTA；首次将图像DiT的PTQ推到W2A4精度仍具备可用生成质量。
