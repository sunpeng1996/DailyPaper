---
title: 'EvoTeam: Multi-Agent Collaboration via Evolving Teams'
title_zh: EvoTeam：基于动态团队迭代的多智能体协作框架
authors:
- Qinuo Cao
- Xin He
- Dianxuan Fu
- Lizhi Zhang
- Zhaoqing Xing
- Jiapu Wang
- Xin Wang
- Na Zou
- Yi Chang
- Qinggang Zhang
affiliations:
- Jilin University
- Nanjing University of Science and Technology
- Shanghai AI Lab
arxiv_id: '2610.39813'
url: https://arxiv.org/abs/2610.39813
pdf_url: https://arxiv.org/pdf/2610.39813
published: '2026-10-29'
collected: '2026-11-04'
category: MultiAgent
direction: 多智能体协作 · 动态团队进化
tags:
- Multi-Agent System
- Collaborative Evolution
- Task Adaptation
- LLM Agent
- Experience Reuse
one_liner: 提出协作导向的多智能体进化框架，跨异质任务复用团队结构与交互规则并保留个体技能复用性
practical_value: '- 可复用「团队库+任务匹配」设计：针对电商多场景（客服、选品、营销文案生成等）预存适配不同任务的agent团队模板，新任务优先匹配复用现有团队，大幅降低架构搭建成本

  - 交互规则按团队隔离的思路可直接迁移：不同业务场景的agent协作规则（如query改写→商品召回→排序的信息传递规则）仅在对应团队内更新，避免跨场景规则冲突导致的效果下降

  - 三级进化机制可参考：落地自进化多agent系统时，可同时迭代团队结构、团队内协作规则、个体agent技能，兼顾协作效率和个体能力跨场景复用

  - 成本优化trick：相同类型任务仅招募团队内必要角色参与执行，减少无效agent交互带来的token消耗，降低推理成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM-based多智能体系统（MAS）进化多聚焦优化单个agent的prompt、技能与执行策略，无法直接提升团队协作效率；后续延伸到协作层面的方法又存在团队重组受限、交互规则跨异质任务不当复用的问题，跨不同类型任务进化时甚至会出现效果下降，亟需能适配异质任务的协作导向进化框架。

### 方法关键点
- 自适应团队组建：维护全局agent池和可复用团队库，新任务优先匹配符合协作要求的现有团队，无匹配则自动生成新团队，再从团队候选名单中招募任务必要的执行agent，减少冗余角色
- 团队范围协作：每个团队绑定专属交互规则库，执行时仅给agent注入对应团队的规则作为协调指导，规则更新仅在团队内生效，避免跨场景冲突
- 多层经验进化：执行后分别在三个层面迭代：更新团队描述与候选名单、增删改团队专属交互规则、优化单个agent的技能库，个体技能可跨所有团队复用

### 关键实验
在GAIA、LoCoBench、LOCA、BeyondSWE 4个基准共6类任务上测试，对比SA、MAS、Meta-Team等7个基线：单基准进化时平均得分58.85，超最强基线Meta-Team 0.55分；混合异质基准进化时平均得分59.58，超Meta-Team 4.03分；跨LLM backbone（DeepSeek与GPT互转）时性能损失不超过4分，同时推理成本低于Meta-Team等主流方法。

### 最值得记住的一句话
多智能体系统进化不能只优化个体能力，针对任务特性动态调整团队结构、隔离不同协作场景的交互规则，才能跨异质任务持续提升协作效率。
