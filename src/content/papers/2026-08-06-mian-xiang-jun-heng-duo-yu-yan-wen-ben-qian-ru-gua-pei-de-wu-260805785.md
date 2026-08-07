---
title: Task-Conditional Flow Matching for Balanced Multilingual Text Embedding Adaptation
title_zh: 面向均衡多语言文本嵌入适配的任务条件流匹配框架
authors:
- Tirth Bhatt
- Naren Kumar S
- Mayank Singh
affiliations:
- Indian Institute of Technology Gandhinagar
arxiv_id: '2608.05785'
url: https://arxiv.org/abs/2608.05785
pdf_url: https://arxiv.org/pdf/2608.05785
published: '2026-08-06'
collected: '2026-08-07'
category: Training
direction: 多语言文本表征 · 损失适配优化
tags:
- Multilingual Embedding
- Flow Matching
- Contrastive Learning
- Curriculum Learning
- Cross-lingual Alignment
one_liner: 针对多任务优化冲突问题，提出任务条件流匹配框架，刷新多语言嵌入Indic MTEB SOTA
practical_value: '- 跨境电商多语言搜索/多语种RAG系统的嵌入适配可直接复用任务条件损失路由逻辑：仅翻译类平行对用Flow Matching做跨语言空间对齐，检索、分类、相关性判等任务保留原生对比/margin损失，避免统一优化的信号冲突

  - 多任务嵌入微调可复用三阶段课程+回放buffer设计：先做基础语义/跨语言对齐打底，再逐步引入高冲突任务，搭配固定比例的前序任务回放样本，有效缓解灾难性遗忘

  - 微调时增加frozen teacher双正则约束：点级对齐单样本embedding余弦相似度、批次级对齐pairwise相似度矩阵，可大幅降低预训练语义结构崩坏风险，避免RAG/召回的泛化性下降

  - 多语言/多任务训练可落地分层采样策略：限制大语料的样本上限、跨任务/跨语言均匀采样，避免高资源任务/语种的梯度碾压小样本任务，适配小语种业务的表征需求'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前多语言文本嵌入适配普遍采用统一对比损失优化异质任务，易出现训练信号冲突，部分任务的性能提升以其他任务下降为代价；同时对比学习的假阴性问题会破坏嵌入空间的连续性，影响跨语言对齐的平滑性，无法兼顾翻译、检索、分类等多类任务的均衡表现。

### 方法关键点
- 任务感知损失路由：仅对翻译类平行句对启用**Flow Matching**学习跨语言连续变换，分类、检索、配对分类任务分别适配多正例InfoNCE损失、硬负样本margin损失等目标，避免统一优化的冲突
- 双Teacher正则：点级对齐student与frozen teacher的单样本embedding余弦相似度，批次级对齐两者的pairwise相似度矩阵，保留预训练模型的全局语义结构
- 三阶段课程学习：Stage1仅用平行语料做跨语言对齐，Stage2引入分类/配对分类任务+23%翻译回放buffer，Stage3加入检索任务+41%前序回放buffer+SimCSE风格单语言一致性正则
- 分层采样策略：限制各数据集的训练样本上限，跨语言均匀采样，避免大语料/高资源语言的梯度碾压小任务/小语种

### 关键实验
在Indic MTEB（覆盖22种印度语言、7类任务）上测评，对比Harrier-0.6B、Qwen3-Embedding-8B等主流base模型，分别获得5.45%、2.72%的整体指标提升，其中聚类任务最高提升21.03个点，跨语言STS、双向文本挖掘任务均实现稳定正向提升。

### 核心结论
匹配损失函数与任务底层语义特性的任务感知优化，是多语言表征学习的高效策略。
