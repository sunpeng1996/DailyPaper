---
title: Prompt Compression via Activation Aggregation
title_zh: 基于激活聚合的Prompt压缩方法
authors:
- Thibaud Ardoin
- Semira Einsele
- Evis Bregu
- Gerhard Wunder
affiliations:
- Freie Universität Berlin
arxiv_id: '2607.08399'
url: https://arxiv.org/abs/2607.08399
pdf_url: https://arxiv.org/pdf/2607.08399
published: '2026-07-09'
collected: '2026-07-10'
category: LLM
direction: LLM推理优化 · Prompt激活压缩
tags:
- Prompt Compression
- Activation Engineering
- LLM Inference
- Representation Learning
- KV Cache
one_liner: 将LLM Prompt压缩为单激活向量注入复用，准确率仅比全prompt低2%
practical_value: '- 电商导购、AI客服等重复系统prompt占比高的场景，可将固定前缀预压缩为单激活向量，替换KV cache降低推理显存与计算开销，并发吞吐提升显著

  - RAG推荐场景下召回的商品/内容长文本可提前压缩为激活向量，无需每次拼接进prompt，减少token消耗同时降低多轮对话推理延迟

  - 可复用W-MLP的权重学习思路，提取LLM中间层对用户query/商品描述的激活权重，做关键语义信息抽取，支撑意图理解、商品标签生成等任务

  - 落地时直接复用「中间层提取+早期层注入」的配置，仅需训练4层小MLP，无需微调目标大模型，迁移成本极低'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM推理中大量重复的系统prompt、few-shot示例、RAG文本块每次需全量计算，KV cache虽可复用但仍保留全序列长度开销，现有压缩方案多需全量微调大模型，成本高泛化性差，亟需轻量免微调的压缩方案。
### 方法关键点
- 三步框架：从冻结LLM中间层提取prompt隐藏状态，经压缩器生成单patch向量，推理时将向量注入早期层占位符token位置替代原prompt
- 两种压缩器对比：轻量4层MLP（W-MLP）学习每个token激活的权重做加权和，对比端到端Transformer压缩器（TC）
- 最优层配置：选择中间层提取（语义信息最丰富）、早期层注入（预留足够层处理压缩信息）
### 关键实验
- 数据集：自定义11类知识检索Toy Task、ARC-Easy多选问答数据集，基线为全prompt（上限）、masked prompt（下限）
- 核心结果：Llama3.1-8B上W-MLP在Toy Task测试集准确率85.35%，仅比全prompt低1.57%，OOD任务准确率63.01%，远超TC的43.89%；ARC-Easy上W-MLP准确率77%，比TC高29个百分点
### 核心结论
单个激活向量即可保留prompt绝大多数语义信息，仅需训练极小MLP即可实现，无需微调大模型，是比KV cache更省资源的重复prompt复用方案
