---
title: 'LoopArena: Benchmarking Models as Runtime Controllers for Loop Engineering'
title_zh: LoopArena：面向循环工程的运行时控制器模型评测基准
authors:
- Yi Wang
- Haopeng Zhang
- Chengxiang Huang
- Rui Dai
- Kaikui Liu
- Piotr Koniusz
- Xiangxiang Chu
affiliations:
- Alibaba Group DreamX Team
- Beijing University of Posts and Telecommunications
- UNSW Sydney
- Data61, CSIRO
arxiv_id: '2608.28281'
url: https://arxiv.org/abs/2608.28281
pdf_url: https://arxiv.org/pdf/2608.28281
published: '2026-08-27'
collected: '2026-08-31'
category: Agent
direction: Agent 循环控制能力评测
tags:
- Agent Benchmark
- Loop Engineering
- Controller-Worker
- Agent Orchestration
- Evaluation Protocol
one_liner: 提出三级成本分层的Controller-Worker架构评测基准，隔离评估Agent循环调度控制器能力
practical_value: '- 做多Agent协作的推荐/广告系统时，可复用Controller-Worker解耦架构，固定执行节点（如召回/排序执行端），单独迭代调度决策节点，降低整体迭代成本

  - 长周期Agent任务评测可复用三级分层设计：先做单决策低成本评测，再做任务切片评测，最后全任务评测，利用高低成本评测的高相关性（ρ=0.9747）大幅降低评测开销

  - 设计长周期Agent调度策略时，不要使用固定重复任务目标的策略，长任务下该策略效果和无控制一致，必须根据运行状态动态调整调度指令'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Loop Engineering成为基于编码Agent组织长周期开发任务的核心范式，但现有评测均对Agent系统做整体评估，无法区分任务成败来自上层循环调度策略还是下层执行Agent的能力，长周期任务中调度错误（信任过期进度、跳过验证、预算浪费、提前终止）占比极高，缺乏专门隔离评估调度控制器能力的基准。
### 方法关键点
- 采用Controller-Worker解耦架构：固定Worker的编码执行能力，仅评估Controller的进度判断、下一步指令生成、终止决策能力，引入Reporter生成结构化Evidence Packet向Controller传递标准化运行状态
- 三级分层评测设置：Type I为单步四选一决策评测，评测时无Worker执行成本；Type II为任务切片评测，从预定义中间状态开始执行；Type III为完整长周期任务评测
- 所有评测配置固定Worker、工具集、任务环境、评测指标，仅替换Controller变量，确保评测公平性
### 关键实验
基于SCBench、BeyondSWE的27个编码任务，对比无控制、固定控制两类基线，以及5款主流LLM作为Controller的效果：Type III全任务下最优Strict Success Rate仅24.69%，提升空间极大；Type II相比Type III平均降低64.4%的推理成本，且两者的Controller排名Spearman ρ达0.9747，一致性极强。
### 核心结论
长周期Agent任务中，仅重复原目标的固定控制策略无法优于无控制基线，有效的循环控制必须根据运行状态动态调整调度策略
