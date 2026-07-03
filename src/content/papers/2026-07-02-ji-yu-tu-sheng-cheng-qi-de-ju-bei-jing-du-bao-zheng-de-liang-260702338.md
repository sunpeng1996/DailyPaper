---
title: HNSW with Accuracy Guarantees Using Graph Spanners -- A Technical Report
title_zh: 基于图生成器的具备精度保证的HNSW向量检索技术
authors:
- Minghao Li
- Raghav Mittal
- Sanjivni Rana
- Suraj Shetiya
- Gautam Das
- Nick Koudas
affiliations:
- University of Toronto
- The University of Texas At Arlington
- IIT Bombay
arxiv_id: '2607.02338'
url: https://arxiv.org/abs/2607.02338
pdf_url: https://arxiv.org/pdf/2607.02338
published: '2026-07-02'
collected: '2026-07-03'
category: RecSys
direction: 向量召回 · HNSW精度增强
tags:
- HNSW
- Approximate Nearest Neighbor
- Graph Spanner
- Recall Guarantee
- Vector Search
one_liner: 提出Certify-then-Rectify分层框架，为工业标准HNSW向量检索提供可调控的理论召回精度保证
practical_value: '- 现有HNSW召回链路可轻量接入Certify-then-Rectify框架做分层降级：先跑标准HNSW，用搜索trace特征做置信度校验，置信度达标直接返回，不达标再走精确检索，兼顾
  latency 和召回率，适合电商搜索、RAG 知识库检索等高阶场景

  - 提出的MBV剪枝技巧（递归下界剪枝+椭圆搜索空间剪枝）可直接复用在现有ANN的精确检索分支，实测能减少25%+的距离计算量，降低精确检索的 latency
  开销

  - 基于EVT的HNSW拉伸因子预估方法可用来评估现有HNSW索引的构建质量，当拉伸因子超过阈值时调整M、ef_construction等超参数，提升基线HNSW的召回稳定性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
HNSW是工业界向量检索的标准方案，但其贪心遍历的启发式逻辑无理论召回保证，高维空间下易陷入局部最优；电商高召回检索、RAG医疗/法律知识库检索等场景对精度要求高，仅95%左右的召回率无法满足需求，传统调大HNSW超参数的方案会线性提升延迟，也无法提供绝对精度保证。
### 方法关键点
- 采用Certify-then-Rectify分层架构：先运行标准HNSW得到候选集，基于Conformal Risk Control的无分布校验器，通过搜索trace的距离特征、路径稳定性特征判断候选集质量，达标则直接返回，否则触发精确检索分支
- 精确检索分支将HNSW底层图视为几何spanner，基于极值理论（EVT）采样预估图的最大经验拉伸因子，构造动态搜索半径保证真kNN全部落在搜索范围内
- 设计MBV剪枝机制：通过递归下界剪枝、椭圆搜索空间剪枝两种策略，大幅减少精确检索阶段的距离计算量，降低延迟
- 整体框架可作为现有HNSW实现的轻量wrapper，无需修改原有构建、搜索逻辑
### 关键实验结果
在SIFT1M、GIST1M、DEEP1M等标准向量数据集上测试，相比无剪枝的精确检索，MBV可将距离计算量降低到总节点数的2.5%~15%；目标召回率90%的设置下，整体框架的平均延迟仅为普通HNSW的1.1~1.5倍，同时提供严格的统计召回保证。

最值得记住的一句话：不需要完全替换现有HNSW链路，仅通过后置校验+按需精确检索的分层设计，就能以极小的平均延迟开销，为向量检索提供可调控的理论精度保证。
