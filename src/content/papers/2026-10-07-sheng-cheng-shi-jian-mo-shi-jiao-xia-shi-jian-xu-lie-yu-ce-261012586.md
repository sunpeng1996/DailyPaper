---
title: 'Realism VS Accuracy: Event Sequence Forecasting from a Generative Modeling
  Perspective'
title_zh: 生成式建模视角下事件序列预测的真实度与准确率权衡
authors:
- Dmitry Osin
- Egor Surkov
- Petr Mokrov
- Igor Udovichenko
- Ivan Karpukhin
- Evgeny Burnaev
- Egor Shvetsov
- Alexander Korotin
affiliations:
- Applied AI Institute
- ITMO University
- Vega Institute Foundation
- SB AI Lab
arxiv_id: '2610.12586'
url: https://arxiv.org/abs/2610.12586
pdf_url: https://arxiv.org/pdf/2610.12586
published: '2026-10-07'
collected: '2026-10-24'
category: RecSys
direction: 事件序列预测 · 生成式建模权衡优化
tags:
- EventSequenceForecasting
- GenerativeModeling
- DiffusionModel
- DistributionalRealism
- PredictionAccuracy
one_liner: 揭示事件序列预测真实度与准确率的固有权衡，提出Wasserstein BaryBooster将真实度转化为准确率
practical_value: '- 做用户行为序列（浏览/下单/加购）预测时，需同时评估准确率与分布真实度，避免生成不符合用户行为分布的假序列，导致召回/排序策略偏差

  - 可复用Wasserstein BaryBooster思路，聚合高真实度扩散模型生成的用户行为样本，提升多步序列预测效果，适配长周期用户兴趣建模场景

  - 序列预测模型选型可复用其双维度（准确率+真实度）评估框架，避免单一指标导致的模型效果错配'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有事件序列预测（如电商用户购买、浏览序列）大多仅关注预测准确率，忽略生成结果的分布真实度，难以支撑高置信度的多时间 horizon 预测场景，无法匹配真实世界的事件分布规律。
### 方法关键点
1. 将多时间 horizon 事件序列预测建模为条件生成问题，构建包含准确率、分布真实度双维度评估指标、强统计基线、真实场景数据集的通用 benchmark；
2. 提出Wasserstein BaryBooster算法，聚合具备高真实度优势的扩散模型输出样本，将分布真实度优势直接转化为预测准确率。
### 关键结果
实验验证所有现有方法均无法同时在准确率与真实度上达到最优，二者存在固有权衡；Wasserstein BaryBooster算法转换扩散模型输出后，预测效果达到SOTA水平。
