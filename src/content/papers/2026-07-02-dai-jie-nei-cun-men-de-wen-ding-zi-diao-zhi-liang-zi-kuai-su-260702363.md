---
title: Stable Self-Modulating Quantum Fast-Weight Programmers with Bounded Memory
  Gates
title_zh: 带界内存门的稳定自调制量子快速权重编程器
authors:
- Kuo-Chung Peng
- Jiun-Cheng Jiang
- Chun-Hua Lin
- Yifeng Peng
- Junghoon Justin Park
- Huan-Hsin Tseng
- Hsin-Yi Lin
- Kuan-Cheng Chen
- Chen-Yu Liu
- Shinjae Yoo
affiliations:
- National Taiwan University
- Stevens Institute of Technology
- Seoul National University
- Brookhaven National Laboratory
- Imperial College London
arxiv_id: '2607.02363'
url: https://arxiv.org/abs/2607.02363
pdf_url: https://arxiv.org/pdf/2607.02363
published: '2026-07-02'
collected: '2026-07-05'
category: Other
direction: 量子时序建模 · 带界门控优化
tags:
- QFWP
- Quantum-Sequence-Modeling
- Time-Series-Forecasting
- Gated-Mechanism
- Long-Sequence-Stabilization
one_liner: 为量子序列建模的自调制QFWP引入带界门控，解决长序列发散问题，提升模型鲁棒性
practical_value: '- 长序列用户行为建模/电商流量/销量预测任务可复用「仅对历史记忆分支加有界激活、保留更新分支不受限」的门控设计思路，缓解记忆爆炸问题

  - 模型变体消融实验可参考其「仅保留新更新调制/仅保留旧状态调制」的对照方法，快速定位核心收益来源

  - 核心框架为量子计算场景设计，暂无法直接迁移到现有推荐/Agent的经典计算栈，仅可参考通用设计思路'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
自调制量子快速权重编程器（QFWP）将时序信息存储在动态编程的变分电路参数中，是实用化量子序列建模方案，但旧状态乘数无界，长序列场景易出现数值发散，限制实际应用。
### 方法关键点
1. 带界旧状态调制规则仅在循环记忆分支施加保号tanh门，加法更新、新更新调制逻辑保持不变，在控住数值范围的同时不破坏原有拟合能力
2. 设计4组对照变体：标准QFWP、全自调制QFWP、仅新更新调制、仅旧状态调制，精准定位性能提升的核心来源
### 关键结果
1. 量子动力学预测任务上，旧状态调制是相对标准QFWP的最稳定提升来源，带界门完全消除长序列发散，整体鲁棒性显著提升
2. 米兰SMS流量预测任务上，原始无界自调制QFWP仅在长输入窗口下有明确收益，行为特征与仅旧状态调制变体高度接近
