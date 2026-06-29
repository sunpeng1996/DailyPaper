---
title: Blackwell Approachability and Gradient Equilibrium are Equivalent
title_zh: Blackwell可接近性与梯度均衡（GEQ）的等价性证明
authors:
- Brian W. Lee
- Nika Haghtalab
- Michael I. Jordan
- Ryan J. Tibshirani
affiliations:
- University of California, Berkeley
- Inria & École Normale Supérieure
arxiv_id: '2606.27315'
url: https://arxiv.org/abs/2606.27315
pdf_url: https://arxiv.org/pdf/2606.27315
published: '2026-06-25'
collected: '2026-06-27'
category: Other
direction: 在线学习框架等价性理论研究
tags:
- Online Learning
- Gradient Equilibrium
- Blackwell Approachability
- Regret Minimization
- Online Optimization
one_liner: 证明梯度均衡与Blackwell可接近性算法等价，打通在线学习多框架迁移路径
practical_value: '- 实时推荐排序、动态定价、在线广告出价等在线优化场景，可直接将成熟regret最小化算法的trick迁移到GEQ类任务，降低研发成本

  - 已有Blackwell可接近性、regret最小化的工程实现可复用解决GEQ场景问题，无需重新开发专用求解器

  - 遇到GEQ相关在线决策任务时，可基于等价性直接套用已有框架的收敛性保证，减少重复理论验证工作'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
Gradient Equilibrium（GEQ）是近年提出的在线优化框架，可泛化离线优化的一阶平稳性，适配在线共形预测等场景，但此前研究未明确GEQ与经典在线学习框架的关联，GEQ误差与regret被认为是不可比较的优化目标，其在在线学习体系中的定位模糊。
### 方法关键点
通过双向高效归约证明算法层面GEQ与Blackwell可接近性完全等价，二者可通过黑箱调用互相求解，无渐进误差损失；同时推导了GEQ的充要条件，建立了无约束/约束决策集下不同GEQ定义的归约路径。
### 关键结果
结合已有的可接近性、regret最小化、校准之间的等价结论，证明GEQ与上述所有经典在线学习框架均等价，可直接将regret最小化中的乐观估计、强自适应性等优化保证迁移到GEQ场景，归约过程无额外效率损耗。
