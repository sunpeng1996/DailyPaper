---
title: 'Dimension-free regimes for unadjusted Langevin in ridge-separable models:
  A subspace robust Wasserstein analysis'
title_zh: 岭可分模型下未调整朗之万算法的无维度场景：子空间鲁棒Wasserstein分析
authors:
- Yuansi Chen
- Francesco Pedrotti
- Peter A. Whalley
affiliations:
- ETH Zürich
- University of Warwick
arxiv_id: '2610.31431'
url: https://arxiv.org/abs/2610.31431
pdf_url: https://arxiv.org/pdf/2610.31431
published: '2026-10-22'
collected: '2026-10-26'
category: Other
direction: 高维贝叶斯推理 · 采样算法理论
tags:
- ULA
- Wasserstein Distance
- Bayesian Inference
- MCMC
- High-dimensional Statistics
one_liner: 采用子空间鲁棒Wasserstein距离分析ULA，给出不同数据规模下的无维度收敛界与适用区间
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-stat.ML
depth: abstract
---

### 动机
经典Wasserstein-2距离下未调整朗之万算法（ULA）的收敛偏差、混合时间随维度增长的结论过于严格，不符合多数统计任务仅需估计低维观测值的实际需求。
### 方法关键点
采用仅约束均值与任意低维边际分布的子空间鲁棒Wasserstein距离分析ULA偏差，适配实际任务观测需求；针对独立同分布数据构建的岭可分势能场景展开理论推导。
### 关键结果
证明数据量$N$相对维度$d$变化时混合效率呈钟形曲线：
1. 过参数化场景下有效维度为数据扰动秩$N$，复杂度仅依赖$N$而非$d$；
2. 大样本场景下$N$足够大时可实现无维度复杂度；
3. 当$N \asymp d$的比例区间，通用无维度保证不成立。
