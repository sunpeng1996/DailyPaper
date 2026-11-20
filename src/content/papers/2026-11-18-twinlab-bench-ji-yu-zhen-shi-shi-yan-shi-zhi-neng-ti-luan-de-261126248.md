---
title: 'TwinLab-Bench: Evaluating AI Scientists in Agentic Twins of Real Labs'
title_zh: TwinLab-Bench：基于真实实验室智能体孪生的AI科学家评测基准
authors:
- Yang Wan
- Linchao Zhu
affiliations:
- Zhejiang University
arxiv_id: '2611.26248'
url: https://arxiv.org/abs/2611.26248
pdf_url: https://arxiv.org/pdf/2611.26248
published: '2026-11-18'
collected: '2026-11-20'
category: Agent
direction: Agent评测 · 自主实验能力评估
tags:
- Agent
- Benchmark
- LLM
- Evaluation
- Autonomous_Experiment
one_liner: 提出首个支持评测AI Agent自主设计实验能力的基准TwinLab-Bench，覆盖理化生工52类真实实验室任务
practical_value: '- 做垂直领域Agent评测时，可复用「孪生环境代理执行被测Agent生成的操作+真实数据作为标准答案」的框架，避免脱离实际业务规则的无效评测

  - 自主决策类Agent（如电商智能选品Agent、广告投放策略Agent）的评测可引入闭卷探针校验，排除大模型记忆带来的评测误差

  - 多任务Agent评测时可按任务域拆分独立环境代理，降低复杂业务场景下的评测环境开发成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
AI科学家Agent需具备三类能力：执行给定工作流、从设计空间选后续测量方案、自主设计实验。现有基准仅覆盖前两类，无法评测开放度最高的自主实验设计能力，且缺乏与真实实验室数据对齐的执行环境。
### 方法关键点
1. 构建覆盖物理、生命科学、工程3大领域共52项真实实验室任务的评测基准，支持100+实验操作类型；2. 每个任务配套独立TwinLab Agent作为环境代理，读取实验室原始数据调用记录构建的计算器，执行被测Agent设计的实验；3. 采用真实实验室记录作为隐藏标准答案评分，引入闭卷探针排除大模型记忆干扰。
### 关键结果数字
TwinLab Agent将偏离真实记录的结果、重复请求不一致结果的概率几乎降至0；当前前沿模型Claude Fable 5.2在该基准上平均得分仅45.0，自主实验设计能力仍有较大提升空间。
