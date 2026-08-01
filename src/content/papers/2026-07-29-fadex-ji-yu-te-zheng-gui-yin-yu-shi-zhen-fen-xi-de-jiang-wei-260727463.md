---
title: 'FADEx: Feature Attribution and Distortion-based Explanation of Dimensionality
  Reduction'
title_zh: FADEx：基于特征归因与失真分析的降维可解释方法
authors:
- Lucas Greff Meneses
- Evandro S. Ortigossa
- Claudio Silva
- Luis Gustavo Nonato
arxiv_id: '2607.27463'
url: https://arxiv.org/abs/2607.27463
pdf_url: https://arxiv.org/pdf/2607.27463
published: '2026-07-29'
collected: '2026-08-01'
category: Other
direction: 降维可解释 · 特征归因
tags:
- Dimensionality Reduction
- Feature Attribution
- Explainability
- Local Interpretation
- SVD
one_liner: 提出适配任意降维方法的逐实例局部特征归因框架，同时提供归因结果与失真分析，性能优于现有方案
practical_value: '- 推荐系统隐空间分析场景：可复用FADEx定位影响用户/item降维后簇分布的核心特征，辅助校准用户画像、物品标签体系

  - 算法迭代验证场景：对召回/排序模块的隐空间降维结果做失真校验，提前规避降维导致的特征信息损失影响业务效果

  - 可解释推荐落地场景：复用FADEx的局部线性近似+加权最小二乘思路，无需额外OOD样本即可生成逐样本特征贡献解释，工程实现成本低'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
非线性降维（DR）是分析推荐/大模型隐空间、高维业务数据的核心工具，但非线性DR本身属于黑盒变换，无法定位单个特征对样本降维后空间位置的影响；现有DR解释方法存在单特征多归因、仅适配特定DR算法的缺陷，落地性差。
### 方法关键点
1. 提出FADEx逐实例局部特征归因方法，通过一阶泰勒展开做局部线性近似，结合SVD生成解释结果
2. 采用加权最小二乘计算局部线性模型，无需OOD样本映射，对所有DR方法通用，可同时输出局部特征归因、降维失真度两类分析结果
### 关键结果
多维度定性、定量实验及案例验证，FADEx生成解释的鲁棒性、可靠性均优于现有同类型方法，可适配多种降维场景的分析需求。
