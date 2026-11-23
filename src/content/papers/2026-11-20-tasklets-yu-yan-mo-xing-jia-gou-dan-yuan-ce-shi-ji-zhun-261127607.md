---
title: 'Tasklets: A Unit-Test Benchmark for Language Model Architectures'
title_zh: Tasklets：语言模型架构单元测试基准
authors:
- Zayd Muhammad Kawakibi Zuhri
- Munachiso Samuel Nwadike
- Kentaro Inui
- Alham Fikri Aji
affiliations:
- Mila, Canada
- MBZUAI, UAE
- RIKEN AIP, Japan
- Tohoku University, Japan
arxiv_id: '2611.27607'
url: https://arxiv.org/abs/2611.27607
pdf_url: https://arxiv.org/pdf/2611.27607
published: '2026-11-20'
collected: '2026-11-23'
category: Eval
direction: 大语言模型架构评测 · 序列混合层
tags:
- Benchmark
- Sequence-Mixing Layer
- LLM Evaluation
- Architecture Testing
- Unit Test
one_liner: 搭建统一小合成任务基准Tasklets，可低成本可复现地评测LLM不同序列混合层的基础计算能力
practical_value: '- 自研或选型LLM序列混合层（如Mamba、Attention变种）时，可复用Tasklets的低成本单元测试流程，先验证基础能力再做下游业务适配，大幅降低试错成本

  - 开发业务域定制小LLM（如电商客服、推荐场景专属LLM）时，可参考Tasklets的任务设计思路，定制针对业务核心能力（如多轮状态跟踪、用户行为召回）的预训练验证任务

  - 团队内部迭代LLM架构时，可引入Tasklets的统一评测框架，避免不同实验的任务设置差异导致的结论偏差，提升迭代效率'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前LLM序列混合层（Attention、Mamba等变种）的基础计算能力评测缺乏统一标准，不同研究的任务选择、设置逻辑差异大，跨方案对比可信度低，新架构验证成本高。
### 方法关键点
1. 搭建Tasklets基准，覆盖召回、序列操作、状态跟踪3大类核心能力，包含Copy、记忆、计数、栈操作、形式语言匹配等子任务；
2. 统一全流程实验配置，支持小模型受控测试，代码完全开源，可复现性强。
### 关键结果
完成20+主流序列混合层（含Mamba2、RWKV6、RetNet、LSTM等）的横向能力对比，输出各架构在不同任务组的得分排名，测试成本远低于全量下游任务评测。
