---
title: Fast Rates for Semi-Supervised Learning via Data-Augmentation Graph Regularization
title_zh: 基于数据增强图正则的半监督学习快速收敛率分析
authors:
- Adam M. Oberman
affiliations:
- Department of Mathematics and Statistics, McGill University
- Mila, Quebec AI Institute
- LawZero
arxiv_id: '2607.07513'
url: https://arxiv.org/abs/2607.07513
pdf_url: https://arxiv.org/pdf/2607.07513
published: '2026-07-08'
collected: '2026-07-13'
category: Training
direction: 半监督学习训练收敛率理论分析
tags:
- Semi-Supervised-Learning
- Data-Augmentation
- Graph-Regularization
- Convergence-Rate
- Algorithmic-Stability
one_liner: 从理论层面解释自监督学习高标注效率成因，证明标注样本量下O(1/n_L)的快速转导收敛率
practical_value: '- 做少样本新品打标、小众类目用户建模等半监督任务时，可引入图拉普拉斯正则约束无标注样本，获得比纯监督更快的收敛速度，降低标注成本

  - 筛选数据增强策略时可参考$R_{\mathrm{DA}}(y)$指标，优先选择跨标签边界切割质量低的增强方法，进一步提升少样本场景下的模型效果

  - 针对标注量不足的召回/排序任务，可简化自监督损失结构，去掉负采样、正交约束等冗余模块，在不损失特征质量的前提下降低训练开销'
score: 4
source: arxiv-stat.ML
depth: abstract
---

**动机**
自监督学习仅用少量标注即可匹配监督学习精度，但标注效率的理论机制长期缺失，现有极限分析依赖精确核、泛化特征等不现实假设。

**方法关键点**
将数据增强在无标注数据上诱导的相似图作为下游学习的图拉普拉斯正则项，迁移Johnson&Zhang的留一法稳定性分析框架到增强图场景，无需前述强假设。

**关键结果数字**
证明转导场景下收敛率达$O(1/n_L)$，远优于监督学习的$O(1/\sqrt{n_L})$；误差界明确纳入增强对齐误差$R_{\mathrm{DA}}(y)$，增强效果越好所需标注量越少；提出的简化损失可移除标准自监督目标的投影头、负采样、正交约束开销，无限数据下仍能恢复top-K理想特征，准确匹配实际观测的精度-标注量曲线。
