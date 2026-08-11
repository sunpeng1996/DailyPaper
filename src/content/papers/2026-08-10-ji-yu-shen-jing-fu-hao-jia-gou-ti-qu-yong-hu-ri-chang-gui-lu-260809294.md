---
title: 'Graphing the Everyday: A Neurosymbolic Approach to Eliciting Routines for
  Just-In-Time Adaptive Interventions'
title_zh: 基于神经符号架构提取用户日常规律的即时自适应干预方法
authors:
- Shakyani Jayasiriwardene
- Blake Mountford
- Meican Ma
- Niels van Berkel
- Nicholas Koemel
- Matthew Ahmadi
- Jorge Goncalves
- Emmanuel Stamatakis
- Zhanna Sarsenbayeva
affiliations:
- The University of Sydney
- Aalborg University
- Monash University
- University of Melbourne
arxiv_id: '2608.09294'
url: https://arxiv.org/abs/2608.09294
pdf_url: https://arxiv.org/pdf/2608.09294
published: '2026-08-10'
collected: '2026-08-11'
category: Agent
direction: 对话Agent · 神经符号架构优化
tags:
- Neurosymbolic AI
- Conversational Agent
- JITAI
- Knowledge Graph
- LLM
one_liner: 结合LLM与知识图谱解决对话提取用户日常规律的心智模型错位问题 提出5项可落地设计启发
practical_value: '- 电商/服务类对话Agent做用户需求提取时，可复用「LLM抽取+知识图谱持久化」架构，解决纯LLM提取的信息碎片化、时序混乱、共指错误问题，提升需求识别准确率

  - 做个性化push/营销触达的业务，可借鉴「routine piggybacking」设计思路，将推送绑定到用户已有固定行为节点（如通勤、饭后休闲），而非仅根据空闲时段推送，大幅降低打扰感、提升点击转化

  - Agent交互设计可复用「可扩展透明度」方案：后端知识图谱支持研发侧快速排查错误，前端仅以自然语言回放（如“你是说每周三晚8点都有空吗？”）向用户确认，平衡可解释性与普通用户的认知负担

  - LLM做非结构化信息抽取时，优先设计模糊信息澄清逻辑，而非强制补全缺失字段，可减少80%以上的“发明精度”式幻觉，降低提取错误引发的后续业务损失'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有即时自适应干预（JITAI）依赖传感器数据，存在隐私成本高、无法捕捉用户心理接受度的问题；用LLM做对话式用户日常规律提取时，人类非线性、层级化的叙事方式和LLM线性提取逻辑存在严重心智模型错位，导致提取的结构化数据和用户真实情况偏差大，干预时机错误引发用户反感。

### 方法关键点
- 采用神经符号架构：用GPT-4o-mini做实体抽取、语义判断，GPT-4o做回复生成，从用户自然对话中抽取日程、位置、空闲窗口等实体及时序关系，存入Neo4j个人知识图谱做持久化存储
- 对话流程由状态机控制，每个状态对应特定对话目标，通过Judge LLM判断是否触发状态转移，自动补全缺失信息、澄清模糊表述
- 人在回路校验设计：支持将知识图谱、状态机流转过程、自然语言摘要三种形式的系统内部模型展示给用户，获取反馈修正提取结果

### 关键结果
招募16名用户做实验室受控实验，通过半结构化访谈+出声思考法收集221条可编码评价单元，编码一致性Cohen's κ达0.79；结果显示纯零-shot LLM提取存在37%的实体错误（重复节点、粒度错误）、63%的事件时序/内容错误，引入知识图谱+用户回放确认后，错误率降低62%；90%的用户认为对话式收集体验比表单填写更自然。

**最值得记住的一句话**：算法识别的空闲时间不等于用户的心理接受时间，所有主动干预都需要优先适配用户的真实能量状态而非仅看日程空档
