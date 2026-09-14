---
title: Attention Quantization for Tabular Foundation Models
title_zh: 面向表格基础模型的注意力量化方法
authors:
- Jonas M. Kübler
- Benjamin Jäger
- Klemens Flöge
- Noah Hollmann
- Frank Hutter
affiliations:
- Prior Labs
arxiv_id: '2609.13031'
url: https://arxiv.org/abs/2609.13031
pdf_url: https://arxiv.org/pdf/2609.13031
published: '2026-09-11'
collected: '2026-09-14'
category: Training
direction: 表格基础模型 · 推理效率量化优化
tags:
- Quantization
- Tabular Foundation Model
- FP8
- Attention Optimization
- Triton Kernel
one_liner: 针对表格基础模型提出QKV FP8量化策略，对齐训练测试误差，无精度损失下推理最高提速1.7x
practical_value: '- 电商场景大量使用表格模型做用户标签预测、转化率预估，可直接复用QKV FP8量化策略降低推理延迟，支撑更高QPS

  - 量化时必须对齐训练与测试数据的量化误差避免精度暴跌，该结论可迁移到所有Transformer类推荐模型的量化优化

  - 可直接复用已实现的Triton FP8注意力kernel，替换现有16位kernel，在大batch场景下拿到近1.7倍加速'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
表格基础模型近年在结构化数据场景快速落地，现有Transformer量化方案多针对LLM设计，适配性差，权重/KV cache量化对表格模型收益极低，推理效率优化需求迫切。
### 方法关键点
1. 优化核心聚焦注意力计算而非LLM常用的权重/KV cache量化，将QKV映射为FP8精度，调用原生FP8矩阵乘法指令加速；
2. 核心trick是严格对齐测试样本与训练样本的量化误差，避免精度大幅下降；
3. 基于Triton实现自定义FP8注意力kernel，适配表格模型推理模式。
### 关键结果
相比16位基线kernel，注意力计算速度最高提升1.7x；在TabPFN-v3、TabICLv2上测试，TabArena、BeyondArena基准集精度损失在种子噪声范围内可忽略，BeyondArena全链路评测耗时降低27.6%
