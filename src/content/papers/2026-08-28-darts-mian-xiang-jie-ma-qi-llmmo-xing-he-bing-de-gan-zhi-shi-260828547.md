---
title: 'DARTS: Decoder-Aware Representation Tuning via Surgery for Model Merging'
title_zh: DARTS：面向解码器LLM模型合并的感知表示调优方法
authors:
- Aaryan Ajay Sharma
- Sai Nishanth Padala
- Seganrasan Subramanian
affiliations:
- ServiceNow
- University of Twente
arxiv_id: '2608.28547'
url: https://arxiv.org/abs/2608.28547
pdf_url: https://arxiv.org/pdf/2608.28547
published: '2026-08-28'
collected: '2026-08-31'
category: LLM
direction: LLM模型合并 · 表示偏差校正
tags:
- Model Merging
- Representation Bias
- Decoder LLM
- Parameter Efficient Tuning
- Autoregressive Generation
one_liner: 针对解码器LLM模型合并的表示偏差问题，提出仅增0.1%参数的校正方案，跨任务性能显著提升
practical_value: '- 多场景LLM合并场景可直接复用熵加权L1损失：优先校正生成时决策关键的高熵token位置，用极少量校准数据即可提升多任务模型效果，几乎无额外推理成本

  - 电商场景整合多专项LLM（如文案生成、客诉回复、营销话术模型）时，可叠加位置校正偏置表，仅加0.1%参数即可缓解自回归偏差累积问题

  - 低资源模型优化可参考其校准范式：仅需50条无标注领域数据+500步训练即可完成校正，单A100上单域校准耗时仅11秒，落地门槛极低'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有模型合并可低成本整合多个专项微调LLM的能力，无需额外训练数据，但合并后存在表示偏差，导致各任务性能明显下降。此前的表示校正方案仅针对编码器视觉模型设计，完全不适用解码器LLM：一是因果注意力机制会让偏差随token位置不断累积，二是不同token位置对生成质量的影响差异极大，位置无关的统一校正和均匀损失会浪费算力在不影响生成效果的低价值位置。
### 方法关键点
- 设计**熵加权L1损失（EWL1）**：按目标模型在各token位置的预测熵加权校正损失，优先修正高熵（决策关键）位置的表示偏差，降低低熵位置（如标点、固定语法）的校正权重
- 新增**位置校正模块**：引入独立的逐位置加性偏置表，无额外网络结构，直接捕获随位置递增的系统性偏差，避免过拟合
- 整体仅增加0.1%的模型参数量，推理无额外延迟，可兼容Task Arithmetic、TIES、DARE等所有主流模型合并方法
### 关键实验结果
基于Llama-2-7B合并代码、数学推理、指令跟随三个专项模型，在HumanEval、GSM8K、AlpacaEval三个基准测试：
- 对比原始表示校正方案，在Task Arithmetic合并框架下平均性能提升4.7个百分点，其中AlpacaEval win rate提升9.1个百分点
- 仅需50条无标注领域校准数据即可稳定收敛，单域校准在A100上仅耗时11秒，性能对学习率的鲁棒性极强
### 核心结论
解码器LLM的合并校正中，损失函数的设计优先级远高于校正模块架构，聚焦关键位置的校正远比对所有位置做均匀优化投入产出比更高
