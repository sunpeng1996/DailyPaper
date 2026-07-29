---
title: 'Penelope: Localized Latent Recurrence for Efficient Structured Reasoning'
title_zh: Penelope：面向高效结构化推理的局部隐态循环框架
authors:
- Yutong Chen
- Shouqian Shi
- Xinran Liu
- Haochen Wang
- Jiaying Wang
- Tianxing Xu
- Yuanxi Wang
- Zirui Ding
arxiv_id: '2607.25915'
url: https://arxiv.org/abs/2607.25915
pdf_url: https://arxiv.org/pdf/2607.25915
published: '2026-07-28'
collected: '2026-07-29'
category: Reasoning
direction: 结构化推理优化 · 局部隐态循环
tags:
- Latent Reasoning
- Decoder-only Transformer
- KV Cache
- Structured Reasoning
- LoRA
one_liner: 面向decoder-only Transformer的局部隐态推理框架，保留推理精度的同时大幅降低结构化推理延迟
practical_value: '- 可借鉴「分层计算拆分+局部循环复用」架构思路：将用户/query的一次性上下文编码和多步推理逻辑拆分，仅循环执行推理相关的少量层，降低导购Agent、投放策略生成等多步推理场景的延迟

  - 渐进式CoT转隐态训练策略可复用：针对搜索query语义理解、售后问题根因分析等需要CoT的场景，可逐步将显式CoT蒸馏为隐态循环，既保精度又避免输出长中间步骤

  - KV Cache复用设计可直接落地工程：固定prompt侧上下文的KV Cache，仅更新循环部分的状态，适合推荐实时个性化推理、广告创意生成等低延迟要求场景的性能优化'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前LLM提升结构化推理能力主要依赖两种路径：要么扩大模型参数规模，导致训练、部署成本陡增；要么通过CoT生成显式中间推理步骤，推理延迟随输出长度线性增长。现有隐态推理方案虽能避免长显式步骤，但仍需重复执行全量Decoder层，边际推理成本仍居高不下，亟需兼顾精度与推理效率的优化方案。

### 方法关键点
- 架构分层拆分：将Decoder拆分为三段，下层前缀仅执行1次编码prompt生成问题相关边界记忆，中间选中的连续层作为循环区间执行隐态迭代，上层仅执行1次生成最终答案
- 局部循环优化：缓存下层前缀的KV供循环区间复用，每次迭代仅更新固定大小的隐态记忆和读入状态，加入时间调制GRU做稳定状态更新，避免迭代漂移
- 渐进式蒸馏训练：采用CoT转隐态课程学习，逐步减少显式CoT步数、增加隐态循环步数，将显式推理能力迁移到隐态循环路径

### 关键结果
基于Llama-3.2-1B、Qwen3.5-0.8B两个开源基座，对比Visible CoT、Coconut、CODI等基线：
- Deep ListOps任务精度达52.25%，较Visible CoT高0.98pp，推理延迟较全Decoder隐态方案Coconut降低46.9%
- ProsQA任务精度78.27%与Coconut持平，延迟降低33.3%
- PrOntoQA任务精度达99.67%接近满精度，延迟降低42.2%

### 核心结论
隐态推理计算可局部化到Decoder的小段连续层中，无需重复执行全量Decoder即可在几乎无损精度的前提下大幅降低推理延迟
