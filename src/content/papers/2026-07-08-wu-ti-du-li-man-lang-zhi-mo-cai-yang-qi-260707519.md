---
title: Gradient-free Riemannian Langevin Sampler
title_zh: 无梯度黎曼朗之万采样器
authors:
- Ricardo Baptista
- Olivier Zahm
affiliations:
- University of Toronto
- UGA
- Inria
- CNRS
- Grenoble INP
arxiv_id: '2607.07519'
url: https://arxiv.org/abs/2607.07519
pdf_url: https://arxiv.org/pdf/2607.07519
published: '2026-07-08'
collected: '2026-07-09'
category: Training
direction: 无梯度MCMC 多模态分布采样优化
tags:
- MCMC
- Gradient-free
- Riemannian-Langevin
- Sampling
- Multimodal-Distribution
one_liner: 提出无需目标密度梯度的GRiLS采样器，重塑局部几何提升多模态分布采样混合效率
practical_value: '- 多兴趣用户表征建模的多模态分布采样场景，可直接复用GRiLS的无梯度设计，降低高维用户向量采样的计算开销，避免兴趣表征模式坍塌

  - 召回/粗排阶段的长尾商品负采样，用GRiLS提升多模态商品分布的采样混合效率，减少样本偏差带来的模型效果衰减

  - 生成式推荐的候选Item采样场景，当目标排序分布导数不可得时，可复用交互粒子估计分布统计量的方案替代梯度计算，降低工程落地门槛'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
标准MCMC方法在多模态概率分布采样时普遍存在混合效果差、易陷入局部模式的问题，依赖梯度的采样方案无法适配导数不可得、或计算成本极高的复杂目标场景。
### 方法关键点
- 设计无梯度黎曼朗之万采样器GRiLS，引入黎曼度量重塑分布局部几何结构，大幅降低模式间跳转的能量门槛，全程无需计算目标密度的梯度
- 采用交互粒子集群实时估计目标分布的均值和协方差，无需提前输入分布先验信息，降低落地限制
### 关键结果
多模态基准测试集上，GRiLS相比现有梯度依赖、无梯度MCMC方案，混合效率提升显著，高维分布下跨模式遍历速度更优
