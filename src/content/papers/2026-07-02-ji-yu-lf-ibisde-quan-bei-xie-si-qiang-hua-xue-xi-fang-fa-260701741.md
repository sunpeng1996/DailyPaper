---
title: Full Bayesian Reinforcement Learning via LF-IBIS
title_zh: 基于LF-IBIS的全贝叶斯强化学习方法
authors:
- Stefano Masini
- Cecilia Viscardi
- Michela Baccini
arxiv_id: '2607.01741'
url: https://arxiv.org/abs/2607.01741
pdf_url: https://arxiv.org/pdf/2607.01741
published: '2026-07-02'
collected: '2026-07-04'
category: Agent
direction: 贝叶斯强化学习 Agent 决策优化
tags:
- Bayesian RL
- Likelihood-Free Inference
- Importance Sampling
- Sequential Decision Making
- Uncertainty Quantification
one_liner: 提出无似然迭代批量重要性采样算法LF-IBIS，解决贝叶斯强化学习需显式似然的落地限制
practical_value: '- 电商小流量冷启动、新品推荐等小样本决策场景可借鉴其策略不确定性量化方法，优化探索-利用权衡，降低试错成本

  - 广告出价、实时流量调控等无显式环境建模的动态场景，可复用其无似然贝叶斯推理框架，无需强制拟合复杂用户/流量分布

  - 在线决策Agent的信念更新模块可参考其迭代批量重要性采样方案，平衡实时更新效率与推理精度'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有贝叶斯强化学习（BRL）可利用先验知识缓解小样本决策痛点，但要求显式可计算的环境似然函数，而真实业务场景（如动态用户行为、实时流量波动）的环境似然通常不可得或难以建模，极大限制了BRL的落地。
### 方法关键点
1. 提出LF-IBIS算法，融合近似贝叶斯计算与迭代批量重要性采样，无需显式似然即可实现全贝叶斯推理；
2. 支持在线信念更新，随新交互数据迭代优化，同时输出环境参数与最优策略的近似后验分布；
3. 天然提供策略不确定性量化能力，可直接用于优化探索-利用权衡。
### 关键结果
在临床试验响应自适应随机化仿真任务上，闭式后验验证了方法的后验计算准确性；在无闭式后验的复杂场景下，可稳定实现最优策略的在线迭代更新。
