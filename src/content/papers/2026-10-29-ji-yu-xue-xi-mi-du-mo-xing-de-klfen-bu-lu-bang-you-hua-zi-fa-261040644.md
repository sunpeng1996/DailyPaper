---
title: Adaptive Scenario Generation for KL-DRO Around a Learned Density Model
title_zh: 基于学习密度模型的KL分布鲁棒优化自适应场景生成方法
authors:
- Aron Brenner
- Saurabh Amin
affiliations:
- Massachusetts Institute of Technology
- Laboratory for Information & Decision Systems
arxiv_id: '2610.40644'
url: https://arxiv.org/abs/2610.40644
pdf_url: https://arxiv.org/pdf/2610.40644
published: '2026-10-29'
collected: '2026-11-01'
category: Other
direction: 分布鲁棒优化 · 小样本决策优化
tags:
- Distributionally Robust Optimization
- KL Divergence
- Scenario Generation
- Stochastic Programming
- Small Data
one_liner: 提出以拟合密度模型为中心的KL-DRO框架与自适应场景生成策略，降低小数据分布偏移下的决策成本
practical_value: '- 电商多品类备货（报童问题场景）小样本冷启动时，可复用基于学习密度模型的KL-DRO框架，替代经验分布鲁棒方案，降低分布偏移下的备货成本

  - 搜索推荐/广告流量分配决策场景，样本量不足时可借鉴自适应场景生成思路，定向采样最坏case的分布样本，避免独立采样遗漏极端风险场景

  - Agent决策鲁棒性优化时，可引入密度模型中心KL球思路，仅对生成模型可生成的合理样本做鲁棒约束，避免无效鲁棒开销'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统DRO歧义集要么仅对经验分布重加权、无法覆盖未观测样本，要么传输球包含生成过程不可能产生的无效样本，额外增加不必要的鲁棒成本；且小样本下独立采样易遗漏最坏情况的稀有样本，求解难度大。

### 方法关键点
1. 提出以拟合历史数据的密度模型为中心的KL球歧义集，仅允许 adversary 按模型分配的概率权重上调未观测高成本样本的权重，避免无效鲁棒；
2. 设计自适应场景生成流程，交替求解有限问题与从学习的标称分布中定向采样当前决策下的最坏情况样本，搭配重要性权重修正采样偏差。

### 关键结果
多品类报童问题、真实电网容量扩展问题上，数据稀缺且模型可捕捉分布结构时，相比以经验分布为中心的方案，分布偏移下成本显著降低，同分布下成本相当；数据量增大或偏移超出模型学习结构时优势消失。
