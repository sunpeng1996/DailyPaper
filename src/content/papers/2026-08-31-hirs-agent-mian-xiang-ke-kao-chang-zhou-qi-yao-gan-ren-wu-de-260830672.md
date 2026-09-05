---
title: 'HiRS-Agent: A Hierarchical Multi-Agent System for Reliable Long-Horizon Remote
  Sensing Task Solving'
title_zh: HiRS-Agent：面向可靠长周期遥感任务的分层多智能体系统
authors:
- Boyang Mu
- Zhiwei Wei
- Mugen Peng
- Wenjia Xu
affiliations:
- 北京邮电大学
- 网络与交换技术国家重点实验室
- 湖南师范大学
- 湖南师范大学地理科学学院
arxiv_id: '2608.30672'
url: https://arxiv.org/abs/2608.30672
pdf_url: https://arxiv.org/pdf/2608.30672
published: '2026-08-31'
collected: '2026-09-05'
category: MultiAgent
direction: 多智能体分层协作架构优化
tags:
- MultiAgent
- Hierarchical Agent
- Reinforcement Learning
- Task Planning
- Tool Use
one_liner: 提出Manager-Specialist两级分层多Agent架构与验证引导优化策略，解决长周期复杂任务执行不稳定、错误传播痛点
practical_value: '- 长周期多阶段业务任务（如电商大促全链路运营、用户生命周期运营）可复用两级分层Agent架构：上层Manager负责任务路由、步骤校验、重规划，下层Specialist绑定领域工具执行子任务，规避单一大模型决策不稳定问题

  - 可借鉴验证引导的分层强化学习策略，分阶段优化多Agent协作规则和工具调用策略，有效降低跨阶段误差传播概率

  - 复杂多步骤任务可引入步骤级校验与提前终止机制，减少无效执行开销，提升整体任务执行效率'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有长周期复杂任务多依赖单块式大模型决策框架，无法适配多阶段任务的相互依赖特性，普遍存在执行不稳定、工具调用错误、跨阶段误差传播等问题，遥感领域任务尤为突出。
### 方法关键点
1. 采用两级分层多智能体架构：Manager层负责动态路由、步骤级校验、重规划与终止控制；Specialist层按任务工作流组织领域专属工具，负责子任务推理与工具执行
2. 引入两阶段监督微调+验证引导的分层强化学习策略，联合优化多Agent协作规则与工具调用策略
### 关键结果
在Earth-Agent Benchmark、ThinkGeo两个基准上，长周期工具调用能力、最终任务准确率均实现大幅提升，验证了结构化多Agent协作的有效性
