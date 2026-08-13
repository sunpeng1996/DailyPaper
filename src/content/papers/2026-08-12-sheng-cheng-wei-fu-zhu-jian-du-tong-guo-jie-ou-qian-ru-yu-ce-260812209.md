---
title: 'Generation as Auxiliary Supervision: Enhancing Visual Understanding at Zero
  Inference Overhead via Decoupled Embedding Prediction'
title_zh: 生成为辅助监督：通过解耦嵌入预测零推理开销增强视觉理解
authors:
- Zhongbin Guo
- Jiahao Xie
- Dongling Xiao
- Qianle Wang
- Ruiqi Lu
- Xiaomin He
- Wanxuan Sun
- Cheng Yang
affiliations:
- ByteDance
arxiv_id: '2608.12209'
url: https://arxiv.org/abs/2608.12209
pdf_url: https://arxiv.org/pdf/2608.12209
published: '2026-08-12'
collected: '2026-08-13'
category: Training
direction: 多模态大模型训练优化
tags:
- MLLM
- Generation Supervision
- Mixture-of-Transformers
- Zero Inference Overhead
- Multimodal Understanding
one_liner: 提出GAS生成引导训练框架，以生成任务为辅助监督增强多模态理解，推理零额外开销
practical_value: '- 电商搜图、商品图文理解场景可直接复用GAS范式，训练阶段新增生成辅助分支，推理无需修改现有链路无性能损耗

  - 解耦共享底层+并行上层分支的训练架构可迁移到推荐模型训练，用辅助任务增强主任务效果且不增加推理成本

  - 构造与主任务强认知关联的辅助生成任务而非通用生成任务，可最大化辅助监督的增益效果'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有多模态大模型（MLLM）的视觉理解与生成任务目标差异大，通用统一框架的生成目标与理解模型采用的连续表征不匹配，难以直接迁移增强预训练MLLM，且多数方案会增加推理开销。

### 方法关键点
提出GAS生成引导训练框架，采用解耦Mixture-of-Transformers（MoT）架构：底层参数共享，上层并行设置理解分支与生成分支，将Next Embedding Prediction作为跨模态生成范式，生成损失仅更新共享视觉通路、不影响上层理解分支；同时构造与认知强关联的生成任务最大化协同效果，训练完成后直接丢弃生成分支。

### 关键结果
跨不同模型规模与训练阶段均提升多模态理解效果，在感知、空间理解类任务上增益最稳定，推理完全无额外开销，经过大量对照实验验证了生成引导训练的可行性。
