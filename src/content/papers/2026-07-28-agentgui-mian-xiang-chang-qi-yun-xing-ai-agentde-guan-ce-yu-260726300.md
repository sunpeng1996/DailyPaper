---
title: 'AgentGUI: An Interface for Observing and Steering Long-Running AI Agents'
title_zh: AgentGUI：面向长期运行AI Agent的观测与调控可视化界面
authors:
- Xuan Zhao
- Jiwoong Sohn
- Qinyue Zheng
- Michael Moor
affiliations:
- ETH Zürich
arxiv_id: '2607.26300'
url: https://arxiv.org/abs/2607.26300
pdf_url: https://arxiv.org/pdf/2607.26300
published: '2026-07-28'
collected: '2026-07-30'
category: Agent
direction: LLM Agent 观测与管控工具
tags:
- LLM Agents
- Agent Observability
- Agent Steering
- GUI
- Open-source Tool
one_liner: 开源本地GUI工具，支持多Agent并发会话的轨迹观测与人工/自动漂移修正，兼容主流开源Agent框架
practical_value: '- 搭建内部Agent运营平台时，可复用其分层轨迹可视化设计，将推理步骤、工具调用、耗时分布、输出产物分模块展示，降低运维排查Agent错误的成本

  - 针对Agent漂移问题，可借鉴自动审计思路：用小成本管理端LLM定期检查任务完成度、输出纠偏提示，小模型场景可提升30%左右任务完成率，token开销仅占总开销1%

  - 多Agent协作场景可参考其团队分组、工件共享、动态切换模型配置的架构，比如推荐场景下用小Agent做用户意图理解、大Agent做生成校验的流程设计'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前LLM Agent已可支撑数小时到数天的长周期任务（如代码开发、科研实验），但运行轨迹混杂推理步骤、工具调用、文件操作日志，人工排查效率极低；现有工具要么仅支持可视化无管控能力，要么绑定特定Agent框架，缺乏统一的观测与调控界面。

### 方法关键点
- 架构为本地部署的FastAPI后端+React前端，每个Agent运行在独立Docker沙箱，支持会话快照保存与恢复，兼容Ollama本地部署、远程GPU、云端推理多种模式
- 可视化层分4维度展示轨迹：活动流（区分推理/工具调用类型）、耗时时间线、Token/API调用debug日志、代码执行控制台，子Agent轨迹支持嵌套展示
- 管控支持两种模式：人工手动干预打断当前执行、重写任务指令；自动审计Manager按配置周期检查任务完成度，输出纠偏反馈自动恢复Agent运行
- 兼容Hermes、Claude Agent SDK等主流Agent框架

### 关键实验
用户研究对比Hermes原生Dashboard，8名参与者识别Agent轨迹关键信息的速度快38%（90s vs 145s每问题，p=0.023），准确率从80%提升到93%（p=0.031），用户认知负荷显著降低；自动漂移修正实验在0.8B-9B的Qwen3.5模型上，单轮审计可将任务完成率最高提升34个百分点（0.8B模型从10%到26%，4B模型从44%到78%），Manager的Token开销仅占总开销的0.19%-0.56%。

可观测性是信任Agent自动化任务的前提，一个能让Agent行为可读、可即时修正的界面，能把黑盒的运行日志转化为人类可验证、可依赖的产出。
