---
title: 'Stable Movement for Nondual Lipschitz Convex Optimization: Efficiency and
  Nearly Optimal Oracle Rates'
title_zh: 非对偶Lipschitz凸优化的稳定迭代：效率与近最优Oracle收敛率
authors:
- David Martínez-Rubio
- Cristóbal Guzmán
affiliations:
- IMDEA Software Institute, Madrid, Spain
- Pontificia Universidad Católica de Chile, Santiago, Chile
arxiv_id: '2609.20701'
url: https://arxiv.org/abs/2609.20701
pdf_url: https://arxiv.org/pdf/2609.20701
published: '2026-09-17'
collected: '2026-09-19'
category: Other
direction: 凸优化理论 · 一阶Oracle复杂度优化
tags:
- Convex Optimization
- Lipschitz Optimization
- Oracle Complexity
- Cutting Plane Method
- First-order Optimization
one_liner: 提出近最优复杂度的非对偶Lipschitz凸优化算法，解决COLT 2015非光滑优化公开问题
practical_value: "- 仅从事上层推荐/广告/Agent业务逻辑开发的从业者无直接可借鉴点，核心为理论贡献\n- 若研发大规模深度学习优化器、非光滑损失求解算法，可参考其嵌套凸集追踪+深度割的迭代框架\n\
  - 带ℓ1正则的稀疏推荐模型训练场景，可复用其ℓ1球约束下$\tilde{O}(GR/T)$的近最优收敛率结论"
score: 4
source: arxiv-cs.LG
depth: abstract
---

## 动机
跨范数场景（ℓp球约束、ℓq范数度量Lipschitz性）下的凸优化算法长期未达到近最优Oracle复杂度，COLT 2015公开的非光滑优化相关问题未得到解决。
## 方法关键点
1. 将凸Lipschitz优化转化为演化束次水平集的嵌套凸集追踪问题，每次迭代要么输出低函数值点，要么对当前次水平集生成深度割，通过选择器稳定性与深度割强制移动的二分性控制迭代次数
2. 提出稳定中心新概念，严格约束T步迭代后中心的ℓq范数移动幅度
3. 基于蒙特卡洛平均的选择器可在实数运算模型下多项式时间实现
## 关键结果数字
p<q场景下T次Oracle查询后误差达$	ilde{O}_{p,q}(GR/T^{1/p-(1/q-1/2)_+})$；p=1、q=2（ℓ1球约束+欧氏Lipschitz性）场景收敛率达$	ilde{O}(GR/T)$，匹配近最优理论界，解决了COLT 2015公开问题的非光滑分支
