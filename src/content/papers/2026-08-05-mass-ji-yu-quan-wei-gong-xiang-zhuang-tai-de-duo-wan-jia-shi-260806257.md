---
title: 'MASS: Multiplayer World Models with Authoritative Shared State'
title_zh: MASS：基于权威共享状态的多玩家世界模型
authors:
- Ziqi Cai
- Siqi Yang
- Yimu Wang
- Zixian Gao
- Yunheng Liu
- Shuchen Weng
- Erwin Wu
- Kaipeng Zhang
- Boxin Shi
affiliations:
- Alaya Lab
- Peking University
- Institute of Science Tokyo
arxiv_id: '2608.06257'
url: https://arxiv.org/abs/2608.06257
pdf_url: https://arxiv.org/pdf/2608.06257
published: '2026-08-05'
collected: '2026-08-07'
category: MultiAgent
direction: 多智体世界模拟 · 共享状态建模
tags:
- MultiAgent
- WorldModel
- StateDisentanglement
- ScalableSimulation
- SharedState
one_liner: 借鉴多人游戏架构解耦世界动态与视图渲染，实现高可扩展低不一致的多智能体世界模拟
practical_value: '- 多Agent协作场景可复用权威全局共享状态架构，解耦全局状态演进与个体视角生成，避免不同Agent视图不一致、重复计算问题

  - 电商多角色Agent（用户、商家、平台）仿真场景可参考无手写规则的学习式状态引擎设计，大幅降低规则维护成本

  - 大规模并发Agent推演任务（如大促流量模拟、推荐策略离线评估）可借鉴其1024并发、万步长稳定演进的工程思路'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频世界模型在多玩家场景下将世界状态与视角相关视觉隐变量耦合，存在计算冗余、跨视图不一致、可扩展性差的缺陷，无法支撑大规模多Agent并行仿真需求。
### 方法关键点
1. 借鉴多人游戏架构，解耦世界动态演进与视图渲染两大模块；
2. 设计学习式Logic Engine，仅基于多智能体联合动作更新全局权威类型化状态，作为唯一循环记忆与同步基准，无手写转移函数；
3. 配套学习式Rendering Engine，基于共享状态按需为任意请求视角生成独立且一致的视图。
### 关键结果
在多玩家Snake基准上，相较SOTA多视图基线状态精度更高、跨视图不一致性更低；可支撑1024并发玩家的预测世界稳定演进10000个循环步。
