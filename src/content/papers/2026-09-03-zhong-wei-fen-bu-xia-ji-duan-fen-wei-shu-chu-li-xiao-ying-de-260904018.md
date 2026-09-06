---
title: A location-invariant estimator of extremal quantile treatment effects for heavy-tailed
  distributions
title_zh: 重尾分布下极端分位数处理效应的位置不变估计器
authors:
- Xin Yu
- Shuwei Huang
- Jicheng Liu
- Jielin Tang
- Bolin Wang
- Yunxiao Zhang
- Tian Zhao
affiliations:
- Huazhong University of Science and Technology
- Tencent
arxiv_id: '2609.04018'
url: https://arxiv.org/abs/2609.04018
pdf_url: https://arxiv.org/pdf/2609.04018
published: '2026-09-03'
collected: '2026-09-06'
category: Other
direction: 因果推断 · 极端分位数效应估计
tags:
- Causal Inference
- Quantile Treatment Effect
- Heavy-tailed Distribution
- Extreme Value Index
- Statistical Estimation
one_liner: 针对重尾分布场景提出位置不变的极端QTE估计方法，具备渐近统计有效性
practical_value: '- 电商大促、用户补贴等策略效果分析中，估算对消费额、LTV等重尾指标的Top分位用户因果效应时，可复用该方法避免分布偏移带来的估计偏差

  - 广告投放ROI、转化等重尾指标的极端分位数效应评估，该方法比传统QTE估计器稳定性更高，适合长尾效果诊断

  - AB实验跨批次、跨人群对比策略的长尾效应时，可利用该方法的位置不变性提升对比结论的可信度'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有重尾分布下的极端QTE估计方法依赖外推结合因果EVI估计，在潜在结果分布发生公共位置偏移时估计结果不一致，与群体QTE本身的位置不变性矛盾。
### 方法关键点
1. 采用逆倾向得分加权，将位置不变的Fraga EVI估计器适配到因果推断场景；
2. 替换传统外推公式为差值计算方案，计算分位数差时位置参数自动抵消，保障估计器的位置不变性。
### 关键结果
理论上证明了所提估计量的一致性与渐近正态性，配套给出一致方差估计器，支持渐近有效统计推断；仿真实验验证了方法的位置不变性、阈值鲁棒性，置信区间覆盖率符合理论预期。
