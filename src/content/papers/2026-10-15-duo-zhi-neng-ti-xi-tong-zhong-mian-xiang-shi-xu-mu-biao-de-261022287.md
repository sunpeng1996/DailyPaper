---
title: Learning Rational Strategies for Temporal Objectives in Multi-Agent Systems
title_zh: 多智能体系统中面向时序目标的理性策略学习
authors:
- Omar Adalat
- Edwin Hamel-De le Court
- Francesco Belardinelli
affiliations:
- Imperial College London
- University of Manchester
arxiv_id: '2610.22287'
url: https://arxiv.org/abs/2610.22287
pdf_url: https://arxiv.org/pdf/2610.22287
published: '2026-10-15'
collected: '2026-10-17'
category: MultiAgent
direction: 多智能体博弈 · 理性策略合成
tags:
- MARL
- Nash Equilibrium
- Temporal Logic
- Stochastic Games
- Rational Synthesis
one_liner: 提出无环境先验的多智能体强化学习框架，学习满足概率时序约束的纳什均衡策略
practical_value: '- 电商广告竞价、推荐资源分配等多利益方博弈场景，可借鉴pltlf定义时序约束（如曝光频率、长期ROI约束），自动编译为奖励信号，避免手动设计奖励的偏差

  - 多Agent推荐系统（用户/商家/平台侧Agent共存）可复用近似NashConv指标评估策略可利用性，避免某方偏离策略导致系统收益下跌

  - 电商中长期优化目标（如复购、留存）可复用论文的有限样本置信度校验方法，无需知道环境动态，仅通过离线rollout即可给出目标达成概率的置信区间，降低线上试错风险'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
传统多智能体策略合成要么假设环境动态完全已知，要么将其他智能体视为完全敌对，输出策略过于保守，无法兼容安全、时效等复杂时序约束，也无法保证策略在理性博弈下的稳定性，在电商竞价、流量分配等多利益方共存的业务场景实用性差。
### 方法关键点
- 采用有限迹概率线性时序逻辑（pltlf）定义各智能体的个性化时序约束，自动编译为确定性奖励自动机，与底层随机博弈做同步乘积，将非马尔可夫时序目标转化为可直接优化的马尔可夫终端奖励
- 适配IPPO、IQL、Nash-Q等主流模型无关MARL算法，引入反事实经验回放缓解终端奖励稀疏问题，给出折扣因子选择的偏差边界，保证优化目标与时序约束满足概率的一致性
- 提出有限样本PAC风格校验机制，无需环境先验即可给出各智能体约束满足概率的置信区间，通过近似NashConv指标评估策略的均衡稳定性
### 关键结果
在8个通用随机博弈基准上测试，6个基准的最优策略时序约束满足概率超过0.9，其中2个追逃博弈、猎鹿博弈的满足概率达1.0，7个基准的近似NashConv低于0.05的均衡容忍阈值，反事实经验回放可平均提升收敛速度30%以上。
### 核心结论
多智能体系统中，仅优化单一方收益远远不够，需同时满足各参与方的时序约束与博弈均衡稳定性，才能保证策略的可落地性。
