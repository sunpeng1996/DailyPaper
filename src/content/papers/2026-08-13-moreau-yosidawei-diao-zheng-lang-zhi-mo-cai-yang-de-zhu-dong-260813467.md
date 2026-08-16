---
title: Active-Trace Complexity Bounds for Moreau--Yosida Unadjusted Langevin Sampling
title_zh: Moreau-Yosida未调整朗之万采样的主动迹复杂度界
authors:
- Yuchen Xin
- Zhihua Zhang
affiliations:
- School of Mathematical Sciences, Peking University
arxiv_id: '2608.13467'
url: https://arxiv.org/abs/2608.13467
pdf_url: https://arxiv.org/pdf/2608.13467
published: '2026-08-13'
collected: '2026-08-16'
category: Other
direction: 非光滑优化采样算法理论分析
tags:
- Langevin Sampling
- Complexity Bound
- Moreau-Yosida Regularization
- Non-smooth Optimization
one_liner: 改进MYULA采样复杂度上界，结构化惩罚下精度依赖从ε⁻³降至ε⁻²
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有MYULA非光滑采样算法的复杂度分析依赖全局曲率上界d/λ，给出的理论界偏松，无法解释结构化惩罚下的实际高效性能。
### 方法关键点
引入参考主动迹B_ref（从π_λ启动的单步MYULA热子步中a_λ的平均值）作为离散误差的核心控制变量，替代传统全局曲率界；推导迭代次数上界与B_ref、算法精度的关联公式，同时给出平滑后目标与原目标的Moreau偏差上界。
### 关键结果数字
- 通用场景下，算法精度依赖为Õ(ε⁻³)，匹配原有理论结果
- 对分段线性、Lasso、组稀疏、总变分等结构化惩罚，B_ref与平滑参数λ无关，精度依赖降至Õ(ε⁻²)，比原有界提升一个数量级
