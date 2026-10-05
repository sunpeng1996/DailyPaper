---
title: 'Triadic Linear Attention: Three-Dimensional Recurrent States for Long-Context
  Sequence Modeling'
title_zh: 三元线性注意力：面向长上下文序列建模的三维循环状态
authors:
- Oliver Sieberling
- Bharat Runwal
- David Jin
- Ryan Chin
- Rameswar Panda
- Yoon Kim
affiliations:
- Massachusetts Institute of Technology
- MIT-IBM Computing Research Lab
arxiv_id: '2609.36529'
url: https://arxiv.org/abs/2609.36529
pdf_url: https://arxiv.org/pdf/2609.36529
published: '2026-09-28'
collected: '2026-10-05'
category: LLM
direction: LLM长上下文 · 线性注意力优化
tags:
- LinearAttention
- LongContext
- TensorState
- SequenceModeling
- ParameterEfficient
one_liner: 提出参数高效的三元线性注意力，用三阶张量状态大幅提升线性注意力长上下文建模与召回能力
practical_value: '- 做长上下文RAG/多轮对话Agent时，可替换现有线性注意力模块为三元线性注意力，仅增加<2%参数即可获得数倍的KV存储容量，降低长序列推理成本

  - 电商长序列用户行为建模场景，可借鉴三阶张量状态的设计，用双key绑定用户行为的时间/场景维度与item维度，在不显著增加参数的前提下提升长行为序列的召回准确率

  - 已上线的线性注意力类模型可通过「升维+继续训练」的方式upcycle到三元版本，无需从头预训练即可获得长上下文能力增益，适合存量模型迭代'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有线性注意力依赖二阶矩阵型循环状态，状态容量直接决定长上下文召回能力，传统扩容方案（扩大头尺寸、增加头数、加宽value维度等）会带来过高的参数与计算开销，无法平衡容量、效率与性能。
### 方法关键点
- 新增第二组key/query投影，将原线性注意力的二阶矩阵状态升级为三阶张量状态，状态容量随第二key维度E线性增长，仅增加两组小投影，参数开销<2%（E=8时）
- 原生兼容数据依赖遗忘门、delta规则、分块并行训练等现有线性注意力优化技术，通过第二key维度的分块切片存储解决三阶张量的显存占用问题
- 支持预训练后升维升级：已训好的普通线性注意力模型可直接将E从1扩展为更大值，仅需少量长上下文继续训练即可获得性能增益
### 关键结果
在400M/1.3B参数规模下，基于Fineweb-Edu预训练、PG19长文本、RULER召回基准测试，对比基线与其他扩容方案：
- E=8时状态容量提升8倍，长上下文召回准确率较普通GDN基线提升26%+，64k上下文下PG19困惑度较基线低0.49
- 同参数同状态容量下，比扩大头、增加头等其他扩容方案的PG19 16k-64k困惑度低0.3~0.6，64k上下文推理速度比Transformer快5.1倍
- 存量普通线性注意力模型升维到E=8后继续训练，可恢复75%左右从零训练三元模型的性能增益

线性注意力的状态容量是决定长上下文性能的核心指标，张量升维扩容可以在极低参数开销下获得显著的长序列性能收益
