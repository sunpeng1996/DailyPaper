---
title: Generalization Analysis of Distributed Kernel-based Robust Gradient Descent
  Algorithms
title_zh: 分布式核鲁棒梯度下降算法的泛化性分析
authors:
- Jun-Yi Meng
- Zheng-Chu Guo
- Yuan Mao
affiliations:
- 浙江大学数学科学学院
- 华中农业大学信息学院
arxiv_id: '2609.11712'
url: https://arxiv.org/abs/2609.11712
pdf_url: https://arxiv.org/pdf/2609.11712
published: '2026-09-10'
collected: '2026-09-13'
category: Training
direction: 分布式训练 · 鲁棒梯度下降优化
tags:
- Distributed Learning
- Gradient Descent
- Kernel Method
- Generalization Bound
- Robust Learning
one_liner: 推导分布式核鲁棒梯度下降最优学习率，松弛本地机器数限制，提出通信效率优化策略
practical_value: '- 电商/推荐场景分布式训练召回、排序模型时，可参考鲁棒损失参数$l_σ$的选取逻辑，适配带噪声的用户行为数据，平衡模型鲁棒性与收敛速度

  - 多节点分布式训练（如跨部门数据隔离的联合建模）可借鉴本文松弛机器数上限的理论结论，合理扩展本地训练节点数量，无需担心泛化性能下降

  - 多机训练场景可复用通信高效优化策略，降低节点间的交互开销，提升整体训练收敛速度'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
海量数据、数据隔离（如跨机构、跨商家数据不能直接合并）场景下，单节点训练难以落地，现有分布式核梯度下降算法存在鲁棒性差、支持的本地机器数上限低、泛化边界宽松、通信开销大的问题。
### 方法关键点
1. 基于再生核希尔伯特空间特性与鲁棒损失$l_σ$的固有属性，结合梯度下降的谱特征，推导分布式核鲁棒梯度下降（DKRGD）的最优学习率，给出$σ$参数的选取规则，同时缓解训练饱和现象、保证统计鲁棒性。
2. 提出全新的算子乘积误差分析方法，得到更紧致的泛化边界，大幅松弛本地机器数的上限限制，同时保留最优学习率。
3. 设计通信高效训练策略，进一步提升DKRGD的收敛性能。
### 关键结果
理论验证DKRGD可在保持最优学习率、模型鲁棒性不变的前提下，可支持的本地机器数量上限较现有方法大幅提升，通信效率显著优于基线分布式梯度下降算法。
