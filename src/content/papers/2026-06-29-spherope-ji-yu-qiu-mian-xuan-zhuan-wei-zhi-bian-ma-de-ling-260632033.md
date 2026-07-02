---
title: 'SpheRoPE: Zero-Shot Optimization-Free 360 Panorama Generation with Spherical
  RoPE'
title_zh: SpheRoPE：基于球面旋转位置编码的零样本无优化360全景生成框架
authors:
- Or Hirschorn
- Aaron Olender
- Eli Alshan
- Ianir Ideses
- Lior Fritz
- Sagie Benaim
affiliations:
- Amazon Prime Video
- Tel-Aviv University
- Hebrew University of Jerusalem
arxiv_id: '2606.32033'
url: https://arxiv.org/abs/2606.32033
pdf_url: https://arxiv.org/pdf/2606.32033
published: '2026-06-29'
collected: '2026-07-02'
category: Multimodal
direction: 多模态生成 · 位置编码优化
tags:
- RoPE
- Diffusion Model
- Text-to-Image
- Text-to-Video
- Zero-Shot
one_liner: 替换扩散Transformer标准RoPE为球面RoPE，无需训练优化即可生成满足拓扑约束的360全景图与视频
practical_value: '- 可复用RoPE分通道改造思路：低频通道编码业务领域先验（如电商场景商品类目层级、用户行为时序特征），高频通道强制周期性约束（如活动周期、上新周期），无需全量重训基础模型即可适配垂直场景需求

  - 零样本领域约束注入方法可迁移至生成式推荐场景：无需微调大模型，推理侧通过修改位置编码+定制化CFG引导，即可让通用生成模型输出符合电商商品排布、广告物料规范的生成内容，降低微调成本

  - 跨backbone兼容的改造方案可降低工程落地成本：该改造逻辑不依赖特定模型架构，可快速迁移到不同基座的生成模型，适合业务侧多基座并行迭代的场景'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有360全景生成方案要么依赖稀缺全景数据微调，成本高泛化性差，要么采用多步优化导致推理延迟过高；通用扩散模型原生具备部分全景先验，但无法满足等距柱状投影（ERP）的严格拓扑约束，拼接区域易出现语义畸变。

### 方法关键点
1. 替换扩散Transformer的标准RoPE为球面RoPE：低频通道重参数化为3D笛卡尔坐标，原生编码球面流形特征；高频通道做谐波量化，强制2π周期一致性，满足球面拓扑约束。
2. 搭配语义畸变CFG显式引导几何结构，全程无需训练、优化，可直接适配预训练扩散Transformer基座。

### 关键结果
在Flux.1、Flux.2、LTX-Video等多个主流文生图、文生视频基座上验证，性能比肩需微调/优化的基线方案，同时完整保留原基座的生成能力，支持跨模态360内容生成。
