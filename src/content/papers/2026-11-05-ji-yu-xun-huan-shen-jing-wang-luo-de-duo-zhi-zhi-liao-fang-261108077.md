---
title: Doubly-robust causal inference for multi-valued treatment regimes with recurrent
  neural networks
title_zh: 基于循环神经网络的多值治疗方案双稳健因果推断方法
authors:
- Jason Poulos
arxiv_id: '2611.08077'
url: https://arxiv.org/abs/2611.08077
pdf_url: https://arxiv.org/pdf/2611.08077
published: '2026-11-05'
collected: '2026-11-08'
category: Other
direction: 因果推断 · 多值处理效应估计
tags:
- CausalInference
- DoublyRobust
- RNN
- TreatmentEffect
- LongitudinalData
one_liner: 扩展纵向目标最小损失估计框架适配多值治疗，融合RNN实现低偏差动态因果效应估计
practical_value: '- 多值处理因果估计框架可直接迁移到电商多干预策略（如多档位优惠券、多召回池规则）的效果评估，解决传统二元因果方法适配性差的问题

  - 纵向LTMLE融合RNN的建模结构可复用在用户长周期行为序列下的动态推荐策略因果归因，降低动态规则下的估计偏差

  - 多分类处理分配建模比系列二分类回归更稳定的结论，可直接用到多干预场景的分流概率建模环节，提升推断稳定性'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有最优干预方案因果估计方法大多局限于二元或连续处理，多值竞争干预场景易违反正性假设，动态规则下估计偏差大，且难以适配时序协变量输入。
### 方法关键点
1. 扩展纵向目标最小损失估计器（LTMLE），引入多分类模型建模多值处理分配逻辑，适配多值竞争干预场景；
2. 融合RNN作为LTMLE框架的基础学习器，同时拟合结果、处理、删失三类时序模型，对比传统集成机器学习方案。
### 关键结果
- 仿真实验显示，集成ML或RNN版LTMLE均近似无偏，覆盖率接近标称值；
- 动态规则下，顺序g计算+集成ML的偏差显著高于LTMLE方案；
- RNN作为处理模型时，多分类建模比系列二分类回归的推断稳定性更强
