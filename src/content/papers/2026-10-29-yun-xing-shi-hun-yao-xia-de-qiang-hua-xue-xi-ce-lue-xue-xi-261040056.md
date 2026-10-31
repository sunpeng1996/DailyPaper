---
title: 'Reinforcement Learning Under Runtime Confounding: Policy Learning and Off-Policy
  Evaluation'
title_zh: 运行时混淆下的强化学习：策略学习与离线策略评估
authors:
- Raphael Kim
- Michele Santacatterina
- Ramin Zabih
- Keith Barnatchez
affiliations:
- Cornell Tech, Cornell University
- NYU Grossman School of Medicine
- Johns Hopkins University
arxiv_id: '2610.40056'
url: https://arxiv.org/abs/2610.40056
pdf_url: https://arxiv.org/pdf/2610.40056
published: '2026-10-29'
collected: '2026-10-31'
category: Training
direction: 强化学习 · 策略训练与离线评估
tags:
- Reinforcement Learning
- Off-Policy Evaluation
- Policy Learning
- Runtime Confounding
- Sequential Decision Making
one_liner: 针对部署时关键变量缺失的运行时混淆问题，提出无偏RL策略学习、高效OPE方法及混淆代价诊断工具
practical_value: '- 电商推荐/广告系统受合规限制无法采集用户敏感属性时，可复用所提运行时混淆下策略学习方法，规避合规风险同时降低策略偏置

  - 离线A/B评估场景下，可引入本文半参数高效OPE流程，解决训练日志有全量特征、上线时特征缺失带来的评估偏差问题

  - 策略上线前可使用本文混淆代价诊断工具，量化缺失特征对推荐/广告效果的影响，提前评估策略上线风险'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
RL在电商、医疗等序列决策场景落地时，受合规、伦理、运维限制，部署阶段无法采集部分训练时可用的关键决策变量（即运行时混淆变量）。这类混淆会随决策序列逐步传播，导致策略学习和离线策略评估（OPE）出现严重偏置，现有RL方法未针对性解决该训练部署特征不匹配问题。
### 方法关键点
1. 提出运行时混淆场景下的无偏策略学习算法，仅依赖部署时可观测特征即可完成无偏训练；
2. 设计半参数高效OPE流程，大幅降低训练部署特征不匹配带来的评估误差；
3. 给出运行时混淆代价的诊断方法，可量化变量缺失对模型效果的影响。
### 关键结果
所提方法在仿真序列决策基准和模拟电商动态定价场景下验证，策略偏置、OPE误差均显著优于现有基线方法，诊断工具可精准量化变量缺失带来的效果损失。
