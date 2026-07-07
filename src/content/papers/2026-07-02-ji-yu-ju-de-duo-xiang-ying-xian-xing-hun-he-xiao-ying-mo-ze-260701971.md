---
title: Moment-Based Selection of Multiresponse Linear Mixed-Effects Models
title_zh: 基于矩的多响应线性混合效应模型选择框架MOMENT
authors:
- Yifan Chen
- Yuedong Wang
- Guo Yu
affiliations:
- University of California, Santa Barbara
arxiv_id: '2607.01971'
url: https://arxiv.org/abs/2607.01971
pdf_url: https://arxiv.org/pdf/2607.01971
published: '2026-07-02'
collected: '2026-07-07'
category: Other
direction: 统计建模 · 多响应纵向数据分析
tags:
- Linear Mixed-Effects Model
- Moment Estimation
- Covariance Estimation
- Convex Optimization
- Variable Selection
one_liner: 提出基于二阶交叉矩的阶段式框架MOMENT，高效求解混合效应模型的随机与固定效应选择问题
practical_value: '- 可复用其协方差矩阵稀疏化+半正定约束的建模思路，用于用户多行为（点击/加购/下单）纵向序列的混合效应建模，挖掘用户个体异质性

  - 其将非凸随机效应选择转化为光滑凸优化的trick，可迁移到用户建模模块的特征选择环节，大幅降低求解开销

  - 多响应相关场景下的建模思路可直接用于多目标排序任务的特征筛选，相比单变量独立分析效果提升显著'
score: 4
source: arxiv-stat.ML
depth: abstract
---

### 动机
线性混合效应模型（LMM）是纵向/聚类/重复测量类非独立数据的核心建模工具，现有模型选择方法多基于似然，随机效应识别难度高、求解效率低，缺乏完善的有限样本理论保证。
### 方法关键点
1. 提出阶段式矩框架MOMENT，利用二阶交叉矩恒等式同时选择、估计随机效应协方差矩阵与固定效应系数；
2. 在半正定约束下通过对角线诱导稀疏性，将随机效应选择问题转化为可通过投影梯度下降高效求解的光滑约束凸优化问题；
3. 给出联合次Weibull误差下的有限样本理论保证，覆盖随机与固定效应选择一致性。
### 关键结果
仿真实验中MOMENT整体表现优异，响应存在相关性时效果远超单变量分析；在血液透析数据集上验证了其对多变量纵向数据建模的可解释性与灵活性。
