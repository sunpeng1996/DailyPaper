---
title: 'How to Estimate Whether You Have Found Several Needles in a Haystack: Measuring
  Calibration in Multi-Label Text Classification'
title_zh: 多标签文本分类校准度度量：如何评估海量样本中的有效标签识别效果
authors:
- Sophie Henning
- Georg Hofmann
- Alexander Schulte
- Alexander Fraser
- Annemarie Friedrich
affiliations:
- TU Munich
- Munich Center for Machine Learning (MCML)
- LMU Munich
- University of Augsburg
- Robert Bosch GmbH
arxiv_id: '2609.26468'
url: https://arxiv.org/abs/2609.26468
pdf_url: https://arxiv.org/pdf/2609.26468
published: '2026-09-22'
collected: '2026-09-23'
category: Eval
direction: 多标签分类 · 置信度校准评估
tags:
- Calibration
- Multi-label Classification
- Confidence Estimation
- Evaluation Metric
- LLM Evaluation
one_liner: 提出正负标签分配等权的分箱方案，实现多标签分类场景下可信的校准误差估计
practical_value: '- 多标签分类（如商品打标、用户兴趣标签预测、query多意图识别）场景下，可复用该正负等权分箱方案评估模型置信度校准效果，避免原分箱方案因负样本占比过高导致的误差低估

  - LLM做极端多标签分类（如海量商品类目预测、多维度广告标签映射）时，可采用该度量验证校准后的置信度是否符合真实准确率，优化低置信结果的人工拦截规则

  - 对标签分布极度不平衡的多标签任务，可参考该分箱思路优化现有ECE（期望校准误差）计算逻辑，提升评估指标的可信度'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有置信度校准度量多针对二分类/多分类任务，多标签场景（负样本占比极高）下的校准误差评估存在明显缺陷：原有分箱方案要么低估误差、仅反映标签频率，要么存在大量小样本分箱导致结果不可靠，无法支撑高风险多标签任务的置信度校验需求。

### 方法关键点
提出正负标签分配等权的新型分箱方案，计算标签维度的期望校准误差时，对正、负样本的贡献分配相同权重，从根源上解决极端标签不平衡场景下的评估偏差问题。

### 关键结果
1. 对比现有分箱方案，新方案在层级多标签、极端多标签分类场景下均能输出有意义的校准误差估计；
2. 验证了当前LLM做多标签预测的置信度校准仍是未解决的开放挑战。
