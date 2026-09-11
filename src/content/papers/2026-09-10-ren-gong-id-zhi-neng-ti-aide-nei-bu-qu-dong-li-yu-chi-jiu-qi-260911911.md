---
title: 'Artificial Id: Drive and Persistent Alignment in Agentic AI'
title_zh: 人工Id：智能体AI的内部驱动力与持久对齐机制
authors:
- Yakov Pyotr Shkolnikov
affiliations:
- Independent Researcher
arxiv_id: '2609.11911'
url: https://arxiv.org/abs/2609.11911
pdf_url: https://arxiv.org/pdf/2609.11911
published: '2026-09-10'
collected: '2026-09-11'
category: Agent
direction: Agent 自适应驱动与持久对齐架构
tags:
- Agent
- Alignment
- Persistent Adaptation
- Autonomous Drive
- Agentic Harness
one_liner: 提出独立于通用推理的人工Id架构，通过差异化持久化实现无明确任务目标的自适应驱动
practical_value: '- 可以参考「驱动-推理分离」架构重构现有Agent执行链路：将停止/重试/优先级调整逻辑从通用LLM推理中剥离，单独封装为轻量化驱动模块，降低推理成本、提升链路可控性

  - 差异化持久化筛选机制可迁移到推荐系统冷启动策略：无明确标注的场景下（如新品探索），通过用户停留时长/复访等「持久化」指标自适应筛选有效召回策略，替代人工指定规则

  - 持久对齐边界的设计思路可复用在生产级Agent的权限管控：将观测输入、后果通道、权限、硬约束放在自适应模块之外，避免Agent自主越权，降低生产环境风险'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前Agent系统依赖人工编写的harness定义目标、重试、停止规则等控制逻辑，无法适配跨任务边界、环境动态变化的场景，且对齐仅针对单次任务轨迹，无法支撑长期运行的智能体需求。
### 方法关键点
- 提出驱动与推理分离的人工Id架构：人工Id模块负责自适应内部驱动，决策当前行为的继续/停止/优先级调整，通用大模型作为「ego」负责任务逻辑推理与执行，二者通过环境反馈形成闭环
- 采用差异化持久化作为底层学习机制：无需给Id模块输入明确的任务目标、奖励信号，仅通过环境中有利于持久存续的状态反馈，筛选保留有效的行为策略
- 设计持久对齐边界：将可信观测、后果通道、持久状态、权限、身份、溯源、硬约束独立于自适应模块之外，作为系统级对齐保障
### 关键实验
在虚拟培养皿的3类仿真环境中，用仅20个参数的极小控制器（无通用推理能力）验证机制有效性：
1. World 2（粗引导失效场景）：自适应群体的sustaining region占比（occupancy）最高达0.856，远超盲测基线0.405和人工编写的感知控制器基准0.674
2. World 3（传感器映射反转/食物源切换场景）：自适应群体可快速重新适配，occupancy恢复到高于基线水平，而冻结参数的群体occupancy低于1%
### 核心结论
长期运行的智能体对齐不再是单次模型输出或单任务轨迹的属性，而是跨任务边界的持续运行系统的整体属性
