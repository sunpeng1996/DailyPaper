---
title: 'ACAP: Asynchronous Coding Agents for Efficient Robot Control'
title_zh: ACAP：用于高效机器人控制的异步编码Agent框架
authors:
- Zexin He
- Rui Li
- Yushi Lan
- Chengkai Jin
- Zhi Hou
- Xingang Pan
affiliations:
- S-Lab, Nanyang Technological University
- University of Oxford
- ACE Robotics
arxiv_id: '2611.31205'
url: https://arxiv.org/abs/2611.31205
pdf_url: https://arxiv.org/pdf/2611.31205
published: '2026-11-22'
collected: '2026-11-25'
category: Agent
direction: 异步编码Agent 多智体协作调度
tags:
- Asynchronous Agent
- Coding Agent
- Multi-Agent Coordination
- Hyper Agent
- Robot Control
one_liner: 提出带超Agent协调的异步编码Agent框架，实现机器人多组件并行执行降低任务耗时
practical_value: '- 可复用「子Agent异步执行+超Agent动态协调依赖」架构，解决推荐链路多模块（召回/排序/混排）并行任务调度的阻塞问题

  - 子Agent按可配置控制分组绑定职责的设计，可迁移到电商多场景Agent的任务拆分，降低单Agent推理延迟

  - 动态切换子Agent/超Agent控制权的机制，可用于大流量下推荐链路资源动态分配，平衡并行效率和耦合需求'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
单编码Agent管控机器人全组件时，独立任务串行执行会产生无意义延迟，同时多组件物理依赖的协调需求无法满足

### 方法关键点
1. 设计ACAP异步框架，将机器人拆分为多个可配置控制组（如机械臂、底盘），每个组绑定专属持久化Member Agent，支持异步推理执行
2. 引入Hyper Agent负责任务分配、依赖协调，动态在主控与Member Agent间切换控制权，兼顾并行效率与强耦合操作需求

### 关键结果
- 72次真实世界测试覆盖25类任务/平台设置，较单Agent Direct Policy任务均衡耗时降低28.2%
- 8类协作场景平均耗时优于固定权限分配方案
- 90次额外测试显示6类任务的30分钟封顶平均耗时均低于单Agent方案
