---
title: 'TiRex-2: Generalizing TiRex to Multivariate Data and Streaming'
title_zh: TiRex-2：适配多变量数据与流式场景的时序预测基础模型
authors:
- Patrick Podest
- Marco Pichler
- Elias Bürger
- Levente Zólyomi
- Bernhard Voggenberger
- Wilhelm Berghammer
- Daniel Klotz
- Sebastian Böck
- Günter Klambauer
- Sepp Hochreiter
affiliations:
- JKU Linz, Austria
- NXAI Lab, Linz, Austria
- NXAI GmbH, Linz, Austria
- Interdisciplinary Transformation University Austria, Linz, Austria
arxiv_id: '2607.01204'
url: https://arxiv.org/abs/2607.01204
pdf_url: https://arxiv.org/pdf/2607.01204
published: '2026-07-01'
collected: '2026-07-02'
category: Other
direction: 时序预测 · 流式多变量基础模型
tags:
- Time Series Forecasting
- xLSTM
- Streaming Inference
- Foundation Model
- Multivariate Forecasting
one_liner: 基于xLSTM的时序基础模型TiRex-2，实现流式场景恒定推理成本的多变量预测
practical_value: '- 电商时序类场景（销量预测、流量预测、用户长行为序列预测）可复用其内存中心循环设计，大幅降低长序列预测的算力开销，适配流式实时推理需求

  - 缺乏多变量时序标注数据时，可借鉴其从大规模单变量语料动态合成多变量样本的预训练pipeline，降低数据准备成本

  - 需融合已知未来协变量（营销活动、节假日信息）的预测场景，可复用双向时间混合器+非对称分组注意力变量混合器架构，同时保证目标变量因果性'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有Transformer时序基础模型存在上下文长度二次复杂度问题，新观测到达时需全量重计算，无法高效适配流式多变量预测场景，也难以兼顾未来已知协变量融合与目标变量因果性约束。

### 方法关键点
基于xLSTM构建内存中心循环架构的TiRex-2，流式下每个patch推理成本恒定；结合双向时间混合器与非对称分组注意力变量混合器，可融合未来已知协变量同时严格保证目标变量因果性；提出合成耦合pipeline，可从大规模单变量语料动态生成多变量样本支撑预训练。

### 关键结果
零-shot性能在GIFT-Eval、fev-bench上达到SOTA；可稳定支持任意长度上下文流式输入，单步推理成本恒定；单变量模式激活参数量38.4M，多变量预测仅需额外激活44.1M参数。
