---
title: 'Revisiting Energy-based Tabular Anomaly Detection: Energy and Reconstruction
  are Complementary'
title_zh: 重访基于能量的表格异常检测：能量与重建信号互补
authors:
- Junichiro Niimi
affiliations:
- Meijo University
arxiv_id: '2608.14186'
url: https://arxiv.org/abs/2608.14186
pdf_url: https://arxiv.org/pdf/2608.14186
published: '2026-08-14'
collected: '2026-08-17'
category: Other
direction: 表格异常检测 · 能量模型集成优化
tags:
- EBM
- DBM
- Anomaly Detection
- Ensemble Learning
- Tabular Data
one_liner: 验证深度玻尔兹曼机能量分数与重建类分数融合可显著提升表格异常检测性能
practical_value: '- 电商风控/反作弊场景可引入DBM能量分数作为现有AE等重建类异常检测模型的互补信号，用秩融合提升效果

  - 多模型集成时优先选择异质性来源的分数（如能量类+重建类），避免同lineage模型融合无增益甚至降效

  - 表格类异常检测任务无需盲目追新SOTA，经典EBM如DBM可作为低成本补充工具纳入基线库'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
当前表格异常检测主流方法（密度代理、重建类、非参数打分器）均间接近似正常样本分布，显式EBM应用极少，受EBM近年深度学习领域复兴启发开展研究。
### 方法关键点
选用双层Deep Boltzmann Machine(DBM)的均值场能量作为异常打分信号，与主流Autoencoder(AE)重建分数通过秩融合做集成，在UCI银行营销、NSL-KDD两个跨领域表格基准上，和8个基线方法做20次随机种子对照实验。
### 关键结果
单DBM能量分数在银行营销数据集上与最强基线AE持平，在NSL-KDD上统计显著优于AE，且显著超过其余7个基线；DBM+AE融合模型在两个数据集上AUROC分别提升0.014（p<0.01）、0.002（p<0.001），其余非EBM类模型与AE融合均无增益甚至降效。
