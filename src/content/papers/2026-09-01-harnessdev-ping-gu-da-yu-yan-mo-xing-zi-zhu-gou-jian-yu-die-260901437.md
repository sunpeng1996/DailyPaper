---
title: 'HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness?'
title_zh: HarnessDev：评估大语言模型自主构建与迭代Agent执行框架的能力
authors:
- Yuhao Wu
- Jingyuan Zhang
- Jiajun Shi
- Xinping Lei
- Qingshui Gu
- Yuxuan Zhang
- Zexuan Wang
- Chen He
- Chen Huang
- Maojia Song
affiliations:
- ByteDance Seed
- Singapore University of Technology and Design
- Georgia Institute of Technology
- M-A-P
- TokenWave.AI
arxiv_id: '2609.01437'
url: https://arxiv.org/abs/2609.01437
pdf_url: https://arxiv.org/pdf/2609.01437
published: '2026-09-01'
collected: '2026-09-02'
category: Agent
direction: Agent 执行框架自主演化评估
tags:
- Agent
- Agent Harness
- Benchmark
- Self-Evolution
- LLM Evaluation
one_liner: 提出HarnessDev基准，从创建与演化两个阶段评估LLM自主构建迭代Agent执行框架的能力与效率
practical_value: '- 业务Agent迭代可优先优化执行框架（harness）：固定模型权重下harness优化最多可带来14%+的任务成功率提升，电商客服、选品Agent的重试机制、上下文压缩、结果校验逻辑可单独迭代，性价比远高于微调模型

  - Agent开发可参考双阶段范式：创建阶段从仅保留基础接口的弱种子开始，避免一开始引入冗余功能；演化阶段基于线上执行反馈迭代，优先修复明确的故障模式而非盲目加功能

  - 迭代harness必须做泛化校验：演化阶段小样本反馈集上的增益平均仅31%能迁移到未见过的任务，且高度依赖执行模型，上线前必须跨任务、跨模型验证效果

  - Agent评估需兼顾能力与成本：不同harness的执行token消耗差距可达19倍，高消耗不一定对应高效果，对高吞吐的电商搜索、推荐Agent的成本控制至关重要'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前Agent评估普遍固定执行框架（harness），仅测下游任务效果，忽略了LLM自主开发、迭代harness的能力。而harness对任务效果影响极大，相同模型在不同harness下任务成功率差异可达14%以上，业界缺乏专门基准评估LLM的harness开发能力。

### 方法关键点
- 基准分为两个阶段：Creation阶段从无执行逻辑的弱种子harness出发，仅提供1-3个开发样例，要求构建完整可运行的harness；Evolution阶段基于已构建的harness，用下游执行反馈持续迭代
- 双维度评估：Capability（未见过的下游任务成功率）、Efficiency（执行时的token消耗）
- 两种评估模式：Self-Eval（创建harness的LLM同时作为执行模型）、Unified-Eval（所有harness用统一固定的执行模型，隔离执行模型影响）

### 关键实验
覆盖代码、数据分析、写作、搜索4个领域5个下游基准共2207个任务，对比6款前沿LLM与人类开发的harness：
- Creation阶段Self-Eval下，LLM构建的harness在写作、机器学习实验领域持平或超过人类参考，代码领域比人类低10-51pct，搜索领域低39-89pct
- Evolution阶段反馈集上平均增益3-13.9pct，但仅平均31%的增益能迁移到未见过的任务，切换执行模型后大部分增益消失

如果模型权重是智能积累的一个载体，harness就是另一个：它显性、可审计、可测试、可复用，可通过故障、反馈和工程压力持续改进。
