---
title: 'Bayes-Optimal BER and AUC: Estimation and Evaluation of Estimators'
title_zh: 贝叶斯最优BER与AUC：估计方法及估计器评估
authors:
- Ryota Ushio
- Takashi Ishida
- Masashi Sugiyama
affiliations:
- Graduate School of Frontier Sciences, The University of Tokyo
- RIKEN AIP
arxiv_id: '2609.02304'
url: https://arxiv.org/abs/2609.02304
pdf_url: https://arxiv.org/pdf/2609.02304
published: '2026-09-02'
collected: '2026-09-05'
category: Eval
direction: 二分类任务最优性能上界评估
tags:
- BayesOptimal
- ModelEvaluation
- BER
- AUC
- SoftLabel
- Classification
one_liner: 推出基于软标签的贝叶斯最优BER/AUC估计器与无需真值的评估框架
practical_value: '- 电商点击/转化预估等不平衡二分类场景可直接用该方法计算AUC/BER理论天花板，判断算法迭代空间，避免无效调参

  - 面对带噪用户行为软标签（如点击置信度、停留时长伪标签），可复用文中保序变换+等渗回归的软标签降噪方法，提升模型训练效果

  - 无最优指标真值时，可直接用扩展后的FeeBee框架评估自定义指标估计器的有效性，无需额外构造合成数据集'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有贝叶斯最优性能估计仅支持准确率指标，无法适配样本不平衡、标注带噪的二分类场景，而这类场景中BER、AUC是核心业务指标，亟需对应的最优上界估计与评估方案。
### 方法关键点
1. 给出基于软标签的贝叶斯最优BER、AUC估计器，支持类先验未知、观测软标签受保序变换/加性噪声污染的真实场景，通过等渗回归+辅助硬标签恢复干净软标签，用硬标签截断均值估计类先验，同时给出有限样本误差边界；
2. 扩展FeeBee评估框架，无需知道最优指标真值即可评估任意最优BER/AUC估计器的效果。
### 关键结果
合成与真实数据集实验均验证了估计器与评估框架的有效性，在带噪、不平衡分类场景下估计偏差比同类基线方法低35%以上。
