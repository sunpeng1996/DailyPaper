---
title: 'GEM: A Generative Embedding Model Bridging Reasoning and Retrieval'
title_zh: GEM：衔接推理与检索的生成式嵌入模型
authors:
- Zhili Shen
- Craig Macdonald
affiliations:
- University of Glasgow
arxiv_id: '2608.13200'
url: https://arxiv.org/abs/2608.13200
pdf_url: https://arxiv.org/pdf/2608.13200
published: '2026-08-13'
collected: '2026-08-14'
category: RAG
direction: 生成式检索 · 推理增强嵌入
tags:
- Generative Embedding
- Dense Retrieval
- Reasoning Augmented Retrieval
- KV Cache
- Contrastive Learning
one_liner: 单模型统一LLM推理与稠密嵌入能力，推理增强检索，支持测试时计算缩放调优
practical_value: '- 电商搜索/站内检索场景可复用「先推理用户查询意图+相关性规则，再生成查询嵌入」范式，解决复杂长query/模糊需求的召回错配问题

  - 工程实现可借鉴<|embed|>专用token+KV cache复用设计，推理后直接取嵌入token隐层作为查询表示，相比拆分推理+编码双模型可降低30%以上推理延迟

  - 训练时可复用其数据生成pipeline：基于推理结果生成对齐的正/难负样本，同时用CLM+对比损失联合训练，避免LLM微调后生成能力灾难性遗忘

  - 面向复杂指令的个性化搜索/推荐场景，可借鉴测试时prompt缩放能力，动态调整推理深度平衡效果与耗时，适配不同流量场景需求'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM的推理/指令跟随能力让用户越来越习惯用自然语言表达复杂信息需求，但传统检索器仅依赖查询与文档的表层/语义相似度匹配，无法理解深层用户意图与约束，导致检索效果与用户需求偏差增大；现有推理增强检索方案多采用多模型pipeline，存在冗余计算，且嵌入与推理的对齐度不足。

### 方法关键点
- 单模型统一生成与嵌入能力：基于Qwen3-4B基座，新增专用<|embed|>标记，先推理输出用户意图与相关性规则，再在推理结果后追加<|embed|>取其隐层作为查询嵌入
- 训练策略：联合CLM（生成）损失与InfoNCE（对比）损失，权重分别为0.1和1.0，既保留LLM原生生成能力，又学习有效嵌入表示
- 对齐数据生成pipeline：针对每个查询先采样8条推理结果，过滤掉与正样本冲突的无效推理，再基于有效推理生成对齐的正样本与难负样本，避免表层匹配捷径学习
- 推理优化：生成查询时复用KV cache，追加<|embed|>后无需重新编码全序列，大幅降低延迟

### 关键结果
在BRIGHT推理密集检索数据集上，平均nDCG@10达29.1，比同基座无推理的嵌入模型高7.7，比8B参数的ReasonIR高4.7，性能接近32B参数的reranker；在FollowIR指令跟随检索数据集上，p-MRR达+11.7，与7B参数的Promptriever持平，Robustness@10比同基座无推理模型高8.6；测试时通过prompt调整推理长度可进一步将nDCG@10提升至30.1，且KV cache复用后长序列编码延迟几乎无增长。

**最值得记住的一句话**：统一推理与嵌入的单模型方案，不仅能通过推理增强检索效果，还能通过KV cache复用大幅降低多模型pipeline的冗余开销，是复杂检索场景的高性价比落地方向。
