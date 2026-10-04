---
title: 'Counterfactual Generation via Flow Matching: Coupling-Sensitive End-to-End
  Rates'
title_zh: 基于流匹配的反事实生成：耦合敏感的端到端误差界
authors:
- Yunrui Guan
- Krishnakumar Balasubramanian
- Shiva Prasad Kasiviswanathan
affiliations:
- Johns Hopkins University
- University of California, Davis
- Amazon
arxiv_id: '2610.01193'
url: https://arxiv.org/abs/2610.01193
pdf_url: https://arxiv.org/pdf/2610.01193
published: '2026-10-01'
collected: '2026-10-04'
category: Other
direction: 反事实生成 · 流匹配理论与方法
tags:
- Counterfactual Generation
- Flow Matching
- Doubly Robust
- SDE Sampler
- KL Bound
one_liner: 提出耦合敏感的流匹配反事实生成框架，给出端到端理论保证，有限步采样效果优于确定性ODE采样
practical_value: '- 反事实生成可用于电商推荐/营销的干预效果预估（如促销、调价后的用户行为模拟），该方法的分数校正SDE采样器在有限计算预算下精度更高，适配低延迟线上场景

  - 样本拆分+双鲁棒训练的范式可迁移到用户行为反事实建模任务，降低观测数据偏差带来的估计误差，提升反事实样本的可靠性

  - 耦合敏感的KL误差界可作为反事实生成模型的量化评估指标，用于衡量电商策略模拟结果的可信度，减少决策风险'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有流匹配反事实生成方法依赖速度场全局正则化假设，误差界维度依赖性差，缺少有限样本下的端到端理论保证，实际有限步采样性能不佳。
### 方法关键点
1. 设计融合样本拆分双鲁棒训练目标的流匹配框架，引入观测事实结果与条件模型拟合的目标结果间的可学习耦合
2. 采用基于高斯平滑插值的分数校正SDE采样器，实现低步数高效生成
3. 推导耦合敏感的欧拉离散KL误差界，误差由源-目标位移矩控制而非全局正则，维度接近线性依赖，同时拆分多来源误差得到端到端生成的有限样本保证
### 关键结果
合成与半合成图像基准实验验证了耦合依赖理论的正确性，有限离散预算下，随机采样器性能优于对应确定性ODE采样器
