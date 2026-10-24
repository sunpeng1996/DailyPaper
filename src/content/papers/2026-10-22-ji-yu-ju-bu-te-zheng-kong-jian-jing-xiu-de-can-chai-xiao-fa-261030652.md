---
title: Residual Calibration via Local Feature-Space Refinement
title_zh: 基于局部特征空间精修的残差校准方法
authors:
- Xihao Wang
- Chengyao Yu
- Ruixing Ming
affiliations:
- Zhejiang Gongshang University, School of Statistics and Data Science
- Southern University of Science and Technology, Department of Statistics and Data
  Science
arxiv_id: '2610.30652'
url: https://arxiv.org/abs/2610.30652
pdf_url: https://arxiv.org/pdf/2610.30652
published: '2026-10-22'
collected: '2026-10-24'
category: Other
direction: 模型后处理 · 置信度校准
tags:
- post-hoc-calibration
- confidence-estimation
- feature-space
- plug-and-play
- multi-view
one_liner: 提出即插即用的LAPE残差校准框架，利用局部邻域样本修正预测置信度，支持多视图输入扩展
practical_value: '- 推荐系统排序/召回模型的置信度校准可直接复用LAPE作为即插即用模块，无需重新训练原模型，大幅降低迭代成本

  - 多模态/多视图召回场景可引入CFAF级联特征增强融合策略，提升多源特征输入下的校准鲁棒性

  - 电商广告高置信度投放、Agent决策置信截断场景，可通过局部邻域非参数修正降低过/欠置信误差，提升决策收益'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有后验校准方法大多基于全局分数变换，仅能优化边缘校准效果，无法捕捉特征空间局部区域的异质性校准偏差，DNN输出的不可靠置信度会直接影响高风险决策（如推荐截断、广告投放）的准确性。
### 方法关键点
1. 提出LAPE残差校准框架，以全局校准器输出为稳定锚点，引入校准样本的邻域非参数局部证据对单样本预测做精细化修正
2. 作为即插即用模块可直接复用已有校准数据，无需修改原模型结构，适配任意DNN模型的后处理校准
3. 额外提出CFAF级联特征增强融合策略，支持多视图输入场景下的校准扩展
### 关键结果
多组实验验证，LAPE可显著提升各类基线校准器的校准质量，在不同数据分布、模型结构下均保持高效推理效率与强鲁棒性
