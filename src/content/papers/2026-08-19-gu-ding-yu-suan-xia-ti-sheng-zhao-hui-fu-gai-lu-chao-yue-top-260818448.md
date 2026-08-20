---
title: 'More Context, Same Budget: Dual-Bounded Relational Recall Beyond Top-K Retrieval'
title_zh: 固定预算下提升召回覆盖率：超越Top-K的双边界关系召回
authors:
- Thomson D. Nguy
affiliations:
- Radiant Institute for Manifold Studies (RIMS)
arxiv_id: '2608.18448'
url: https://arxiv.org/abs/2608.18448
pdf_url: https://arxiv.org/pdf/2608.18448
published: '2026-08-19'
collected: '2026-08-20'
category: RAG
direction: RAG · 召回预算分配优化
tags:
- Retrieval
- RAG
- Graph Retrieval
- Top-K
- Budget Allocation
one_liner: 固定检索预算下，相关性种子加图邻接上下文分配策略比平级Top-K完整证据召回率高23.8个百分点
practical_value: '- 做RAG问答/商品多跳检索场景时，可拆分固定上下文预算：一部分给Top-K高相关性结果，剩余配额分配给高相关结果的图邻接关联内容，在不增加成本的前提下提升完整召回率

  - 多跳查询（如电商场景"找适合1岁宝宝穿的奥特曼IP羽绒服"）可优先启用关系召回策略，单维度对比查询可保持原有Top-K策略，最大化收益同时减少bad case

  - 召回效果评估可新增「完整支持证据召回率」指标，替代单一的召回率/precision，更贴合下游LLM/推荐系统需要完整证据链的诉求

  - 做策略迭代时可采用配对对照设计，固定排序阶段、预算上限，仅调整分配规则，能精准量化策略本身的收益，排除其他变量干扰'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG/检索系统默认采用平级Top-K截断分配上下文预算，当证据存在依赖关系（如多跳推理需要A的关联信息B才能完整回答）时，Top-K会遗漏低独立相关性但关键的关联证据，而增大预算又会超过上下文窗口限制，因此需要在固定预算下优化上下文分配策略，提升完整证据召回能力。

### 方法关键点
- 提出双边界关系召回（DBRR）框架，固定检索对象数、token数双重预算上限，将预算拆分为两部分：一部分分配给相关性排序得到的种子结果，剩余配额用于提取种子的图邻接关联上下文
- 采用配对对照设计：实验组和对照组共享完全相同的相关性排序阶段、预算上限，仅上下文分配规则不同（对照组为平级Top-K截断）
- 评估核心指标为「完整支持证据召回率」：仅当召回上下文包含回答所需全部官方证据时才算命中，比传统部分召回指标更严格

### 关键实验
- 数据集：HotpotQA FullWiki共7405条问题，其中桥接类（多跳）问题5918条，对比类问题1487条
- 对比基线：同排序阶段、同预算的平级Top-K召回
- 核心结果：DBRR完整证据召回率较基线提升23.8个百分点，其中桥接类问题提升28.7个百分点，仅192个问题效果劣于基线；对比类问题提升4.2个百分点，未达预设显著性阈值

检索质量不仅取决于item的相关性得分排序，更取决于有限上下文预算如何围绕已找到的高相关内容做分配，而非无脑取Top-K。
