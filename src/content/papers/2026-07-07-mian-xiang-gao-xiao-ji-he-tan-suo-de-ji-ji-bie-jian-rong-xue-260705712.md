---
title: 'Retrieving a Set, Not Independent Passages: Set-Level Compatibility Learning
  for Efficient Set Exploration'
title_zh: 面向高效集合探索的集级别兼容性学习检索框架
authors:
- Mooho Song
- Jay-Yoon Lee
affiliations:
- Seoul National University
arxiv_id: '2607.05712'
url: https://arxiv.org/abs/2607.05712
pdf_url: https://arxiv.org/pdf/2607.05712
published: '2026-07-07'
collected: '2026-07-08'
category: RAG
direction: RAG检索优化 · 集级别证据兼容性建模
tags:
- Set-Retrieval
- Multi-hop-QA
- RAG
- Compatibility-Learning
- Efficient-Retrieval
one_liner: 提出非LLM的集级别检索框架，兼顾证据兼容性建模与低推理延迟，性能优于传统单段检索
practical_value: '- 电商搭配推荐、多意图query召回等需要组合选择的场景，可借鉴集级别兼容性训练目标，直接对候选组合打分，避免逐点打分忽略互补性的问题

  - 业务RAG系统的多段召回优化可复用ParaSet+SetCE两阶段架构：轻量预计算embedding做候选集生成，小cross-encoder做集级别重排，平衡延迟与效果

  - 广告素材组合投放、推荐页商品组选品等场景，可复用论文的候选集构造方法（增/删/换黄金集合生成负例+margin排序损失），大幅降低组合优化的标注成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
多跳QA、RAG等任务需要联合选择多段互补证据，传统逐段独立打分或局部序贯决策无法建模段间兼容性，易出现单段相关但组合无效的问题；现有LLM-based集合选择方案计算成本过高，无法落地到延迟敏感的业务场景。

### 方法关键点
- 把多跳检索定义为query-集合兼容性打分问题，提出模型无关的margin排序损失：通过对黄金证据集做增/删/换扰动构造不同质量的负例，优先优化召回再兼顾精度，训练模型对完整兼容集合打更高分
- 两阶段高效集检索架构：ParaSet轻量打分器基于预计算的bi-encoder embedding做浅层自注意力交互，结合beam搜索快速探索候选集合，支持KV cache加速；SetCE是cross-encoder重排器，用相同的集级别目标训练，对ParaSet输出的候选集做精细打分
- 集级别检索和传统单段检索结果天然互补，直接合并两者输出可进一步提升整体效果

### 关键实验结果
在HotpotQA、2WikiMultiHop、MuSiQue三个多跳QA基准上测试，对比bi-encoder、单段cross-encoder、序贯检索等baseline：ParaSet+SetCE配合单段CE5的组合方案，在HotpotQA上EM达到42.9%，比CE10高2.8个百分点，推理延迟仅0.196s/query，比LLM-based集选择快10.7倍，比多步Agent检索快44倍。

最值得记住的结论：集级别检索不是单段检索的替代品，而是互补组件，两者结合可在几乎不增加过多延迟的前提下，大幅提升需要多证据组合的任务效果。
