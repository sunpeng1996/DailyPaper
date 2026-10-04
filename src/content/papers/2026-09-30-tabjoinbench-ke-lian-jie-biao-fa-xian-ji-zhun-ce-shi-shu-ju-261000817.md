---
title: 'TabJoinBench: A Benchmark for Joinable Table Discovery'
title_zh: TabJoinBench：可连接表发现基准测试数据集
authors:
- Sandipan De
- Jin Wang
- Vivek Gupta
affiliations:
- Arizona State University
arxiv_id: '2610.00817'
url: https://arxiv.org/abs/2610.00817
pdf_url: https://arxiv.org/pdf/2610.00817
published: '2026-09-30'
collected: '2026-10-04'
category: Other
direction: 数据湖可连接表发现 · 基准构建
tags:
- TableJoin
- Benchmark
- DataLake
- Evaluation
- FeatureEngineering
one_liner: 构建覆盖三类数据湖场景的可连接表发现基准，配套开源数据集与评估流程
practical_value: '- 做推荐/广告特征工程时，可复用基准的扰动测试方法，验证内部多源异构特征表自动匹配方案的鲁棒性，避免数据质量问题导致的特征拼接错误

  - 基准的query-candidate验证策略可直接迁移到电商场景下的多源数据（用户行为、商品属性、交易、供应链等）可关联表自动发现流程，降低特征挖掘的人力成本

  - 不同类别表匹配方法的横向评估结论可直接参考，根据业务数据特点选择最优的可连接表检索方案，无需重复做对比实验'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有可连接表发现研究均采用自定义基准开展评估，缺乏统一评测体系，公平对比和结果复现难度极高，无法支撑数据湖多场景下的方法选型。
### 方法关键点
1. 覆盖语义、关系、混合三类主流数据湖场景，针对不同数据源设计专用验证策略构造可靠的query-candidate配对；
2. 通过可组合扰动算子系统性引入结构、表示、语义三类改动，在贴近真实数据异构性的同时保证ground truth准确性；
3. 内置基于集合、基于特征、学习式、通用LLM embedding四类代表性方法的评估pipeline，全量数据集、标注、生成流程完全开源。
### 关键结果
完成了四类主流可连接表发现方法的横向效果对比，填补了该领域统一评估基准的空白，可直接用于新方法的快速验证。
