---
title: 'GRAPE: Gradient Refinement and Progress-Aware Exploitation for Query-Efficient
  High-Dimensional Bayesian Optimization'
title_zh: GRAPE：面向查询高效高维贝叶斯优化的梯度精炼与进度感知框架
authors:
- Richard Cornelius Suwandi
- Feng Yin
affiliations:
- School of Artificial Intelligence, The Chinese University of Hong Kong, Shenzhen
arxiv_id: '2608.25116'
url: https://arxiv.org/abs/2608.25116
pdf_url: https://arxiv.org/pdf/2608.25116
published: '2026-08-25'
collected: '2026-08-27'
category: Training
direction: 黑盒优化 · LLM Prompt调优
tags:
- Bayesian-Optimization
- Black-box-Optimization
- Prompt-Optimization
- Sample-Efficiency
- Gaussian-Process
one_liner: 提出两阶段高维贝叶斯优化框架GRAPE，提升黑盒优化、LLM提示优化等任务的查询效率
practical_value: '- 电商推荐/广告的超参调优场景可复用GRAPE框架，减少AB测试次数，降低调优成本，加快最优参数收敛速度

  - LLM Agent的Prompt调优、RAG系统的召回/排序参数调优等黑盒优化任务，可直接替换现有贝叶斯优化基线，提升调优效率

  - 高维排序模型的特征权重迭代优化场景，可借鉴梯度精炼+进度感知方向选择的设计，避免无效迭代步，降低计算开销'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
高维黑盒函数优化是机器学习核心难题，现有局部贝叶斯优化方法优先选择下降概率高的方向，忽略下降幅度，导致步长保守、查询浪费，尤其不适配评估成本高的场景（如LLM Prompt调优、超参AB测试）。
### 方法关键点
两阶段GRAPE框架第一阶段通过闭式采集函数锐化局部梯度后验，单调降低局部不确定性；第二阶段基于下降条件最大化期望降幅选择更新方向，后验足够锐化时收敛到真实最速下降方向。
### 关键结果
黑盒对抗攻击任务上比基线平均提速5.4×；LLM Prompt优化任务上最终平均regret比次优方法降低3.8 log-units，查询效率显著领先。
