---
title: Graph Neural Multilevel Preconditioners for Iterative Solvers
title_zh: 面向迭代求解器的图神经多级预条件器
authors:
- Zechen Zhang
- Rui Peng Li
- Yousef Saad
affiliations:
- University of Minnesota
- Lawrence Livermore National Laboratory
arxiv_id: '2607.28456'
url: https://arxiv.org/abs/2607.28456
pdf_url: https://arxiv.org/pdf/2607.28456
published: '2026-07-30'
collected: '2026-08-03'
category: Other
direction: GNN · 稀疏线性系统迭代求解优化
tags:
- GNN
- Preconditioning
- Multilevel Methods
- Iterative Solvers
- Sparse Matrix
one_liner: 以代数多重网格层级为结构先验，提出适配通用稀疏系统的统一框架图神经多级预条件器
practical_value: '- 核心为科学计算领域数值求解方向学术贡献，电商/推荐/Agent业务可直接借鉴点有限

  - 若涉及大规模稀疏矩阵迭代求解类底层算法优化，可参考AMG层级+GNN融合的结构先验设计思路'
score: 3
source: arxiv-cs.LG
depth: abstract
---

### 动机
大规模稀疏线性系统求解是科学计算核心任务，经典代数多重网格（AMG）预条件器虽扩展性强，但在非对称/不定系统上鲁棒性显著下降，现有数据驱动的GNN预条件器对AMG式层级结构的实际应用价值缺乏系统性研究。
### 方法关键点
图神经多级预条件器（GMP）将AMG层级作为结构先验，在统一框架内端到端学习平滑、约束、插值三类算子，可作为即插即用组件适配标准Krylov求解器，覆盖通用稀疏系统场景。
### 关键结果
在800+稀疏矩阵基准集上对比经典AMG、单级ILUT、SOTA GNN预条件器，明确了多级GNN预条件可提升收敛速度的适用区间，同时量化了其相较于强单级基线存在额外开销的边界。
