---
title: 'LLM-Based Agents for Software and Systems Security: Approaches, Applications,
  and Assessment'
title_zh: 基于LLM的软件与系统安全Agent：技术、应用与评估综述
authors:
- Jingjing Nie
- Jiawei Guo
- Krishna Meda
- Haipeng Cai
affiliations:
- University at Buffalo, SUNY, USA
arxiv_id: '2608.28490'
url: https://arxiv.org/abs/2608.28490
pdf_url: https://arxiv.org/pdf/2608.28490
published: '2026-08-28'
collected: '2026-08-31'
category: Agent
direction: LLM Agent 技术体系与评估综述
tags:
- LLM Agent
- Cybersecurity
- Agent Architecture
- Agent Evaluation
- Systematic Review
one_liner: 系统梳理2023-2026年LLM安全Agent的技术、应用、评估体系，指出领域核心短板
practical_value: '- 可复用该综述梳理的Agent架构设计维度（感知、记忆、规划、工具调用等），搭建业务侧通用Agent框架

  - 可借鉴安全Agent的评估思路，设计包含结果指标、轨迹指标、安全边界的业务Agent评估体系

  - 针对高风险业务场景（如电商交易决策、广告投放策略），可参考其提出的权限边界、行为可审计性设计要求，规避Agent决策风险'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
软件与系统安全工作流属于多步程序性任务，LLM Agent可自动化该类流程，但当前领域存在术语定义不统一、应用风险差异大、评估体系不可比的问题，缺乏系统性梳理。
### 方法关键点
对2023-2026年领域内同行评议论文开展系统性综述，覆盖三大维度：1）技术方案：含Agent架构、感知、记忆、推理规划、动作空间、编排、自优化；2）应用场景：覆盖各类安全任务；3）评估体系：含数据集、结果与轨迹指标、安全度量、对比基线。
### 关键结果
梳理发现当前领域已落地具备行动能力的Agent，但普遍缺乏权限边界约束与行为可审计能力；明确了当前技术、应用、评估层面的核心局限与未来研究方向。
