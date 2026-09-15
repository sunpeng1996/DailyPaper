---
title: 'AlgoEvo: Self-Evolving Agentic Search for Automated Algorithm Discovery'
title_zh: AlgoEvo：面向自动算法发现的自进化智能体搜索框架
authors:
- Junhao Qiu
- Qinglong Hu
- Xialiang Tong
- Mingxuan Yuan
- Liyong Lin
- Qingfu Zhang
affiliations:
- City University of Hong Kong
- Huawei Noah’s Ark Lab
- A*STAR Institute of Advanced Intelligence and Computing
arxiv_id: '2609.15820'
url: https://arxiv.org/abs/2609.15820
pdf_url: https://arxiv.org/pdf/2609.15820
published: '2026-09-14'
collected: '2026-09-15'
category: Agent
direction: Agent · 自动算法发现与优化
tags:
- Agent
- LLM4AD
- Automated Algorithm Design
- Experience Reuse
- Skill Library
one_liner: 提出Agent驱动的自进化算法发现框架，用可插拔技能库和层级经验库适配多类优化任务
practical_value: '- 可复用「技能库+层级经验库」的Agent架构：将召回/排序/多目标优化等不同业务场景的范式知识封装为可插拔skill，无需为每个场景重写Agent执行逻辑

  - 层级经验沉淀机制可直接迁移到推荐/广告策略迭代：把每轮AB实验的效果、修改点、上下文做成经验卡，用MCTS树组织，下次策略优化直接检索相关经验减少试错

  - 跨任务知识蒸馏逻辑可复用：将多个业务场景验证有效的通用规则（如多目标帕累托权衡、召回算子协同）沉淀到通用技能库，提升新场景冷启动效率

  - Agent动作编排可借鉴：让Agent根据当前优化瓶颈（如AUC停滞、转化率负向）动态决定是做诊断、改策略、还是小流量验证，替代固定的周期性迭代流程'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM驱动的自动算法发现框架依赖人工预定义的刚性搜索流程，存在自适应推理受限、跨范式迁移能力弱、执行反馈无法复用的问题，不同优化范式（单目标/多目标/多组件）需要维护独立代码库，资源浪费大且迭代效率低。

### 方法关键点
- 自主Agent驱动搜索循环：Agent动态决策当前执行操作（读代码/诊断问题/编辑代码/评估效果），替代固定的生成-评估-选择流程
- 可插拔设计技能库：将单目标、多目标、多组件等不同范式的知识、接口、评估规则封装为独立skill，核心引擎无需修改即可适配不同任务
- 三层层级经验库：单步评估生成记录上下文、修改、收益、原理的经验卡；同任务经验卡组成MCTS搜索树，用UCB做经验选择指导后续探索；跨任务验证的有效模式沉淀到技能库实现自进化

### 关键实验
覆盖6个基准任务（单目标TSP/CVRP、多目标Bi-TSP/Bi-FJSP、多组件CVRP-DR/FJSP 4-Ops），对比FunSearch、EoH、MEoH等SOTA专用基线；单目标任务仅用35-39次评估（基线用满500次）性能领先4-7%，token消耗降低23%-54%；多组件任务性能领先SOTA 1%-2%，token消耗降低56%-80%；跨任务迁移可带来4.7%-4.8%的性能提升。

### 核心洞见
将算法/策略迭代从固定流程的盲目试错，升级为带经验沉淀的Agent自主优化，可同时提升最终效果和迭代效率。
