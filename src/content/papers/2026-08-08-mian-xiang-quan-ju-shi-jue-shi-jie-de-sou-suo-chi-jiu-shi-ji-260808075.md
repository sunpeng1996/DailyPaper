---
title: 'Search over the Visual World: Persistent Visual Memory, Layered Indexes, and
  Source-Grounded Evidence'
title_zh: 面向全局视觉世界的搜索：持久视觉记忆、分层索引与源数据证据链
authors:
- Sankalp Nagaonkar
- Rohit Garg
- Ankit Raj
- Ashish Choithani
- Ashutosh Trivedi
affiliations:
- VideoDB
arxiv_id: '2608.08075'
url: https://arxiv.org/abs/2608.08075
pdf_url: https://arxiv.org/pdf/2608.08075
published: '2026-08-08'
collected: '2026-08-11'
category: Multimodal
direction: 多模态检索 · 视觉记忆系统设计
tags:
- Video Retrieval
- Visual Memory
- Multimodal Search
- System Design
- Retrieval Infrastructure
one_liner: 提出面向持续流入视觉数据的搜索系统架构与VDB格式，检索召回优于商用视频原生引擎
practical_value: '- 直播/短视频电商多模态检索场景可借鉴分层索引+多时间粒度语义拆分设计，避免全量回放视频，降低检索时延

  - Agent 端视觉记忆模块可复用「记忆-上下文-证据」三层拆分框架，保证结果可溯源到原始视觉片段，提升可解释性

  - 无需盲目堆叠视频专属预训练大模型，通过优化检索系统架构、组合通用组件也能拿到更高召回效果，降低落地成本'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有视频检索系统针对固定语料设计，仅返回文件或时间戳，无法适配Agent面对的持续流入的摄像头、直播、存档视觉数据场景，存在需全量回放筛选上下文、结果无溯源证据等痛点。
### 方法关键点
1. 提出视觉世界搜索的形式化模型，拆分「记忆（全量留存数据）-上下文（任务筛选数据）-证据（溯源原始片段）」三层逻辑，基于分析器定义场景、持久化理解产物、共享时间轴多场景空间、能力声明分层索引搭建系统框架；
2. 落地生产可用的VDB数据格式，支持规划检索、状态化排查、直接访问、证据链合成等多类搜索接口，模型无关，直播流为一等公民，分割、采样、嵌入、排序等环节均可自定义配置。
### 关键结果
在4个公开数据集共9800+查询的语义检索对比中，通用组件搭建的VDB流水线Macro Recall@1/3/10达73.09%/83.39%/91.20%，优于商用视频原生引擎的65.75%/77.13%/89.10%，仅Recall@50略低0.35pct。
