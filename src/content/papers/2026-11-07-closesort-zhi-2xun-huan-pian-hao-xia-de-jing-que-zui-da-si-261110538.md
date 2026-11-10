---
title: 'Close and Sort: Exact Maximum-Likelihood Aggregation of Cyclic Rank-Two Preferences'
title_zh: CloseSort：秩2循环偏好下的精确最大似然排序聚合算法
authors:
- Kehan Liu
- Zhaoyun Chen
- Xianquan Yan
affiliations:
- National University of Singapore
arxiv_id: '2611.10538'
url: https://arxiv.org/abs/2611.10538
pdf_url: https://arxiv.org/pdf/2611.10538
published: '2026-11-07'
collected: '2026-11-10'
category: RecSys
direction: 排序聚合 · 循环成对偏好精确求解
tags:
- rank_aggregation
- Kemeny_ranking
- pairwise_comparison
- LLM_evaluation
- exact_algorithm
one_liner: 提出O(nlogn)的CloseSort算法，可高效求解带循环的秩2成对偏好的加权Kemeny最大似然排序
practical_value: '- 推荐/广告多模型融合排序聚合场景，若成对偏好（多模型打分差、用户点击偏好）的对数胜率矩阵秩2占比高，可直接用CloseSort替代Borda等基线，带循环偏好场景下相对Borda降44%归一化regret，速度比精确DP高数千倍

  - LLM-as-judge评估、A/B测试多variant排序场景，可先对成对胜率矩阵做秩2投影，再用CloseSort排序，低样本量下比直接用经验最优排序的泛化性能更好，64次成对观测时胜率达85.7%

  - 当排序问题存在非传递循环偏好（如电商品类A优于B、B优于C、C优于A的用户投票），可尝试用秩2投影+CloseSort的范式，比仅用符号的排序方法更贴合加权最大似然目标，n=32时符号最优排序有63.6%概率是次优'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
成对偏好是推荐、搜索、LLM评估的核心输入（比如用户点击、多排序模型差异、LLM judge比较结果），将其转换为最大似然排序是加权Kemeny问题，通用场景下为NP-hard，现有秩2场景的精确算法仅用比较符号、不优化似然，且无法处理带循环的偏好，亟需高效且精确的加权解法。

### 方法关键点
- 将对数胜率矩阵$W_{ij}=\log(p_{ij}/p_{ji})$分解为2维向量$h_i$的行列式$W_{ij}=det(h_i,h_j)$，新增闭合向量$h_0=-\sum h_i$，将似然优化目标转换为闭合多边形的有向面积最大化问题
- 对$n+1$个向量做极角排序，从$h_0$处切开得到线性排序，即CloseSort算法，因子已知时复杂度$O(n\log n)$，完整矩阵输入时复杂度$O(n^2+n\log n)$
- 给出稳定性保障：当残差$E$的上三角$L_1$范数小于最优多边形最小相邻边行列式$\delta$时，秩2投影的CloseSort结果仍是全局最优，该阈值是紧的

### 关键结果数字
- 合成数据：64次成对观测时，秩2投影+CloseSort相对经验最优排序的泛化胜率达85.7%；$n=18$时推理速度比精确DP快8407倍
- LLM judge的Arena-Hard数据集：秩2投影捕捉89.2%的对数胜率能量，带循环偏好的场景下，CloseSort相对Borda降44%的归一化regret，相对8个基线均获得正的归一化收益

### 核心结论
带循环的秩2成对偏好排序问题无需NP-hard求解，极角排序即可得到精确最大似然结果，速度和泛化性均显著优于现有基线
