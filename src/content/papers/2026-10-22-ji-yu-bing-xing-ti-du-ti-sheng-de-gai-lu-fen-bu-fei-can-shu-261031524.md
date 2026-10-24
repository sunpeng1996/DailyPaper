---
title: Nonparametric autoregressive estimation of probability distributions with parallel
  gradient boosting
title_zh: 基于并行梯度提升的概率分布非参数自回归估计方法
authors:
- Rémy Chapelle
affiliations:
- Université Paris-Saclay, UVSQ, Inserm, CESP
- Université Paris-Saclay, Université Paris Cité, ENS Paris-Saclay, CNRS, SSA, Inserm,
  Centre Borelli
- École du Val-de-Grâce, Service de Santé des Armées
arxiv_id: '2610.31524'
url: https://arxiv.org/abs/2610.31524
pdf_url: https://arxiv.org/pdf/2610.31524
published: '2026-10-22'
collected: '2026-10-24'
category: Other
direction: 高维概率分布估计 · 非参数自回归建模
tags:
- Nonparametric Estimation
- Autoregressive Model
- Gradient Boosting
- Probability Distribution
- High Dimensional Data
one_liner: 提出结合并行梯度提升的非参数自回归框架，实现高维场景下联合概率分布的高效准确估计
practical_value: '- 可借鉴自回归因子分解思路优化高维用户/商品特征的联合分布建模，缓解维度灾难

  - 并行梯度提升的条件分布估计方案可直接复用在CTR/CVR分布预估场景，无需复杂调参

  - 特征依赖图稀疏时，可套用论文给出的收敛率边界理论指导建模复杂度评估'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
高维场景下联合概率分布非参数估计长期受维度灾难困扰，现有方法难以平衡灵活性与计算效率，无法适配工业级高维特征建模需求。
### 方法关键点
1. 将联合分布自回归因子分解为多个条件分布乘积，基于次可加损失函数推导自回归估计器的收敛率边界，其精度瓶颈仅取决于分解后最难估计的单个条件因子；
2. 结合无向依赖图的变量消去过程，可利用图稀疏性进一步收紧收敛率上界，降低建模开销；
3. 落地实现基于并行梯度提升的非参数自回归估计器，无需额外优化因子分解顺序。
### 关键结果
在多组模拟与真实数据集上的估计性能均优于同类基线，效果具备竞争力。
