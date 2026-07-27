---
title: Benchmarking Fine-tuning and Retrieval Strategies for a Multimodal Language
  Model on the NRC Reactor Operator Licensing Examination
title_zh: 多模态大模型在NRC反应堆操作员执照考试中的微调与检索策略基准测试
authors:
- Isak Hwang
- Yoon Pyo Lee
affiliations:
- Hanyang University
- University of Illinois Urbana-Champaign
arxiv_id: '2607.22067'
url: https://arxiv.org/abs/2607.22067
pdf_url: https://arxiv.org/pdf/2607.22067
published: '2026-07-24'
collected: '2026-07-27'
category: Eval
direction: 垂直领域LLM 微调与RAG策略评估
tags:
- SFT
- RAG
- RAFT
- Chunking
- Multimodal LLM
- Domain Adaptation
one_liner: 基准测试8种大模型+检索配置，得出核领域最优微调+RAG组合策略
practical_value: '- 垂直领域RAG+微调选型可复用该测试框架：先测纯SFT、纯RAG、SFT+RAG、RAFT等多组合对比，避免盲目投入复杂方案

  - 分模型状态选Chunking策略：基模型适配结构感知Chunking，微调后模型适配固定滑动窗口Chunking，可直接在电商知识库RAG链路验证

  - 垂直领域知识问答优先验证SFT+RAG组合：纯RAG效果远弱于微调+检索的结论可复用，无需过度投入纯RAG优化'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
垂直领域LLM应用要求输出严格贴合领域知识，当前缺乏对微调、检索组合策略的系统性基准验证。
### 方法关键点
以Gemma 4 31B-IT为基模型，对比8种配置：纯基模型、基于Gemini蒸馏CoT rationales的SFT、BM25 RAG、RAFT，同时对比固定大小滑动窗口Chunking和结构感知Chunking两种检索分片策略，测试集为14套2015-2021年NRC反应堆操作员执照考试题（7套压水堆+7套沸水堆），以人类及格线80%为评估标准。
### 关键结果
SFT+固定窗口Chunking RAG组合表现最优，14套考试中8套达标，总准确率79.7%（置信区间覆盖及格线），压水堆题准确率达80.2%；无微调的所有配置均未通过任何考试；Chunking最优策略随模型训练状态反转，相同检索条件下RAFT效果弱于普通SFT。
