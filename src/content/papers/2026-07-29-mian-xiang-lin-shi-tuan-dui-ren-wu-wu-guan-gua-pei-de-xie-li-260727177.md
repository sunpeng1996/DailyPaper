---
title: Partner Capability Estimation for Task-Agnostic Adaptation in Ad-Hoc Teamwork
title_zh: 面向临时团队任务无关适配的协作方能力估计方法
authors:
- Peter Tisnikar
- Maja Swieczkowska
- Benteng Ma
- Gerard Canal
- Matteo Leonetti
affiliations:
- King's College London
- University of Oxford
arxiv_id: '2607.27177'
url: https://arxiv.org/abs/2607.27177
pdf_url: https://arxiv.org/pdf/2607.27177
published: '2026-07-29'
collected: '2026-07-30'
category: Agent
direction: Agent 临时协作能力推断与适配
tags:
- Ad-hoc Teamwork
- Capability Estimation
- Human-AI Collaboration
- Bayesian Inference
- Multi-agent Planning
one_liner: 提出无需群体预训练的近似贝叶斯方法，推断协作方任务无关能力向量，提升人机/多智体临时协作效率
practical_value: '- 电商/广告场景中建模商家/主播/广告主的跨任务履约能力时，可复用CE-CM的无预训练轻量推断框架，仅通过少量交互数据就能快速完成冷启动能力刻画，无需依赖大规模历史样本预训练

  - 面对用户行为多义性（如点击、搜索query意图多样）时，可参考CE-CM-Div的多轨迹匹配思路，不与单一路径做匹配，而是基于可行行为集做召回/推断，降低误判率

  - 涉及多角色任务分配的场景（如客服机器人工单分配、广告流量分层分配），可先推断协作方的能力约束再做规划，能有效减少不可行任务分配，提升整体协作效率'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有临时多智体协作方法大多绑定固定任务，依赖群体预训练，且默认协作方能力已知，但实际人机协作中人类能力隐式、行为多变，现有方法无法跨任务复用协作方模型，适配效率低。

### 方法关键点
- 提出CE-CM近似贝叶斯框架，将协作方能力建模为任务无关的二进制向量，通过「采样候选能力→模拟该能力下的协作轨迹→匹配观测轨迹→更新能力信念」的迭代循环在线推断，无需预训练，仅需少量交互即可更新
- 扩展CE-CM-Div，对每个能力候选生成多组多样化规划轨迹做匹配，解决人类行为多样、次优导致的单轨迹匹配鲁棒性差的问题
- 推断得到的能力向量直接用于构造多智能体MDP做联合规划，任务分配时自动规避协作方不可行的动作

### 关键实验
在TidyUP、Overcooked两个协作域测试，搭配225条15名参与者的人类交互数据集，对比乐观基线、悲观基线：TidyUP域5次任务内能力推断汉明距离降至0.1以内，动作分配匹配度达75%+，不可行动作分配减少70%+；人类数据集上CE-CM-Div相对CE-CM能力推断误差降低30%-48%，采样接受率提升10倍以上。

### 核心结论
能力仅能约束协作行为的可行域，无法决定具体策略选择，复杂场景下需同时建模能力约束与行为偏好才能实现最优协作
