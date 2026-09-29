---
title: When Does Dense Retrieval Need Asymmetric Geometry? A Bias-Variance Theory
  of Shared and Dual Projections
title_zh: 稠密检索何时需要非对称几何：共享与双投影的偏差-方差理论
authors:
- Maojun Sun
- Yancheng Yuan
- Jian Huang
- Ruijian Han
affiliations:
- The Hong Kong Polytechnic University
arxiv_id: '2609.32488'
url: https://arxiv.org/abs/2609.32488
pdf_url: https://arxiv.org/pdf/2609.32488
published: '2026-09-26'
collected: '2026-09-29'
category: RecSys
direction: 稠密检索 · 投影架构动态选择
tags:
- DenseRetrieval
- BiasVariance
- DualProjection
- AsymmetricGeometry
- CARS
one_liner: 提出稠密检索共享/双投影选择的偏差方差边界与CARS选择器，降低49-96%选择regret
practical_value: '- 电商/搜索召回场景适配冻结Embedding时，小样本（训练对<100）优先选共享投影降低过拟合，样本量≥1024且query/item语义分布差异大时选双投影，MS
  MARCO场景下NDCG@10最高可提升2.19%

  - 可直接复用CARS选择器的交叉拟合逻辑：多次拆分训练集分别拟合双/共享投影，通过跨拆分拟合一致性判断是否需要非对称架构，无需额外标注即可集成到现有适配器训练流程

  - 多语言/跨域检索等query和item分布错配大的场景，优先验证双投影效果，分布差越大双投影的性能收益越高，90度错配下收益是0错配的4.6倍

  - 低资源检索适配时不要固定单一投影架构，根据样本量、分布匹配度、投影秩动态选择，相对固定架构最高可降低96%的选择损失'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
稠密检索是RAG、语义搜索、电商召回的核心组件，当前业界适配冻结预训练Embedding时，对选择共享投影还是双投影缺乏量化指导：盲目用双投影易在小样本下过拟合，固定用共享投影会浪费大样本下的性能提升空间，亟需明确的选择边界。
### 方法关键点
- 推导两类投影的精确近似误差：共享投影只能建模对称PSD算子，双投影可拟合任意低秩算子，误差差来自方向信号建模能力的差异
- 建立局部高斯偏差-方差边界：当方向信号平方超过双投影额外自由度的估计成本（$oldsymbol{δ^2 > σ^2*r(2p-r-1)/2}$）时，双投影的泛化风险更低
- 提出CARS选择器：通过多次对半拆分训练集，计算双/共享投影拟合差的交叉一致性，无需假设噪声分布即可自动选择最优架构
### 关键实验
在5个BEIR基准数据集、4个主流预训练Embedding（E5、BGE、GTE、Contriever）上测试：
1. query-document旋转角度从0°升到90°时，双投影相对共享投影的NDCG@10优势提升4.6倍
2. 训练对n=32时共享投影赢13/16测试单元，n≥1024时双投影赢全部32测试单元
3. CARS选择准确率达90.1%，相对固定架构基线降低49-96%的held-out regret
### 核心结论
稠密检索的投影架构没有绝对最优，需同时结合query-item分布匹配度、训练样本量、投影秩三个因素动态决策。
