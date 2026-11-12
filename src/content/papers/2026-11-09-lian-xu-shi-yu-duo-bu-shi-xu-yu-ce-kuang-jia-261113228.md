---
title: Continuous Horizon Forecasting
title_zh: 连续时域多步时序预测框架
authors:
- Malcolm Wolff
- Elliott Zackrone
- Souhaib Ben Taieb
- Michael W. Mahoney
- Kin G. Olivares
affiliations:
- Amazon
- University of California, Berkeley
- Mohamed bin Zayed University of Artificial Intelligence
arxiv_id: '2611.13228'
url: https://arxiv.org/abs/2611.13228
pdf_url: https://arxiv.org/pdf/2611.13228
published: '2026-11-09'
collected: '2026-11-12'
category: Other
direction: 时序预测 · 多时域策略优化
tags:
- TimeSeriesForecasting
- MultiHorizonForecasting
- ContinuousOperator
- BiasVarianceDecomposition
- InferenceOptimization
one_liner: 将多时域预测从离散索引重构为查询变量的连续算子范式，降低估计方差并支持任意时域查询
practical_value: '- 电商销量、流量、库存多时域预测场景可直接复用CH范式，替换原有离散多步预测策略，支持任意时间点按需查询，无需为每个时域单独训练模型

  - 大促等临时需要预测未训练时域的场景，用CH无需重新训练即可输出插值/外推结果，大幅降低业务迭代成本

  - CH的低方差特性可提升长尾、小样本时序预测稳定性，适合商家侧小体量销量、客单价等预测场景'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有多时域预测均采用离散策略，存在误差累积、无法按需查询任意时域、估计方差高的问题，难以适配电商大促等灵活多变的业务预测需求。
### 方法关键点
1. 提出连续时域（CH）策略，将预测定义为连续算子，把预测时域作为查询变量而非固定索引，统一覆盖递归、直接、多步三类现有预测范式
2. 配套给出通用算子逼近定理、连续时域偏差-方差分解的理论支撑，形式化证明CH相较离散策略的估计方差优势
### 关键结果
在M系列基准的16个大规模数据集上验证，RMSE精度与SOTA离散策略持平，同时独有并行推理、目标时域按需查询、未见时域插值/外推能力
