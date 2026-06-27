---
title: 'Ribbon: Scalable Approximation and Robust Uncertainty Quantification'
title_zh: Ribbon：面向鲁棒不确定性量化的可扩展近似方法
authors:
- Graham Gibson
- John Tipton
- Kellin Rumsey
- Natalie Klein
arxiv_id: '2606.27269'
url: https://arxiv.org/abs/2606.27269
pdf_url: https://arxiv.org/pdf/2606.27269
published: '2026-06-25'
collected: '2026-06-27'
category: Other
direction: 不确定性量化 · 可扩展机器学习近似
tags:
- Uncertainty Quantification
- Bayesian Bootstrap
- Influence Function
- Laplace Approximation
- Post-hoc Estimation
one_liner: 用单次拟合模型影响函数线性化替代重训练，实现可扩展鲁棒不确定性量化
practical_value: '- 推荐/排序模型可直接复用Ribbon的post-hoc线性代数方案输出不确定性，无需多次重训练或MCMC，大幅降低算力成本

  - 面对电商用户行为分布偏移、模型误设等场景，可利用其鲁棒sandwich covariance得到更可靠的不确定性估计，辅助流量灰度、冷门item探索决策

  - 可通过验证集调节concentration parameter α校准不确定性尺度，适配高客单价商品推荐、广告投放等不同风险等级的业务场景'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
复杂高维或误设模型的预测不确定性量化难度高，全贝叶斯推理、bootstrap重采样等方法虽能输出有理论依据的不确定性估计，但需后验采样或重复模型拟合，算力成本难以适配现代大规模ML模型。

### 方法关键点
- 用单次拟合模型的influence function线性化替代重复重训练，保留Bayesian bootstrap的一阶数据重加权结构，仅需post-hoc线性代数运算
- 支持通用concentration parameter α，构成可校准的Dirichlet-reweighted族，不确定性尺度可在验证集上调优
- 理论上，似然正确设定时渐近等价于flat-prior Laplace approximation，模型误设时可恢复鲁棒sandwich covariance

### 关键结果
在合成回归、MNIST分类、California Housing基准测试中，预测性能与主流方法相当，多个场景下校准性更优，全程无需重复模型训练。
