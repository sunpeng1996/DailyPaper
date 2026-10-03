---
title: 'RLE-Bench: A Qualifying Exam for Coding Agents as Robot Learning Engineers'
title_zh: RLE-Bench：面向机器人学习工程师编码智能体的资格测试基准
authors:
- Haitong Ma
- Chenxiao Gao
- Rushi Qiang
- Bo Dai
- Na Li
affiliations:
- Harvard University
- Georgia Institute of Technology
arxiv_id: '2609.34210'
url: https://arxiv.org/abs/2609.34210
pdf_url: https://arxiv.org/pdf/2609.34210
published: '2026-09-28'
collected: '2026-10-03'
category: Agent
direction: 编码Agent 机器人场景全链路能力测评
tags:
- Agent
- Benchmark
- Robotics
- Evaluation
- Code Generation
one_liner: 推出覆盖4类机器人开发全流程的编码Agent测评基准RLE-Bench及综合能力评估体系
practical_value: '- 多维度任务聚合打分思路可迁移到电商场景Agent（如客服、选品Agent）能力评估，替代单一任务成功率指标，更全面衡量落地能力

  - 全流程覆盖的Benchmark设计方法可复用，搭建推荐系统LLM Agent测评集时可覆盖召回、排序、文案生成全链路，而非单一环节测评

  - 跨模态反馈下的Agent能力评估范式可借鉴，用于评估需处理图文、用户行为多模态输入的电商导购Agent实际表现'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有机器人领域测评基准多聚焦策略、控制器等单一模块性能，无法覆盖编码Agent在真实物理场景下的全链路工程能力，包括异构模块集成、资源约束下优化、多模态反馈推理等核心能力。

### 方法关键点
推出RLE-Bench测评基准，覆盖交互控制、策略学习、感知与估计、机械设计4类典型机器人开发全流程任务，针对不同任务设计专属指标，最终聚合生成统一RLE指数，可系统对比编码Agent多维度能力差异，同时配套典型任务案例分析定位能力短板。

### 关键结果数字
公开11款主流大模型驱动的编码Agent测评排名，GPT-6 Astra以73.4的RLE指数位列第一，第二名Claude Fable 5.1得分为64.0，头部模型在各流程的能力分差可达20分以上
