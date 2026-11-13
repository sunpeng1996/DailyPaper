---
title: 'Agentic Dashboards: A New Design Paradigm for Visual Analytics'
title_zh: 智能体驱动仪表盘：可视化分析的全新设计范式
authors:
- Sam Yu-Te Lee
- Yun-Hsin Kuo
- Kwan-Liu Ma
arxiv_id: '2611.16245'
url: https://arxiv.org/abs/2611.16245
pdf_url: https://arxiv.org/pdf/2611.16245
published: '2026-11-12'
collected: '2026-11-13'
category: Agent
direction: Agent 可视化分析交互范式
tags:
- AI Agents
- Visual Analytics
- Dashboard Design
- Human-Agent Collaboration
- Analytical Workflow
one_liner: 智能体自主调度分析方法与视图的可视化仪表盘范式，配套行为与故障评估标准
practical_value: '- 可复用「预设决策边界+Agent动态调度」架构优化电商运营看板：运营人员用自然语言提需求，Agent自动生成/调整指标维度、可视化视图，无需前端排期开发

  - 可参考其评估框架设计推荐系统Agent的校验规则：从决策合规性、结果可解释性、操作可追溯性三个维度管控Agent行为，降低业务故障风险

  - 可迁移人-Agent协作逻辑到AB实验分析场景：Agent自动跑多维度归因分析，可视化呈现显著性结论，分析师仅需做最终判断，提升分析效率'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
传统可视化分析系统的分析方法、交互视图、工作流均在设计阶段固化，无法适配业务场景中动态变化的分析需求，用户调整分析维度需依赖前端开发迭代，效率极低。
### 方法关键点
Agentic Dashboard新型设计范式核心逻辑为：
1. 设计者角色从开发固定界面转为定义Agent的合法决策空间，无需预先绑定分析流程与视图组件
2. Agent可在运行时根据用户自然语言指令，自主选择分析方法、生成适配的可视化视图、协调多视图联动逻辑
3. 配套覆盖决策合规性、结果可解释性、故障可追溯性的Agent行为评估框架
### 结果
给出了基于现有Coding Agent能力的可落地方案，验证了该范式可将自定义分析需求的交付周期从天级缩短到分钟级，大幅降低可视化系统的迭代成本
