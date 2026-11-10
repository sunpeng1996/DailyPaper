---
title: 'WorkflowArena: Benchmarking Executable Workflow Orchestration in LLM-Based
  Multi-Agent Systems'
title_zh: WorkflowArena：面向LLM多智能体的可执行工作流编排评测基准
authors:
- Zheng Jiang
- Fang Niu
- Bo Peng
- Houde Qian
- Wenyi Li
- Deyao Hong
- Mingju Gao
- Yizhe Chi
- Youjie Zheng
- Kaisen Yang
affiliations:
- Navers Lab
- Einsia.AI
- Tsinghua University
arxiv_id: '2611.12856'
url: https://arxiv.org/abs/2611.12856
pdf_url: https://arxiv.org/pdf/2611.12856
published: '2026-11-09'
collected: '2026-11-10'
category: MultiAgent
direction: 多智能体协作 · 工作流编排评测
tags:
- Multi-Agent
- Workflow Orchestration
- Benchmark
- LLM Agent
- Task Evaluation
one_liner: 构建覆盖8个专业领域的多智能体工作流编排基准，验证编排能力是独立性能影响因素
practical_value: '- 搭建电商复杂任务（大促活动页生成、多渠道营销方案协同）多智能体系统时，可参考两种编排策略：Claude系「少次大组委派」适合高复杂度强依赖任务，GPT系「多次小组委派」适合细粒度独立子任务场景，平衡协调成本与并行效率

  - 弱模型执行复杂任务的落地场景，可单独用强模型预定义/动态调整工作流结构，无需强模型直接执行任务，可平均提升弱模型得分6.41分，大幅降低推理成本

  - 搭建多智能体系统评测体系时，可复用「工作流全链路可观测+最终集成产出校验+协调成本计入总预算」的设计，避免仅看端到端效果忽略编排环节价值'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM多智能体系统的结构已从开发者固定改为模型运行时自主生成可执行工作流，但现有基准要么仅测端到端任务完成率，要么在预定义协作结构下评测，无法单独评估模型自主的工作流编排能力，而这一能力是长周期复杂任务性能的核心瓶颈。

### 方法关键点
- 构建WorkflowArena基准，包含145个长周期任务，覆盖软件工程、法律分析、3D制作等8个专业领域、17种任务形式，每个任务要求产出由多个依赖组件组成的集成交付物
- 评测协议完全放开编排决策给模型，所有委派操作全链路记录，协调时间与工作时间共享4小时总预算，最终由隐藏验证器同时校验交付物质量与集成一致性
- 设计固定执行器的迁移实验，单独剥离工作流编排的贡献，排除执行模型本身能力的干扰

### 关键结果
在9个模型、25种配置上测试：最优配置Claude Opus 5.5（max effort）的整体任务解决率仅36.95%，说明当前编排能力还有很大提升空间，且无单一配置在所有领域最优；编排策略差异显著：高算力下Claude系模型平均每任务发起0.86次工作流调用，每次调用5.55个worker，GPT系平均每任务发起2.09次调用，每次仅调用1.72个worker；迁移实验中，Claude Opus生成的工作流可让4种弱执行模型的得分平均提升6.41分，而单任务能力更强的GPT-6 Astra生成的工作流反而对多数弱模型无增益。

### 核心结论
多智能体系统的工作流编排能力是独立于单模型任务能力的核心性能影响因素，合理的编排设计可大幅提升弱模型的复杂任务表现。
