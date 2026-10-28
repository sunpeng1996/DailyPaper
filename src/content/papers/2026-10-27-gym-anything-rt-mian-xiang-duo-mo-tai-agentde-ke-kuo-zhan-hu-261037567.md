---
title: 'Gym-Anything-RT: Scaling Real-Time Environments for Vision-Language Agents'
title_zh: Gym-Anything-RT：面向多模态Agent的可扩展实时交互评测框架
authors:
- Pranjal Aggarwal
- Sean Welleck
affiliations:
- Carnegie Mellon University
arxiv_id: '2610.37567'
url: https://arxiv.org/abs/2610.37567
pdf_url: https://arxiv.org/pdf/2610.37567
published: '2026-10-27'
collected: '2026-10-28'
category: Agent
direction: 多模态Agent · 实时交互能力评测
tags:
- Vision-Language Agent
- Real-Time Interaction
- Agent Benchmark
- Automated Environment Generation
- Agent Evaluation
one_liner: 推出可控实时交互评测环境自动生成框架，量化多模态Agent实时交互能力短板
practical_value: '- 开发实时交互类Agent（如电商直播导购Agent、实时互动广告Agent）时，可参考文中思路：将低延迟要求的感知、动作执行逻辑下沉到自动化脚本层，抵消大模型推理延迟的影响

  - 搭建Agent评测体系时，可复用「同一任务多维度控制变量」设计：同一任务下分别控制实时性、难度、交互模式，精准定位能力短板，避免把任务难度问题误判为实时性问题

  - 高动态场景（如实时搜索推荐、动态广告投放）的模型选型中，可参考结论：大模型高算力消耗的深度推理模式在实时场景下收益极低，应优先优化推理速度而非推理深度'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前多模态Agent在数学、桌面操作等环境等待Agent推理的非实时场景已取得明显进展，但在需要实时交互的场景（如动态界面交互、实体设备操作）表现未知，现有评测要么任务耦合多种能力无法定位失败原因，要么没有控制实时性变量的设计，亟需可精准控制变量的评测框架，量化Agent的实时交互能力短板。

### 方法关键点
- 定义6项实时交互核心能力维度：3D视觉理解、时序推理、规划、陌生界面探索等，覆盖实时交互核心需求
- 搭建Creator-Auditor多Agent自动生成流水线：生成Agent编写视觉小游戏代码、输出Oracle解法，审计Agent验证任务可解性、无作弊捷径，自动生成可控难度、可控交互模式的评测任务
- 支持同一任务多维度控制：可切换实时/非实时模式、调整环境速度（1×到64×减速、暂停）、5档难度、2种交互模式，实现精准控制变量评测

### 关键实验
生成100个实时小游戏及对应的非实时版本，评测多款前沿闭源、开源模型：
- GPT-6 Astra (xHigh) 实时模式通过率仅9.0%，非实时模式提升至66.0%，暂停环境后通过率进一步提升至75.0%，64倍减速时通过率达57.0%
- 允许Agent编写代码执行感知和动作时，Astra的实时通过率从9.0%提升至31.0%
- 人类在20个随机抽样任务上通过率达45.0%，远高于当前最强模型的9.0%

### 核心结论
当前前沿多模态Agent的实时交互最大瓶颈是推理速度，而非任务理解能力，通过代码下沉低延迟逻辑可部分抵消延迟缺陷
