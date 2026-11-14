---
title: How Do People Debug Complex SQL Queries With LLMs? A Qualitative Study
title_zh: 用户使用大语言模型调试复杂SQL查询的行为定性研究
authors:
- Nicole Sullivan
- Ella Cao
- Leilani Battle
- Magdalena Balazinska
affiliations:
- University of Washington, USA
arxiv_id: '2611.16108'
url: https://arxiv.org/abs/2611.16108
pdf_url: https://arxiv.org/pdf/2611.16108
published: '2026-11-11'
collected: '2026-11-14'
category: LLM
direction: LLM应用 · 用户行为定性研究
tags:
- LLM
- SQL Debugging
- User Study
- Human-AI Collaboration
- Qualitative Analysis
one_liner: 通过16人用户调研揭示LLM辅助SQL调试的用户行为模式，提出三阶段推理模型与工具优化方向
practical_value: '- 开发面向分析师/算法工程师的SQL辅助Agent时，可预设TA、参谋等多角色选项，匹配不同用户的任务委托习惯

  - Agent交互设计需支持灵活的上下文控制，允许用户主动屏蔽部分上下文，满足局部问题排查需求

  - 工具自动化档位需覆盖从全手动到全自动的梯度选项，避免高自动化降低中高级用户使用意愿'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
当前LLM已被广泛用于SQL生成与调试场景，但行业缺乏对用户使用LLM调试SQL的行为逻辑的基础认知，无法针对性优化相关辅助工具。

### 方法关键点
招募16名不同SQL水平的参与者（8名初学者、4名中级、4名高级），对比有无LLM支持下的复杂SQL调试行为，结合定性分析提炼用户推理模式与交互习惯。

### 关键结果
1. 基准测试显示主流LLM已具备合格的SQL调试能力；
2. 用户对LLM普遍信任，但任务委托策略差异极大，可归纳为三状态SQL推理模型；
3. 用户普遍会主动为LLM分配助教、参谋等协作角色，通过隐藏上下文控制LLM的作用边界；
4. 明确后续LLM调试工具需支持角色预设、上下文管理、梯度自动化三个核心优化方向。
