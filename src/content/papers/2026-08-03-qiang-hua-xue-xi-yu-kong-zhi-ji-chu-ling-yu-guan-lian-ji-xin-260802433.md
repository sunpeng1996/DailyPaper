---
title: Foundations of Reinforcement Learning and Control:Connections and New Perspectives
title_zh: 《强化学习与控制基础：领域关联及新研究视角》
authors:
- Claire Vernade
- Onno Eberhard
- Martha White
- Florian Dörfler
- Csaba Szepesvári
- Miroslav Krstic
- Michael Muehlebach
affiliations:
- University of Technology Nuremberg
- Max Planck Institute for Intelligent Systems
- University of Alberta and Alberta Machine Intelligence Institute (Amii)
- ETH Zürich
- University of California San Diego
arxiv_id: '2608.02433'
url: https://arxiv.org/abs/2608.02433
pdf_url: https://arxiv.org/pdf/2608.02433
published: '2026-08-03'
collected: '2026-08-05'
category: Other
direction: 强化学习与控制理论融合基础研究
tags:
- Reinforcement Learning
- Control Theory
- Adaptive Control
- Actor-Critic
- Dynamic Programming
one_liner: 梳理RL与控制理论的共通性及差异，提出二者融合的新范式并在经典运动控制任务验证
practical_value: '- 电商推荐的动态排序/冷启动场景可借鉴自适应控制的稳定性思路，优化RL-based推荐策略的鲁棒性，避免策略波动导致的业务指标震荡

  - 搭建Agent决策模块时可参考actor-critic与自适应控制融合的范式，提升动态环境下（如大促流量波动、用户兴趣突变）的决策效率

  - 基于RL的流量分配/广告出价系统可复用跨领域融合思路，平衡探索效率与系统稳定性，降低线上试错成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
RL与控制理论同根于动态规划，核心目标均为基于反馈优化未知动态系统的控制器，但二者经过长期独立演化，形成了完全不同的方法论、目标导向与研究文化，领域间存在显著认知壁垒，缺乏体系化的关联梳理与融合路径。
### 方法关键点
- 体系化对比自适应控制、actor-critic RL算法的核心逻辑、适用边界与优劣，建立跨领域的统一认知框架
- 设计两类范式融合的新方案，适配数据驱动的动态决策场景
- 选取经典 locomotion 控制任务完成方案验证
### 关键结果
形成的统一认知框架可帮助两个领域的专家快速理解对方领域的工具与方法，融合方案在经典运动控制任务中兼具高于单一RL方案的稳定性，及高于传统控制方案的环境适应性。
