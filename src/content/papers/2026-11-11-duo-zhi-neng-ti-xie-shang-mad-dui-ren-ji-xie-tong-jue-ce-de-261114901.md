---
title: Understanding the Effects of Multi-Agent Deliberation for Human-AI Decision-Making
title_zh: 多智能体协商（MAD）对人机协同决策的作用效果与设计机制研究
authors:
- Harry Yizhou Tian
- Ming Yin
affiliations:
- Purdue University, USA
arxiv_id: '2611.14901'
url: https://arxiv.org/abs/2611.14901
pdf_url: https://arxiv.org/pdf/2611.14901
published: '2026-11-11'
collected: '2026-11-13'
category: Agent
direction: Agent 人机协同决策优化
tags:
- Multi-Agent
- Human-AI Collaboration
- Decision Support
- LLM
- User Study
one_liner: 通过两类决策任务用户实验，拆解多智能体协商的收益来源与设计参数的实际效果
practical_value: '- 做电商/广告内容审核、营销文案fact-check类Agent决策辅助系统时，优先落地多轮交互而非直接叠加多个Agent，单Agent性能存在明确瓶颈时再加第二个异源LLM提升效果

  - MAD设计阶段不要盲目添加devil''s advocate（唱反调）角色，会拉低整体决策准确率同时提升用户挫败感，仅高风险需强纠错场景可权衡使用

  - 涉及人参与的MAD系统，优先让用户做被动审阅者而非主动参与者，可在不显著降低准确率的前提下大幅降低用户认知负担

  - 多Agent输出存在分歧时，让Agent先完成多轮协商再输出给用户，可降低用户困惑度、提升对AI辅助的感知有用性'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有MAD（多LLM结构化协商）在纯AI任务上表现优异，但能否提升人机协同决策的准确率、核心收益来源与最优设计参数均无实证支撑，常规单AI单次输出的决策辅助范式瓶颈明显，亟需明确MAD在人机协同场景的落地价值与设计规范。

### 方法关键点
- 选取两类有明确真值的决策任务：LLM响应错误校验（ReaLMistake数据集）、政治言论事实核查（自定义标注数据集）
- 拆解MAD两个核心维度：多AI、多轮交互，对比4种辅助范式：单AI单轮、单AI多轮、双AI独立静态输出、MAD
- 控制两类设计变量：3种AI人设（无预设人设、领域专家、devil's advocate）、2种用户参与度（主动参与协商、被动审阅协商记录）
- 累计招募818名用户完成对照实验，以决策准确率、用户主观体验为核心评估指标

### 关键实验结果
- MAD对比单AI单轮辅助，两类任务准确率分别提升12.8pp（ReaLMistake）、9.9pp（事实核查），对比双AI静态输出分别提升11.3pp、20pp
- 收益核心来源是多轮交互，第二AI仅在单AI性能不足（ReaLMistake单AI准确率低）时贡献额外收益
- Devil's advocate人设使两类任务准确率分别下降10.1pp、5.4pp，同时显著提升用户挫败感；用户主动参与仅在ReaLMistake任务提升7.9pp准确率，但代价是挫败感上升

**最值得记住的一句话：** 多智能体协商的核心价值来自多轮交互而非多AI堆叠，设计阶段需优先保障交互效率，避免盲目叠加角色或强制用户参与。
