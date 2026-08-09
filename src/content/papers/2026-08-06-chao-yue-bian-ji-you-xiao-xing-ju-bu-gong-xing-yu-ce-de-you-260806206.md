---
title: 'Beyond Marginal Validity: Finite-Sample Guarantees for Localized Conformal
  Prediction'
title_zh: 超越边际有效性：局部共形预测的有限样本保证
authors:
- Anton Conrad
- Rustam Isaev
- Denis Belomestny
- Eric Moulines
- Sergey Samsonov
affiliations:
- Laboratoire de Recherche d’EPITA
- HSE University
- University of Duisburg–Essen
- Mohamed bin Zayed University of Artificial Intelligence
- Lomonosov Moscow State University
arxiv_id: '2608.06206'
url: https://arxiv.org/abs/2608.06206
pdf_url: https://arxiv.org/pdf/2608.06206
published: '2026-08-06'
collected: '2026-08-09'
category: Other
direction: 共形预测理论 · 有限样本保证
tags:
- Conformal Prediction
- Finite-Sample Guarantee
- Conditional Coverage
- Distribution-Free Inference
- Quantile Regression
one_liner: 为随机局部共形预测提供同时控制条件有效性与预言机效率的有限样本高概率界
practical_value: '- 电商推荐/广告排序场景可借鉴RLCP思路，对用户/物品特征相似的局部样本单独校准，解决全局校准下特定人群/品类置信度不准问题

  - 带宽偏差-方差tradeoff结论可直接用于局部校准模块超参调优，根据可获得的校准样本量动态调整局部邻域大小

  - 共形分位数回归的局部保证结论可迁移到销量预测、CVR预测等回归任务，提升极端样本下预测区间的可靠性'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
共形预测可为任意黑盒预测器提供有限样本、无分布的边际覆盖保证，但边际有效性会掩盖严重的协变量特定校准偏差，而精确无分布的条件覆盖在有限样本下无法实现，现有随机局部共形预测（RLCP）理论缺少同时控制条件有效性与oracle效率的有限样本保障。
### 方法关键点
在条件得分CDF的Hölder正则性、标准密度与核假设下，对任意固定得分推导局部邻域上一致的高概率界；进一步分析数据拆分学习得分场景，将保证分解为固定得分校准误差和得分估计误差两部分。
### 关键结果
1. 边界可分解为$O(h^\beta)$的局部偏差项和随校准样本量增大下降的校准项，明确了带宽的偏差-方差权衡关系
2. 得分学习效果越好，局部校准的保证边界越紧
