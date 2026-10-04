---
title: 'IQS-BO: In-Context Query Selection for Bayesian Optimisation'
title_zh: 《IQS-BO：面向贝叶斯优化的上下文内查询选择方法》
authors:
- Luca Geminiani
- Nadja Klein
affiliations:
- Scientific Computing Center (SCC), Karlsruhe Institute of Technology (KIT)
arxiv_id: '2610.01269'
url: https://arxiv.org/abs/2610.01269
pdf_url: https://arxiv.org/pdf/2610.01269
published: '2026-10-01'
collected: '2026-10-04'
category: Other
direction: 黑盒优化 · 贝叶斯优化效率提升
tags:
- Bayesian-Optimization
- Prior-Fitted-Network
- In-Context-Learning
- Black-Box-Optimization
- Query-Selection
one_liner: 提出基于监督学习的PFN架构IQS-BO，大幅降低贝叶斯优化查询选择开销且效果优于现有基线
practical_value: '- 推荐/广告系统超参调优场景可复用IQS-BO的低开销查询选择逻辑，替代传统BO的高斯过程+采集函数组合，大幅降低调参耗时

  - 预训练PFN类模型时可复用混合先验构造思路，引入真实业务场景常见的带扭曲输入、窄最优解、平台期的函数样本，提升下游任务适配性

  - 需快速黑盒优化的Agent决策场景（如实时投放策略调整）可引入全上下文IQS-BO，单步前向即可输出最优查询点，降低决策延迟'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
传统贝叶斯优化（BO）每步需重拟合代理模型、最大化采集函数，计算开销极高；现有基于PFN的上下文BO方案要么仍依赖采集函数数值优化，要么无代理模型导致决策规则固定，基于监督学习的查询选择此前缺乏明确的标签构造方案。
### 方法关键点
1. 提出IQS-BO架构，基于合成先验做监督训练，单步前向即可预测每个候选点为全局最优的概率，目标最小化对应该事件的后验概率；
2. 支持两种部署模式：无代理模型的全上下文BO，或接入固定概率代理模型仅摊销决策步骤；
3. 提出PFN预训练混合先验，融合GP采样与带扭曲输入、窄最优、平台期的非平稳核函数样本，适配传统GP代理建模效果差的场景。
### 关键结果
查询选择开销仅为传统采集函数方法的极小占比，在合成及真实基准上效果匹配或优于基于GP的标准BO与现有上下文BO方案；混合先验预训练可进一步稳定提升优化性能。
