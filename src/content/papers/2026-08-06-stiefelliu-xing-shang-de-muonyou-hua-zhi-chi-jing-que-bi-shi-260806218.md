---
title: Muon on the Stiefel Manifold Admits an Exact Closed-Form Update
title_zh: Stiefel流形上的Muon优化支持精确闭式更新
authors:
- Mikhail Solonko
- Molozhavenko Alexander
- Maxim Rakhuba
affiliations:
- HSE University
arxiv_id: '2608.06218'
url: https://arxiv.org/abs/2608.06218
pdf_url: https://arxiv.org/pdf/2608.06218
published: '2026-08-06'
collected: '2026-08-08'
category: Training
direction: 正交约束优化 · 深度学习训练优化
tags:
- Constrained Optimization
- Muon Optimizer
- Riemannian Optimization
- Stiefel Manifold
- Skewon
one_liner: 推导Stiefel流形上Muon的精确闭式更新，提出带收敛保证的高效正交约束优化算法Skewon
practical_value: '- 推荐系统用户/物品嵌入训练、Semantic ID生成的正交约束场景，可直接替换现有迭代式Muon变种为Skewon，降低计算开销同时保证收敛性

  - LoRA微调（尤其是多场景多任务LoRA）的权重正交正则优化，可复用Skewon的闭式更新逻辑，减少调参成本

  - 现有带正交约束的模型训练链路无需大幅改造即可接入Skewon，适配Adam等常规优化器的工程实现流程'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
Stiefel流形（列正交矩阵集合）广泛应用于深度学习嵌入正则、对比学习、正交约束训练等场景，现有流形适配版Muon优化方法多依赖启发式、近似或迭代更新，计算效率不稳定且缺乏严格收敛保证。
### 方法关键点
1. 严格推导证明Stiefel流形上的Muon更新存在精确闭式解，无需迭代近似；
2. 基于该闭式解开发Skewon算法，实现正交约束优化的高效工程落地；
3. 从理论上证明Skewon在光滑非凸场景下的一阶收敛性。
### 关键结果
相比现有启发式流形Muon变种，Skewon更新计算效率提升显著，同时消除了启发式方法的收敛性风险，可直接适配各类带正交约束的深度学习训练任务。
