---
title: Discovering Learning Rules that Shape Others
title_zh: 可塑造对手行为的学习规则发现方法
authors:
- Hong Jun Lee
- Ziyan Wang
- Jun Wang
- Stefanos Leonardos
- Yali Du
affiliations:
- King's College London
- Harvard University
- University College London
arxiv_id: '2611.08335'
url: https://arxiv.org/abs/2611.08335
pdf_url: https://arxiv.org/pdf/2611.08335
published: '2026-11-05'
collected: '2026-11-07'
category: MultiAgent
direction: 多智体强化学习 · 对手塑形
tags:
- Multi-Agent RL
- Opponent Shaping
- Meta-Learning
- General-Sum Games
- Algorithm Discovery
one_liner: 提出无需感知对手参数的通用和博弈对手塑形更新规则DUOS，竞赛性能双第一
practical_value: '- 电商竞价、智能谈判等多Agent博弈场景可复用DUOS的无对手参数感知设计，规避依赖对手私有信息的落地瓶颈

  - 元学习自动发现更新规则的思路可迁移到推荐动态博弈场景（如商家定价优化、流量分配博弈），替代人工设计的策略更新逻辑

  - 自博弈性能评估范式可用于多Agent业务系统的离线验证，提升真实环境部署的鲁棒性'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
通用和博弈场景下，现有LOLA、M-FOS等对手塑形方法部署时需要获取对手的参数、策略、奖励等私有信息，落地限制大；单智能体元学习更新规则（如DiscoRL）仅依赖自身经验即可取得SOTA效果，但尚未适配多智能体通用和博弈场景。

### 方法关键点
提出DUOS，将单智能体元学习更新规则框架扩展到通用和博弈场景，元训练阶段最大化智能体生命周期期望收益，仅通过自身经验更新内部网络，无需感知对手的任何私有信息即可实现对手塑形效果，是首个针对通用和博弈智能体的元学习更新规则方法。

### 关键结果数字
在公开多智能体竞赛中，归一化平均得分排名第1，自博弈性能排名第1
