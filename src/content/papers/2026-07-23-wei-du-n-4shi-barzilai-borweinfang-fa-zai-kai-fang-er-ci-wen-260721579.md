---
title: Barzilai-Borwein Fails Superlinear Convergence on an Open Set of Quadratics
  for Every Dimension $n\geq 4$
title_zh: 维度n≥4时Barzilai-Borwein方法在开放二次问题集上不满足超线性收敛
authors:
- Dawei Li
- Xiaotian Jiang
- Mingyi Hong
affiliations:
- University of Minnesota
arxiv_id: '2607.21579'
url: https://arxiv.org/abs/2607.21579
pdf_url: https://arxiv.org/pdf/2607.21579
published: '2026-07-23'
collected: '2026-07-25'
category: Other
direction: 连续优化理论 · BB步长收敛性分析
tags:
- Barzilai-Borwein
- Convergence_Analysis
- Gradient_Descent
- Optimization_Theory
one_liner: 证明n≥4时BB1方法在正测度严格凸二次问题集上仅线性收敛，否定其几乎处处超线性收敛猜想
practical_value: '- 高维（≥4维）模型训练场景用BB类步长优化器时，不可默认其有超线性收敛效率，高维 ill 条件任务需搭配步长自适应调整策略

  - 可复用论文给出的梯度、目标间隙几何序列上下界，作为训练收敛性监控的阈值参考，提前识别收敛异常

  - 核心为优化理论贡献，无BB优化器收敛异常问题的业务无需额外调整现有策略'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
Barzilai-Borwein（BB）是无额外计算开销的梯度下降步长策略，工业界广泛应用，但收敛动力学机制研究不足，长期悬而未决的核心问题是：其是否对几乎所有严格凸二次问题和初始化都能实现超线性收敛。
### 方法关键点
针对所有n≥4的有限维度，构造了具有正勒贝格测度的非空开放严格凸二次问题与初始点集合，采用计算机辅助证明四维投影BB动力学存在非共振吸引七周期的结构，推导得到梯度各分量、误差能量范数、目标间隙的双边几何界，明确上下界常数分别为ρ_min=1e-6、ρ_max=0.61。
### 关键结果
证明该问题集合下长BB方法（BB1）仅能线性收敛，完全排除超线性收敛可能性，否定了BB几乎处处超线性收敛的学界猜想。
