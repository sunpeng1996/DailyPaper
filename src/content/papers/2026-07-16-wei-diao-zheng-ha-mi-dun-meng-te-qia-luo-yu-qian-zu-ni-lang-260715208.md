---
title: Delocalization of bias in unadjusted Hamiltonian Monte Carlo and underdamped
  Langevin
title_zh: 未调整哈密顿蒙特卡洛与欠阻尼朗之万算法的偏差去局域化研究
authors:
- Yifan Chen
- Xiaoou Cheng
- Jonathan Niles-Weed
- Jonathan Weare
affiliations:
- University of California, Los Angeles (UCLA) Department of Mathematics
- Courant Institute, New York University
arxiv_id: '2607.15208'
url: https://arxiv.org/abs/2607.15208
pdf_url: https://arxiv.org/pdf/2607.15208
published: '2026-07-16'
collected: '2026-07-19'
category: Other
direction: 高维概率分布采样算法理论优化
tags:
- HMC
- Langevin Dynamics
- Sampling Theory
- Bias Control
- High-dimensional Statistics
one_liner: 将偏差去局域化结论拓展至未调整HMC与欠阻尼Langevin，降低高维采样迭代复杂度
practical_value: '- 本研究为纯统计采样理论成果，面向电商/推荐/Agent业务的直接可落地性极低

  - 若团队自研高维用户/物品表征分布采样组件，可参考其偏差控制结论优化迭代效率'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
未调整HMC、欠阻尼Langevin采样器自带固有偏差，传统引入Metropolis-Hastings调整消偏差的方案会因步长受限大幅提升迭代复杂度，现有偏差去局域化结论仅覆盖过阻尼Langevin算法。
### 方法关键点
提出通用矩阵多项式框架刻画离散积分器的传播算子，解决离散化带来的技术难点，将偏差去局域化结论拓展至未调整HMC、欠阻尼Langevin两类算法。
### 关键结果数字
在变量弱交互或稀疏交互假设下，仅需$O(\sqrt{K})$步积分（含$\log d$项修正）即可控制高维分布任意K维边际的$W_2$偏差；欠阻尼Langevin结论适配所有大摩擦参数场景，同时证明过阻尼Langevin的Leimkuhler-Matthews积分器同样存在偏差去局域化特性。
