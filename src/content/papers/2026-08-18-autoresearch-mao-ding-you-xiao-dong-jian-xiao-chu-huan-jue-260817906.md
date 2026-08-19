---
title: 'AutoResearch: Insight In, Hallucination Out'
title_zh: AutoResearch：锚定有效洞见、消除幻觉的多Agent自主科研系统
authors:
- Yiming Ren
- Xiang Liu
- Qumeng Sun
- Xiao Zhang
- Jiahao Li
- Haoyang Zhang
- Junjie Wang
affiliations:
- Infinite Evolution Lab, EvoMap
arxiv_id: '2608.17906'
url: https://arxiv.org/abs/2608.17906
pdf_url: https://arxiv.org/pdf/2608.17906
published: '2026-08-18'
collected: '2026-08-19'
category: Agent
direction: Agent 自主科研流程优化
tags:
- Multi-Agent
- Autonomous Research
- Hallucination Mitigation
- Evidence-based Verification
- Agent Workflow
one_liner: 提出两阶段多Agent协同自主科研框架，从洞见生成到实验验证全链路消除幻觉
practical_value: '- 可复用两阶段Agent架构优化业务算法迭代流程：先融合业务沉淀的领域知识库+行业新信号，经多模型交叉校验输出可落地的实验方案，减少无效实验投入

  - 落地Agent系统时可拆分执行、审核、诊断为独立角色：审核Agent仅接收假设、方案、实验原始数据进行独立校验，避免锚定执行链路的前置决策，降低错误结论（如误把指标波动当策略收益）的概率

  - 可复用证据驱动的迭代决策机制：为每个业务优化方向预设明确的收益阈值，连续迭代增益不达标时自动终止，减少推荐/广告策略调优的资源浪费'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有自主科研系统仅关注流程自动化的覆盖范围，存在两个核心缺陷：一是洞见生成环节无法持续沉淀领域知识，难以将外部新兴信号转化为符合领域逻辑、可验证的研究假设，大量无效探索浪费资源；二是实验执行环节缺乏独立校验机制，实现错误、测量偏差、逻辑偏差等问题容易传播为看似合理的虚假结论，本质是系统级幻觉，亟需兼顾洞见合理性与结论可靠性的全链路框架。

### 方法关键点
- 两阶段核心架构：划分为**Idea Generation**与**Idea Execution**，前者将信号+知识转化为接地的可验证假设与执行计划，后者将计划转化为有证据支撑的结论，从流程上切断幻觉传播路径
- 洞见生成层：融合动态采集的高可信度科研/行业信号+沉淀的领域知识库，先提取可跨场景迁移的机制性洞见，再经3个独立模型生成候选假设、3个评审Agent交叉校验，至少2票通过才输出可执行研究计划
- 执行验证层：将实验拆解为带依赖的任务图，拆分规划、编码、执行、审核、批评为独立Agent角色；审核Agent不继承执行链路的上下文，仅基于原始实验证据判断结果有效性，不达标则触发诊断/重跑/修订流程，所有结论必须有可追溯的实验证据支撑才会被接受

### 关键实验结果
在3类代表性场景验证效果：1）跨模态检索RSICD基准上，自动生成的方案将mean Recall从32.84提升到34.69，审计确认的问题事件仅5个，远低于对比系统的11~27个；2）矩阵乘优化任务中，仅产生4个问题事件，优于对比系统的5~8个，且能主动发现计时bug输出稳定可复现的结果；3）3个Kaggle基准任务上，可基于实验证据自动做出继续、修订、终止的决策，避免无意义的长期探索。

### 最值得记住的结论
自主系统的价值从来不是单纯提升自动化比例，而是要确保从输入洞见到输出结论的全链路都有可追溯的可靠依据，真正做到「Insight In, Hallucination Out」。
