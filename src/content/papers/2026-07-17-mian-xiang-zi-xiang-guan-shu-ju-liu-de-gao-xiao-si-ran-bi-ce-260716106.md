---
title: An Efficient Likelihood Ratio Test for Online Changepoint Detection in the
  Presence of Autocorrelation
title_zh: 面向自相关数据流的高效似然比在线变点检测方法
authors:
- Yuntang Fan
- Paul Fearnhead
- Idris A. Eckley
- Gaetano Romano
affiliations:
- Lancaster University
arxiv_id: '2607.16106'
url: https://arxiv.org/abs/2607.16106
pdf_url: https://arxiv.org/pdf/2607.16106
published: '2026-07-17'
collected: '2026-07-21'
category: Other
direction: 在线变点检测 · 时序数据流处理
tags:
- Changepoint Detection
- Time Series
- Autoregressive Process
- Streaming Data
- Likelihood Ratio Test
one_liner: 针对自相关数据流优化似然比统计量，提出O(log n)复杂度低延迟在线变点检测算法
practical_value: '- 电商/推荐场景的点击、转化、用户行为时序流普遍存在自相关，可替换原有IID假设的变点检测方案，降低指标异动、流量异常的误报率

  - AR(p)-focus单步O(log n)复杂度适配高频率数据流，可直接集成到实时A/B实验指标监控、推荐系统效果漂移检测链路中

  - 做用户行为突变、黑灰产流量异动识别时，可直接复用其针对AR序列优化的广义似然比统计量设计，缩短检测延迟'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有在线变点检测算法普遍基于IID观测假设，应用到存在时序依赖的真实数据流（如用户行为、业务指标流）时，会出现误报率升高、检测延迟变长的问题，无法适配高频率流数据的实时检测需求。
### 方法关键点
1. 将广义似然比（GLR）统计量扩展到p阶自回归（AR(p)）过程，适配自相关时序数据特性
2. 基于focus算法优化实现，最终AR(p)-focus算法单迭代平均计算复杂度为O(log n)
### 关键结果
仿真实验中，针对存在时序相关的数据集，检测能力显著优于基于IID假设的对比方法，同时在真实电信数据集上验证了落地可行性
