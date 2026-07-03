---
title: Neural Certificate Pricing for Combinatorial Optimization Problems
title_zh: 面向组合优化问题的神经证书定价方法
authors:
- Jingyi Chen
- Xinyuan Zhang
- Xinwu Qian
affiliations:
- Department of Civil and Environmental Engineering, Rice University
arxiv_id: '2607.01185'
url: https://arxiv.org/abs/2607.01185
pdf_url: https://arxiv.org/pdf/2607.01185
published: '2026-07-01'
collected: '2026-07-03'
category: Other
direction: 组合优化 · 神经求解器性能优化
tags:
- Combinatorial Optimization
- Neural Solver
- Unsupervised Learning
- Dual Pricing
- Amortized Inference
one_liner: 无监督神经证书定价NCP框架，大幅提升组合优化求解效率与泛化能力
practical_value: '- 电商多仓调度、广告预算分配、组合选品等带约束的组合优化场景，可复用NCP的无监督对偶定价思路，替代枚举式约束校验，降低求解耗时

  - 可借鉴「神经网络预测+结构化恢复层」架构，解决推荐系统中大规模组合决策问题，平衡求解精度与推理速度

  - 其强分布外泛化特性可迁移到冷启动场景的组合决策，比如新商品池选品、新广告主预算分配，减少重新训练成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
组合优化问题因离散结构存在指数级搜索空间，传统方法需枚举大量候选解才能验证最优性，求解效率低，泛化性差，难以适配大规模工业约束决策场景。
### 方法关键点
无监督框架NCP利用「解的结构可行性可多项式时间验证、最优性验证需指数搜索」的不对称性，训练神经网络预测证书级对偶价格，搭配结构化恢复层构造原始边际解；本质为摊销分离，无需枚举违反约束的不等式，通过学习残差价格实现总效应的聚合恢复，满足证书一致性条件时解全局可行，且预测价格的一阶误差仅会带来目标值的二阶损失。
### 关键结果
在三类组合优化问题上，要么大幅优于现有SOTA神经基线，要么仅用极小部分计算开销就能匹配SOTA精度，同时分布外泛化能力显著更强。
