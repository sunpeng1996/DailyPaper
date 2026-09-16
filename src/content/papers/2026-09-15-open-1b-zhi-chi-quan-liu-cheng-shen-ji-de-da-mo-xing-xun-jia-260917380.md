---
title: 'OPEN-1B: A Fully Auditable Training Run'
title_zh: OPEN-1B：支持全流程审计的大模型训练框架
authors:
- John Donaghy
- Brian Wilcox
- Oğuzhan Ersoy
- Shikhar Rastogi
- Adam St Arnaud
- Alexey Titov
- Jordan Greenberg
- Ben Fielding
- Harry Grieve
affiliations:
- Gensyn
arxiv_id: '2609.17380'
url: https://arxiv.org/abs/2609.17380
pdf_url: https://arxiv.org/pdf/2609.17380
published: '2026-09-15'
collected: '2026-09-16'
category: Training
direction: 大模型训练 · 可复现性与审计
tags:
- LLM
- Training
- Reproducibility
- Auditability
- Quantization
one_liner: 实现跨异构硬件比特级可复现训练，开源1.61B可审计LLM及配套工具
practical_value: '- 训练需保证可复现的业务LLM（如电商合规营销模型）时，可复用RepOps的三个核心trick：固定归约顺序、统一亚正常数处理、计数器驱动随机数生成，解决跨硬件训练结果不一致问题

  - int8量化感知预训练场景下，直接复用每步重计算量化步长的方案代替可学习步长，既解决量化训练不稳定问题，还能比bf16可复现训练提速1.8倍

  - 有监管合规要求的模型训练场景，可复用拓扑不变数据流+分布式审计方案，实现训练过程全链路可追溯，满足合规要求'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有开源LLM即使公开权重、训练数据、配方，受浮点运算非结合性影响，跨硬件无法实现比特级复现，无法证明公开checkpoint确实按声明配方训练，存在隐藏数据、注入偏见/后门的风险，现有学习证明等方案仅能提供概率性验证，无法完全规避风险。

### 方法关键点
- 设计RepOps算子库：通过固定全平台归约顺序、统一禁用乘加融合、全平台将亚正常数刷新为0、采用计数器驱动的随机数生成，实现跨CPU/NVIDIA/Apple GPU的比特级可复现运算
- 实现拓扑不变数据流：训练批次顺序仅由全局种子决定，与集群拓扑、并行度无关，支持单设备重放任意训练步骤
- 采用分布式审计方案：多个独立审计方各自验证部分训练步骤，共同覆盖全训练流程，降低单设备审计成本
- 开源1.61B参数Open-1B模型，原生支持int8量化感知预训练，配套全量预训练数据、每100步中间checkpoint、训练代码和审计工具

### 关键实验
基于400B token多源公开数据集训练，对比同参数量OLMo 2 1B，OLMES得分25.4，仅比训练了4T token的OLMo 2低6.5分；int8量化训练比可复现bf16训练快1.8倍，400B token后与bf16基线的loss差仅0.2nats；可复现训练算力开销约为优化后PyTorch基线的5倍，6节点强缩放效率达71%。

最值得记住的结论：可复现性的核心是主动对齐所有硬件的最低能力行为，而非依赖各硬件默认实现。
