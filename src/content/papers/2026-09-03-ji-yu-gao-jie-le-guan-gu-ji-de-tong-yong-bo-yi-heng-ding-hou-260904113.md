---
title: Constant regret in general games via higher-order optimism
title_zh: 基于高阶乐观估计的通用博弈恒定后悔界学习算法
authors:
- Omar Abbadi
- Rida Laraki
- Panayotis Mertikopoulos
arxiv_id: '2609.04113'
url: https://arxiv.org/abs/2609.04113
pdf_url: https://arxiv.org/pdf/2609.04113
published: '2026-09-03'
collected: '2026-09-06'
category: Other
direction: 通用博弈在线学习后悔界优化
tags:
- Online Learning
- Regret Minimization
- Game Theory
- OptFTRL
- Constant Regret
one_liner: 提出HOOD算法，在通用N玩家正则博弈中实现与轮数无关的O(N³log²K)个体后悔界
practical_value: '- 多智能体竞价广告、平台供需博弈场景的在线策略优化，可借鉴HOOD的高阶乐观+折扣设计，降低策略震荡带来的营收损耗

  - 长期在线决策类任务（如长周期用户价值优化）可复用策略升维+熵正则的组合，实现与决策轮数无关的恒定后悔，避免长期性能衰减

  - 非博弈优化、多智能体决策方向的业务从业者可直接跳过，无直接落地价值'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有通用N玩家正则博弈的无耦合学习算法后悔界随博弈轮数亚线性增长，无法支撑长期稳定决策，核心瓶颈是策略更新过程的不可控大幅震荡，是此前恒定后悔界研究的核心卡点。
### 方法关键点
提出高阶乐观折扣算法（HOOD），为OptFTRL的改进变种：1. 引入带折扣的(N+1)阶预测器，自适应平滑策略更新步长；2. 在升维后的博弈策略空间上施加熵正则，可控抑制策略序列的大幅震荡。
### 关键结果数字
在任意N玩家、单玩家最多K个动作的通用正则博弈中，实现与博弈轮数完全无关的O(N³log²K)个体后悔界，显著优于同期独立研究给出的O(N²¹log⁴K)后悔界。
