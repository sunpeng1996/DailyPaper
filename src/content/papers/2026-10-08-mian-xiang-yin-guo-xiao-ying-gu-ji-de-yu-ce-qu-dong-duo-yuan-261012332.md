---
title: Prediction-Powered Data Fusion for Treatment Effect Estimation
title_zh: 面向因果效应估计的预测驱动多源数据融合方法
authors:
- Yonghan Jung
- Shu Yang
affiliations:
- University of Illinois Urbana-Champaign
- North Carolina State University
arxiv_id: '2610.12332'
url: https://arxiv.org/abs/2610.12332
pdf_url: https://arxiv.org/pdf/2610.12332
published: '2026-10-08'
collected: '2026-10-10'
category: Other
direction: 因果效应估计 · RCT与观测数据融合
tags:
- Causal Inference
- Treatment Effect Estimation
- RCT
- Observational Study
- Data Fusion
one_liner: 无特殊假设前提下融合小样本RCT与大样本观测数据，产出无偏且更高精度的ATE、CATE估计器
practical_value: '- 电商AB测试场景可复用该框架，融合小流量RCT实验数据与全量用户观测行为数据，在保证效果评估无偏的前提下提升估计精度，大幅降低AB实验所需的流量成本

  - 做用户异质性策略收益分析时，可直接复用DR-Fusion/R-Fusion方法计算不同分层的策略增益，无需假设观测数据无混淆，更贴合电商复杂场景的真实数据特征

  - 策略迭代效果预判场景可借鉴「无偏性保留+大样本精度增强」的融合思路，结合小流量验证数据与历史全量数据，快速得到更可靠的策略收益估计'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
小样本RCT可输出无偏因果效应但样本量不足导致精度低，大样本观测数据量级充足但存在混淆偏差，现有融合方案要么对观测数据有强假设，要么无法保障估计无偏，且异质性因果效应（CATE）相关研究缺口大。
### 方法关键点
1. 提出无额外观测数据假设的融合框架，保留RCT估计无偏性的同时借大样本观测数据提升估计精度
2. 实现带闭式权重、置信区间的平均因果效应（ATE）估计器AIPW-Fusion
3. 推出两款CATE学习器DR-Fusion、R-Fusion，无需假设观测数据无混淆，也不需要显式建模混淆函数
### 关键结果
实验验证相比SOTA方法，ATE估计精度提升22%-38%，CATE估计MSE降低25%-42%，且全程保持估计无偏
