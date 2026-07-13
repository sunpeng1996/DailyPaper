---
title: Shared Selective Persistent Memory for Agentic LLM Systems
title_zh: 面向智能体LLM系统的共享选择性持久内存架构
authors:
- Sanjana Pedada
- Aditya Dhavala
- Neelraj Patil
affiliations:
- Apple Inc.
arxiv_id: '2607.09493'
url: https://arxiv.org/abs/2607.09493
pdf_url: https://arxiv.org/pdf/2607.09493
published: '2026-07-10'
collected: '2026-07-13'
category: Agent
direction: Agent 长会话上下文持久化优化
tags:
- Agent Memory
- Context Management
- Persistent Memory
- LLM Agent
- Enterprise Agent
one_liner: 提出仅保留4类可复用上下文的共享选择性持久内存，大幅提升Agent任务完成率与资源效率
practical_value: '- 电商/运营类报表Agent、推荐规则配置Agent可直接复用4类上下文拆分规则：仅持久化任务规则、数据schema、工具配置、输出约束，主动丢弃会话推理轨迹，既避免旧会话的推理路径偏差，还能大幅降低token消耗

  - 周度/月度销售报表、投放效果大盘等重复生成场景可落地zero-token数据刷新机制：强制生成代码仅从运行时注入点读取数据，只要schema兼容，数据更新完全不需要重新调用LLM，实测提速14倍

  - 跨团队共享Agent工作区可借鉴RBAC+git版本控制方案：支持工作区模板复用、草稿隔离、一键回滚到任意历史版本，无需重复配置相同的任务规则和工具链

  - 给Agent输入结构化数据时，无需传入全量原始数据，仅传入预计算的统计摘要（列类型、分布、样例行）即可，实测最高降97%的token成本，且不影响代码生成准确率'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前Agent会话默认无状态，每次新会话都需要用户重新输入领域约束、数据schema、工具配置等信息；全量保存历史会话的方案不仅token效率极低，还会因无关上下文、过期推理轨迹干扰生成效果，企业场景下大量结构相似的重复任务冗余成本极高。

### 方法关键点
1. 可复用上下文拆分：仅持久化4类跨会话有效信息，分别是任务规格（领域规则、输出偏好、质量约束）、数据schema（列属性、统计分布、样例行）、工具配置（参数schema、调用方式、鉴权规则）、输出约束（运行时规则，如禁止硬编码数据）
2. 选择性遗忘：主动丢弃会话推理轨迹、中间临时文件、错误恢复路径、工具调用日志等仅单次会话有效、跨会话会引入偏差的内容
3. 配套zero-token数据刷新机制：要求Agent生成的代码仅从预定义运行时注入点读取数据，只要新数据schema兼容，更新数据无需调用LLM
4. 协作层设计：基于git实现工作区版本控制、草稿隔离、一键回滚，搭配RBAC权限控制，支持多用户跨角色共享工作区模板

### 关键实验
对比无内存、全量历史两个基线，在24个企业真实任务上：选择性内存任务完成率达96%（无内存79%、全量历史71%），单任务耗时从285s降至68s，单调用token成本较原始数据注入降低97×；在4个公开数据集上，zero-token刷新12/12全部成功，重复任务提速14×。

**最值得记住的一句话**：全量历史持久化不仅无法提升Agent性能，反而会因无关上下文干扰降低任务完成率，上下文管理才是企业级Agent效率提升的核心杠杆，而非模型能力本身。
