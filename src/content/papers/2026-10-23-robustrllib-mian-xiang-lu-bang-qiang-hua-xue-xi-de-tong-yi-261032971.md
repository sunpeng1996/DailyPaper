---
title: 'RobustRLlib: A Unified Library and Benchmark for Robust Reinforcement Learning
  Algorithms'
title_zh: RobustRLlib：面向鲁棒强化学习的统一算法库与基准
authors:
- Xi Chen
- Fengqi Hu
- Zeyu Shen
- Jiaying Xu
- Shangding Gu
- Pan Xu
- Anqi Liu
- Laixi Shi
affiliations:
- Johns Hopkins University
- University of California San Diego
- University of California Berkeley
- Duke University
arxiv_id: '2610.32971'
url: https://arxiv.org/abs/2610.32971
pdf_url: https://arxiv.org/pdf/2610.32971
published: '2026-10-23'
collected: '2026-10-26'
category: Training
direction: 鲁棒强化学习 · 算法库与基准评测
tags:
- Robust RL
- Benchmark
- Algorithm Library
- Distribution Shift
- Sim-to-Real
one_liner: 开源整合17类鲁棒RL算法的统一库与基准，覆盖273种扰动场景完成算法能力边界评测
practical_value: '- 做推荐场景RL策略（如动态定价、流量调控）的鲁棒性优化时，可直接复用RobustRLlib中17种开箱即用的鲁棒RL算法，避免重复造轮子

  - 评估RL策略在真实业务扰动（如流量突增、用户行为分布漂移）下的表现时，可复用其273种扰动配置的评测框架，快速定位策略鲁棒性短板

  - 开发适配电商场景的定制化鲁棒RL算法时，可基于其统一接口的可扩展代码框架快速迭代，省去底层环境、训练、评测模块的开发成本'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
鲁棒RL是强化学习落地真实场景的核心基础，但现有算法复用性差，不同扰动场景下的能力边界不清晰，严重阻碍其工业落地。
### 方法关键点
推出开源RobustRLlib，统一接口整合17种主流鲁棒在线RL、离线RL、安全RL算法；内置覆盖分布漂移、sim2real迁移等场景的增强评测平台，支持人形机器人、视觉-语言-动作等多类任务。
### 关键结果数字
完成273种扰动配置下的系统性评测，输出当前鲁棒RL算法的最新能力图谱，明确了现有算法的有效适用场景与待优化的鲁棒性缺口；开源代码可复现、易扩展，支持直接落地现有算法或快速开发新的鲁棒RL方案。
