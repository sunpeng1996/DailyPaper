---
title: 'Beyond Distributional Fidelity: Causal-Penalized Diffusion for Synthetic Tabular
  Data'
title_zh: 超越分布保真：面向结构化表格合成的因果惩罚扩散模型
authors:
- Lan Tao
- Yongxian He
- Shirong Xu
- Yidong Ouyang
- Guang Cheng
affiliations:
- University of California, Los Angeles
- University of California, San Diego
- Xiamen University
arxiv_id: '2610.11407'
url: https://arxiv.org/abs/2610.11407
pdf_url: https://arxiv.org/pdf/2610.11407
published: '2026-10-08'
collected: '2026-10-10'
category: Other
direction: 结构化表格生成 · 因果正则优化
tags:
- Tabular Data Generation
- Diffusion Model
- Causal Regularization
- Generative Model
- Causal Fidelity
one_liner: 为表格扩散生成模型添加因果差异惩罚，兼顾统计保真度与因果保真度
practical_value: '- 电商用户/行为表格数据扩增场景，可在TabDDPM等扩散生成目标中加入因果效应差异惩罚，避免生成数据丢失核心业务因果关系（如营销优惠->转化率的因果关联）

  - 做A/B测试仿真、反事实策略评估时，采用该方法生成的合成数据因果一致性更高，可降低因因果错配导致的模拟结论偏差

  - 现有表格生成模型可直接接入该因果惩罚模块，无需大幅重构原有模型架构，落地成本低'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有合成表格生成模型仅优化分布保真，统计相似性无法保证保留真实数据的因果效应，不能满足反事实推断、A/B仿真等对因果一致性有要求的场景。
### 方法关键点
1. 定义因果保真度为真实/合成数据上目标估计量的推断分布差异，理论证明高统计保真不必然带来高因果保真
2. 提出因果感知训练框架，在生成目标中添加因果差异惩罚项，基于TabDDPM实例化因果惩罚扩散模型，采用on-policy得分函数估计器优化
3. 证明了因果正则可提升期望因果保真的适用边界条件
### 关键结果
在多组处理效应仿真实验和2个基准数据集上，因果保真度显著提升的同时，统计保真度保持业内可比水平
