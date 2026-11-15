---
title: Linear Regression with Self-Selection Bias in Polynomial Time
title_zh: 多项式时间复杂度下带自选择偏差的线性回归算法
authors:
- Felix Zhou
affiliations:
- Yale University
arxiv_id: '2611.17228'
url: https://arxiv.org/abs/2611.17228
pdf_url: https://arxiv.org/pdf/2611.17228
published: '2026-11-12'
collected: '2026-11-15'
category: Other
direction: 统计学习 · 线性回归优化算法
tags:
- Linear Regression
- Self-Selection Bias
- Polynomial Time Algorithm
- Tensor Decomposition
- Latent Variable
one_liner: 提出首个多项式时间的带自选择偏差多线性回归器估计算法，解决此前算法对k指数依赖的性能瓶颈
practical_value: '- 推荐场景用户行为存在自选择偏差的回归建模任务，可参考其基于协变量高阶Hermite矩的偏差修正分析思路

  - 多隐变量（如多兴趣表征、多场景回归参数）估计场景，可复用其隐式高阶张量分解+最小二乘的两步参数估计框架

  - 多回归器类任务（如max-affine回归类应用）可借鉴其将复杂度从k指数级降到多项式级的优化思路'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
带自选择偏差的k个n维线性回归器估计问题，此前最优算法复杂度对k呈指数依赖，无法适配高维、大k场景，也不支持回归器间存在关联噪声的设定。

### 方法关键点
1. 针对大响应值的观测样本，证明其$\oldsymbol{\log n}$阶Hermite矩可近似分解为回归器的张量幂之和；
2. 两步算法框架：先通过隐式高阶张量分解输出与回归器平行的单位向量，再用改进的普通最小二乘提取回归器估计值。

### 关键结果
- 针对未知索引的问题变体，实现了$oldsymbol{\mathrm{poly}(n,k,1/\varepsilon)}$时间复杂度，是该问题首个多项式时间解法；
- 支持回归器间存在相关噪声，同时给出了max-affine回归问题的首个多项式时间算法，性能显著优于此前指数复杂度方案。
