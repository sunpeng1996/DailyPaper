---
title: 'SIMQ: A Single Graph-based Index for Multi-Vector Query'
title_zh: SIMQ：面向多向量查询的单图索引框架
authors:
- Yifan Lu
- Jiabao Jin
- Xiaoyao Zhong
- Peng Cheng
- Xiangyu Wang
- Haotian Li
- Hua Chen
- Junqing Chen
- Wei Xi
- Heng Tao Shen
affiliations:
- Tongji University
- Ant Group
- Xi'an Jiaotong University
arxiv_id: '2611.22079'
url: https://arxiv.org/abs/2611.22079
pdf_url: https://arxiv.org/pdf/2611.22079
published: '2026-11-17'
collected: '2026-11-18'
category: RAG
direction: RAG · 多向量检索性能优化
tags:
- Multi-Vector Retrieval
- ANN Search
- Graph Index
- ColBERT
- MaxSim
- RAG
one_liner: 基于采样聚类与单图索引实现纯CPU可运行的高性能多向量检索，无需GPU聚类或交互矩阵
practical_value: '- 电商搜索/商品RAG场景下的多向量检索可直接复用SIMQ的CPU索引构建方案，避免GPU聚类的高成本，小数据集Quora场景构建时间仅68s，较PLAID的4282s下降98%以上

  - 推荐粗排阶段若采用多向量语义匹配，可复用SIMQ+的count-based打分+动态候选集策略，解决细粒度聚类下近似分区分度不足问题，避免排序反转，相同参数下Recall@100最高提升12%

  - 现有业务在用的向量检索库（如VSAG、HNSWlib）可直接集成SIMQ架构，兼容多种图索引后端，无需重构现有管线即可快速支持多向量检索能力'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
ColBERT等多向量检索模型通过MaxSim晚交互机制实现SOTA语义匹配精度，是电商搜索/商品RAG/推荐语义召回的核心技术，但原生实现复杂度高、扩展性差。现有加速方案存在显著瓶颈：PLAID依赖GPU做全量语料k-means聚类，查询时需计算全量centroid-query交互矩阵，成本高延迟大；MUVERA等数据无关压缩方案召回不稳定，需要多次重复流水线补偿误差，无法满足工业级场景要求。
### 方法关键点
- 数据感知采样聚类：基于PAG策略从语料token向量中抽样初始质心，通过图导航分配剩余向量，仅对超大簇做递归二分拆分，无需全局迭代k-means，纯CPU即可完成大规模索引构建
- 单图索引架构：对所有簇质心构建单一通用图索引，兼容HNSW/NSG/DPG等多种主流图后端，无需依赖残差压缩存储
- 两级查询优化：基础版SIMQ用质心内积近似MaxSim打分完成粗筛，SIMQ+改用查询token命中次数打分+动态候选集策略，避免细粒度聚类下近似分偏置导致的排序反转
### 关键实验结果
在5个公开基准数据集（NQ/Quora/SciDocs/LoTTE/HotpotQA）上对比PLAID/MUVERA/IGP等基线：相同召回下QPS最高提升2倍以上；Quora数据集索引构建时间仅68秒，较PLAID的4282秒下降98%以上；PAG聚类与k-means召回差距<1%，QPS高3%左右；SIMQ+相同参数下Recall@100较基础版最高提升12%。
最值得记住的结论：纯CPU环境下通过数据感知采样聚类+单图索引即可实现工业级可用的多向量检索能力，无需依赖GPU或交互矩阵计算。
