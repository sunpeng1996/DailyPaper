---
title: Enhancing Bayesian Optimization and Active Learning Through Kernel Diversity
title_zh: 基于核多样性提升贝叶斯优化与主动学习性能
authors:
- Heng Zhang
- Haotian Xiang
- Qin Lu
- Konstantinos D. Polyzos
- Tara Javidi
affiliations:
- University of Georgia
- University of California San Diego
arxiv_id: '2608.24721'
url: https://arxiv.org/abs/2608.24721
pdf_url: https://arxiv.org/pdf/2608.24721
published: '2026-08-25'
collected: '2026-08-26'
category: Training
direction: 贝叶斯优化 · 主动学习效率优化
tags:
- Bayesian Optimization
- Active Learning
- Gaussian Process
- Kernel Ensemble
- Hyperparameter Tuning
one_liner: 提出KENDO统一框架，用核集成替代MCMC采样，大幅提升贝叶斯优化与主动学习的效率效果
practical_value: '- 推荐/大模型超参调优场景可替换传统MCMC贝叶斯优化为KENDO-BO，最多降低5倍计算开销，大幅提升调参效率

  - 冷启动标注采样等主动学习场景可采用KENDO-AL，对比MCMC基线最多提升27倍速度，同时保障预测校准效果

  - 核集成+自适应贝叶斯加权的思路可迁移至多目标排序优化场景，无需改动单优化器结构即可适配多目标需求'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
贝叶斯优化(BO)、贝叶斯主动学习(AL)的超参选择存在明显痛点：点估计方案易出现模型误配，导致效果不佳；全贝叶斯方案依赖MCMC采样，计算开销极高，落地难度大。

### 方法关键点
提出统一框架KENDO，用核集成+自适应贝叶斯加权替代超参采样，结合分歧感知采集策略，分别实例化为面向BO任务的KENDO-BO、面向AL任务的KENDO-AL；通过随机标量化扩展至多目标优化场景，保留单优化器的条件结构，降低适配成本。

### 关键结果
1. 单/多目标优化任务中，KENDO-BO效果比肩或优于SOTA方案，计算开销最多降低5倍；
2. 主动学习任务中，KENDO-AL预测校准效果优于基于MCMC的基线，推理速度最多提升27倍。
