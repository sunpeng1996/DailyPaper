---
title: 'JOVE: Joint Execution and Verification for Resource-Aware LLM Task Graphs'
title_zh: JOVE：面向资源感知LLM任务图的联合执行与验证框架
authors:
- Haoran Zhang
- Dongjun Kim
- Seohyeon Cha
- Kevin S Chan
- Ananthram Swami
- Gustavo De Veciana
- Haris Vikalo
affiliations:
- University of Texas at Austin
- DEVCOM Army Research Laboratory
arxiv_id: '2610.03296'
url: https://arxiv.org/abs/2610.03296
pdf_url: https://arxiv.org/pdf/2610.03296
published: '2026-10-02'
collected: '2026-10-05'
category: Agent
direction: Agent 任务图多LLM调度优化
tags:
- LLM Routing
- Task Graph
- Online Learning
- Resource Optimization
- Selective Verification
one_liner: 提出在线框架JOVE联合优化LLM任务图的执行分配与选择性验证，保精度下大幅降本提效
practical_value: '- 多LLM调度约束建模：可直接复用JOVE的「动态API成本影子价格+节点延迟分位数约束」框架，落地到电商Agent导购、推荐文案生成、商品属性抽取等多LLM调用场景，平衡长期预算与单次请求延迟要求

  - 选择性验证降本：借鉴D最优信息增益计算方法，仅对不确定性高的子任务输出做付费验证（用小模型/人工标注），无需全量校验即可高效更新模型适配性估计，可降低验证成本30%以上

  - 任务粒度资源分配：将复杂用户请求（如多轮定制化推荐需求）拆分为DAG子任务后，用JOVE的轻量MILP求解子任务到不同规格LLM的最优分配，相同精度下可降低推理成本4倍以上'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
复杂推理查询拆分为DAG任务图调度异构LLM执行已成为主流方案，但生产环境存在两大核心痛点：一是不同LLM对各子任务的适配性事前未知，分配不合理易导致成本过高、延迟超标；二是执行后无法直接获知子任务输出正确性，全量验证成本极高，过往方法默认反馈免费，不符合实际预算与延迟约束。
### 方法关键点
- 整体框架：先将用户查询拆分为DAG任务图，每个子任务匹配候选LLM池，联合决策子任务的执行LLM分配与输出是否需要验证
- 约束建模：用动态更新的API成本影子价格控制长期预算，将任务图的概率延迟约束拆解为节点级延迟分位数约束，通过求解每查询的混合整数线性规划(MILP)得到最优分配
- 在线学习：基于LinUCB估计不同LLM对应子任务的执行质量，用D最优准则计算验证的信息增益并加入优化目标，引导选择性验证，验证异步执行不影响当前响应速度
- 理论保证：证明合理验证权重区间下，模型质量学习的regret为次线性，收敛性有保障
### 关键实验
在Bamboogle、MMLU-Pro、GPQA、LiveBench-Reasoning四个推理基准上测试，对比CoT、SoT、Plato等无约束推理基线，以及WR-Online等资源感知基线，JOVE精度与最强基线相当，同时成本降低3.7~16.3倍，延迟降低8.3~17.0倍，延迟达标率超过96%。
### 核心结论
复杂LLM任务通过子任务分解+多模型动态调度+选择性验证的组合，可在不损失精度的前提下实现数量级的成本与延迟优化。
