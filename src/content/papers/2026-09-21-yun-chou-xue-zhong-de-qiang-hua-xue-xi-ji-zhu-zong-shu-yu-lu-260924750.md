---
title: 'Reinforcement Learning in Operational Research: A Technical Review and Practical
  Roadmap'
title_zh: 运筹学中的强化学习：技术综述与实践路线图
authors:
- Yahan Lu
- Dongyang Xia
- Nursen Aydin
- Shadi Sharif Azadeh
affiliations:
- Delft University of Technology (Department of Transport & Planning)
- University of Warwick (Warwick Business School)
arxiv_id: '2609.24750'
url: https://arxiv.org/abs/2609.24750
pdf_url: https://arxiv.org/pdf/2609.24750
published: '2026-09-21'
collected: '2026-09-22'
category: Other
direction: 强化学习与运筹学融合落地综述
tags:
- Reinforcement Learning
- Operational Research
- Combinatorial Optimization
- Sequential Decision Making
- Digital Twin
one_liner: 系统梳理RL赋能运筹学的三类核心角色，整合前沿进展并给出落地与研究路线图
practical_value: '- 电商履约、库存调度、动态定价等场景可直接复用RL+OR的三类融合范式，替代纯启发式规则提升决策效率

  - 推荐系统长周期序列决策（如用户生命周期运营、多目标排序调参）可参考文中RL适配动态不确定环境的落地方案

  - 组合优化类问题（如广告投放预算分配、流量调控）可采用RL嵌入传统OR求解器的架构，平衡精度与耗时'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统运筹学（OR）方法难以适配复杂动态系统下实时、数据驱动的决策需求，现有RL与OR融合研究分散、缺乏系统性技术梳理与落地指引。
### 方法关键点
系统归纳RL赋能OR的三类核心定位：1）直接求解动态不确定环境下的序列决策问题；2）作为端到端方案或组件嵌入启发式/精确OR方法，求解组合优化问题；3）结合数字孪生系统实现扩展现实分析；逐一拆解各范式的实现要求、优劣势与适用边界。
### 关键结果
整合近年RL+OR融合的前沿进展，形成可落地的技术选型框架与未来研究路线图，明确了不同场景下的方案选型逻辑，可直接指导工业动态决策系统搭建
