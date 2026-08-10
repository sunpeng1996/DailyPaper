---
title: An End-to-End Agent Auditing Engine
title_zh: 端到端Agent审计引擎A2E：全链路多维度测评框架
authors:
- Haoning Wang
- Mingxun Zhang
- Chenyue Yu
- Yingjun Shang
- Xia Hu
- Guanchu Wang
- Na Zou
affiliations:
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2608.07346'
url: https://arxiv.org/abs/2608.07346
pdf_url: https://arxiv.org/pdf/2608.07346
published: '2026-08-07'
collected: '2026-08-10'
category: Agent
direction: Agent测评 · 全链路多维度评估
tags:
- Agent Evaluation
- Trajectory Analysis
- LLM Agent
- Multi-Harness Benchmark
- Observability
one_liner: 提出适配多Agent框架与基准的端到端测评引擎，覆盖全生命周期细维度能力评估
practical_value: '- 可复用分层监控设计，对业务端电商导购Agent、推荐Agent做全链路轨迹埋点，统一观测规划、工具调用、结果输出各阶段的性能与异常

  - 可借鉴生命周期对齐的评估体系，Agent选型时不只看最终正确率，额外纳入token消耗、调用延迟、工具召回率等业务敏感维度做综合打分

  - 其Agent Task Protocol（ATP）的解耦设计可迁移，实现不同Agent框架（如LangGraph、CrewAI）与业务场景任务的快速适配，减少对接开发量

  - 实验结论可直接复用：同模型下不同Agent框架在不同任务上表现差异极大，无全局最优框架，需针对电商导购、售后、内容生成等场景单独选型'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前LLM Agent落地性能很大程度取决于harness框架（负责prompt构造、工具接口、上下文管理、执行策略等），仅评估底层模型无法反映部署后真实表现。现有测评方案要么只看最终正确率，无法定位过程问题；要么需要为每个harness与基准数据集写专属适配代码，侵入原生执行逻辑，轨迹保真度低，缺乏统一的端到端全链路测评基础设施。

### 方法关键点
- 三层架构设计：任务层基于Agent Task Protocol（ATP）解耦基准与Agent框架，无需为每对组合开发适配代码；监控层基于OpenTelemetry实现无侵入埋点，采集结构化、可追溯的标准化执行轨迹；评估层对齐Agent全生命周期，覆盖推理、行动、结果、运行质量四大维度共23项细粒度指标
- 数据库中心化存储：轨迹、指标、测评结果统一入库，支持增量评估、跨实验对比，新增指标无需重复运行Agent即可基于已有轨迹计算

### 关键实验
控制底层模型统一为DeepSeek-V4-pro/GLM-5.2，对9个主流Agent框架（LangGraph、CrewAI、Agno等）、23个公开基准完成全组合测评：① 单轮任务下各harness正确率差异极小，多轮交互任务下正确率差异最高达0.8；② 不同harness的token消耗差异最高达3.5倍，而整体正确率仅在0.57-0.68区间波动；③ 无全局最优harness，不同任务下的最优框架完全不同。

### 核心结论
Agent harness不是模型的轻量wrapper，其prompt构造、工具表示、执行逻辑设计会显著影响最终性能与成本，测评不能只看最终正确率。
