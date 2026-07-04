---
title: Conditional Inference Trees and Forests for Feature Selection
title_zh: 面向特征选择的条件推理树与森林方法研究
authors:
- Robert Milletich
- Justin Downes
- Steve Goley
- Newel Hirst
affiliations:
- Amazon Web Services
arxiv_id: '2607.01417'
url: https://arxiv.org/abs/2607.01417
pdf_url: https://arxiv.org/pdf/2607.01417
published: '2026-07-01'
collected: '2026-07-04'
category: Training
direction: 特征工程 · 特征排序与选择优化
tags:
- Feature Selection
- Random Forest
- Feature Ranking
- Model Efficiency
- Tabular Data
one_liner: 验证CIF作为top-k特征排序方法的效果，给出兼顾性能与效率的调优方案
practical_value: '- 做电商推荐/广告排序的特征筛选时，可使用CIF替代传统CART做top-k特征排序，降低多切分点特征带来的分裂选择偏置

  - CIF落地时优先开启自适应停止、采用近似阈值搜索，仅损失最多0.011的下游效果，可降低4~10.8倍的模型拟合耗时

  - 高维稀疏特征场景下用CIF做特征选择时，需适当提升单棵树的特征采样比例，避免重要特征被漏选'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
传统CART树存在分裂选择偏置，会优先选择切分点更多的特征；条件推理树/森林（CIT/CIF）虽解决了偏置问题，但重复permutation测试、阈值搜索带来极高算力开销，缺乏工业级落地的效果与效率验证。
### 方法关键点
基于真实基准数据集、运行时长消融实验、合成特征恢复实验，系统评估CIT/CIF作为top-k特征排序方法的表现；提出Bonferroni校正的+1 Monte Carlo permutation p值控制节点拒绝率；针对运行效率做多参数消融。
### 关键结果数字
CIF在22个数据集的17种分类方法中排名第4，8个数据集的18种回归方法中排名第3；关闭自适应停止、使用精确阈值搜索分别提升4.0~8.4倍、1.9~10.8倍拟合耗时，下游效果损失最高仅0.011。
