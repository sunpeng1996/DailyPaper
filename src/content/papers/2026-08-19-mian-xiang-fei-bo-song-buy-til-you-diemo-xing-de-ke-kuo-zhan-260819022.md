---
title: Scalable Amortized Variational Inference for Non-Poisson Buy-'Til-You-Die Models
title_zh: 面向非泊松Buy-'Til-You-Die模型的可扩展摊销变分推理
authors:
- Sulagna Ghosh
- Aaron Schein
affiliations:
- The University of Chicago
arxiv_id: '2608.19022'
url: https://arxiv.org/abs/2608.19022
pdf_url: https://arxiv.org/pdf/2608.19022
published: '2026-08-19'
collected: '2026-08-20'
category: RecSys
direction: 用户生命周期价值预测 · 大规模客户行为建模
tags:
- BTYD
- Amortized Variational Inference
- Customer Lifetime Value
- Weibull Renewal Process
- User Behavior Modeling
one_liner: 提出基于Weibull更新过程的WTYD模型，将非泊松BTYD拟合速度提升千倍且精度无损
practical_value: '- 非契约型电商的复购预测、CLV预估、用户分层场景可直接替换原有泊松假设的BTYD模型，同时支持规律型（订阅）、聚类型（大促集中下单）购买行为建模，推理速度相比MCMC类非泊松方案提升2个数量级以上

  - 摊销变分推理+重参数梯度+Rao-Blackwell化降方差的组合范式，可直接迁移到其他大规模概率用户行为建模场景，无需逐客拟合参数，可直接适配千万级以上用户规模的GPU并行训练

  - 用Weibull分布替代Gamma分布、在保留建模表达性的同时换取端到端梯度优化能力的思路，可用于其他需要平衡模型解释性与工业级可扩展性的概率模型改造'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
传统BTYD（Buy-'Til-You-Die）客户行为模型普遍假设交易服从泊松过程，无法刻画用户购买的规律性（如订阅型用户固定周期复购）或聚类性（如大促期集中下单）；现有非泊松BTYD扩展依赖MCMC推理，拟合千万级用户需要数天，无法满足大规模电商业务的实时性需求。
### 方法关键点
- 提出WTYD（Wei-'Til-You-Die）模型，用Weibull更新过程替换原有非泊松模型的Gamma更新过程，二者建模能力相近但Weibull的解析特性支持端到端梯度优化；
- 采用摊销变分推理框架，通过识别网络输出每个用户的变分参数，无需逐客单独拟合，天然适配GPU并行加速；
- 变分分布采用Weibull族结合重参数梯度，叠加Rao-Blackwell化降低梯度方差，还支持直接扩展用户侧协变量特征。
### 关键结果
500万电商用户数据集拟合仅需8分钟，对比当前SOTA的Pareto/GGG模型（预估需3-4天）速度提升超500倍，预测精度无明显损失；400万美国大选捐赠者公开数据集验证了协变量扩展的有效性，模拟实验证实参数与隐变量恢复效果与SOTA相当。
### 核心结论
在概率建模中通过微小的分布假设调整换取工程可扩展性，可在几乎不损失建模效果与可解释性的前提下，将千万级用户行为建模的耗时从天级压缩到分钟级，完全适配工业级业务需求
