---
title: 'Prompt Coach: An Empirical Evaluation of an Agentic Tutor for Learning Prompt
  Engineering in Software Development'
title_zh: Prompt Coach：面向开发人员提示工程学习的智能代理辅导系统实证评估
authors:
- Rohit Mehra
- Kapil Singi
- Vikrant Kaulgud
- Vibhu Saujanya Sharma
- Swapnajeet Gon Choudhury
- Swati Sharma
- Adam P. Burden
- Majd Sakr
affiliations:
- Accenture Labs, India
- Accenture, India
- Accenture, USA
arxiv_id: '2607.06074'
url: https://arxiv.org/abs/2607.06074
pdf_url: https://arxiv.org/pdf/2607.06074
published: '2026-07-07'
collected: '2026-07-09'
category: Agent
direction: Agent 提示工程智能辅导
tags:
- Agentic Tutor
- Prompt Engineering
- Empirical Study
- IDE Integration
- LLM-based Education
one_liner: 嵌入IDE的苏格拉底式引导代理辅导系统，可快速提升开发人员提示工程能力
practical_value: '- 可复用苏格拉底式引导框架，在内部LLM开发工具中嵌入流程内的prompt质量自动评估与自助修正提示，降低团队prompt工程门槛

  - 多维度prompt质量评估逻辑可迁移到推荐系统的query改写、RAG召回query优化场景，自动识别低质量query并引导用户补全信息

  - 轻量化短周期（60分钟）的干预式能力提升实验设计可复用，用于验证新算法工具对业务团队的效能提升效果'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
Prompt工程已成为软件开发核心技能，但传统教学方案难以适配其动态、交互式、强上下文依赖的特性，开发人员普遍缺乏高效的轻量化学习路径。
### 方法关键点
嵌入IDE的Agent辅导系统Prompt Coach，基于开发者代码库与目标LLM行为特征，从多维度评估prompt质量，通过苏格拉底式提问引导开发者自主修正prompt，全程融入开发工作流无需切换场景。
### 关键结果数字
15名专业开发者仅经过1次60分钟的使用，prompt质量得到统计意义上的显著提升，其中开发者普遍忽略的维度提升幅度最大；所有参与者均认可其对prompt能力的提升作用，信任度与采用意愿均处于较高水平
