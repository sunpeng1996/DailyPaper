---
title: 'MediPFN: Amortized In-Context Nuisance Learning and Inference for Causal Mediation
  Analysis'
title_zh: MediPFN：面向因果中介分析的摊销式上下文干扰学习推理框架
authors:
- Shi Bo
- Jiaming Hu
affiliations:
- Department of Mathematics and Statistics, Boston University
arxiv_id: '2611.13219'
url: https://arxiv.org/abs/2611.13219
pdf_url: https://arxiv.org/pdf/2611.13219
published: '2026-11-09'
collected: '2026-11-11'
category: Other
direction: 因果中介分析 · 表格大模型推理优化
tags:
- Causal Mediation Analysis
- Tabular Foundation Model
- In-Context Learning
- Uncertainty Quantification
- Amortized Inference
one_liner: 提出适配预训练表格大模型的因果中介分析框架MediPFN，置信区间更准、速度比bootstrap快59.1倍
practical_value: '- 电商运营策略归因可复用该框架的因果效应拆分逻辑，快速区分策略的直接效果与中介变量传导的间接效果，例如量化优惠活动的直接拉新、通过社交传播的间接拉新占比

  - AB实验显著性评估场景可借鉴其 amortized inference 替代bootstrap的思路，在保证统计准确性的前提下将不确定性量化计算速度提升近60倍，降低算力成本

  - 表格大模型落地因果场景可复用「交叉拟合影响函数估计器+独立误差分位数预测头」的架构，减少多干扰函数拟合叠加的不确定性，提升估计结果可靠性'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
因果中介分析需将处理效应拆分为中介传导的间接路径与其他路径的直接效应，传统基于表格大模型的估计方案构建置信区间时，需同时考虑多个干扰函数拟合、组合引入的不确定性，bootstrap类方法计算成本极高。
### 方法关键点
1. 提出MediPFN摊销推理框架，适配预训练表格大模型完成干扰预测，通过交叉拟合影响函数估计器组合多步预测结果；
2. 新增独立预测头从已知间接效应的模拟表格中学习估计器标准化误差的分位数，结合监督微调、对称化、独立校准输出置信区间，同时给出标准假设下的覆盖边界理论保障。
### 关键结果
实验中MediPFN的置信区间覆盖度显著优于所有对比方法，更接近标称水平；不确定性量化速度比bootstrap快59.1倍。
