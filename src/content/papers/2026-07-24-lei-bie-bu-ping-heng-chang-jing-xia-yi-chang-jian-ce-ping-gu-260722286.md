---
title: An Insight on Evaluation Metrics Under the Imbalanced Case of Anomaly Detection
title_zh: 类别不平衡场景下异常检测评估指标深度分析
authors:
- Romain Hermary
- Nesryne Mejri
- Djamila Aouada
affiliations:
- University of Luxembourg
arxiv_id: '2607.22286'
url: https://arxiv.org/abs/2607.22286
pdf_url: https://arxiv.org/pdf/2607.22286
published: '2026-07-24'
collected: '2026-07-27'
category: Eval
direction: 不平衡场景 异常检测评估指标研究
tags:
- Anomaly Detection
- Evaluation Metrics
- Class Imbalance
- AUROC
- AUPR
one_liner: 分析四类常用异常检测指标在不同不平衡度下的特性，给出跨数据集评估的实操指引
practical_value: '- 电商反作弊、异常流量检测、薅羊毛识别等类不平衡场景下，可参考结论选择适配的评估指标，避免单一指标误导模型选型

  - 跨不同异常占比的业务数据集对比模型效果时，优先选择稳定性更高的指标，不要直接对标公共基准的指标数值

  - 做模型ABTest时，可复用metric landscape可视化方法，同时权衡TPR、TNR对应的业务收益，而非仅参考单一F1或AUC得分'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
异常检测天然存在严重类别不平衡，AUROC、AUPR、F1、MCC等常用指标的取值含义随异常占比动态变化，跨数据集对比模型效果、解读指标结果的难度极高，现有评估方案缺乏明确实操指引。
### 方法关键点
系统分析四类常用异常检测指标在不同不平衡程度下的行为特性，提出metric landscape可视化方法，将指标值与真正率（TPR）、真负率（TNR）直接关联，直观呈现不同指标的偏好性和稳定性。
### 关键结果
明确了四类指标在不同异常比例下的适用边界，输出跨不同不平衡度数据集解读、对比异常检测模型效果的可落地指导，可有效降低类不平衡场景下的评估偏差。
