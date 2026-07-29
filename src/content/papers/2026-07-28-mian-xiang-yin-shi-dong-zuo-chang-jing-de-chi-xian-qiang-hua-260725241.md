---
title: 'Learning from the Unseen: Offline Reinforcement Learning with Hidden Actions'
title_zh: 面向隐式动作场景的离线强化学习鲁棒评估方法
authors:
- Zeyu Bian
- Ying Zhou
- Yifan Cui
affiliations:
- Department of Statistics, Florida State University
- Department of Statistics, University of Connecticut
- Center for Data Science, Zhejiang University
arxiv_id: '2607.25241'
url: https://arxiv.org/abs/2607.25241
pdf_url: https://arxiv.org/pdf/2607.25241
published: '2026-07-28'
collected: '2026-07-29'
category: Eval
direction: 离线强化学习 · 隐式动作策略评估
tags:
- Offline-RL
- Off-Policy-Evaluation
- Hidden-Action
- Multiple-Robustness
- Influence-Function
one_liner: 首个解决离线RL隐式动作问题，提出多重鲁棒LURE估计器，支持有效统计推断
practical_value: '- 电商动态调价、序列推荐、广告投放等RL落地场景中，若存在未记录的运营动作、用户隐式决策等隐式动作，可引入LURE框架用下一状态作为动作代理，降低策略离线评估的偏差

  - LURE的多重鲁棒设计思路可直接复用，当业务中部分拟合模块精度不足时，只要多个nuisance组件的部分组合拟合正确，仍能保证策略效果估计一致性，减少离线评估误导性结论

  - 基于RL的推荐策略训练时，若数据集存在动作缺失、噪声问题，可适配LURE的识别框架，无需额外标注真实动作，降低数据标注成本'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
标准离线RL算法默认数据集中动作可无误差观测，但真实业务场景中大量真实动作不可见，仅能获取带噪声的代理变量，导致现有方法估计偏差高、结论不可靠。
### 方法关键点
针对无限horizon折扣MDP的离轨策略评估场景，利用下一状态作为隐式动作的天然代理，实现策略值可识别；基于影响函数构建LURE估计器，具备多重鲁棒性，满足渐近正态性，可支撑有效统计推断，为业内首个针对隐式动作离线RL问题的解决方案。
### 关键结果
仿真实验验证LURE估计精度优于基线方法，在基于MIMIC-III数据库的脓毒症管理场景测试中，相比现有离线RL方法估计偏差显著降低。
