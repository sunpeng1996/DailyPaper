---
title: 'PICPIs: Prediction-Interval-Conditional Prediction Intervals'
title_zh: PICPIs：预测区间条件约束的自适应不确定性预测区间
authors:
- Xuelin Yang
- Baihe Huang
- Yilong Hou
- Guido Imbens
- Michael I. Jordan
affiliations:
- University of California, Berkeley
- Stanford University
- Inria Paris
arxiv_id: '2609.25388'
url: https://arxiv.org/abs/2609.25388
pdf_url: https://arxiv.org/pdf/2609.25388
published: '2026-09-21'
collected: '2026-09-23'
category: Other
direction: 共形预测 · 不确定性区间校准
tags:
- conformal_prediction
- uncertainty_quantification
- calibration
- statistical_inference
- distribution_free
one_liner: 提出满足预测值自洽约束的PICPIs框架，为非参数不确定性量化提供局部校准的区间估计
practical_value: '- 推荐CTR/CVR打分校准场景可复用PICPIs自洽约束逻辑，为预估分分层提供统计置信度保证，替代人工阈值划分

  - 广告流量分层出价场景可引入PICPIs生成的局部校准区间，优化高低价值流量的出价策略，降低决策不确定性

  - A/B实验局部效果评估中可使用PICPIs区间量化指标波动的统计显著性，减少假阳性判断'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
共形预测领域传统边际有效性在决策依赖的预测值上分辨率不足，基于协变量的完全条件保证理论上不可实现，缺乏兼顾落地可行性与局部校准性的不确定性区间方案。
### 方法关键点
提出PICPIs自洽约束框架，区间$I$满足$
\mathbb{E}[Y \mid p(X) \in I] \in I
$，无需修改原预测模型即可生成数据自适应的预测分层区间，配套可落地的构造算法，支持概率预测、多分类两类任务。
### 关键结果
理论上区间宽度收敛速率为$n^{-1/3}$，仅遗漏任意小比例的预测值；实证覆盖概率、区间宽度指标均优于传统区间基线，可直接支撑下游决策。
