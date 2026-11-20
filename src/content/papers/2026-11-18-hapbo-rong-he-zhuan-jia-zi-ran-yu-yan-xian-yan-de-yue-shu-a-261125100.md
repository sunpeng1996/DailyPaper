---
title: 'HapBO: Harnessed $α$-$π$ Bayesian Optimization via Expert Natural Language
  Priors'
title_zh: HapBO：融合专家自然语言先验的约束型α-π贝叶斯优化方法
authors:
- Jean-Sébastien Giroux
- Rose Guay Hottin
- Marco Bonizzato
affiliations:
- Polytechnique Montréal 电气工程系
- MILA – Québec AI Institute
- Université de Montréal 神经科学系
arxiv_id: '2611.25100'
url: https://arxiv.org/abs/2611.25100
pdf_url: https://arxiv.org/pdf/2611.25100
published: '2026-11-18'
collected: '2026-11-20'
category: Training
direction: 贝叶斯优化 · 自然语言先验注入
tags:
- Bayesian Optimization
- Hyperparameter Tuning
- LLM Prior
- Natural Language Prior
- Sample Efficient
one_liner: 将自然语言专家/LLM先验编译为可复用信念函数，实现零in-loop调用的高效贝叶斯优化
practical_value: '- 推荐/广告系统超参调优时，可将运营、算法专家的自然语言经验（如「出价高于1元的广告CTR更高」）编译为信念函数注入BO流程，优化全程无LLM调用，大幅降低调优成本

  - Agent任务的工具选择、参数优化冷启动阶段，可将历史经验的自然语言描述转为可复用先验，仅12-20次查询即可拿到更优结果，适配小预算优化场景

  - BO注入业务先验时可复用有界乘数约束 trick，既保留原有采集函数的收敛性，还能对抗错误先验的负面影响，避免专家经验偏差导致优化结果崩溃'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
传统Bayesian Optimization (BO) 依赖显式概率先验提升采样效率，但工业场景的专家经验、业务规则多为自然语言形式无法直接使用，现有LLM辅助BO方法需在优化循环中反复调用LLM，成本高且易受错误先验干扰。
### 方法关键点
1. 仅单次调用专家/LLM提取结构化信念，确定性编译为值域[0,1]的可复用信念函数π，不受高斯分布限制；
2. 基于α-πBO框架，将π作为有界正乘数作用于采集函数，优化全程无LLM调用；
3. 理论证明对Expected Improvement (EI) 采集函数，即使存在对抗性错误先验，也能保留标准简单后悔收敛率。
### 关键结果
在40个HPOBench任务上取得最低总后悔值；真实场景下仅需12-20次查询即可提升优化效果，耗时和token成本仅为其他LLM-based BO方法的极小部分，优化全程零in-loop token开销。
