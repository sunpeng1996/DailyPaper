---
title: Efficient and Optimal Learning of Discrete Distributions with Person-Level
  Privacy
title_zh: 支持用户级隐私的离散分布高效最优学习算法
authors:
- Gautam Kamath
- Mahbod Majid
- Ankur Moitra
- Argyris Mouzakis
- Jonathan Ullman
affiliations:
- New York University
- Massachusetts Institute of Technology
- University of Texas at Austin
- University of Waterloo
- Northeastern University
arxiv_id: '2610.31612'
url: https://arxiv.org/abs/2610.31612
pdf_url: https://arxiv.org/pdf/2610.31612
published: '2026-10-22'
collected: '2026-10-25'
category: Other
direction: 隐私保护 · 差分隐私分布学习
tags:
- Differential Privacy
- Discrete Distribution Learning
- Sum-of-Squares
- Person-Level Privacy
- Information Theory
one_liner: 提出多项式时间用户级差分隐私离散分布估计算法，复杂度达信息论最优水平
practical_value: '- 可借鉴用户级差分隐私的离散分布估计框架，用于电商用户行为分布、商品点击分布的隐私建模，满足数据合规要求

  - 多项式时间DP估计算法可替换现有隐私计算模块的高复杂度估计逻辑，降低端到端计算延迟

  - 近信息论最优的样本复杂度边界可指导隐私推荐系统的训练数据量规划，减少冗余数据收集'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有用户级差分隐私（DP）下的离散分布学习方案难以同时满足多项式时间复杂度、近最优样本复杂度要求，无法适配大规模用户的隐私合规建模需求。

### 方法关键点
1. 面向批量用户场景：n个用户各贡献m个i.i.d样本，目标是将k维离散分布的估计总变差误差控制在α内
2. 提出6阶sum-of-squares鲁棒估计器，通过迹有界对角占优矩阵校准经验协方差与多项式协方差的差值，结合对称Grothendieck不等式构造可靠性证书

### 关键结果数字
- 纯(ε,0)-DP场景下样本量n=Õ(k/(α²m)+k/(α√m ε)+k/ε)，为首个多项式时间下仅差对数因子达信息论最优的方案
- 近似(ε,δ)-DP场景下n=Õ(k/(α²m)+k/(α√m ε)+k+log(1/δ)/ε)，δ=2^-Θ(k)时固定参数下样本量仅为Õ(k)
