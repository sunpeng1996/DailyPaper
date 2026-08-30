---
title: 'Making Latent Evolution Explicit: Operator-Structured Transitions for World
  Action Models'
title_zh: 显式化隐态演化：面向世界动作模型的算子结构化转移方法
authors:
- Xiaoxiao Lu
- Yunlong Dong
- Jiahao Shi
- Ye Yuan
affiliations:
- Huazhong University of Science and Technology
- Principia AI
arxiv_id: '2608.27259'
url: https://arxiv.org/abs/2608.27259
pdf_url: https://arxiv.org/pdf/2608.27259
published: '2026-08-27'
collected: '2026-08-30'
category: Agent
direction: Agent 世界模型隐态时序转移优化
tags:
- World Action Model
- Latent Transition
- Koopman Operator
- Inductive Bias
- Dynamical Systems
one_liner: 提出基于上下文调制算子的LEON架构，为世界动作模型的隐态时序转移提供演化专属归纳偏置
practical_value: '- 推荐系统用户/物品隐态的长短期时序演化建模可参考算子结构化转移设计，替代纯Transformer的token交互范式，引入演化专属归纳偏置，降低时序预测误差

  - 动态场景下的Agent行为/环境状态预测可复用「上下文调制算子+加性强迫」的双路结构，平衡共性演化规律与个性化突发扰动的建模需求

  - 隐态预测模块可独立替换原有系统的转移预测组件，无需重构整体表征与策略耦合逻辑，升级成本低，适合存量系统迭代'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有World Action Models（WAMs）在隐空间做状态演化预测时，普遍采用Transformer类预测器，归纳偏置聚焦token交互而非时序演化，限制了转移预测的准确性与鲁棒性，且转移模块常与表征、策略耦合难以独立优化。

### 方法关键点
提出Latent Evolution Operator Network（LEON），基于受控Koopman生成器演化理论：1）将当前隐态映射到可观测空间；2）通过上下文调制的共享演化算子结构建模共性时序转移规律；3）新增加性强迫通路补充个性化突发变化；4）完全解耦转移实现、表征学习、预测-策略耦合三个模块。

### 关键结果
在受控动力系统验证了算子传播与加性强迫的互补作用；在两类采用不同隐态预测-策略耦合方式的WAM架构中，LEON均显著提升闭环性能与鲁棒性，完全替换原有转移模块时依然有效。
