---
title: 'Rollcast: Proper-Score Gated Rolling Anchors for Adaptive Probabilistic Time-Series
  Forecasting'
title_zh: Rollcast：基于适当评分门控滚动锚点的自适应概率时间序列预测
authors:
- Giancarlo Vercellino
affiliations:
- Independent Researcher
arxiv_id: '2609.05561'
url: https://arxiv.org/abs/2609.05561
pdf_url: https://arxiv.org/pdf/2609.05561
published: '2026-09-03'
collected: '2026-09-09'
category: Other
direction: 概率时序预测 · 滚动统计锚点融合
tags:
- Time-Series-Forecasting
- Probabilistic-Forecast
- Mixture-of-Experts
- Statistical-Forecasting
- Predictive-Calibration
one_liner: 基于滚动统计锚点混合与状态感知门控的高性能可解释单变量概率时序预测方法
practical_value: '- 滚动统计锚点+状态门控的轻量化融合框架可直接迁移到电商销量/流量/库存时序预测场景，无需复杂大模型即可获得接近Oracle的预测效果

  - 基于历史相似状态匹配残差分布的不确定性估算方法，可复用到推荐系统时序类特征的不确定性建模，提升冷启动场景排序鲁棒性

  - 递归粒子混合生成多步预测的思路，可借鉴到长周期促销效果预判、库存备货规划等业务，降低多步预测的误差累计'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
传统单全局模型概率时序预测泛化性弱、可解释性差，现有预测组合方案需单独拟合多模型，部署成本高。
### 方法关键点
1. 采用滚动均值、中位数、极值、回归端点、分位数等轻量统计锚点表征时序当前状态
2. 引入状态依赖softmax门控，通过最小化负对数预测密度学习各锚点的融合权重
3. 匹配历史相似状态的残差分布输出局部不确定性，通过递归粒子混合生成多步预测
### 关键结果
在8种时序生成过程、2000条独立序列评测中：
- 90%标称预测区间覆盖率达86.2%，95%标称区间覆盖率达91.5%
- 90%区间宽度仅比Oracle宽13.6%，整体CRPS比Oracle高14.4%
- 自回归、随机波动、厚尾、方差突变场景下性能最接近Oracle
