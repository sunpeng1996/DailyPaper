---
title: The State-Prediction Separation Hypothesis
title_zh: 状态-预测分离假说及双流Transformer架构的实现与验证
authors:
- Giovanni Monea
- Nathan Godey
- Kianté Brantley
- Yoav Artzi
affiliations:
- Cornell University
- Harvard University
arxiv_id: '2607.01218'
url: https://arxiv.org/abs/2607.01218
pdf_url: https://arxiv.org/pdf/2607.01218
published: '2026-06-30'
collected: '2026-07-02'
category: LLM
direction: LLM 架构优化 · 双流计算分离
tags:
- Transformer
- LLM Pretraining
- KV cache
- Training Efficiency
- Architecture Optimization
one_liner: 提出Transformer状态与预测计算分离的双流架构，以极小推理 overhead 提升训练效率和下游性能
practical_value: '- 推理成本敏感的业务场景（如电商个性化文案生成、Agent实时交互）可直接复用SPS架构，仅损失6%~10%推理吞吐量、KV
  cache内存几乎无增长，即可获得2~3pp的下游任务精度提升

  - 训练数据有限的垂直领域LLM（如商品属性理解、搜索Query语义匹配模型）可采用SPS设计，仅用一半训练token就能达到标准Transformer的精度，大幅降低训练数据收集与标注成本

  - 长序列依赖的业务任务（如用户全生命周期行为建模、长会话Agent）可参考SPS的梯度分离思路，将状态存储和即时预测的表征解耦，提升长序列记忆的有效性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
标准Transformer的每个时间步隐层状态同时承担两个冲突的任务：预测下一token、存储供后续步骤使用的状态信息，二者的梯度相互干扰，导致训练效率和模型性能受限；在高质量训练数据日益稀缺的背景下，提升数据效率成为LLM落地的核心需求。

### 方法关键点
- 提出状态-预测分离（SPS）假说，将原有的单计算流拆分为状态流和预测流，在每个输入token后插入专用的<predict>虚拟token，二者共享位置编码
- 状态流（输入token对应的KV）持久化存入KV cache，供所有后续步骤访问；预测流（<predict>token对应的KV）仅保留最近w=64步的滑动窗口，超出后直接丢弃
- 仅在<predict> token位置计算下一token预测损失，梯度分别流向两个独立的表征空间，避免相互干扰

### 关键实验结果
在53M~1.678B共5个参数规模下预训练，数据集采用FineWeb-Edu，对比标准Transformer、2XMEMORY、DELAYEDSTATE三个基线：SPS仅用一半的训练token就能达到标准Transformer的验证损失，下游零-shot任务平均精度提升2.3~3.1pp，推理峰值内存仅增加1%，吞吐量仅下降6%~10%；1.6B参数规模下，SPS用18B训练token就能达到标准Transformer用47B token的NLL水平，数据效率提升2.6倍。

最值得记住的一句话：将Transformer隐层状态的预测和状态存储职责解耦，是在不显著增加推理成本的前提下大幅提升训练数据效率和模型性能的有效路径。
