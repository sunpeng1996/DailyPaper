---
title: 'Dr. Claw: An AI Scientist Workspace for Vibe Research'
title_zh: Dr. Claw：面向可控人机协作研究的AI科学家工作空间
authors:
- Dingjie Song
- Hanrong Zhang
- Dawei Liu
- Yixin Liu
- Zongxia Li
- Zhengqing Yuan
- Siqi Zhang
- Henry Peng Zou
- Zhiling Yan
- Yuxuan Zhang
affiliations:
- Lehigh University
- University of Illinois Chicago
- University of Pennsylvania
- University of Maryland
- University of Notre Dame
arxiv_id: '2609.00365'
url: https://arxiv.org/abs/2609.00365
pdf_url: https://arxiv.org/pdf/2609.00365
published: '2026-08-30'
collected: '2026-09-08'
category: Agent
direction: Agent 人机协同研究工作流编排
tags:
- Human-in-the-loop
- Agent Orchestration
- Auditable Workflow
- Coding Agent
- Process Traceability
one_liner: 封装现有CLI编码Agent，提供可审计可追溯的人机协同全流程研究编排层
practical_value: '- 架构层面可复用「封装成熟执行Agent + 仅新增编排管控层」的思路，无需重复开发代码生成、工具调用等基础能力，可快速落地推荐策略迭代、广告素材生产等场景的AI助手

  - 四个持久化状态对象（Task Graph/Artifact Store/Decision Log/Execution Trace）的设计可直接迁移，解决电商大促策略迭代、推荐AB实验全流程追溯、审计、故障无感知恢复的痛点

  - 分阶段标准化技能库+自动匹配+手动调用的能力设计可复用，将电商推荐的召回优化、排序调参、AB实验、效果分析等拆成可复用技能，大幅降低重复开发成本

  - 人机分工边界的设计思路可直接复用：AI负责高吞吐、可模板化的执行任务，人掌握目标设定、约束定义、最终验收权，既提升效率也控制业务风险'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有CLI编码Agent已具备长会话读写文件、代码执行能力，但复杂工作全流程分散在多工具之间，过程决策数据无留存，可审计性、可追溯性差，跨工具上下文切换成本高；现有端到端自治Agent过度追求自动化，忽视人的可控性需求，无法适配真实业务的灵活迭代要求。
### 方法关键点
- 不自研执行Agent，直接封装现有CLI编码Agent，仅新增编排管控层，明确人机分工：AI负责可并行、可模板化的执行任务，人掌握目标设定、约束定义、验收决策等核心控制权
- 核心设计四个持久化状态对象：Task Graph、Artifact Store、Decision Log、Execution Trace，全流程状态可追溯、故障可恢复
- 三层解耦架构：交互层（统一工作空间）、编排层（状态与生命周期管理）、执行层（多执行器适配）；配套覆盖5个研究阶段的171个可复用技能库，支持自动匹配、手动调用
### 关键结果
固定后端执行器（GPT-5.4 Codex）对比原生CLI Agent：3个医学研究任务中，Dr. Claw研究完整性平均得分0.952，高于原生Agent的0.873，其中研究规范性指标（局限性分析、亚组分析、参考文献引用）通过率提升34%~100%；原生Agent无任何过程审计数据留存，Dr. Claw全量留存所有过程数据，支持故障非破坏性恢复。7名AI PhD的回溯研究显示，对比无AI工具、通用AI助手，Dr. Claw的任务完成时间更短、输出质量更高、工具切换次数更少，用户体验显著更优。
> 最值得记住的一句话：AI辅助复杂工作流的核心瓶颈已从单点执行能力转向全流程编排与人机协同边界管控，封装成熟执行能力、强化过程可控性的轻量编排层投入产出比远高于自研端到端自治Agent
