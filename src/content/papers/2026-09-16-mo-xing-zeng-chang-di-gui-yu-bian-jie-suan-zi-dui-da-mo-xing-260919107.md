---
title: How Model Growth, Recursion, and Boundary Operators Influence Scaling Exponents
title_zh: 模型增长、递归与边界算子对大模型预训练缩放指数的影响研究
authors:
- Zixi Chen
- Akshay Vegesna
- Samip Dahal
- Andrew Gordon Wilson
affiliations:
- New York University
- Q Labs
arxiv_id: '2609.19107'
url: https://arxiv.org/abs/2609.19107
pdf_url: https://arxiv.org/pdf/2609.19107
published: '2026-09-16'
collected: '2026-09-17'
category: Training
direction: 大模型预训练 · 缩放定律优化
tags:
- Scaling Law
- Looped Transformer
- Model Growth
- Boundary Operator
- Pre-training
one_liner: 证明架构干预可改变预训练缩放指数，实现随计算规模扩大的复利式效率增益
practical_value: '- 自研业务垂类小模型（如商品理解、用户意图识别LLM）可直接加入边界算子，不增加参数量即可获得约1.25倍预训练效率提升，适配小算力场景

  - 数据受限场景（如垂类电商数据不足需多epoch训练）可使用权重共享的looped transformer，增加递归深度代替扩参，减少过拟合同时获得2.2倍计算效率提升

  - 预训练行业大模型时可采用模型增长策略：训练中期堆叠复制已有Transformer块并解绑权重，实现1.55倍以上的计算效率提升，显著降低训练成本

  - 架构修改后必须单独调优超参数，直接复用原生Transformer的超参会完全掩盖架构带来的效率增益'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
传统认知认为架构干预仅能改变缩放定律的常数项，无法改变核心指数项，而指数项优化能带来随计算规模增长的复利式效率增益；当前大模型训练算力成本高、高质量文本数据稀缺，急需突破缩放效率瓶颈的架构方案。

### 方法关键点
- 基于prelude-core-coda统一框架对比6类Transformer变体：原生Transformer、加边界算子的Transformer、权重共享递归Transformer、解绑权重递归Transformer、带权重共享的增长式模型、解绑权重的增长式模型
- 边界算子设计为：归一化残差流后注入prelude层输出，缓解Transformer深度诅咒问题
- 模型增长策略：训练中期增加core模块迭代次数，权重共享模式直接增加递归次数，解绑模式复制已有core块后独立训练

### 关键结果数字
在FineWeb数据集预训练，对比原生Transformer基线：
- 仅添加边界算子即可在1e20 FLOPs时获得1.25倍计算效率，增益随规模扩大持续上升
- 解绑权重的增长式模型在1e20 FLOPs时效率是基线的1.55倍，7.4B参数版本仅用GPT-3 13B约1/20的计算量即可达到相同CORE指标
- 多epoch数据受限场景下，增加递归深度比直接扩参的计算效率高2.2倍

最值得记住的结论：架构优化不仅能提升固定规模下的效率，还可改变缩放指数获得随规模增长的复利增益，核心是提升单位计算下的模型有效深度。
