---
title: 'Plans Work in Mysterious Ways: Evaluating a Plan Mode for Spreadsheet Agents'
title_zh: 电子表格Agent规划模式的交互效果与用户体验评估
authors:
- Aayush Kumar
- Avik Dutta
- Sumit Gulwani
- Gustavo Soares
- Advait Sarkar
- Emerson Murphy-Hill
affiliations:
- Microsoft
arxiv_id: '2607.23670'
url: https://arxiv.org/abs/2607.23670
pdf_url: https://arxiv.org/pdf/2607.23670
published: '2026-07-26'
collected: '2026-07-28'
category: Agent
direction: 端用户编程Agent · 交互模式设计评估
tags:
- Spreadsheet Agent
- Human-AI Collaboration
- Plan Mode
- End-User Programming
- User Study
one_liner: 通过24人组内对照实验验证电子表格Agent规划模式可降低迭代成本提升用户协作体验
practical_value: '- 面向电商运营、商家的非专业用户Agent（如报表生成、活动策划Agent）可加入Plan Mode，先通过澄清问题对齐需求再执行，比事后迭代改结果省35%的token成本，减少用户返工

  - Plan Mode可复用3个低门槛设计：生成≤7步的粗粒度非技术化计划、计划实时展示执行状态、支持局部执行，即便用户很少编辑计划，可视化执行路径也能提升用户控制感和满意度

  - 可根据场景自适应触发Plan Mode：创建类、长周期复杂任务默认触发，对于习惯迭代修改结果的高频用户默认使用直接执行模式，兼顾不同用户的交互习惯'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
Plan Mode 已是专业编程Agent的标配功能，但电子表格这类端用户编程场景的用户习惯迭代式工作、不关心技术实现正确性，前置规划是否适配这类场景的用户 workflow 缺乏实证验证，需明确其实际业务价值。
### 方法关键点
- 架构上采用独立的Plan Agent和执行Agent分离设计，避免跨阶段工具滥用，基座采用Claude Sonnet 4.5
- Plan Mode核心设计：可编辑的持久化计划面板、支持局部执行、动态更新步骤执行状态、规划阶段只读访问表格、用户显式切换模式
- 规划流程设计：先发起澄清问题（不重复追问，未回答的问题自动做假设并在计划中披露），生成不超过7步的粗粒度非技术计划，用户确认后再执行
### 关键实验结果
24人组内对照实验，对比无规划的直接执行Act Mode，覆盖创建类（预算/日程）、分析类（度假选址/电影选品）两类任务：
1. 两种模式最终产出的表格功能、质量无显著差异
2. Plan Mode下37%的需求来自事前澄清，事后迭代需求占比仅10%，远低于Act Mode的35%迭代占比，LLM token消耗降低35%（11k vs 17k）
3. 70%+用户在创意支持、人机协作维度更偏好Plan Mode，创建类任务的偏好度显著高于分析类任务
### 核心结论
即便用户几乎不使用编辑计划、局部执行等高级功能，可视化的计划路径本身就能给用户带来更强的控制感，提升人机协作体验，不需要过度纠结功能的实际使用率。
