---
title: 'Comparing Human Role-Players and LLM-Simulated Clients in Online Counselling
  Training: An Analysis of Counselling Patterns'
title_zh: 在线咨询培训中人类扮演者与LLM模拟来访者的咨询模式对比
authors:
- Eric Rudolph
- Philipp Steigerwald
- Jens Albrecht
affiliations:
- Technische Hochschule Nürnberg Georg Simon Ohm
arxiv_id: '2610.40563'
url: https://arxiv.org/abs/2610.40563
pdf_url: https://arxiv.org/pdf/2610.40563
published: '2026-10-29'
collected: '2026-11-01'
category: LLM
direction: LLM角色扮演 · 虚拟用户模拟
tags:
- LLM
- Role-Play
- User Simulation
- Conversational AI
- Behavior Analysis
one_liner: 对比真人与Mixtral 8x7b模拟的咨询来访者，验证LLM角色扮演用于职业培训的可行性
practical_value: '- 可复用4-bit量化轻量MoE模型（如Mixtral 8x7b）模拟用户角色，落地电商客服/销售话术培训场景，降低真人陪练的人力与协调成本

  - 句子级细粒度对话行为模式标注方法，可迁移到电商客服对话质量评估、用户隐性偏好识别的标注体系搭建

  - LLM模拟用户的行为一致性验证框架，可复用在推荐/搜索系统的用户仿真测试环节，替代部分真人AB测降低实验成本'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
传统咨询培训依赖真人角色扮演，存在日程协调成本高、角色稳定性差、场景一致性难以保障等痛点，亟需低成本可复用的虚拟角色方案替代部分真人陪练。
### 方法关键点
1. 先后采集两组对话数据：新手咨询师与真人peer扮演的来访者交互、新手咨询师与4-bit量化Mixtral 8x7b模拟的来访者交互；
2. 基于句子级咨询沟通模式标注体系，对比两类交互下的对话动态与咨询师行为差异。
### 关键结果
两类场景下的咨询应用模式同时存在共性与差异，LLM模拟来访者可有效支撑咨询能力培训，当前方案仍需优化角色一致性与对话真实度。
