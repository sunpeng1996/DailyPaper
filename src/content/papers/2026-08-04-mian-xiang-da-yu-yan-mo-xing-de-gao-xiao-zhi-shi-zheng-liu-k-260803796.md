---
title: 'Efficient Knowledge Distillation for LLMs: Offline Top-K Logits and a Fused
  Chunked KL Loss'
title_zh: 面向大语言模型的高效知识蒸馏：离线Top-K Logits与融合分块KL损失
authors:
- Bakbergen Ryskulov
- Iker García-Ferrero
- David Montero
- David Jansen
- Ali Hashemi
- Jezabel R. Garcia
- Antonio Tiene
- Román Orús
affiliations:
- Multiverse Computing
arxiv_id: '2608.03796'
url: https://arxiv.org/abs/2608.03796
pdf_url: https://arxiv.org/pdf/2608.03796
published: '2026-08-04'
collected: '2026-08-05'
category: Training
direction: 大模型蒸馏 · 训练效率与长上下文优化
tags:
- Knowledge Distillation
- LLM Training
- Memory Optimization
- Long Context
- KL Loss
one_liner: 提出离线Top-K缓存蒸馏+融合分块KL损失，大幅降低LLM蒸馏显存占用并提升训练效率
practical_value: '- 垂类小模型蒸馏优先采用离线Top-K logit缓存方案，仅缓存教师每个token的Top-100 logits，效果与在线蒸馏相当，单H200
  GPU训练速度提升29%、吞吐量提升40%，无需训练时加载大教师模型，大幅降本

  - 训练长上下文小模型（电商长商品理解、Agent长对话建模）时可直接复用开源的融合分块KL损失实现，显存峰值随序列长度线性增长，单H200可支持32768 tokens蒸馏，上下文长度比普通KL损失提升4倍

  - 蒸馏损失设计优先选「logit KL损失+隐层特征MSE损失」组合，比单用logit KL损失在MMLU高0.7个点、GSM8K高1.6个点，稳定提升小模型效果

  - 蒸馏训练可采用朴素序列打包（无样本间注意力掩码），仅损失约1个点MMLU，大幅提升长上下文显存利用率，适合低成本小模型训练场景'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
端侧、低延迟部署场景普遍需要小模型，而小模型通常通过大模型知识蒸馏得到，但传统在线蒸馏需同时加载教师与学生模型，每次迭代还要跑教师前向，显存与计算成本极高；同时普通KL损失的词表级张量显存峰值会限制训练上下文长度，长上下文小模型的蒸馏成本居高不下，工业界缺少可落地的高效蒸馏工程方案。

### 方法关键点
- 离线Top-K蒸馏：提前一次计算教师模型每个token的Top-100 logits并缓存，训练时学生直接与缓存logits计算KL损失，无需训练过程中加载教师模型
- 融合分块KL损失：将输出层投影与损失计算融合，按序列块处理数据，全程不实例化完整词表级logit张量，显存峰值仅与序列长度线性相关，支持更长上下文训练
- 配套优化：蒸馏损失采用logit KL+隐层特征MSE的组合，训练支持朴素序列打包提升显存利用率

### 关键实验
- 对比4种蒸馏方案，单H200 GPU 8K上下文下蒸馏Llama3.1 8B到3.2B模型，离线Top-K方案与在线蒸馏损失几乎一致，单步速度快29%，吞吐量高40%
- 融合分块KL损失在8K上下文下比离线稠密KL显存低20GB，单卡支持32768 tokens蒸馏，上下文长度是稠密KL的4倍；256K序列微基准测试中，比稠密KL显存低15.6倍，比前向分块KL速度快3.3倍
- 消融验证：仅用隐层特征损失会导致效果崩溃，必须加logit KL损失；朴素序列打包仅损失约1个点MMLU

最值得记住的一句话：LLM知识蒸馏优先用离线Top-K缓存方案降本，长上下文场景直接上融合分块KL损失，损失组合选logit KL加隐层特征损失即可拿到最优性价比。
