---
title: 'T-Search: An Open Agentic Retriever and Playground for Hard Multi-Step Search'
title_zh: T-Search：面向多步复杂搜索任务的开源Agent检索器与实验平台
authors:
- Olga Tsymboi
- Ramil Latypov
- Aleksandr Medvedev
- Danil Taranets
- Dmitrii Stoianov
- Nikita Gulyakov
- Gleb Alektorov
- Anatolii Potapov
affiliations:
- T-Tech
arxiv_id: '2610.06782'
url: https://arxiv.org/abs/2610.06782
pdf_url: https://arxiv.org/pdf/2610.06782
published: '2026-10-05'
collected: '2026-10-06'
category: Agent
direction: Agent 多步检索优化
tags:
- Agentic Retrieval
- Multi-step Search
- GSPO
- RAG
- Recall Optimization
- Open Source
one_liner: 基于Qwen3.6-35B训练的双语开源Agent检索器，检索生成解耦，性能超更大规模开源模型
practical_value: '- 架构设计可直接复用：采用检索与生成完全解耦的方案，检索Agent仅输出带 justification 的证据块，下游生成模型、上游检索后端（如商品库、内容库、BM25/稠密检索）均可任意替换，无需重训检索Agent，适配业务现有技术栈

  - 多轮Agent上下文管理技巧：每轮仅保留显式保存的证据、轮次摘要、问题覆盖状态与下一轮目标，完全丢弃历史工具调用全量日志，避免上下文膨胀导致的性能退化，可直接迁移到所有长流程业务Agent（如导购、售后客服）

  - 低成本训练范式可复用：先构造对抗过滤的合成搜索任务（过滤单步可解、闭卷可答样本），再做轮次切片SFT，最后以纯召回指标为单一奖励做GSPO强化学习，无需调用LLM做奖励打分，大幅降低检索类Agent的训练成本

  - 性能调优trick：可采用3次并行检索轨迹+RRF融合的方式，在可接受的 latency 成本下提升约5个点的Recall@10，适合对召回率要求高的业务场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有深度搜索Agent大多端到端训练，将检索与生成效果绑定，评估依赖答案正确性，无法单独优化检索性能，且大模型长轨迹推理延迟高、成本高，缺乏可直接复用的开源多步检索专用Agent。

### 方法关键点
- 架构解耦：检索Agent仅负责多轮搜索、证据筛选与排序，输出带理由的证据块，下游生成模型与搜索后端可任意替换，无需重训
- 多轮内存设计：每轮仅保留显式保存的证据、轮次摘要、问题覆盖状态与下一轮目标，丢弃历史工具日志，单轮上下文限制32k token，最多5轮
- 训练流程：首先生成对抗过滤的双语合成搜索任务，过滤可单步检索、闭卷可答的简单样本，再做轮次切片的SFT，最后以最终召回率为单一奖励做GSPO强化学习，无需LLM法官
- 性能优化：支持3次并行检索轨迹用RRF融合提升召回

### 关键实验
在7个英俄多步搜索基准上测评，对比GLM-5.1、Qwen3.5-397B等更大模型，单轮次T-Search平均Recall@10达56.0，较基座提升14.4个点；3次轨迹融合后平均Recall@10达61.3，超过所有开源 baseline。

### 核心结论
检索与生成解耦的专用检索Agent，可在更低延迟下实现优于通用大模型的多步检索效果，是RAG系统升级的高性价比方案
