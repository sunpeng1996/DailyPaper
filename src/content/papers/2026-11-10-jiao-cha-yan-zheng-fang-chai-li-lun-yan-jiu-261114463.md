---
title: A Theory of Cross-Validation Variance
title_zh: 交叉验证方差理论研究
authors:
- Nathaniel S. O'Connell
- Jaime L. Speiser
affiliations:
- Department of Biostatistics and Data Science, Wake Forest University School of Medicine
arxiv_id: '2611.14463'
url: https://arxiv.org/abs/2611.14463
pdf_url: https://arxiv.org/pdf/2611.14463
published: '2026-11-10'
collected: '2026-11-12'
category: Eval
direction: 模型评估 · 交叉验证策略优化
tags:
- Cross-Validation
- Variance
- Model Evaluation
- Resampling
- AUC
one_liner: 推导交叉验证估计方差的有限样本恒等式，给出方差最优的交叉验证设计选择原则
practical_value: '- 算法迭代离线评估优先选K-fold交叉验证，比Monte Carlo、bootstrap交叉验证的估计方差更低，降低效果对比误判概率

  - 小样本冷启动模型评估可选留一法（leave-one-out），可获得K-fold类方法中最小的估计方差，提升小样本评测可靠性

  - 分类模型AUC评估优先选留对法（leave-pair-out），相比普通K-fold能得到方差更低的AUC估计，提升分类效果评估稳定性'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
交叉验证是机器学习模型效果评估的通用方案，但不同拆分策略的估计方差差异缺乏统一理论解释，从业者难以选择最优交叉验证设计。
### 方法关键点
从观测样本在训练、验证两个角色的权重视角出发，推导得到交叉验证估计方差的精确有限样本恒等式，可覆盖MSE、AUC等常见评估指标；将方差拆解为仅和训练集大小相关的采样方差、与拆分策略相关的随机折方差两部分。
### 关键结果
1. K-fold交叉验证为一阶方差最优的拆分方案，一阶方差与K值无关；2. 合理模型假设下，留一法是所有K-fold方案中方差最小的；3. AUC评估场景下，留对法为方差最优方案；4. 交叉验证估计服从渐近正态分布，方差匹配推导的恒等式结果。
