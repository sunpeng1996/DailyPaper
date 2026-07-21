---
title: Prediction-Only Distillation in Linear and Logistic Regression
title_zh: 线性与逻辑回归场景下的仅预测自蒸馏方法
authors:
- Hien Dang
- Pratik Patil
- Alessandro Rinaldo
affiliations:
- University of Texas at Austin
arxiv_id: '2607.15450'
url: https://arxiv.org/abs/2607.15450
pdf_url: https://arxiv.org/pdf/2607.15450
published: '2026-07-16'
collected: '2026-07-21'
category: Training
direction: 模型训练 · 无原始标注自蒸馏优化
tags:
- Knowledge Distillation
- Self-Distillation
- Linear Regression
- Logistic Regression
- Model Calibration
one_liner: 提出无原始标注场景下的仅预测自蒸馏方案，混合师生预测可稳定降低预测风险
practical_value: '- 历史标注数据丢失/不可获取时，可直接用已训模型打伪标+新无标注数据蒸馏小模型，适配端侧/低延迟推理场景

  - 蒸馏后无需额外训练，仅用少量独立标注校准集估计混合权重，即可获得比原教师模型更优的预测效果，工程成本极低

  - OOD特征场景下也适用，可用于电商新流量/新类目下的模型效果兜底，不需要重新标注全量数据'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有自蒸馏方案依赖原始训练标注数据，但工业部署中常出现原始标注丢失的情况，仅能访问已训预测器和新增无标注特征，传统方法无法落地。
### 方法关键点
采用fresh-X预测混合自蒸馏范式：
1. 用已有教师模型给新增无标注特征打伪标，训练同架构纯蒸馏学生模型；
2. 最终输出为教师与学生预测结果的仿射组合；
3. 最优混合权重无法仅通过无标注数据识别，仅需少量独立标注校准集即可在训练后单次估计得到，无需额外模型拟合。
### 关键结果
- 岭回归场景下，几乎所有师生正则化参数组合中，混合预测风险都严格低于教师模型，新增特征为OOD、协方差各向同性时同样生效；
- 二分类逻辑回归场景下，混合预测效果优于教师模型与纯蒸馏学生模型。
