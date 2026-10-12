---
title: A Baseline Assessment for the Agentic Web Technology Stack
title_zh: Agentic Web技术栈基准评估及多维度性能对比
authors:
- Vagner Figueredo de Santana
- Diogo Cortiz
affiliations:
- NIC.br, Brazil
- PUC-SP, Brazil
arxiv_id: '2610.13703'
url: https://arxiv.org/abs/2610.13703
pdf_url: https://arxiv.org/pdf/2610.13703
published: '2026-10-09'
collected: '2026-10-12'
category: Agent
direction: Agent 技术栈选型与性能基准测试
tags:
- AgenticWeb
- MultiAgent
- Benchmark
- LLMAgent
- FrameworkEvaluation
one_liner: 提出MASTIF多智能体测试框架，完成3类LLM/协议/框架的Agentic Web组合基准评估
practical_value: '- 选型参考：电商导购/购物Agent可优先选Qwen2.5-7B + 无额外协议（Standard）+ LangChain组合，任务完成率可达79.5%，同时兼顾低延迟和低token消耗

  - 工具调用优化：需要高频调用电商商品检索/加购/领券等工具的场景，可选用MCP协议 + Semantic Kernel组合，Qwen2.5-7B下工具调用成功率最高达68.1%

  - 测试框架复用：可直接复用开源MASTIF框架做业务场景Agent的多维度评估，内置的15种通用工具+自定义Web交互工具可覆盖大部分电商Web任务测试需求

  - 成本优化技巧：非跨Agent协作场景不要额外加A2A/MCP协议，否则会显著提升任务耗时和token消耗，最高可增加30%+的冗余成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前Agentic Web领域协议、框架、LLM迭代速度极快，技术碎片化严重，开发者和企业缺乏统一的选型基准，搭建多智能体系统时面临技能、治理、基础设施等多重挑战，没有不同组件组合的量化性能对比参考。
### 方法关键点
- 提出开源MASTIF多智能体测试框架，支持接入主流推理服务，内置13种通用工具+2种Web交互工具，可自动记录延迟、token消耗、推理路径等全链路指标
- 测试矩阵覆盖3类LLM（Mistral-7B-Instruct-v0.1、Qwen2.5-7B、Llama-4-Scout-17B-16E-Instruct）、3类通信协议（无协议Standard、A2A、MCP）、4类主流Agent框架（LangGraph、LangChain、CrewAI、Semantic Kernel）
- 定义任务完成率、收敛时间、token冗余度、工具调用成功率、社会价值稳定性5维评估体系，采用GPT-4o-mini作为独立裁判模型避免同系列模型偏好泄露
### 关键实验结果
- 基于Mind2Web基准分层采样300个任务（覆盖电商、旅行、信息查询等场景），共完成10800次任务执行
- 最优任务完成率组合为Qwen2.5-7B + Standard + LangChain，达79.5%，比Llama-4-Scout同配置高出110%
- 工具调用最优组合为Qwen2.5-7B + MCP + Semantic Kernel，成功率达68.1%
- 无额外协议的Standard配置相比A2A/MCP协议平均降低25%的收敛时间和18%的token消耗
### 核心结论
Agent技术栈选型没有通用最优解，需根据业务场景对完成率、延迟、成本、工具能力的优先级选择对应组合，非跨Agent协作场景无需额外引入通信协议
