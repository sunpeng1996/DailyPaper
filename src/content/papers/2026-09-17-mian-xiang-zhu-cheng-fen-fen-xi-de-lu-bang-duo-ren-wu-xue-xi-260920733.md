---
title: Robust Multi-Task Learning for Principal Component Analysis
title_zh: 面向主成分分析的鲁棒多任务学习方法
authors:
- Dali Liu
- Haolei Weng
arxiv_id: '2609.20733'
url: https://arxiv.org/abs/2609.20733
pdf_url: https://arxiv.org/pdf/2609.20733
published: '2026-09-17'
collected: '2026-09-20'
category: Training
direction: 鲁棒多任务学习 · 特征降维
tags:
- Multi-Task Learning
- PCA
- Robust Learning
- Dimensionality Reduction
- Minimax Optimization
one_liner: 提出抗离群任务的鲁棒多任务PCA框架，达到最小最大最优收敛速率
practical_value: '- 多场景（如不同城市/类目/活动）用户/物品高维特征降维时，可复用该框架的离群任务鲁棒逻辑，避免大促、冷门类目等异常场景样本污染全局特征空间

  - 跨域召回、多任务排序的特征预训练环节，可借鉴其matrix-depth的离群任务检测方法，自动过滤低质量/异常任务，提升模型跨场景泛化性

  - 离线特征工程中对多源高维数据做PCA降维时，可直接复用该方法，在异质数据场景下得到更鲁棒的低维特征表示'
score: 4
source: arxiv-stat.ML
depth: abstract
---

### 动机
传统PCA在多源异质数据降维时，无法适配任务间相似度未知、存在任意分布离群任务的场景，易导致eigenspace估计出现严重偏差，无法满足多场景建模的特征鲁棒性需求。
### 方法关键点
1. 设计两款鲁棒多任务PCA流程，跨任务挖掘相似性结构优化eigenspace估计精度，同时对离群任务保持鲁棒性；
2. 其中一款方案基于matrix-depth概念设计，实现了估计误差与离群任务占比的最优依赖，解决了鲁棒多任务学习的核心挑战；
3. 理论上严格证明了方法的非渐近收敛速率，在多类场景下达到minimax最优界。
### 关键结果
仿真与真实数据集验证，在存在30%以内离群任务的异质多源场景下，eigenspace估计精度显著优于传统单任务/多任务PCA基线，与理论推导的最优性能边界完全匹配
