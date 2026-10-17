---
title: 'The Tilted Sampling Problem: Optimism, Posterior Sampling, and Logarithmic
  Regret'
title_zh: 倾斜采样问题：乐观估计、后验采样与对数悔界
authors:
- Mohammad Pedramfar
- Siamak Ravanbakhsh
affiliations:
- Mila – Québec AI Institute
- McGill University
arxiv_id: '2610.21908'
url: https://arxiv.org/abs/2610.21908
pdf_url: https://arxiv.org/pdf/2610.21908
published: '2026-10-15'
collected: '2026-10-17'
category: Other
direction: 在线学习 · 采样优化悔界分析
tags:
- Online Learning
- Regret Minimization
- Posterior Sampling
- Gibbs Distribution
- Thompson Sampling
one_liner: 提出倾斜采样通用悔界框架，给出对数T悔界保证及UCS、TS²两种对应采样算法
practical_value: '- 电商/广告RLHF对齐场景可参考采样regret定义，优化采样分布与目标Gibbs分布的KL散度，兼顾生成结果的奖励得分与多样性

  - 推荐系统exploration、冷启动召回等多样性采样场景可直接复用UCS、TS²算法，相比传统UCB/Thompson采样获得更低累积regret

  - 固定温度的在线采样场景可参考对数T悔界结论，无需分配过多流量做探索即可收敛到目标分布，降低业务探索成本'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
熵正则化RL、RLHF、奖励引导生成等场景需要输出多样高质量结果，而非选择单一最优动作，现有经典悔界最小化框架无法匹配这类软最优分布采样的需求。
### 方法关键点
采样regret被定义为学习器输出分布与未知奖励诱导的目标Gibbs分布的温度归一化累积KL散度，统一了bandit与RL领域基于采样、KL正则化的相关范式；推出UCS、TS²两种采样算法，分别对应经典UCB、Thompson采样的采样优化版本，给出统一悔界分解，包括首个基于后验随机Gibbs分布新边界的贝叶斯采样悔界分解。
### 关键结果
固定温度下采样regret可达到对数级$O(\log T)$，远优于传统regret的$\widetilde{O}(\sqrt{T})$；悔界上界为$min\{\sqrt{T\log T}, \beta\log T\}$，其中$\beta$为逆温度，当$T/\log T \leq \beta^2$时走平方根分支，否则走对数分支。
