---
title: A Sensitivity Framework for Assessing External Validity
title_zh: 评估实验结果外部有效性的敏感性分析框架
authors:
- Ariel Boyarsky
- Naoki Egami
- Hongseok Namkoong
affiliations:
- Columbia Business School, Decision, Risk, and Operations Division
- Massachusetts Institute of Technology, Department of Political Science, Statistics
  and Data Science Center
arxiv_id: '2611.16242'
url: https://arxiv.org/abs/2611.16242
pdf_url: https://arxiv.org/pdf/2611.16242
published: '2026-11-12'
collected: '2026-11-15'
category: Other
direction: 因果推断 · 实验外部有效性评估
tags:
- Causal_Inference
- External_Validity
- Partial_Identification
- Debiasing
- Multi-site_Experiment
one_liner: 提出适配多站点实验外推的偏识别框架，结合优化与去偏方法量化因果结论的外部适用边界
practical_value: '- 多站点AB实验外推场景可引入该偏识别框架，结合站点特征（如城市层级、客群结构）给出新站点的效应区间，避免直接复用实验结论的偏差

  - 可借鉴效应层级假设（交互效应弱于直接效应）约束外推参数，降低多特征下小样本站点集的外推不确定性

  - 约束优化结合去偏的思路可复用在推荐系统跨域迁移的效果预估场景，给未知域的指标波动提供可信区间'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
多站点随机实验的内部有效结论往往无法直接外推至未实验站点，当站点数量远少于调节因果效应的站点级特征维度时，传统外推方法易过拟合、结论不可靠。
### 方法关键点
1. 提出通用偏识别框架，支持效应层级原则等任意仿射参数约束下的跨站点外推评估；
2. 开发适配约束优化估计量的新型去偏方法，得到半参数高效的偏识别边界估计，解决参数欠定导致的协方差矩阵奇异问题。
### 关键结果
在6国小额信贷多站点数据集上验证，每次单留1国作为目标域，用剩余站点数据可生成对应国家的因果效应外部有效性区间，不同外推假设直接对应不同宽度的可信边界。
