---
title: On the Complexity of Entrywise Power Matrix Factorization
title_zh: 逐元素幂矩阵分解的计算复杂度分析
authors:
- Nicolas Gillis
- Subhayan Saha
- Stefano Sicilia
- Arnaud Vandaele
affiliations:
- University of Mons, Mons, Belgium
arxiv_id: '2607.04875'
url: https://arxiv.org/abs/2607.04875
pdf_url: https://arxiv.org/pdf/2607.04875
published: '2026-07-06'
collected: '2026-07-12'
category: Other
direction: 基础矩阵分解 计算复杂度理论研究
tags:
- Matrix Factorization
- Computational Complexity
- NP-hard
- Fixed-parameter Tractable
- Low-rank Approximation
one_liner: 系统分析逐元素幂矩阵分解（EPMF）的复杂度，给出完整可解性边界与适用条件
practical_value: '- 若业务场景尝试EPMF做低秩拟合，固定秩r时可直接采用多项式时间算法求解，无需额外复杂调优

  - 当r≥2且使用近似EPMF时，无需追求全局最优解，可直接采用启发式迭代方法收敛到局部最优即可

  - 通用大规模数据场景下不建议优先选用EPMF做特征降维或矩阵补全，其复杂度高于传统SVD/MF'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有低秩矩阵分解广泛用于数据降维、补全等场景，逐元素幂矩阵分解（EPMF）作为含参数p的泛化分解框架（包含p=1模模型、p=2平方根秩分解等常用特例），此前缺乏完整的复杂度理论支撑，相关问题可解性边界不明确。

### 方法关键点
1. 将精确EPMF等价转换为矩阵元素符号翻转的signing问题，证明两类问题复杂度完全等价；
2. 分别对精确求解场景、Frobenius范数近似求解场景做复杂度推导，给出不同秩r约束下的可解性条件。

### 关键结果
精确EPMF是强NP难问题，改进了此前平方根秩的弱NP难结论；固定秩r时精确EPMF可多项式时间求解，r作为输入时普通矩阵场景下为固定参数可跟踪（FPT），时间复杂度与输入矩阵规模线性相关；近似EPMF即使在r=2的最小非平凡场景下也为NP难。
