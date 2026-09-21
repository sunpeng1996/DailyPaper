---
title: Schedule optimization for tau-leaping in masked discrete diffusion
title_zh: 掩码离散扩散模型中tau-leaping采样的调度优化
authors:
- Cecilia Secchi
- Giacomo Zanella
arxiv_id: '2609.21960'
url: https://arxiv.org/abs/2609.21960
pdf_url: https://arxiv.org/pdf/2609.21960
published: '2026-09-18'
collected: '2026-09-21'
category: Other
direction: 离散扩散 · 采样调度优化
tags:
- discrete diffusion
- tau-leaping
- sampling schedule
- factorization error
- generative modeling
one_liner: 推导掩码离散扩散tau-leaping采样的最优调度，量化调度对因子分解误差的影响
practical_value: '- 若采用离散扩散做GenRec/Semantic ID生成，可复用论文推导的tau-leaping最优调度，在不增加采样步数的前提下降低因子分解误差，提升生成质量

  - 可借鉴论文提出的依赖密度ρ估计方法，针对推荐序列/商品ID的依赖特性定制采样调度，效果优于通用均匀调度

  - 当生成序列的token依赖存在退化特性时，采用论文给出的非均匀调度，可获得比均匀调度更优的渐近误差阶'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
掩码离散扩散普遍采用tau-leaping方法加速采样，每步并行揭示多个坐标时用乘积分布替代联合条件分布，会产生即使预测器完全准确也无法消除的因子分解误差$ε_\text{fact}$，现有调度选择缺乏系统理论指导。
### 方法关键点
1. 给出$ε_\text{fact}$的精确积分表示，引入分布相关的依赖密度$\rho$刻画坐标间条件依赖随已揭示坐标比例的演化规律；2. 推导有限$K$步优化问题的递归平稳方程，在单调性条件下证明唯一最优解存在；3. 给出$N,K\to\infty$时最优极限平滑调度的显式刻画，量化随机块大小相对确定性规划的额外代价。
### 关键结果
当$\rho_N$一致收敛到严格正连续剖面时，优化固定平滑调度仅能改善$ε_\text{fact}$的首项常数，不改变$N/K$的缩放阶；若$\rho_N$退化，适配调度可比均匀调度提升误差的渐近阶。
