---
title: 'Hierarchical Empirical-Bayes Naive Bayes: Minimax Smoothing and Calibration
  with AODE Extension'
title_zh: 分层经验贝叶斯朴素贝叶斯：极小极大平滑与AODE扩展校准
authors:
- Nguyen Thai Anh
- Truong Viet Vu
- Tran Thien Thanh
- Vo Nguyen Quoc Bao
- Ngo Hoang Tu
affiliations:
- Van Lang University
- Ho Chi Minh City University of Transport
arxiv_id: '2608.11162'
url: https://arxiv.org/abs/2608.11162
pdf_url: https://arxiv.org/pdf/2608.11162
published: '2026-08-11'
collected: '2026-08-12'
category: Other
direction: 基础分类器优化 · 高基数离散特征平滑
tags:
- Naive Bayes
- High Cardinality Features
- Smoothing
- Empirical Bayes
- Probabilistic Calibration
one_liner: 提出自适应平滑的HEB-NB及HEB-AODE分类器，提升高基数离散数据的分类精度与校准性能
practical_value: '- 电商/推荐场景下高基数离散特征（商品ID、用户标签、搜索Query等）的概率统计平滑，可替换原有Laplace平滑，采用本文自适应Dirichlet先验平滑方法，降低log-loss

  - CTR/CVR预估等需要概率校准的场景，可采用HEB-NB结合互信息加权的方案，最多降低70%的top-1 ECE，提升排序概率的可信度

  - 轻量级线上分类、召回粗排等低延时需求场景，HEB-AODE保留闭式推理的速度优势，效果优于传统AODE，可直接替换基线'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统朴素贝叶斯（NB）的固定强度平滑（如Laplace）忽略特征基数、样本量、类别不平衡特征，在高基数离散数据上存在不可消除的偏差，严重影响概率输出准确性与校准度。

### 方法关键点
1. 提出分层经验贝叶斯NB（HEB-NB），为每个类-特征条件概率配置Dirichlet先验，通过Type-II极大似然自适应学习先验浓度，保留闭式推理效率的同时实现跨类信息共享；
2. 扩展得到HEB-AODE，将自适应平滑能力迁移到NB的结构松弛版本，适配更复杂的特征依赖场景；
3. 结合互信息加权进一步优化概率校准效果。

### 关键结果
31个UCI/OpenML基准数据集上，HEB-NB的概率类指标平均Friedman排名第一，高基数数据集上log-loss最高下降22.1%；HEB-AODE相对原生AODE实现稳定效果提升；结合互信息加权后top-1 ECE降低41%-70%。
