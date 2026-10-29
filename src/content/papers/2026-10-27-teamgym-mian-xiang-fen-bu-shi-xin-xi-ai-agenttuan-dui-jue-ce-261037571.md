---
title: 'TeamGym: A Gym for Team Decision-Making by AI Agents with Distributed Information'
title_zh: TeamGym：面向分布式信息AI Agent团队决策的评测训练环境
authors:
- Chanwoo Park
- Jaywoong Jeong
- Zachary Wojtowicz
- Yubin Kim
- Taekyun Lee
- Kaiqing Zhang
- Asuman Ozdaglar
affiliations:
- MIT
- KAIST
- UT Austin
- University of Maryland
arxiv_id: '2610.37571'
url: https://arxiv.org/abs/2610.37571
pdf_url: https://arxiv.org/pdf/2610.37571
published: '2026-10-27'
collected: '2026-10-29'
category: MultiAgent
direction: 多智能体协作 · 团队决策评测训练
tags:
- MultiAgent
- LLMAgent
- Benchmark
- TeamDecision
- PolicyOptimization
one_liner: 开源多领域分布式信息AI Agent团队决策评测训练环境，量化沟通检索gap并支持策略优化
practical_value: '- 可复用PIU拆解方法优化多Agent推荐系统：比如面向电商选品、投放、定价的多Agent决策链路，先拆解出每个决策的最小必要关键信息集，再分配给对应角色Agent，避免信息冗余或缺失，降低信息传递成本

  - 沟通gap、检索gap的量化思路可直接迁移：在拆分用户、商品、商家侧信息给不同Agent时，量化信息拆分、检索带来的推荐/投放效果损失，针对性优化信息共享机制和RAG链路

  - 通信结构选择的结论可落地：若团队信息分散度高，优先用轮询/动态选发言人的顺序通信结构，避免无协调的同时发言带来的错误扩散；若最终决策模型能力强，可选择同步通信提升效率

  - 单奖励RL训练方法降低多Agent落地成本：不需要为每个Agent单独设计协作类奖励，仅优化最终的业务目标（比如GMV、点击率），即可让Agent自发涌现信息共享、发言顺序优化等协作行为，大幅降低训练复杂度'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前多Agent系统落地加速，但主流评测训练均面向单Agent场景，缺乏可精准控制信息分布、通信规则的标准化环境，无法量化团队决策中信息检索、共享、整合环节的短板，也难以高效训练协作策略。
### 方法关键点
- 提出Pivotal Information Unit (PIU) 拆解方法：对每个决策任务，筛选出「单独必要、共同充分」的最小信息集合，可精准控制PIU在不同Agent间的分配规则
- 覆盖法律、金融、医疗、软件工程4大领域12个公开语料的决策任务，支持5种通信结构、灵活的token预算配置
- 定义两类可量化的性能gap：沟通gap（信息拆分给多Agent vs 单Agent持有全量PIU的成功率差）、检索gap（Agent从原始文档提取PIU vs 直接获取PIU的成功率差）
- 支持基于最终决策奖励的强化学习训练，可同时优化参与者、协调者策略
### 关键结果
测试8款主流LLM，三类场景平均沟通gap达22.9pp，平均检索gap达19.9pp；仅用最终决策奖励做策略训练，金融任务决策得分最高提升19.2pp，可自发涌现全员发言、最优发言人选择等协作行为。
### 核心结论
AI团队决策效果并非单Agent能力的简单叠加，信息分配方式、通信结构对最终效果的影响远大于单Agent能力提升。
