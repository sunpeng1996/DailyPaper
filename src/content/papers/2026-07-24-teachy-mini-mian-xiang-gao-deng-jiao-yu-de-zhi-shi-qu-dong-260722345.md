---
title: 'Teachy Mini: Development and Preliminary Evaluation of a Knowledge-Based Generative
  Social Robot for Higher Education'
title_zh: Teachy Mini：面向高等教育的知识驱动生成式社交机器人开发与初评
authors:
- Stephan Vonschallen
- Karim Kaufmann
- Dominique Oberle
- Friederike Eyssel
- Theresa Schmiedel
affiliations:
- Institute of Information Systems, Zurich University of Applied Sciences, Switzerland
- Center for Cognitive Interaction Technology, Bielefeld University, Germany
arxiv_id: '2607.22345'
url: https://arxiv.org/abs/2607.22345
pdf_url: https://arxiv.org/pdf/2607.22345
published: '2026-07-24'
collected: '2026-07-27'
category: Agent
direction: 教育场景智能Agent 负责任行为设计
tags:
- Generative Social Robot
- RAG
- Prompt Orchestration
- Knowledge-Based Design
- Agent Evaluation
one_liner: 结合系统提示、RAG与状态化提示编排实现知识驱动设计，打造高等教育场景负责任的生成式辅导社交机器人
practical_value: '- 可控输出场景可复用「知识约束+RAG+状态化prompt编排」组合方案，降低大模型幻觉，提升输出合规性，可直接迁移到电商商品文案生成、智能导购回复等场景

  - 交互类Agent（如电商客服、直播助理）的设计可参考KBD原则，在对齐业务规范的同时优化个性化引导、情感支持等能力，提升用户感知体验

  - Agent效果评估可复用「主观感知维度+业务核心指标+用户偏好控制」的校验框架，平衡合规性、体验与业务目标'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
大模型驱动的生成式社交机器人（GSR）可实现个性化交互，但存在幻觉、透明度不足、错误引导用户等风险，现有方案缺乏可落地的负责任行为设计落地方案。
### 方法关键点
在Reachy Mini机器人平台落地知识驱动设计（KBD）要求，通过三类技术实现：系统prompt明确行为规则，RAG确保输出基于给定权威材料，状态化prompt编排跟踪用户交互上下文实现个性化引导，最终打造Teachy Mini辅导系统。
### 关键结果
24名用户参与对照实验显示：Teachy Mini的负责任辅导行为感知得分显著高于无KBD的对照组；个性化、材料 grounded 解释、引导式提问、情感支持等能力的一致性比对照组更高；控制用户偏好变量时，KBD对客观任务收益有显著正向影响。
