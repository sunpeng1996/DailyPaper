---
title: Machine Unlearning for Gibbs Supervised Learning Algorithms
title_zh: 面向Gibbs监督学习算法的精确机器遗忘方法
authors:
- Yaiza Bermudez
- Samir M. Perlaza
- Iñaki Esnaola
affiliations:
- INRIA
- Université de la Polynésie française
- University of Sheffield
- Princeton University
arxiv_id: '2609.29409'
url: https://arxiv.org/abs/2609.29409
pdf_url: https://arxiv.org/pdf/2609.29409
published: '2026-09-24'
collected: '2026-09-27'
category: Training
direction: 机器学习训练 · 机器遗忘技术
tags:
- Machine Unlearning
- Gibbs Learning
- ERM
- Relative Entropy Regularization
- Variational Optimization
one_liner: 基于ERM-RER变分框架实现Gibbs监督学习算法的精确机器遗忘，无需全量重训
practical_value: '- 电商推荐场景下应对用户「被遗忘权」合规需求时，可复用该方法实现Gibbs类召回/排序模型的精确数据遗忘，避免全量重训的算力成本

  - 借鉴框架内的样本动态重加权机制，可灵活调整训练样本权重（如高价值转化样本升权、噪声样本降权），无需重新启动全流程训练

  - 对于采用ERM-RER范式训练的生成式推荐模型，可直接复用该变分优化思路实现快速迭代调整'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
为满足GDPR等法规要求的「被遗忘权」，现有机器遗忘方案要么精度损失显著，要么需全量重训算力成本极高，且缺乏针对Gibbs监督学习算法的精确遗忘方案。
### 方法关键点
基于带相对熵正则的经验风险最小化（ERM-RER）构建变分框架：以原模型的相对熵为正则约束，最大化待遗忘数据集的期望经验风险，优化变量为模型空间的概率测度，最终输出新的Gibbs概率测度作为遗忘后模型。
### 关键结果
- 实现精确遗忘：遗忘后模型分布与在保留数据集上从零训练的模型完全一致
- 衍生通用ERM-RER样本重加权框架：可通过调整参考测度和正则因子灵活实现样本升权/降权，支持控制Gibbs算法泛化误差
