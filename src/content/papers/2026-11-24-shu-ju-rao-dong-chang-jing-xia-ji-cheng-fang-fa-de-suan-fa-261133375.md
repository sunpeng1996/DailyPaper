---
title: Evaluating Ensemble Methods for Algorithmic Stability Under Data Perturbations
title_zh: 数据扰动场景下集成方法的算法稳定性评估
authors:
- Benjamin Edelhertz
- Simon D. Nguyen
- Tyler H. McCormick
affiliations:
- University of Washington
arxiv_id: '2611.33375'
url: https://arxiv.org/abs/2611.33375
pdf_url: https://arxiv.org/pdf/2611.33375
published: '2026-11-24'
collected: '2026-11-27'
category: Training
direction: 集成训练 · 算法稳定性优化
tags:
- Ensemble Learning
- Data Perturbation
- Algorithmic Stability
- Subbagging
- Rashomon Set
one_liner: 量化数据扰动下不同集成方法的稳定性表现，明确subbagging与Rashomon集成的适用边界及优化方案
practical_value: '- 电商广告/推荐分类任务（如点击/转化预测）遇到数据扰动导致的预测波动时，优先采用subbagging集成策略提升稳定性，效果优于Rashomon集成

  - 对本身稳定性较好的分类器做subbagging时需调优bag数量，避免引入过大Monte Carlo噪声，可搭配inflated argmax缓解不稳定问题

  - 排序/召回模型的离线评估环节可新增数据扰动下的稳定性校验指标，避免过拟合高影响样本导致的线上效果波动'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有分类算法在决策边界附近敏感度高，叠加过拟合高影响样本的问题，易出现预测结果不稳定，而常规集成策略的稳定性表现缺乏系统量化验证，甚至可能反向降低原有稳定分类器的鲁棒性。
### 方法关键点
系统对比subbagging、Rashomon集成两种策略在不同数据扰动水平下的稳定性表现，引入inflated argmax方法缓解subbagging对稳定分类器引入的噪声问题，从影响均衡角度解释集成策略的稳定机制。
### 关键结果
1. subbagging可大幅提升不稳定分类器的稳定性，但效果随扰动水平变化，对稳定分类器会引入Monte Carlo噪声，该噪声仅随bag数量增长缓慢下降；
2. Rashomon集成仅在存在足够预测多样性时可稳定不稳定分类器，无法替代subbagging作为通用方案；
3. 搭配inflated argmax可有效缓解subbagging带来的额外噪声问题。
