---
title: 'BLOKS: Scaling Kernel Solvers with Sketched Block Preconditioning'
title_zh: BLOKS：基于草图块预条件的可扩展核求解器
authors:
- Giordano Vitale
- Giacomo Meanti
- Marco Rando
- Blanca Ayuso de Dios
- Lorenzo Rosasco
affiliations:
- Università degli Studi di Genova
- Université Côte d'Azur
- Università degli Studi Milano–Bicocca
- Consiglio Nazionale delle Ricerche (CNR)
- Istituto Italiano di Tecnologia
arxiv_id: '2610.13382'
url: https://arxiv.org/abs/2610.13382
pdf_url: https://arxiv.org/pdf/2610.13382
published: '2026-10-09'
collected: '2026-10-13'
category: Training
direction: 大规模核模型训练效率优化
tags:
- Kernel Ridge Regression
- Preconditioning
- Sketching
- GPU Acceleration
- Large-scale Training
one_liner: 提出结合块Jacobi近似与sketch的预条件器，实现内存无关的大规模高性能KRR求解
practical_value: '- 做推荐系统大规模用户/物品特征的KRR类建模时，可复用该sketch+块预条件技巧，无需压缩参数规模即可降低训练内存开销，保证模型精度

  - 该GPU内存高效实现思路可迁移到推荐系统矩阵分解、核回归等需要大规模线性代数求解的训练工程中，降低资源占用

  - sketch+块预条件的组合思路可复用在大模型LoRA微调的优化器加速场景，降低矩阵求逆类操作的时间开销'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
Kernel Ridge Regression（KRR）理论完备，常被用于深度学习特性分析，但精确求解的时间、内存成本极高，难以适配大规模数据集。现有近似求解器的预条件步骤要么内存开销过大，要么需要压缩模型参数量，会损失模型表达能力与精度。
### 方法关键点
- 基于共轭梯度开发Nyström-sketched KRR求解器BLOKS，核心是结合块Jacobi近似与sketch的新型预条件器
- 预条件器内存开销完全独立于数据集规模与参数量，支持大模型扩展
- 提供了内存高效的GPU加速实现版本
### 关键结果
在大规模核求解器标准基准数据集上，精度表现与SOTA方法相当或更优，同时保持更友好的时间/内存复杂度
