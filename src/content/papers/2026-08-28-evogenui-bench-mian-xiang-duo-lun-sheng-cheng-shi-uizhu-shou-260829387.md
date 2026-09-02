---
title: 'EvoGenUI-Bench: Evaluating LLMs as Multi-Turn Generative UI Assistants'
title_zh: EvoGenUI-Bench：面向多轮生成式UI助手的大语言模型评测基准
authors:
- Yue Peng
- Lanke Xia
- Zihan Wang
- Jiahao Ye
- Ke Ning
- Hongyi Wen
affiliations:
- New York University Shanghai
arxiv_id: '2608.29387'
url: https://arxiv.org/abs/2608.29387
pdf_url: https://arxiv.org/pdf/2608.29387
published: '2026-08-28'
collected: '2026-09-02'
category: Eval
direction: 大模型评测 · 多轮生成式UI助手
tags:
- LLM Evaluation
- Generative UI
- Multi-turn Interaction
- Benchmark
- UI Agent
one_liner: 提出覆盖3场景的多轮生成式UI评测基准，新增跨轮留存指标诊断LLM生成UI的多轮能力缺陷
practical_value: '- 电商智能装修、个性化导购UI生成类Agent可复用该基准的多轮评测逻辑，加入跨轮状态留存校验，避免迭代UI时丢失原有功能

  - 可借鉴该基准多维度校验方案（截图+DOM+运行日志+操作轨迹），用于生成式UI Agent的自动化效果验收，降低人工评测成本

  - 工具绑定类UI任务的故障归因结论可直接复用，开发Agent时优先优化外部状态对齐、需求拆解模块，提升多轮交互成功率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前LLM可生成交互式UI，但现有评测仅针对单轮输出，未覆盖用户需求迭代时的多轮UI维护能力，无法衡量界面状态、功能的跨轮一致性。

### 方法关键点
构建EvoGenUI-Bench，覆盖信息展示、可执行交互、工具绑定外部状态3类场景，含150组五轮任务共750轮交互；评测时在浏览器运行生成产物，结合截图、源码、DOM、操作轨迹、运行日志多维度校验，新增相邻轮次通过率（APR）指标衡量跨轮功能留存。

### 关键结果
8款主流LLM中最优模型单轮通过率仅74.9%，五轮完整任务成功率仅37.3%；工具绑定场景下APR低至52.4%；故障归因显示展示类问题集中在信息架构，交互类问题多为状态传播绑定错误，工具类问题额外涉及外部状态对齐、需求拆解缺陷。
