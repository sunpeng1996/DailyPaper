---
title: 'Trial by Trace: Benchmarking AI Agent Harnesses for Reliability and Failure
  Attribution'
title_zh: 基于执行轨迹的AI Agent Harness可靠性与故障归因基准TraceTrial-Bench
authors:
- Zhiyong Cao
- Hengjie Zhu
- Yongxin Wang
- Xuchen Li
- Jintao Li
- Shuxia Liu
- Dunqiang Liu
- Bo Wang
- Kairan Zhang
- Cong Lin
affiliations:
- Institute of Automation, CAS
- Zhongguancun Academy
- Institute of Information Engineering, CAS
- Tsinghua University
- Beijing Institute of Technology
arxiv_id: '2610.32285'
url: https://arxiv.org/abs/2610.32285
pdf_url: https://arxiv.org/pdf/2610.32285
published: '2026-10-22'
collected: '2026-10-27'
category: Agent
direction: Agent Harness可靠性评测与故障归因
tags:
- Agent
- Harness
- Reliability
- Benchmark
- Failure Attribution
one_liner: 推出首个Agent Harness专属评测基准TraceTrial-Bench，支持分层评估与可溯源故障归因
practical_value: '- 电商/推荐场景落地Agent时，不能仅以最终任务成功率作为唯一指标，需单独监控Harness层可靠性，避免31.1%的成功任务隐藏的Harness隐性故障影响长期稳定性

  - 可复用Trajectory Tracing+Multi-source Evidence Acquisition架构，采集Agent执行轨迹、上下文、环境状态多源数据，用于导购Agent、智能客服Agent的线上故障快速定位

  - 内部Agent Harness选型时，可参考TraceTrial-Bench的7个可靠性维度设计自定义评测用例，量化不同Harness的适配性与稳定性差异，降低选型风险'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent基准大多聚焦模型能力与整体任务成功率，无法区分任务失败源于模型决策错误还是Harness（连接模型与工具/环境的运行时层）故障，且大量成功任务实际存在Harness隐性缺陷，缺乏专门针对Harness可靠性的可溯源评测体系。
### 方法关键点
- 把Harness可靠性划分为上下文、执行、治理、生命周期、可观测性、工具、验证7个维度，设计95个机制导向的专家级任务，保留各Harness原生接口与执行逻辑做语义等价对比
- 核心模块：Trajectory Tracing模块采集原生执行轨迹并统一为Trace IR格式；Multi-source Evidence Acquisition模块聚合Agent上下文、Harness记录、环境状态三类证据；Failure Attribution模块通过预定义机制链实现运行级故障归因
- 双层评估框架：独立评估Agent任务完成率与Harness可靠性，避免两类结果互相干扰
### 关键实验结果
覆盖4款主流Harness（Claude Code、Codex、DeepSeek Harness、OpenClaw）、9款LLM、95个任务共3420次运行，宏观平均Harness得分区间为59.8%~72.0%，31.1%的运行达成任务成功但至少存在1项Harness指标不合格，其中OpenClaw的Harness宏观得分最高（72.0%），Codex得分最低（59.8%）。
### 最值得记住的结论
Agent性能是模型与Harness的共同属性，仅看最终任务成功率会掩盖3成以上的Harness隐性故障。
