---
title: The Past and Future of AI Scientists
title_zh: AI科学家的发展历程与未来展望
authors:
- Ross D. King
affiliations:
- University of Cambridge
- Chalmers University of Technology
arxiv_id: '2608.14407'
url: https://arxiv.org/abs/2608.14407
pdf_url: https://arxiv.org/pdf/2608.14407
published: '2026-08-14'
collected: '2026-08-17'
category: Agent
direction: 科学智能Agent 架构设计与分级标准
tags:
- AIScientist
- ScientificAgent
- AutonomousSystem
- NeuroSymbolicAI
- SelfDrivingLab
one_liner: 系统梳理AI科学家的演进脉络、分类体系与自主等级，给出通用技术架构与发展路线
practical_value: '- 6级科学自主等级框架可直接复用在电商/广告Agent的能力分级设计，从工具级（仅执行指定计算）到全自主级（独立识别业务问题并落地优化）的分层迭代路标可大幅降低Agent落地的试错成本

  - 神经符号+概率的混合架构可迁移到生成式推荐/搜索系统，用LLM做语义理解、召回/排序策略假设生成，用知识图谱/规则引擎做结果校验，用概率体系表示用户偏好不确定性，可大幅减少LLM幻觉带来的bad
  case

  - 科研闭环的模块设计可复用在电商业务的自主迭代Agent，打通「业务问题识别→策略假设生成→AB实验设计→结果归因分析→策略迭代」全链路，降低运营/算法团队的人工重复劳动'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
全球面临气候变化、粮食安全、耐药性等重大公共挑战，传统人类科研效率已无法匹配需求，AI是唯一可实现科研生产力量级提升的可行路径；当前科研AI的单点组件（预测模型、LLM工具、实验室机器人等）已全部验证可行，核心瓶颈从单点能力突破转向跨模块系统整合。

### 方法关键点
- 明确四类科学AI的边界：仅做单点预测的科学AI、仅完成计算闭环的LLM agent科学系统、做物理实验闭环的自动驾驶实验室、打通全科研链路的集成AI科学家
- 提出0-5级科学自主等级框架，明确不同等级下人类的参与度边界，要求将自主度与能力、通用性、可靠性、风险等维度分开评估
- 给出联邦式模块化AI科学家架构，采用神经符号+概率的混合设计，覆盖科学记忆、文献接口、假设生成、逻辑/概率推理、实验设计、设备控制、溯源审计、安全管控等核心模块

### 关键结果
2009年推出的Adam是首个实现自主全新科学发现的系统，2015年的Eve奠定了当前自动驾驶实验室的标准架构，面向2050年实现诺奖级自主科学发现的Nobel Turing Challenge当前进度超前于计划。

### 核心结论
任何科研链路的断点都会让系统退化为工具，真正的自主AI科学家必须打通「知识→问题→假设→实验→知识迭代」的完整闭环。
