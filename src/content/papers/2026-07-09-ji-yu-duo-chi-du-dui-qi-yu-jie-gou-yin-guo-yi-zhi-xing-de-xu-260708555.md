---
title: 'CAAD: Causality-Aware Multivariate Time Series Anomaly Detection via Multi-Scale
  Alignment and Structural Causal Consistency'
title_zh: 基于多尺度对齐与结构因果一致性的因果感知多变量时序异常检测
authors:
- Xin Wang
- Yunshi Wen
- Yanan He
- Haotian Xu
- Youlan Zhao
- Michel Ferreira Cardia Haddad
- Tengfei Ma
affiliations:
- Stony Brook University
- Rensselaer Polytechnic Institute
- Yale University
- Queen Mary University of London
arxiv_id: '2607.08555'
url: https://arxiv.org/abs/2607.08555
pdf_url: https://arxiv.org/pdf/2607.08555
published: '2026-07-09'
collected: '2026-07-12'
category: Other
direction: 多变量时序异常检测 · 因果一致性校验
tags:
- Time Series
- Anomaly Detection
- Causality
- Multi-Scale Alignment
- Causal Consistency
one_liner: 提出因果感知多变量时序异常检测框架CAAD，通过格兰杰因果一致性检验捕捉系统潜在异常
practical_value: '- 可迁移到电商多业务指标（流量/CTR/CVR/GMV）异常检测场景，用因果一致性替代单纯时序相似性判据，更易识别流量作弊、链路故障等隐性异常

  - 多尺度对齐trick可复用在多时间粒度时序特征融合场景，适配小时级/天级/周级等不同统计周期的业务指标建模

  - 因果偏差量化方法可辅助异常根因分析，通过定位拓扑关系断裂点快速缩小异常排查范围，降低运维成本'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有多变量时序异常检测方法仅聚焦表征的时序相似性，忽略系统内部因果关系断裂这一故障核心特征，难以捕捉潜伏性异常。
### 方法关键点
1. 将异常检测重构为对外生变量的格兰杰因果一致性持续验证任务，把外生时序变量建模为残差，将异常定义为外部干预导致的显著偏差
2. 引入多尺度对齐模块建模系统动态演化规律，基于梯度矩阵监控内部因果关系断裂
3. 同时量化动态演化、关系拓扑两类因果偏差，捕捉细微因果偏移
### 关键结果
在真实工业数据集上表现优于多数SOTA基线，实现高精度异常检测
