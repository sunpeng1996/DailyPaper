---
title: Metadata, Structure, or Strategy? A Decomposition of RAG Context Enrichment
title_zh: 元数据、结构还是策略？RAG上下文增强的分解研究
authors:
- Saber Zerhoudi
- Michael Granitzer
- Jelena Mitrovic
affiliations:
- University of Passau
- Interdisciplinary Transformation University Austria
arxiv_id: '2606.29645'
url: https://arxiv.org/abs/2606.29645
pdf_url: https://arxiv.org/pdf/2606.29645
published: '2026-06-28'
collected: '2026-06-30'
category: RAG
direction: RAG系统设计 · 效果归因分析
tags:
- RAG
- LLM
- Evaluation
- Metadata
- Retrieval
one_liner: 控制变量拆解RAG上下文增强三大要素，推翻 richer context 一定更好的默认假设
practical_value: '- 业务RAG（电商问答、商品检索Agent等）遵循「少即是多」原则：只保留任务必需的元数据，多余元数据会抢占LLM注意力反而降低准确率，比如时效性任务仅保留商品上架时间即可，不需要额外添加置信度、溯源信息

  - 用过程性层次框架预判元数据可用性：只有对应操作在预训练中是频繁且预测必要的元数据（如时间对比）才添加，不可处理的元数据（如来源可信度评级）加了也没用反而添乱

  - 多跳推理类Agent任务中，高质量领域检索分解模板的收益远大于元数据增强，小模型对齐正确策略也能超过裸跑的大模型，降本提效效果明显

  - 结构化上下文优先选择轻量格式（如Markdown）而非JSON，能大幅降低结构带来的性能损失，还能减少输入token，降低KV cache开销'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG研究普遍默认「更丰富的上下文就能带来更好的效果」，业界会给检索结果添加各类质量元数据、结构化整理、采用多跳检索策略，但以往评测同时改变元数据、结构、策略三个变量，无法拆分各自的独立贡献，混淆变量导致结论不可靠，因此需要控制变量实验明确各要素的真实影响。

### 方法关键点
- 拆分三个独立变量：元数据分5级从无到全（G0原始文本→G1空结构→G2加时序→G3加置信度冲突→G4加溯源），结构分无结构原始文本和结构化原子记录，检索策略分单轮top-k、LLM自分解、模板引导检索三类
- 新增结构化但无元数据的空白对照组，填补了以往研究缺失的控制条件
- 评测覆盖6个不同类型基准、4个来自3个模型家族的LLM，累计评估超过24000个回答

### 关键结果
- 绝大多数上下文增强都会降低准确率：纯结构化格式（无额外元数据）就会损害推理任务性能，仅在FEVER事实验证任务微涨0.012
- 只有时序元数据对时间敏感任务有正向收益，TempLAMA上G1→G2提升0.22 F1，后续添加置信度、溯源元数据反而抵消了收益
- 存在**利用率-准确率鸿沟**：提示模型使用置信度元数据可将利用率从14%提升到70%，但准确率反而下降0.032~0.192，更容易处理的元数据会抢占任务相关元数据的注意力
- 对齐后小模型反超大模型：带正确对齐的元数据与策略的GPT-4.1-mini，比使用原始上下文的前沿模型GPT-4.1高出19个F1点

### 核心结论
RAG的瓶颈不是模型能拿到多少信息，而是模型能有效吸收多少信息，RAG设计的核心问题是「该去掉什么元数据」而非「该添加什么元数据」
