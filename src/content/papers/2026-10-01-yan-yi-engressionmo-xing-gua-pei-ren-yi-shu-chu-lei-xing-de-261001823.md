---
title: Generalized Engression Models
title_zh: 《广义Engression模型：适配任意输出类型的统一分布回归框架》
authors:
- Xinwei Shen
- Zijian Guo
- Francis Bach
affiliations:
- Department of Statistics, University of Washington
- Center for Data Science, Zhejiang University
- Inria, École Normale Supérieure, PSL Research University
arxiv_id: '2610.01823'
url: https://arxiv.org/abs/2610.01823
pdf_url: https://arxiv.org/pdf/2610.01823
published: '2026-10-01'
collected: '2026-10-04'
category: Other
direction: 通用分布建模 · 多类型输出回归
tags:
- Distributional Regression
- Generative Model
- Nonparametric Model
- Multivariate Output
- Mixed-type Data
one_liner: 提出适配任意类型多变量输出的统一非参数分布回归框架，性能优于领域专用SOTA
practical_value: '- 多目标推荐场景可复用该框架的统一建模思路，同时拟合点击率（连续）、加购/下单（离散）、偏好序列（排序）等多维度混合类型目标，无需为单目标单独建模

  - 离散/排序类标签训练的梯度断裂问题可借鉴其随机扰动平滑损失的trick，保障端到端优化的稳定性

  - 多变量联合分布建模能力可用于冷启动用户/物品的稀疏特征补全，推断缺失的多维度行为标签分布'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有分布回归方法仅适配单类输出（连续/二分类/排序等），且大多只拟合条件分布的边际统计量（如均值），无法建模多变量混合类型输出的联合分布，适用场景受限。
### 方法关键点
1. 基于打分规则驱动的深度生成模型engression扩展，引入适配不同数据类型的link函数，统一支持连续、离散、排序等任意类型输出
2. 新增随机扰动机制平滑损失，解决link函数不连续时的梯度训练问题，支持端到端梯度下降优化
3. 理论证明该框架对连续、离散、混合类型输出均具备通用表征能力
### 关键结果数字
在242类物种分布基准、17维混合类型医疗结果两个任务上，边际指标得分与单类型专用模型持平，联合分布拟合效果优于专用模型，性能匹配或超过领域定制SOTA模型
