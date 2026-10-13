---
title: 'GroundAnything: Reconciling Parallel Decoding with Precise Visual Grounding
  at Flash Speed'
title_zh: GroundAnything：兼顾并行解码与高精度视觉定位的高速基础模型
authors:
- Qize Yu
- Lianrui Fan
- Bowen Ping
- Xini Ding
- Zetian Song
- Junbo Niu
- Kaixuan Wang
- Tianxing Chen
- Yue Chen
- Minghua He
affiliations:
- XPeng Inc.
- Peking University
- The University of Hong Kong
- University of California, Berkeley
- Princeton University
arxiv_id: '2609.39600'
url: https://arxiv.org/abs/2609.39600
pdf_url: https://arxiv.org/pdf/2609.39600
published: '2026-09-29'
collected: '2026-10-13'
category: Multimodal
direction: 多模态视觉定位 · 并行推理优化
tags:
- Visual Grounding
- Parallel Decoding
- Diffusion Model
- Self-Speculative Decoding
- Multimodal LLM
one_liner: 提出4B参数视觉定位基础模型，通过双向扩散并行解码兼顾高速推理与高精度定位
practical_value: '- 电商多模态搜索/商品图像理解场景可复用自投机解码方案，在实时低延迟要求下获得4.5倍推理提速，精度损失不到1pp，满足业务时延要求

  - 多模态模型训练可借鉴AR转扩散的联合优化范式，无需从头训练扩散模型，大幅降低多模态定位模型的训练成本

  - 低延迟多模态交互Agent的视觉定位模块可直接落地该开源4B模型，精度接近GPT-6 Astra，推理成本远低于闭源大模型'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
自回归（AR）视觉grounding模型串行输出空间预测，引入高额串行延迟，且空间特征不存在天然的左到右生成顺序，原有范式存在逻辑缺陷。

### 方法关键点
将定位任务重构为视觉证据提取，采用双向扩散实现并行分块去噪，训练流程包括：多源数据集+专属数据引擎预训练、AR转扩散的联合目标训练、有监督微调+GRPO强化后调，支持熵引导解码、自投机解码两种推理模式。

### 关键结果数字
- 4B参数AR变体在30个基准上平均精度72.42%，超同规模SOTA，优于GPT-6 Astra的71.35%
- 并行解码版本精度61.75%，领先此前快速度基线LocateAnything的53.32%
- 自投机模式较AR版本提速4.51倍，COCO F1mIoU仅下降0.74pp，适配低延迟实时场景
