---
title: 'Route Me If You Can: A Benchmark for Query Reformulation Selection'
title_zh: QueryRoute：面向LLM查询改写选择的标准化基准数据集
authors:
- Hai Son Le
- Negar Arabzadeh
- Amin Bigdeli
- Radin Hamidi Rad
- Sajad Ebrahimi
- Charles L. A. Clarke
- Ebrahim Bagheri
affiliations:
- Toronto Metropolitan University
- University of California, Berkeley
- University of Waterloo
- Mila - Quebec AI Institute
- University of Toronto
arxiv_id: '2609.14885'
url: https://arxiv.org/abs/2609.14885
pdf_url: https://arxiv.org/pdf/2609.14885
published: '2026-09-14'
collected: '2026-09-16'
category: QueryRec
direction: 查询改写选择 · 检索系统基准构建
tags:
- QueryReformulation
- Retrieval
- Benchmark
- LLM
- QueryRouting
one_liner: 发布标准化LLM查询改写选择基准QueryRoute，冻结昂贵中间件支持跨方法可复现对比
practical_value: '- 电商搜索/RAG系统可参考自适应query改写选择框架，针对不同query、检索器（BM25/稠密向量）选择最优改写策略，无需重新训练改写模型即可提升检索效果

  - 工程上可直接复用基准中的改写策略池（10种LLM改写+原query）和selector选型逻辑：BM25检索场景优先选LLM-as-judge selector，稠密检索场景直接用固定最优改写即可，避免额外路由开销

  - 评估指标可复用决策质量维度：除了常规检索指标外，增加near-oracle率、help/hurt率，避免平均指标掩盖单query劣化问题'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM查询改写没有通用最优策略，不同query、领域、检索器下最优改写差异大，但现有研究因候选池、检索配置、标注规则不一致无法横向对比，缺少标准化基准支撑可复现的改写选择研究。

### 方法关键点
- 构建QueryRoute基准，冻结所有昂贵中间件：覆盖3757条查询（含TREC DL、BEIR、BRIGHT三大场景）、11种候选改写（原query+10种LLM改写策略）、5种LLM改写backbone、3种检索器（BM25/SPLADE/BGE），共619905条检索结果和oracle标注
- 定义统一的查询改写选择问题框架，提供8类selector基线：固定策略、监督分类、相似性路由、QPP预测、LLM-as-judge等
- 配套多维度评估体系：除常规nDCG@10等检索指标外，新增near-oracle率、help/hurt率等决策质量指标

### 关键结果
- 可优化空间充足：oracle上限比原query平均提升nDCG@10 24个百分点（TREC DL场景：0.424→0.666），比最优固定改写平均提升10个百分点
- 现有最优selector为LLM-as-judge，BM25场景下比最优固定改写提升nDCG@10 2~3个百分点，仅能覆盖约30%的oracle提升空间
- 稠密检索（BGE/SPLADE）场景下，所有学习型selector效果均不如固定最优改写，无需额外路由开销

### 核心结论
没有通用最优的LLM查询改写策略，自适应选择仅在稀疏检索场景下有收益，更强的检索器会完全抵消改写选择的优化价值
