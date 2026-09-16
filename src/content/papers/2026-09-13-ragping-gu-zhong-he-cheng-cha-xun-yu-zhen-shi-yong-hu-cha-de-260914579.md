---
title: 'Beyond Benchmark Scores: How Synthetic and Authentic Query Distributions Diverge
  in RAG Evaluation'
title_zh: RAG评估中合成查询与真实用户查询的分布差异研究
authors:
- Filip J. Kucia
- Barbara M. Gawlik
affiliations:
- Warsaw University of Technology
- Sparrows AI sp. z o.o.
arxiv_id: '2609.14579'
url: https://arxiv.org/abs/2609.14579
pdf_url: https://arxiv.org/pdf/2609.14579
published: '2026-09-13'
collected: '2026-09-16'
category: Eval
direction: RAG评估 · 合成与真实查询分布对齐
tags:
- RAG
- Evaluation
- Query Distribution
- Hybrid Retrieval
- Deployment Readiness
one_liner: 实证RAG评估中合成与真实查询的分布差异，指出仅依赖合成基准会导致次优架构选择
practical_value: '- 搭建电商/政务类RAG智能客服、搜索助手时，不能仅依赖合成查询做评估，必须提前收集50-100条目标用户的真实小样本query验证效果，避免选到高
  latency 无收益的检索架构

  - 电商搜索、Query 推荐场景离线评估需注意合成/真实query的分布差：用户真实搜索普遍偏短，BM25类稀疏检索的收益可能远低于离线合成长query的测试结果，需平衡
  latency 与实际精度

  - RAG系统上线前必须补充未答案query的拒答、澄清或转人工逻辑，合成基准完全覆盖不到这类场景，电商场景下错误回答会直接导致用户投诉、转化率下跌'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前RAG系统上线前普遍依赖从目标文档库生成的合成查询做离线评估，该方案成本低、易规模化，但隐含分布偏移风险：合成查询无法反映真实用户的行为特征，仅靠其评估可能高估系统效果，甚至选出错误的上线架构，此前缺乏明确的实证量化该差距的影响。

### 方法关键点
- 构建两组对照查询集：1851条Gemini Notebook生成的合成教务查询，322条学生调研收集的真实教务查询
- 从5个维度量化两类查询的分布差：意图分布、查询长度、源文档覆盖度、可评估性、检索指标
- 对比3种主流检索配置的效果：ChromaDB纯稠密检索、Qdrant纯稠密检索、Qdrant混合检索（稠密向量+BM25稀疏检索）

### 关键实验结果
- 真实查询平均长度仅6.8词，为合成查询（15.7词）的43%；真实查询仅覆盖53个文档源，合成查询覆盖165个，真实查询Top3源占比达44.4%，远高于合成的15.1%
- 合成基准下表现最优的混合检索Hit@5达0.896，但在真实查询下Hit@5仅0.527，效果反而低于纯稠密检索的0.545，同时 latency 是最快配置的8倍
- 49%的真实查询无法被静态文档库回答，合成查询完全未覆盖这类拒答场景

### 核心结论
合成基准仅验证RAG系统的理想检索上限，小批量真实用户query才是验证落地鲁棒性、选型最优架构的核心依据
