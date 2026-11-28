---
title: 'So Many Ways to Multiply 3times3 Matrices: A Large Dataset of Rank-23 Schemes'
title_zh: 3×3矩阵乘法秩23方案大规模数据集
authors:
- Andrew Igorevich Perminov
affiliations:
- Research Center for TAI
- Institute for System Programming, Moscow
arxiv_id: '2611.31155'
url: https://arxiv.org/abs/2611.31155
pdf_url: https://arxiv.org/pdf/2611.31155
published: '2026-11-22'
collected: '2026-11-28'
category: Other
direction: 快速矩阵乘法 · 数据集构建
tags:
- Fast Matrix Multiplication
- Dataset
- Gradient Descent
- Alternating Least Squares
- Flip Graph Search
one_liner: 公开包含62029个两两不等价的3×3矩阵乘法秩23方案的数据集
practical_value: '- 主要为快速矩阵乘法领域学术研究提供数据支撑，电商/推荐业务场景直接可迁移价值较低

  - 若做推荐系统底层算子优化（如大规模Embedding矩阵运算加速），可参考该数据集的秩23方案提升3×3矩阵乘法效率'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
3×3矩阵乘法当前最优整数系数方案秩为23，但此前公开的秩23方案集合覆盖的秩模式数量极少，学界对该秩下本质不同的方案数量认知不足。
### 方法关键点
采用梯度下降结合交替最小二乘的数值方法，搭配翻转图搜索，生成具备三元、整数或有理系数的秩23矩阵乘法方案，基于因子矩阵秩构成的秩模式不变性筛选两两不等价的方案。
### 关键结果数字
公开62029个两两不等价的秩23方案数据集，覆盖的秩模式数量远高于此前公开数据集：Heule等的17376个方案仅含387种秩模式，Mårtensson等的15316个方案仅含568种秩模式，大幅填补了该领域数据缺口。
