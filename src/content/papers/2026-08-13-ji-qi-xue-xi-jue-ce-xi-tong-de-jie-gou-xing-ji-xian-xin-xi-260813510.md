---
title: 'On the Structural Limits of Machine Learning Decision Systems: An Information-Theoretic,
  Interaction-Based, and Stochastic-Dynamical Perspective'
title_zh: 机器学习决策系统的结构性极限：信息论、交互与随机动力学视角
authors:
- Nestor R. Barraza
- Gabriel Pena
affiliations:
- Universidad Nacional de Tres de Febrero
- Universidad de Buenos Aires
arxiv_id: '2608.13510'
url: https://arxiv.org/abs/2608.13510
pdf_url: https://arxiv.org/pdf/2608.13510
published: '2026-08-13'
collected: '2026-08-15'
category: Other
direction: 机器学习基础理论 · 性能边界分析
tags:
- Information_Theory
- Decision_System
- Performance_Bound
- Stochastic_Dynamics
- LLM_Agent
one_liner: 从信息论、交互建模、随机动力学视角推导ML决策系统固有性能边界，明确算法上限受数据生成过程约束
practical_value: '- 做推荐/广告算法优化前，可先用Fano界、Cramér-Rao不等式估算当前任务的理论性能天花板，避免无意义的算法调参内卷

  - 构建LLM+Agent推荐系统时，需重点校验数据独立性、遍历性、分布稳定性假设是否成立，否则模型泛化性会严重低于预期

  - 把交互型推荐系统视作反馈驱动的随机过程建模，可提前预判宏观涌现行为，规避流量突变、马太效应等业务风险'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前ML决策系统普遍仅以预测精度、计算效率为核心评估指标，忽略了底层数据生成过程的结构属性对性能的根本性约束，导致大量无意义的算法优化内卷。
### 方法关键点
1. 基于Fano-type bounds分析分类任务最小可实现误差，基于Cramér-Rao不等式分析参数估计精度极限，明确两类极限仅由底层数据模型决定，与算法复杂度无关；
2. 拆解独立性、遍历性、分布稳定性三类隐含假设对推理有效性的影响机制；
3. 将包含LLM的Agent架构等决策系统建模为反馈驱动的随机过程，分析状态依赖动力学引发的宏观涌现行为。
### 核心结论
数据模型的合理性是提升预测能力的核心前提，所有算法优化都无法突破数据本身带来的信息论边界。
