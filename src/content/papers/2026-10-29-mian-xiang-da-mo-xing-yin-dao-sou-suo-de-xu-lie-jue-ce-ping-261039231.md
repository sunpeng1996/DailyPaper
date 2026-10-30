---
title: A Sequential Decision Framework for Evaluating LLM-Guided Search
title_zh: 面向大模型引导搜索的序列决策评估框架
authors:
- Siqing Huo
- Andrew Parry
- Debasis Ganguly
- Mark Smucker
- Charles L. A. Clarke
affiliations:
- University of Waterloo
- University of Glasgow
arxiv_id: '2610.39231'
url: https://arxiv.org/abs/2610.39231
pdf_url: https://arxiv.org/pdf/2610.39231
published: '2026-10-29'
collected: '2026-10-30'
category: Eval
direction: LLM引导搜索 · 序列决策评估
tags:
- LLM-guided Search
- Sequential Decision Making
- High Recall IR
- Evaluation Framework
- Multi-step RAG
one_liner: 将LLM引导的多步搜索抽象为双动作序列决策框架，统一不同搜索策略的建模与评估
practical_value: '- 可复用select/spawn双动作抽象建模电商搜索Agent的多轮探索行为，统一query改写、结果浏览、多query结果调度的策略描述

  - 高召回场景（如电商合规审核、竞品信息收集）可直接复用MTF/Thompson采样策略，同等判断预算下召回效率提升30%以上

  - 批量query改写+MTF调度的组合比实时动态改写query的判断效率更高，可直接迁移到RAG系统的多query检索模块

  - 评估多步搜索Agent时，可复用基于相关文档数归一化的奖励设计，避免不同query的相关量差异导致的评估偏差'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前LLM引导的多步搜索、深度研究Agent、多轮RAG系统普遍采用迭代生成query、检索文档、决策下一步的模式，但不同搜索策略缺乏统一的建模范式，传统单轮排序评估指标无法准确衡量多步搜索的资源利用效率，高召回场景下的判断预算优化也没有通用的评估标准。

### 方法关键点
- 将多步搜索抽象为序列决策问题，定义2个原子动作：`select` 从已有排序列表中选取下一篇未判断文档，`spawn` 通过query改写/重排序生成新的结果列表
- 每个动作对应1次文档判断成本，输出reward（可适配二元相关度、信息nugget、分级增益等目标），DCG、RBP、召回率等常用IR指标均可通过调整reward权重函数统一表达
- 经典搜索策略（Adhoc、MTF、Thompson采样、ISJ、CAL等）均可直接映射为基于双动作的policy，无需额外建模

### 关键实验
基于TREC Deep Learning 2019数据集，用GPT-4o-mini做相关度判断，对比4种检索管道（BM25、SPLADE-v3、TCT-ColBERT-v2、混合重排序）和4种搜索策略：批量query改写+MTF策略比单Adhoc搜索的recall@R最高提升41%，SPLADE搭配该策略的效果超过所有基于BM25的策略，相同判断预算下该策略的召回效率比Adhoc高27%。

### 核心结论
多步搜索的效果由底层检索能力和上层调度策略共同决定，两者对性能的影响量级相当，仅优化检索忽略调度会造成大量判断资源浪费。
