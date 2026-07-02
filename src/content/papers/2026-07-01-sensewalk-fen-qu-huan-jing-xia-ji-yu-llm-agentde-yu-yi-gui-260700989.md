---
title: 'SenseWalk: Agent-Based Semantic Trajectory Simulation Powered by Large Language
  Models in Zoned Environments'
title_zh: SenseWalk：分区环境下基于LLM Agent的语义轨迹模拟系统
authors:
- Ziyue Lin
- Xinhang Xie
- Kangyi Wang
- Siming Chen
affiliations:
- School of Data Science, Fudan University
arxiv_id: '2607.00989'
url: https://arxiv.org/abs/2607.00989
pdf_url: https://arxiv.org/pdf/2607.00989
published: '2026-07-01'
collected: '2026-07-02'
category: Agent
direction: Agent 语义轨迹模拟系统构建
tags:
- LLM Agent
- Semantic Trajectory
- Simulation System
- Social Force Model
- Behavior Simulation
one_liner: 提出结合LLM Agent与社会力模型的语义轨迹模拟系统，降低数据采集与工具使用门槛
practical_value: '- 线下商圈/到店电商场景可复用该模拟框架生成用户到店行为语义轨迹数据，解决真实数据采集成本高、语义缺失问题

  - 做用户行为模拟时可借鉴「LLM逻辑决策+物理规则模型」的混合架构，兼顾行为语义合理性与物理可行性

  - 面向业务人员的模拟工具可参考低代码配置+可视化分析的交互设计，降低非技术人员使用门槛'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
语义轨迹分析可挖掘人类移动背后的行为逻辑，但真实场景下高质量语义轨迹数据采集成本高、语义信息不足，现有模拟工具专业门槛高，从业者难以落地。
### 方法关键点
1. 搭建SenseWalk交互式系统，基于LLM-powered Agent模拟用户移动决策逻辑；
2. 设计LLM与社会力模型混合的模拟工作流，同时保证轨迹的物理合理性与语义连贯性；
3. 配套可视化交互界面，支持自定义模拟配置、输出结果分析。
### 关键结果
定量实验验证模拟工作流有效性，12人用户研究显示系统易用性、使用效率相比传统工具显著提升，非技术人员可快速上手。
