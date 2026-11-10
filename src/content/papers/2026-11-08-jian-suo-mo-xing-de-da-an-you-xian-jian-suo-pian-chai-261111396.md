---
title: Search-by-Answer Bias in Retrieval Models
title_zh: 检索模型的答案优先检索偏差
authors:
- Adiel Avigad
- Shauli Ravfogel
- Yoav Goldberg
affiliations:
- Bar-Ilan University
- NYU Center for Data Science
arxiv_id: '2611.11396'
url: https://arxiv.org/abs/2611.11396
pdf_url: https://arxiv.org/pdf/2611.11396
published: '2026-11-08'
collected: '2026-11-10'
category: RAG
direction: RAG 检索模块偏差分析
tags:
- DenseRetrieval
- BiasAnalysis
- RAG
- Embedding
- KnowledgeConflict
one_liner: 验证8种主流密集检索模型普遍存在优先召回包含已知答案段落的答案优先检索偏差
practical_value: '- 电商RAG导购/客服检索场景需新增关系匹配校验逻辑，避免召回包含热门已知答案、但不符合用户查询关系的无效段落

  - 动态商品/时效性资讯检索场景，可在排序阶段加入时效性权重，抵消模型对旧有热门答案的偏好，减少过时信息召回

  - 可复用论文的受控对比实验范式，评估自有业务embedding检索模型的偏差程度，针对性做微调校正'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
密集检索是语义搜索、RAG系统的核心组件，理想状态下应基于查询的语义关系召回匹配段落，但现有检索模型的预训练backbone携带大量世界知识，可能存在优先召回包含模型已知答案的段落的偏差，导致在多答案查询、时效性查询、垂域检索场景下召回错误或过时信息，影响下游任务效果。
### 方法关键点
- 构造两类受控对比实验：对象对比（两段都匹配查询关系，仅答案对象不同，一个是模型已知的标准答案，一个是同类型替代答案）、关系-对象冲突（一段匹配查询关系但用替代答案，一段包含标准答案但关系不匹配）
- 设计对象知识诊断指标，用检索模型的backbone token预测头计算模型对标准答案相对替代答案的偏好得分，验证该得分与检索排序结果的相关性
- 覆盖8种主流检索模型：DPR、Spider系列、Contriever、E5-large、Qwen3-Embedding 4B/8B
### 关键结果
基于LAMA/TREx事实三元组构造数据集，每个模型采样1000组合格样本，同时用QAMPARI多答案数据集做真实场景验证：对象对比场景下，对象知识得分与检索偏好的Pearson相关性达0.21~0.52，E5-large、Qwen3-4B/8B对标准答案段落的偏好率分别达91.5%、90.9%、94.6%；关系-对象冲突场景下，相关性达0.13~0.30，Qwen3-8B最高有65%的概率优先召回包含标准答案但关系错误的段落。
> 最值得记住的结论：越是参数量大、知识丰富的embedding模型，答案优先检索偏差越显著，在垂域、动态、多答案检索场景下必须针对性校正。
