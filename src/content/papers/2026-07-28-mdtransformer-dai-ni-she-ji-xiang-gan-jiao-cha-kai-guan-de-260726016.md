---
title: 'MDTransformer: A Hardware-Software Co-Design of Mode-Division Photonic Transformer
  Accelerator with Inverse-Designed Coherent Crossbar'
title_zh: MDTransformer：带逆设计相干交叉开关的模分光子Transformer加速器
authors:
- Solomon Micheal Serunjogi
- Rachmad Vidya Wicaksana Putra
- Ayat Taha
- Muhammad Shafique
- Mahmoud Rasras
arxiv_id: '2607.26016'
url: https://arxiv.org/abs/2607.26016
pdf_url: https://arxiv.org/pdf/2607.26016
published: '2026-07-28'
collected: '2026-07-30'
category: Other
direction: Transformer 光子推理加速软硬件协同设计
tags:
- Photonic Accelerator
- Transformer Inference
- Hardware-Software Co-design
- Low-power Computing
one_liner: 提出软硬件协同设计的模分光子Transformer加速器，大幅降低面积功耗并提升能效
practical_value: '- 可关注光子加速器商业化落地进展，未来可用于降低LLM、推荐大模型在线推理的算力成本

  - 论文验证了sub-4-bit精度推理可满足Transformer效果要求，可在现有推理链路中尝试更低比特量化降本

  - 单波导多模并行的设计思路可迁移到分布式推理的多通道任务拆分，提升单卡推理吞吐'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有光子Transformer加速器（PTA）依赖昂贵多波长光源、大尺寸点积单元，落地效率低、实用性差。
### 方法关键点
1. 软硬件协同设计基于模分光数据流的MDTransformer，通过空间模干涉实现矩阵运算，将逆设计多模耦合器、交叉件、马赫曾德尔IQ调制器集成到紧凑型模分光子张量核（MPTC），直接在光域执行矩阵乘法
2. TE0-TE3共4个导模各作为独立计算通道，单波导实现4倍并行，无需光谱滤波、无自由光谱范围限制
3. 采用相干检测+IQ调制联合编码幅值与相位，支持复数运算覆盖Transformer全操作范围，有效精度达sub-4-bit，模间串扰低于-30dB，兼容1550nm单激光器连续波工作
### 关键结果数字
对比SOTA PTA，在DeiT系列、BERT系列工作负载下，实现40.4%面积缩减、63.6%功耗降低、40.6%能效提升，延迟与SOTA相当
