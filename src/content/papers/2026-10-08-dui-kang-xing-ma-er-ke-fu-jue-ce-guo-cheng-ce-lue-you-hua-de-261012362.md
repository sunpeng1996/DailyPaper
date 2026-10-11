---
title: Closing the Horizon Gap in Policy Optimization for Adversarial MDPs
title_zh: 《对抗性马尔可夫决策过程策略优化的Horizon差距填补方法》
authors:
- Mingyi Li
- Taira Tsuchiya
arxiv_id: '2610.12362'
url: https://arxiv.org/abs/2610.12362
pdf_url: https://arxiv.org/pdf/2610.12362
published: '2026-10-08'
collected: '2026-10-11'
category: Agent
direction: 对抗MDP 策略优化 regret界提升
tags:
- Adversarial MDP
- Policy Optimization
- Regret Bound
- Reinforcement Learning
- Horizon Gap
one_liner: 通过正则化Q函数填补对抗MDP策略优化的regret horizon差距 达到当前最优界
practical_value: '- 做多轮对话Agent、长周期广告投放等序列决策场景的策略优化时，可参考正则化Q函数的全局状态-动作对联合更新思路，降低长序列累计regret

  - 针对Horizon较长的序列决策业务（如用户生命周期价值优化），可借鉴本文消除Horizon放大因子的思路，优化长周期策略的稳定性

  - 若业务无底层策略优化自研需求，本文主要为学术贡献，可直接复用价值有限'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有对抗MDP下的策略优化算法计算效率优于全局占比度量类算法，但regret界存在额外的Horizon H因子放大问题，性能上限更低。

### 方法关键点
基于正则化Q函数实现策略优化，全局联合管控所有状态-动作对的本地更新稳定性，而非单独控制每个状态的更新，避免引入Horizon相关的误差放大。

### 关键结果
- 已知转移场景下高概率regret界为$\widetilde O(\sqrt{HS(H+A)T})$，未知转移场景下为$	ilda O(HSootelax{AT})$（哦不对，正确的是$\widetilde O(HS\\sqrt{AT})$）
- 两类场景均消除了原策略优化方法的H因子冗余，后者匹配当前已知最优界
- 可扩展到对抗线性混合MDP场景，获得同等Horizon依赖优化效果
