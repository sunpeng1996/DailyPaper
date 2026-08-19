---
title: 'AdaLens: Interactive Storyline for Monitoring and Steering Long-Running Agentic
  Data Analysis'
title_zh: AdaLens：长运行智能体数据分析的监控与引导交互式故事线系统
authors:
- Yangtian Liu
- Yan Miao
- Shuhan Liu
- Yunfan Zhou
- Dae Hyun Kim
- Di Weng
- Yingcai Wu
affiliations:
- State Key Lab of CAD&CG, Zhejiang University
- Department of Computer Science and Engineering, Yonsei University
- School of Software Technology, Zhejiang University
arxiv_id: '2608.17834'
url: https://arxiv.org/abs/2608.17834
pdf_url: https://arxiv.org/pdf/2608.17834
published: '2026-08-18'
collected: '2026-08-19'
category: Agent
direction: Agent 数据分析过程可观测与引导优化
tags:
- Agentic Workflow
- Human-AI Interaction
- Process Visualization
- Observability
- Steerability
one_liner: 提出基于故事线可视化的交互式系统，支持长运行Agent数据分析的可观测与精准干预
practical_value: '- 可复用故事线可视化框架到长运行推荐Agent的效果监控场景，把召回/排序分支、用户特征维度、中间转化指标映射为故事线元素，直观呈现多链路执行逻辑

  - 直接照搬FOCUS/IGNORE/ELABORATE三级意图干预机制，替代纯自然语言Prompt引导，降低运营人员对推荐/数据分析Agent的干预成本

  - 编排层可参考orchestrator-worker架构支持多任务并行执行，同时内置干预钩子，支持运营对低价值任务分支实时暂停/终止，节省计算资源

  - 数据维度的联动溯源设计可复用到特征归因场景，自动关联特征参与的分析/推荐分支、对应效果指标，降低人工溯源成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前LLM驱动的Agent数据分析系统支持长周期多分支自动执行，但传统交互式界面仅适配单轮turn-by-turn交互，无法满足两个核心需求：一是可观测性，分析师无法直观追踪多分支执行进度、中间结论与数据溯源关系；二是可引导性，人工干预需重构全量上下文用自然语言描述，成本高且精准度不足。

### 方法关键点
- 架构层采用orchestrator-worker分布式架构，orchestrator负责全局规划、结果合成与上下文管理，worker负责单任务执行、结果结构化输出（含摘要、原子结论、关联证据）
- 可视化层设计故事线主视图，将分析计划、中间摘要、原子结论、关联数据列映射为时间轴上的可视化元素，通过数据列的轨迹流转直观呈现分析谱系，支持多粒度缩放查询
- 交互层支持两层干预：意图层支持对可视化元素直接执行FOCUS/IGNORE/ELABORATE操作，自动生成引导指令注入上下文；执行层支持对任务线程直接创建/启动/暂停/修改/终止，无需中断全局流程

### 关键结果
通过2个真实数据集（社交媒体数据、NBA时空追踪数据）的案例研究，以及用户研究验证效果，系统SUS易用性得分达87.08，用户对可观测性与可引导性的满意度均超90%。

### 核心结论
将Agent的执行过程结构化映射为可直接交互的可视化元素，是降低长运行Agent人工干预成本、提升可控性的核心路径。
