---
title: 'MoME: Mixture-of-Memory Embeddings for Context-Aware Sparse Lookup'
title_zh: MoME：面向上下文感知稀疏查询的混合记忆嵌入机制
authors:
- Muchen Li
- Leonid Sigal
- Renjie Liao
affiliations:
- University of British Columbia
- Vector Institute for AI
- Canada CIFAR AI Chair
- NSERC CRC Chair
arxiv_id: '2609.15126'
url: https://arxiv.org/abs/2609.15126
pdf_url: https://arxiv.org/pdf/2609.15126
published: '2026-09-13'
collected: '2026-09-21'
category: LLM
direction: LLM内存增强 · 稀疏查询优化
tags:
- MoME
- Memory Embedding
- Sparse Lookup
- LLM Efficiency
- Context-Aware
one_liner: 提出上下文感知混合记忆嵌入MoME，低开销解决传统单槽token记忆表的多义语义冲突
practical_value: '- 电商搜索/推荐的多义query、多义item召回场景可复用多槽设计：给每个query/item的Embedding分配多个语义槽，用用户上下文（搜索历史、浏览序列）训练门控选槽，解决单向量召回的语义混淆问题（如「苹果」区分水果/电子产品）

  - 大规模Embedding表优化可借鉴token分组策略：用语义聚类把相似item/query映射到同一行内存，节省的容量扩容槽数，在不增加存储开销的前提下提升语义表达能力

  - 基于LLM的电商Agent（导购、客诉）可集成MoME替换原有Value Embedding：仅增加<2%推理开销即可提升多义实体理解准确率，适配用户query语义多变的业务场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM的token索引记忆嵌入均采用单槽设计，同一个token的不同语义（如`python`指代编程语言/动物）只能共享一个固定向量，存在容量错配、上下文盲的问题，且内存表冗余度高，制约模型效果提升。
### 方法关键点
- 每个token对应M个记忆槽，以上游Transformer输出的隐藏状态为输入训练门控网络，动态选择Top-K个槽加权聚合，得到适配当前上下文的记忆向量
- 可选token分组策略：预训练阶段基于语义相似性把相近token映射到同一行内存，节省的容量用于增加每行的槽数，提升训练效率
- 记忆向量注入Attention的Value流，与原生Value投影并行计算，最小化推理延迟开销
### 关键实验
在nanochat、Llama3/MobileLLM、Qwen3三类骨干架构上做受控预训练，对比Value Embedding、STEM、Bigram等基线，等参/等训练FLOP设置下，验证集bpb最高下降0.3%，CORE指标最高提升4.2%，训练吞吐量仅下降<2%；推理延迟随模型规模增大降低到2%以内，多义token路由分析显示同一token不同语义的槽位区分度达90%以上。
### 核心结论
上下文感知的多槽记忆设计，是在几乎不增加额外计算开销的前提下，解决token多义性冲突、提升LLM内存利用效率的高性价比路径
