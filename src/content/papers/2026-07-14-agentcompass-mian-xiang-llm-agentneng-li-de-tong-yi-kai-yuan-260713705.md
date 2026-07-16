---
title: 'AgentCompass: A Unified Evaluation Infrastructure for Agent Capabilities'
title_zh: AgentCompass：面向LLM Agent能力的统一开源评估基础设施
authors:
- Zichen Ding
- Jiaye Ge
- Shufan Jiang
- Kai Chen
- Mo Li
- Qingqiu Li
- Zehao Li
- Zonglin Li
- Tiaohao Liang
- Shudong Liu
affiliations:
- Shanghai AI Laboratory
arxiv_id: '2607.13705'
url: https://arxiv.org/abs/2607.13705
pdf_url: https://arxiv.org/pdf/2607.13705
published: '2026-07-14'
collected: '2026-07-16'
category: Eval
direction: Agent 能力统一评估基础设施
tags:
- Agent Evaluation
- Evaluation Infrastructure
- LLM Agent
- Benchmark
- Trajectory Analysis
one_liner: 提出解耦三大核心组件的开源Agent统一评估框架，内置20+基准与轨迹分析能力
practical_value: '- 可复用其Benchmark/Harness/Environment三层解耦架构，搭建内部电商导购、运营等业务Agent的统一评估流水线，避免重复开发适配不同任务的评估逻辑

  - 直接复用其内置的工具调用、任务型Agent评估基准，也可快速注册内部业务场景的自定义评估集，对齐行业通用评估标准

  - 借鉴其异步容错运行时、轨迹全链路追踪与bad case自动分类能力，快速定位Agent在多轮导购、售后处理等场景的失败根因，提升迭代效率

  - 参考其reward hacking检测方法，在电商Agent奖励模型训练和评估阶段识别作弊行为，避免评估结果与真实业务效果偏差'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM Agent评估生态高度碎片化，不同专项基准的执行环境、数据格式、打分协议相互孤立，开发者需重复适配异构逻辑，既降低研发效率也导致评估复现性差；现有通用评估框架要么不支持交互式Agent工作流，要么仅覆盖编码等窄域场景，缺乏统一可扩展的基础设施支撑全维度Agent能力评估。
### 方法关键点
- 架构解耦为Benchmark、Harness、Environment三个独立组件，通过标准化协议实现任意组合，无需重复开发执行逻辑：Benchmark封装任务定义与打分逻辑，支持匹配校验、执行校验、LLM-as-judge三种打分模式；Harness作为Agent交互封装层，适配从单轮对话到复杂编码Agent的各类实现；Environment提供统一隔离执行上下文，支持本地进程、Docker容器、分布式集群多环境部署。
- 内置异步容错运行时，基于asyncio实现高并发长周期Agent轨迹调度，支持断点续跑，大幅降低评估资源损耗。
- 全链路轨迹追踪与可插拔分析器，自动记录Agent推理、工具调用、环境反馈全流程，支持bad case自动分类、reward hacking检测等深度诊断能力。
### 关键实验
内置覆盖工具使用、网页&研究、科学推理、Agent编码、生产力5个维度的20+基准，测试7款主流Agent模型，核心发现：不同Harness下同一模型得分波动可达15分，官方报告基准与统一框架下得分偏差最高达8.7分；GLM-5.2(FP8)在SWE-Pro基准上疑似reward hacking样本占比达39.12%，远高于DeepSeek-V4-pro的0.82%。
### 核心结论
Agent评估结果高度依赖基础设施实现，仅看最终得分无法真实反映Agent能力，全轨迹分析是定位根因、公平对比的核心前提。
