---
title: 'LLMs and Agentic AI Systems for Smart Grids: A Tutorial on Architectures and
  Applications'
title_zh: 面向智能电网的大模型与智能体AI系统架构及应用教程
authors:
- Daniela Rojas
- Abdulwahab Albassam
- Aidan G. Leung
- Jett Ngo
- Ryan Luo
- Peter R. Quawas
- Junpyung Kim
- Kangkai Liang
- Mansi Nanavati
- Jonathan Mai
affiliations:
- University of California San Diego
- University of Alberta
arxiv_id: '2607.18147'
url: https://arxiv.org/abs/2607.18147
pdf_url: https://arxiv.org/pdf/2607.18147
published: '2026-07-20'
collected: '2026-07-22'
category: Agent
direction: Agent 垂直领域架构设计与评估
tags:
- Agent
- LLM
- Tool Use
- Evaluation Framework
- Architecture Design
one_liner: 提出求解器锚定的Agent设计原则与四维评估框架，在智能电网场景验证落地效果
practical_value: '- 垂直领域Agent可复用「求解器锚定」设计原则，LLM仅负责编排、检索、解释逻辑，数值计算完全交可信工具，最后加校验 gate
  过滤输出，可解决电商优惠计算、库存调度类Agent的数值错误问题

  - 垂直Agent评估可复用四维框架：任务效用、工具调用正确性、输出保真/安全降级、成本时延，适配到电商场景可对应业务效果、工具准确率、合规性、推理成本四个核心维度

  - 复杂多步任务的Agent分层架构可参考：编排层（LLM）+ 计算层（业务可信工具/规则引擎）+ 校验层（规则验证器），可直接迁移到电商大促资源分配、广告预算调度等场景'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
垂直技术领域落地LLM与Agent时存在三大痛点：LLM易生成数值看似合理但违反物理/业务约束的结果；不同任务的评估标准不统一；LLM与外部工具的计算边界模糊，缺乏统一的设计与评估范式。
### 方法关键点
1. 提出**求解器锚定**设计原则：所有数值结果必须来自可信求解器且通过显式校验才能输出；
2. 梳理垂直领域LLM Agent的核心组件：提示策略、Agent架构；
3. 提出四类评估框架：任务效用、求解器锚定正确性、输出保真与安全失败、成本与时延。
### 关键结果
在4个智能电网场景做对照实验：EV充电调度Agent相比纯LLM基线，未满足能量需求降低7.5-9.5x，完全复现CVXPY最优解；电网故障诊断Agent修复17/39故障案例，总违规率降低52.3%。
