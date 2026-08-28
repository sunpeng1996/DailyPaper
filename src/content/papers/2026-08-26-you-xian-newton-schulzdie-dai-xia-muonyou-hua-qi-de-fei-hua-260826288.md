---
title: 'Muon with Finite Newton-Schulz: The Smoothing Benefit in Nonsmooth Nonconvex
  Optimization'
title_zh: 有限Newton-Schulz迭代下Muon优化器的非光滑非凸优化收敛保证
authors:
- Mingyi Li
- Taira Tsuchiya
affiliations:
- The University of Tokyo
- RIKEN
arxiv_id: '2608.26288'
url: https://arxiv.org/abs/2608.26288
pdf_url: https://arxiv.org/pdf/2608.26288
published: '2026-08-26'
collected: '2026-08-28'
category: Training
direction: 大模型预训练优化器 · Muon收敛性分析
tags:
- Muon
- Newton-Schulz
- Nonconvex Optimization
- LLM Pretraining
- Optimizer
one_liner: 证明Muon的有限Newton-Schulz迭代为平滑机制而非近似误差，可保障非光滑非凸优化收敛
practical_value: '- 训练自研LLM/排序模型时，Muon的Newton-Schulz迭代次数无需过多，取O(log(1/ε))即可平衡精度与计算开销，无需追求精确极分解

  - 针对推荐场景非光滑损失（如带截断的pairwise损失、离散约束损失），可优先用有限步Newton-Schulz的Muon替代AdamW，避免精确极分解版Muon不收敛问题

  - 优化器二次开发时，可借鉴谱平滑思路，通过有限次迭代构造Lipschitz连续的谱映射，无需额外注入扰动即可获得非光滑场景收敛性'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
Muon已成为LLM预训练的主流优化器，通过少量Newton-Schulz迭代实现动量的近似正交化，现有理论要么将有限迭代视为精确极分解的近似误差，要么仅适用于光滑目标，无法解释其在非光滑非凸场景的实际效果，且精确极分解版Muon已被证实在非光滑场景可能不收敛，有限迭代的实际作用长期被低估。
### 方法关键点
- 基于折现online-to-nonconvex（O2NC）转换框架，将Muon的更新规则视为在线学习器，通过悔界推导平稳性保证
- 证明有限Newton-Schulz迭代将不连续的极映射转换为奇异值的Lipschitz映射，本质是构造了带平滑谱势的在线学习器
- 推导Newton-Schulz深度的权衡关系：深度增加会降低极分解近似误差，但会提升映射的Lipschitz常数，平衡二者仅需对数级深度
### 关键结果
- 非光滑非凸场景下，仅需q=O(log(1/ε))步Newton-Schulz迭代，即可达到O(ρ⁻¹ε⁻³ + ε⁻²)的样本复杂度，匹配当前非光滑非凸优化的最优界
- 光滑非凸场景下，样本复杂度达到O(ε⁻²)（确定性）、O(ε⁻⁴)（随机），与精确极分解版Muon的最优界一致，且随机场景下r²σ²/ε²项优化为rσ²/ε²
### 核心结论
Muon的有限Newton-Schulz迭代不是近似误差，而是保障非光滑场景收敛的核心设计，深度仅需对数增长即可满足精度要求
