---
title: 'Beyond Relevance-Centric Retrieval: Rubric-Oriented Document Set Selection
  and Ranking'
title_zh: 超越相关性导向检索：基于评分准则的文档集选择与排序
authors:
- Kailin Jiang
- Lei Liu
- Jian Xi
- Hui Xu
- Junlin Liu
- Baochen Fu
- Shaoqing Ren
- Bin Li
- Vichwang
- Yu Lu
affiliations:
- 中国科学技术大学
- 腾讯元宝团队
- 中国科学院大学
- 山东大学
arxiv_id: '2607.19747'
url: https://arxiv.org/abs/2607.19747
pdf_url: https://arxiv.org/pdf/2607.19747
published: '2026-07-21'
collected: '2026-07-23'
category: RAG
direction: RAG检索优化 · 文档集评估
tags:
- RAG
- Retrieval
- Document Reranking
- Evaluation Benchmark
- Rubric
one_liner: 提出覆盖9维度的文档集评估基准与免训练的评分准则导向文档选排方法
practical_value: '- 优化电商/客服Agent的RAG检索模块时，可在原有相关性评估基础上补充冗余、冲突、互补性3个跨文档维度，减少上下文浪费，降低LLM幻觉

  - 可复用三级九维rubric设计思路，针对业务场景生成query专属评估准则，直接作为免训练的文档选择信号，无需额外标注训练数据

  - reranker选型参考：单轮短问答场景选setwise类reranker，多轮长文本/商品咨询场景选推理增强型reranker，避免跨场景泛化不足'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统检索评估以单文档相关性为核心，通过nDCG聚合得分，完全忽略文档间冗余、冲突、互补性等交互关系。RAG/Agent场景下检索的文档集直接输入LLM，集合质量决定下游生成质量上限，原有评估体系既无法精准诊断检索瓶颈，也无法为优化提供明确方向。

### 方法关键点
- 推出**SETWISEEVALKIT**评估基准，覆盖文档级（相关性、真实性、质量）、集合级（互补性、冗余、冲突）、全局级（完备性、密度、可达性）三级9维度，包含28K高质量query专属评估rubric，适配短问答、长文本两类场景
- 提出**RUBRIC4SETWISE**免训练选排方法，直接将rubric评估准则转化为文档选择信号，自适应选择最优文档子集，无需额外标注与训练

### 关键实验
- 数据集：短问答场景覆盖HotpotQA等4个多跳QA数据集共2061样本，长文本场景覆盖ResearchQA的200个多轮搜索实例
- 对比12款主流reranker：现有方法rubric覆盖率最高仅45%，跨文档协调维度表现普遍较差，无单一方法能在两类场景同时登顶
- RUBRIC4SETWISE在短问答场景平均仅用2.66篇文档，EM较次优方法高0.97、F1高0.62；长文本场景仅用20.52篇文档、4.52轮搜索，LLM裁判得分较次优高3.49分，均为SOTA

### 核心结论
检索系统的优化目标应该从「召回相关文档」转向「组装最优文档集」，rubric导向的评估-优化闭环能以更低的资源消耗获得更好的下游生成效果
