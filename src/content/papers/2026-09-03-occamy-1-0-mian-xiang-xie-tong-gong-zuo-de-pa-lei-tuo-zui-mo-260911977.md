---
title: 'Occamy-1.0: Open Pareto-frontier 35B Intelligence for Co-work'
title_zh: Occamy-1.0：面向协同工作的帕累托最优开源35B智能模型
authors:
- Wenhui Chen
- Shiwen Cheng
- Hao Dong
- Chenda Duan
- Ruixiang Feng
- Zhong Guan
- Boqiang Guo
- Xueyuan Han
- Haojie Hao
- Liangmeng Huang
affiliations:
- Accio Team
arxiv_id: '2609.11977'
url: https://arxiv.org/abs/2609.11977
pdf_url: https://arxiv.org/pdf/2609.11977
published: '2026-09-03'
collected: '2026-09-15'
category: Agent
direction: Agent 协同工作能力优化
tags:
- Co-work Agent
- Pareto Optimization
- Model Merging
- Long-horizon Reasoning
- Reinforcement Learning
one_liner: 基于Qwen3.6-35B训练的低成本协同工作Agent模型，性能媲美超大规模前沿系统
practical_value: '- 训练垂直领域Agent可复用分阶段专家训练+参数合并范式：先分别训练长周期任务专家、短周期工具调用专家，再合并得到统一模型，无需推理时路由，成本与单模型一致，适合自部署电商运营、广告投放自动化等场景

  - 长horizon Agent训练可落地token精确轨迹捕获+环境状态回放机制，解决上下文截断/改写后的策略信用分配问题，大幅降低多步任务的训练数据噪声

  - Agent成本优化可参考同准确率下的步骤效率奖励设计：相同完成度的任务，调用轮次更少的轨迹获得更高奖励，可在效果无损的前提下降低多轮调用的累计latency和成本，适合高并发Agent服务

  - 垂直领域Agent训练数据构造可采用环境优先+能力优先双合成路线，经过统一可执行性校验后再进入训练集，大幅减少无效训练数据，降低数据成本'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
协同工作Agent需多轮调用工具、处理长周期任务，累计推理成本和latency随轮次线性升高，但大多数任务步骤仅需要状态跟踪、工具调用、错误恢复能力，不需要前沿大模型的顶级推理能力，现有方案要么效果不达落地要求，要么推理成本过高，缺少35B尺寸下兼顾性能和成本、支持自部署的协同工作模型。

### 方法关键点
- 数据层：采用环境优先+能力优先双路线合成可执行任务合约，覆盖长/短周期任务、工具调用、编码、指令遵循等多类Agent场景，经过统一可执行性、语义一致性校验后进入训练集，总规模为15K条轨迹、403.3M token
- 基础设施层：适配多套Agent执行框架，支持token精确捕获、跨上下文改写的状态回放，解决长周期任务的策略信用分配问题
- 训练层：分三阶段训练，首先训练面向长周期任务的Marathon Expert（SFT+HDPO强化学习）和面向短周期工具调用的Sprint Expert（SFT），再通过参数合并融合两类专家能力，最后用SAO强化学习做全局能力对齐

### 关键结果
- 同等35B尺寸下，在Claw-Eval（平均分82.2）、WildClawBench（49.16）、CommerceAgentBench（37.4）等多个协同工作基准上均为最优，相比基线Qwen3.6-35B分别提升12.7、8.76、17.8分，工具调用任务AutomationBench pass1提升20.1分
- 性能媲美GPT-5.6 Sol、Qwen3.8-Max等超大规模前沿模型，同时处于成本-性能帕累托前沿的低成本拐点，推理成本仅为前沿大模型的1/5~1/10

**最值得记住的一句话**：Agent落地的核心不是追平前沿大模型的单项能力，而是在具体场景下找到性能和成本的最优平衡点，用更小的模型完成90%以上的实际工作。
