---
title: The First-Order Oracle Complexity of Lipschitz Convex Optimization in Nondual
  Settings
title_zh: 非对偶设置下Lipschitz凸优化的一阶预言机复杂度
authors:
- David Martínez-Rubio
- Brian Bullins
- Cristóbal Guzmán
- Mathieu Molina
affiliations:
- IMDEA Software Institute, Madrid, Spain
- Purdue University, West Lafayette, IN, USA
- Pontificia Universidad Católica de Chile, Santiago, Chile
- Tel Aviv University, Israel
arxiv_id: '2609.20687'
url: https://arxiv.org/abs/2609.20687
pdf_url: https://arxiv.org/pdf/2609.20687
published: '2026-09-17'
collected: '2026-09-19'
category: Other
direction: 凸优化理论 · 一阶算法复杂度分析
tags:
- Convex-Optimization
- First-Order-Method
- Oracle-Complexity
- Online-Learning
- Lipschitz-Optimization
one_liner: 解决非光滑版COLT公开问题，证明小可行域几何可提升凸优化收敛速率，给出匹配下界的最优速率界
practical_value: "- 做L1正则约束的稀疏召回/排序模型训练时，可参考其给出的ℓ1-ball下$\tilde O(1/T)$收敛速率上限，评估当前所用优化器的效率天花板\n\
  - 在线实时推荐场景的regret理论分析可复用其基于sequential fat-shattering维度的上下界推导框架\n- 大规模凸优化问题的复杂度下界评估可直接复用其ℓp/ℓq场景下的量化结论"
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
经典一阶凸优化收敛速率分析多基于通用假设，未考虑可行域与目标Lipschitz范数的几何匹配关系，COLT 2015公开问题提出p<q时ℓp球可行域是否能提升ℓq范数Lipschitz目标的优化速率，此前未得到非光滑场景下的证明。
### 方法关键点
1. 构造全新在线学习博弈框架，用观测到的仿射损失最大值评估比较器
2. 引入sequential fat-shattering维度作为组合度量，推导博弈值的上下界
3. 证明仅需可行域与次梯度集合满足凸、中心对称、符合极小极大定理即可适用相关结论
### 关键结果数字
ℓ1球下欧氏Lipschitz凸优化速率达到$	ilde O(1/T)$，较经典$O(1/	ext{√}T)$速率提升一个数量级，所有速率结果与已有下界匹配，仅差对数因子。
