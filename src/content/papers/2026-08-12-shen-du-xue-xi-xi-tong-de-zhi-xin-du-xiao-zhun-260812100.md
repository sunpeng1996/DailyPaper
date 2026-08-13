---
title: Confidence Calibration of Deep Learning Systems
title_zh: 深度学习系统的置信度校准
authors:
- Coby Penso
affiliations:
- Bar-Ilan University
arxiv_id: '2608.12100'
url: https://arxiv.org/abs/2608.12100
pdf_url: https://arxiv.org/pdf/2608.12100
published: '2026-08-12'
collected: '2026-08-13'
category: Training
direction: 深度学习训练 · 置信度校准
tags:
- Confidence_Calibration
- Conformal_Prediction
- Label_Noise
- Domain_Adaptation
- Differential_Privacy
one_liner: 提出标签噪声、域偏移、隐私约束场景下无需干净验证数据的深度学习置信度校准系列方法
practical_value: '- 处理推荐/搜索场景下的用户点击标签噪声问题时，可复用噪声感知的Conformal Prediction框架，得到更可靠的预测置信度，降低bad
  case风险

  - 跨域推荐场景无目标域标注数据时，可复用基于源域性能+域差异估计目标域精度的方法，实现无标注下的模型校准

  - 对用户行为数据隐私要求高的电商场景，可借鉴本地差分隐私+Conformal Prediction的方案，平衡隐私保护与预测可靠性'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
高风险业务场景下，模型置信度估计可靠性与预测精度同等重要，现有校准方法依赖干净验证数据，而实际落地常面临标签噪声、域偏移、数据隐私约束，无法满足前提。

### 方法关键点
1. 标签噪声场景：通过噪声模型建模噪声与干净标签分布的关联重构无噪置信度，扩展得到噪声感知Conformal Prediction方法，鲁棒估计一致性得分；
2. 无监督域适配场景：基于源域性能与域差异估计目标域精度，无需目标域标注即可完成校准；
3. 隐私约束场景：实现本地差分隐私加持的Conformal Prediction框架，同时满足不确定性量化、隐私保护要求。

### 关键结果
系列方案打通校准理论与安全关键场景落地路径，可输出抗噪声、隐私合规的高可靠性神经网络预测结果。
