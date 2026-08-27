---
title: 'Query Expansion Is More Than Generation: Improving Dense Retrieval through
  Better Integration'
title_zh: 查询扩展不止是生成：优化整合策略提升稠密检索效果
authors:
- Siyuan Sun
- Mihai Surdeanu
affiliations:
- University of Arizona
arxiv_id: '2608.25521'
url: https://arxiv.org/abs/2608.25521
pdf_url: https://arxiv.org/pdf/2608.25521
published: '2026-08-26'
collected: '2026-08-27'
category: QueryRec
direction: 查询扩展 · 稠密检索优化
tags:
- Query Expansion
- Dense Retrieval
- LLM
- Zero-Shot
- Vector Interpolation
one_liner: 提出无训练AnchorQE框架，向量层插值查询与扩展内容，无监督校准系数提升稠密检索性能
practical_value: '- 电商搜索query扩展场景可直接替换传统拼接方案：原query与LLM生成的扩展内容分别编码后做向量插值，无需重训召回模型、修改索引，零成本适配现有链路

  - 无监督插值系数校准方法可直接复用：取流量前8条无标注query的检索结果，计算扩展的检索强度和与原query检索结果的一致性乘积作为系数，无需标注数据

  - 单向量输出方案比多流召回后融合latency低95%以上，适配高QPS的电商搜索/推荐场景，不需要改造现有稠密索引架构

  - 若LLM生成的扩展质量不稳定，可默认采用0.15左右的小插值系数，在不损失原query检索效果的前提下小幅提优，避免扩展带偏召回结果'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM 可零样本生成查询扩展内容，但传统拼接或仅用扩展的整合方式，常导致冻结稠密检索效果下降，过往研究多聚焦生成内容优化，对扩展的整合策略缺乏系统探索。

### 方法关键点
- AnchorQE 方案：原查询与扩展内容分别经 query encoder 编码、归一化后，线性插值再归一化得到最终查询向量，无需重训模型、修改索引，单向量输出适配现有稠密检索链路
- SC-AnchorQE 无监督系数校准：取前8条无标注查询的检索结果，计算扩展自身top1检索强度、扩展与原查询top10检索结果一致性，两者乘积作为插值系数α，后续固定系数服务
- 理论证明该插值方案与加权 CombSUM 分数融合的排序结果等价，同时有角度边界约束，避免扩展大幅偏离原查询意图

### 关键实验
覆盖 TREC-DL、LoTTE、BEIR 三大检索基准，对比传统拼接、扩展-only、QuDAR 等基线，相同扩展内容下，AnchorQE 比传统整合方法最高提升12.89%，无监督校准的系数比开发集调优的固定系数最高高3.81%，单向量检索 latency 比多流融合低95%以上。

### 核心结论
查询扩展的效果不仅取决于生成内容质量，整合方式的影响甚至更大，合理的整合策略可让相同扩展内容从负收益转为正收益。
