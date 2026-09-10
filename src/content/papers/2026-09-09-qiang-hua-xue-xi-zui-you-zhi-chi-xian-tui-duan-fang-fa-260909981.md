---
title: Optimal Value Inference for Reinforcement Learning
title_zh: 强化学习最优值离线推断方法
authors:
- Nan Lu
- Ethan Lee
- James M. Robins
- David Simchi-Levi
- Junwei Lu
arxiv_id: '2609.09981'
url: https://arxiv.org/abs/2609.09981
pdf_url: https://arxiv.org/pdf/2609.09981
published: '2026-09-09'
collected: '2026-09-10'
category: Eval
direction: 离线RL评估 · 长时序决策价值推断
tags:
- Reinforcement-Learning
- Offline-RL
- Value-Inference
- Neyman-Orthogonality
- Policy-Evaluation
one_liner: 提出基于自诱导Bellman方程的去偏RL最优值估计器，支持长时序非平稳策略下的离线有效推断
practical_value: '- 电商推荐、动态定价场景做长周期策略评估时，可复用去偏估计器，基于历史离线轨迹估算最优策略的长期收益，降低上线试错成本

  - LLM Agent工具调用的策略迭代环节，可借鉴softmax平滑Bellman算子的方法，优化长序列决策下的价值推断精度，减少策略漂移

  - 非平稳行为策略下的离线RL建模，可直接复用nuisance估计流程，无需假设行为策略固定，适配真实业务的环境动态变化'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有离线RL最优值推断依赖行为策略固定、决策时序有限的强假设，无法适配推荐、动态定价、LLM Agent等真实场景中策略动态变化、决策周期极长的需求，缺乏可靠的离线最优值评估方法。
### 方法关键点
1. 推导自诱导Bellman方程的两个 nuisance 固定点，用softmax近似最大Bellman算子实现平滑；
2. 基于Neyman正交构造去偏估计器，突破行为策略时变、决策时序发散的限制；
3. 给出可落地的 nuisance 估计算法流程。
### 关键结果
合成实验验证数值性能优于基线方法，在共享单车调度、LLM Agent工具调用两个真实场景下实现有效最优值推断，仅要求nuisance收敛速率达到主流ML方法可实现的水平即可保证渐近正态性。
