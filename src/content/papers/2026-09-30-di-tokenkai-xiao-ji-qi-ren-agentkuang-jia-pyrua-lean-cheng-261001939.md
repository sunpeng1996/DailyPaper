---
title: 'Fewer Tokens, Better Action: GPT-6 Astra Robot Agents with 14% Higher Success
  Rate but 65% Fewer Tokens'
title_zh: 低Token开销机器人Agent框架PyRUA-Lean：成功率升14%，Token减65%
authors:
- Ruiyang Si
- Jianxin Bi
- Shunyu Yang
- Rui Ni
- Wenbo Huang
- Qiang Wang
- Shulong Jiang
- Duomin Wang
- Xiuyu Li
- Haiwen Feng
affiliations:
- Peking University
- National University of Singapore
- NVIDIA
- Impossible Research
arxiv_id: '2610.01939'
url: https://arxiv.org/abs/2610.01939
pdf_url: https://arxiv.org/pdf/2610.01939
published: '2026-09-30'
collected: '2026-10-02'
category: Agent
direction: Agent 执行接口优化 · 低Token开销
tags:
- Agent
- LLM
- Code Execution
- Token Efficiency
- VLM
one_liner: 提出交互式代码执行框架PyRUA-Lean，提升机器人Agent成功率同时大幅降低Token消耗
practical_value: '- Agent接口可替换传统逐次tool calling模式，将多步调用、条件判断、重试逻辑封装为单次LLM调用的代码块，直接减少LLM调用次数与Token开销，适用于电商导购、推荐系统决策Agent等所有多步任务场景

  - 上下文管理采用选择性返回机制：仅把LLM显式请求的结果塞入上下文，中间计算、临时变量存储在外部runtime的持久化命名空间，避免无效信息占用Token配额

  - 复杂任务可将领域通用逻辑（如电商的库存校验、优惠计算、履约规则）封装为标准Python方法，LLM通过生成代码组合逻辑完成任务，比纯tool calling成功率更高、成本更低'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前VLM驱动的Agent多采用tool calling模式，每步操作都要触发LLM调用，且中间观察、执行结果会自动累积进上下文，导致Token开销极高、推理成本居高不下，同时受LLM调用次数限制，复杂长周期任务的成功率难以提升，亟需更高效的Agent执行接口。

### 方法关键点
- 设计交互式Python代码执行框架，将所有能力封装为统一对象的可调用方法，LLM生成Python代码块组合调用这些能力
- 支持反馈驱动的原语组合：单个代码块可封装多步原语调用、条件判断、本地重试逻辑，中间执行不触发LLM调用，仅在代码块执行结束后返回结果
- 实现选择性观察机制：只有代码中显式`print`的状态、主动请求的输出才会返回给LLM塞入上下文，中间结果全部存在runtime的持久化命名空间中，无需传递给LLM

### 关键实验
在LIBERO-PRO、RoboTwin 2.0、RoboCasa365三个基准共700个模拟任务实例上，和使用相同GPT-6 Astra规划器、相同底层能力的tool calling基线对比：1. 整体成功率从63.1%提升到71.7%，相对提升14%；2. 双方都完成的任务上，LLM调用次数减少49%，输入Token减少65%，推理成本平均降低2.2倍；3. 长周期多步任务收益最明显，长horizon任务成功率提升36pp，多步堆叠排序任务提升40pp。

### 核心结论
对于依赖多步工具调用的LLM Agent，代码执行接口相比传统tool calling可以同时提升任务成功率和降低Token开销，核心是把中间执行逻辑、状态管理从LLM上下文转移到外部runtime。
