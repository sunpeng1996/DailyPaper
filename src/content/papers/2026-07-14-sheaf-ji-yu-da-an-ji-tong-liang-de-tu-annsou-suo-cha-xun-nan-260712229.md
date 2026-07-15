---
title: 'SHEAF: Self-profiled Hardness Estimation from Answer-set Flux for Predicting
  Query Hardness in Graph-based ANN Search'
title_zh: SHEAF：基于答案集通量的图ANN搜索查询难度预测方法
authors:
- Dongfang Zhao
arxiv_id: '2607.12229'
url: https://arxiv.org/abs/2607.12229
pdf_url: https://arxiv.org/pdf/2607.12229
published: '2026-07-14'
collected: '2026-07-15'
category: Other
direction: 图ANN搜索 · 查询难度预测
tags:
- ANN Search
- Query Difficulty Estimation
- HNSW
- CAGRA
- Efficiency Optimization
one_liner: 提出SHEAF查询难度估计方法，低成本预测图ANN搜索所需最优波束宽度
practical_value: '- 电商向量搜索场景可复用SHEAF思路，动态调整ANN搜索波束宽度，在保障召回率的前提下提升QPS，降低算力成本

  - 仅需两次浅探针搜索即可完成难度预估，无需额外标注训练，工程落地成本低，可直接对接HNSW/CAGRA等主流ANN索引

  - 可推广至多模态向量检索、推荐系统召回阶段的动态算力分配，对高难度查询倾斜算力保障效果'
score: 8
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有图基ANN搜索采用全局固定波束宽度权衡召回率与吞吐，但不同查询达到相同召回所需波束宽度差异可达32倍，静态几何属性LID对最小波束的预测相关性极弱，无法实现动态算力分配。
### 方法关键点
提出SHEAF难度度量，将查询难度定义为两次不同浅探针宽度下top-k返回结果集的通量（变化程度），基于该特征构建无需真值的自画像估计器，直接输出单查询所需最优波束宽度。
### 关键结果
在4类公开数据集、CAGRA/HNSW等主流ANN索引的CPU/GPU环境测试中，SHEAF预测相关性优于5种基线方法最高达1.55倍，仅需两次浅探针搜索，无查询时真值依赖。
