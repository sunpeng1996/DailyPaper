---
title: 'Cleo: A Transparent and Controllable Chatbot for Conversational Commerce'
title_zh: Cleo：面向对话式电商的透明可控聊天机器人
authors:
- Kevin Schott
- Jan Lattenkamp
- Daniel Hienert
- Dagmar Kern
affiliations:
- GESIS – Leibniz Institute for the Social Sciences
arxiv_id: '2608.06068'
url: https://arxiv.org/abs/2608.06068
pdf_url: https://arxiv.org/pdf/2608.06068
published: '2026-08-06'
collected: '2026-08-07'
category: Agent
direction: Agent 对话式电商透明推荐系统
tags:
- Conversational Commerce
- Hybrid LLM
- Explainable Recommendation
- Transparent Ranking
- RAG
one_liner: 提出混合架构的对话式电商推荐Agent，分离排序与生成，实现可解释低幻觉的购物辅助
practical_value: '- 可直接复用「确定性排序模块+LLM生成模块解耦」的混合架构，既保留对话流畅性，又从根源避免LLM干预排序逻辑导致的结果不可控、幻觉问题

  - 用户需求抽取环节可落地「小样本prompt抽取+三层后处理校验」流程：通过单位转换、类目对齐、非法值过滤，确保自然语言需求到结构化属性的映射准确率

  - 可解释性设计可直接复用：将排序的属性损失值、过滤规则直接暴露给用户，相比纯自然语言解释可信度更高，能显著提升电商用户决策信任度

  - 多商品对比功能可采用「规则计算属性差异+LLM格式化为自然语言」的方案，既保证参数准确无幻觉，又降低用户对比商品的认知负荷'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前对话式电商推荐要么是传统分面搜索缺乏交互流畅性，要么是端到端LLM推荐存在黑箱、幻觉、过度说服等问题，用户难以理解排序逻辑，也不信任推荐结果；多商品对比需要手动核对参数，认知负荷极高，亟需兼顾流畅交互、可控可信、决策支持的对话式推荐方案。

### 方法关键点
- 混合分层架构：管理层负责对话状态管理，功能层分离确定性Ranker和LLM生成模块，排序逻辑完全独立不受LLM影响
- 需求抽取流程：用小样本prompt将用户自然语言需求映射为结构化JSON属性，再通过单位转换、类目对齐、非法值过滤三层后处理修正抽取错误
- 可解释排序机制：先做类目过滤（品牌、GPU等硬性要求），再计算价格、内存、存储、屏幕尺寸四个维度的数值损失，按总损失升序排序，所有损失值可查询可解释
- 生成约束：所有LLM输出（回复、商品亮点、多品对比）全部基于RAG grounded到商品库参数和用户需求，避免幻觉和过度说服内容

### 系统与实验
当前为演示系统，基于3638款笔记本的结构化参数构建，支持文本/语音交互、实时重排序、属性级解释、最多3款商品的AI对比功能。后续计划开展三组用户实验：混合架构vs纯LLMvs传统分面搜索的效果对比、解释功能对用户信任和决策效率的影响、用户对引导与自主权的偏好。

### 核心结论
将确定性决策逻辑与LLM生成能力解耦，是平衡对话式推荐的交互流畅性与可控可信性的核心路径。
