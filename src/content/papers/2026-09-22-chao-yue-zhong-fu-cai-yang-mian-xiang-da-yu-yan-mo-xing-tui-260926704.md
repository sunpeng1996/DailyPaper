---
title: 'Beyond Repeated Sampling: Learning Search Policies for LLM Reasoning'
title_zh: 超越重复采样：面向大语言模型推理的搜索策略学习
authors:
- Ismail Labiad
- Matthieu Kowalski
- Marc Schoenauer
- Rémi Munos
- Julia Kempe
affiliations:
- Meta FAIR
- Université Paris-Saclay
- Inria
- CNRS
- NYU Courant Institute
arxiv_id: '2609.26704'
url: https://arxiv.org/abs/2609.26704
pdf_url: https://arxiv.org/pdf/2609.26704
published: '2026-09-22'
collected: '2026-09-23'
category: Reasoning
direction: LLM推理 · 小模型引导大模型探索
tags:
- LLM Reasoning
- Reinforcement Learning
- Exploration Policy
- Concept Generation
- Transfer Learning
one_liner: 基于强化学习训练小模型生成推理概念，引导冻结大模型推理效果翻倍且可跨模型迁移
practical_value: '- 推理侧优化可复用「小模型生成引导信号+大模型执行」的架构，不需要改动大模型权重，适配闭源大模型的业务场景，例如电商大模型导购、智能客服的复杂问题求解

  - 强化学习训练小模型的奖励设计可直接参考max-of-mean策略，奖励下游任务成功率而非中间指标，适配搜索/推荐侧多候选排序、query改写的效果优化

  - 单轨迹批量生成多个候选策略的方法可替代多次迭代采样，保留KV cache复用能力，提升推理吞吐、降低线上服务延迟，适配大促等高并发场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM推理阶段的主流探索策略是重复采样，仅通过token级噪声生成候选，容易产出大量近重复结果，无法覆盖语义级的差异化解法；此前的概念引导采样方法收益对基线采样参数高度敏感，一旦基线启用探索性参数后收益几乎消失，且迭代生成概念效率低、单问题生成概念数少，难以提升难例求解效果。

### 方法关键点
- 优化概念生成范式：单轨迹一次性生成最多10个高信号、无重复的问题专属概念，替代原有迭代生成方案，大幅提升概念多样性
- 小模型可训练架构：仅用强化学习训练7B量级的概念生成器，大模型作为答案生成器全程冻结，奖励采用两种聚合策略：max-of-max（任意概念引导的答案正确即给1分）、max-of-mean（取各概念对应答案准确率的最大值）
- 难例适配优化：仅针对大模型重复采样完全无法解决的难例训练与评估，避免天花板效应掩盖方法收益

### 关键实验
在DeepMath 1k难例测试集上，对比朴素重复采样基线，RL训练后的7B概念生成器引导32B冻结大模型，pass@128从19.0%提升至39.2%，效果翻倍；训练后的7B概念生成器效果超过未训练的32B概念生成器，且无需重训练即可迁移到不同家族的Llama-3.3-70B大模型，将其pass@128从26.2%提升至34.3%；推理侧概念生成的额外算力开销仅为单条答案生成的24%，几乎不增加整体推理成本。

### 核心结论
小模型可以训练为可复用的搜索策略，在不改动大模型权重的前提下，大幅提升大模型的难例求解效果，甚至超过更大的未调整概念生成器的表现
