---
title: 'Optimal Transport Meets Reinforcement Learning: A Survey'
title_zh: 最优传输与强化学习交叉应用研究综述
authors:
- Yujie Zhu
- Charles A. Hepburn
- Matthew Thorpe
- Giovanni Montana
affiliations:
- University of Warwick
arxiv_id: '2610.01413'
url: https://arxiv.org/abs/2610.01413
pdf_url: https://arxiv.org/pdf/2610.01413
published: '2026-10-01'
collected: '2026-10-04'
category: Agent
direction: Agent决策优化 · 最优传输交叉应用
tags:
- Optimal Transport
- Reinforcement Learning
- Imitation Learning
- Offline RL
- Distribution Shift
one_liner: 系统梳理最优传输在强化学习中的应用逻辑、选型方法、落地挑战与开放问题
practical_value: '- 离线RL优化推荐/广告排序时，可采用OT距离替代KL/JS散度解决分布弱重叠下的度量失效问题，适配流量分布漂移场景

  - 构建用户行为模仿Agent时，可参考综述中的OT ground cost设计逻辑，编码用户行为序列的时空关联特征提升度量准确性

  - 落地OT正则化RL算法时，可复用综述给出的计算优化方案、OT公式选型逻辑，降低工程落地门槛'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
RL算法迭代中需频繁比较状态访问、动作输出、环境转移等各类概率分布，但传统KL/JS等散度在分布弱重叠场景（如模仿学习、离线RL、分布漂移部署）下度量效果大幅下降，无法满足需求。
### 方法关键点
系统梳理OT在RL目标与算法中的落地路径，对现有方案逐一拆解OT的作用、对比的分布类型、采用的OT公式、时序结构处理方式；同时归纳不同OT选型的底层动机、ground cost设计规则、计算复杂度优化等实操要点。
### 关键结果
明确当前领域三大核心开放问题：可扩展的轨迹级传输方案、分布质量不匹配的原则性处理方法、OT正则化RL的完整理论分析框架，为后续研究与落地指明方向。
