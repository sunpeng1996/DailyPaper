---
title: Supporting Reflection in LLM-based Exploratory Search
title_zh: 面向大语言模型探索式搜索的反思能力支持系统
authors:
- Giulia Di Fede
- Salvatore Andolina
affiliations:
- Politecnico di Milano
arxiv_id: '2607.11810'
url: https://arxiv.org/abs/2607.11810
pdf_url: https://arxiv.org/pdf/2607.11810
published: '2026-07-13'
collected: '2026-07-14'
category: LLM
direction: LLM探索式搜索 · 元认知交互设计
tags:
- Exploratory Search
- Metacognition
- LLM
- Human-AI Interaction
- Information Retrieval
one_liner: 提出TrailLM系统，通过探索路径追溯与子目标管理增强LLM探索式搜索的用户反思能力
practical_value: '- 电商/内容平台的模糊搜索场景（如用户找小众穿搭、冷门旅游攻略）可借鉴子目标自动拆分+路径追溯设计，降低用户探索门槛，减少搜索跳出率

  - 自研Agent搜索工具的交互层可复用TrailLM的历史会话tagging+子目标对齐逻辑，提升长任务搜索的可控性，降低用户认知负荷

  - 面向B端的行业搜索产品（如电商商家选品调研、内容创作者选题工具）可加入探索路径可视化功能，帮助用户复盘调研过程、避免信息遗漏'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有LLM探索式搜索优先输出快速答案，跳过了用户在陌生领域探索时必需的迭代意义建构过程，容易让用户被动接受信息、缺乏对搜索过程的批判性反思，进而提升接收错误、有偏见信息的风险，也难以匹配用户动态演化的模糊搜索需求。

### 方法关键点
- 核心设计围绕三大目标：子目标对齐监控、新兴探索路径发现、信息意义建构支撑，对齐用户探索过程的元认知需求
- 界面分为主对话区+右侧固定边栏：主区支持正常LLM问答，自动从回答中提取可选探索子目标，用户点击即可加入子目标列表
- 边栏持久展示当前总探索目标、子目标列表、交互历史trail卡片：用户可手动编辑目标/子目标，给每张历史交互卡片打子目标标签，支持按子目标筛选历史，点击卡片即可回溯到对应对话节点

### 关键结果
目前仅完成原型开发，尚未发布正式实验结果，后续计划开展受控用户研究验证设计效果。

### 核心洞见
LLM辅助搜索不能只追求答案获取效率，对齐用户的意义建构流程、保留用户反思的空间，才能真正提升长周期探索任务的整体体验。
