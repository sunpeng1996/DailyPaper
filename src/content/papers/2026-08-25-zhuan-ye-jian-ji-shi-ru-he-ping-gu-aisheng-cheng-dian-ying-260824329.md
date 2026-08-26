---
title: How Do Professional Editors Evaluate the Editing Quality of AI-Generated Cinematic
  Video Ads?
title_zh: 专业剪辑师如何评估AI生成电影感视频广告的剪辑质量
authors:
- Po-Ming Law
- Weizhi Li
- Arpit Narechania
affiliations:
- Adaptive Machines, Inc
- The Hong Kong University of Science and Technology
arxiv_id: '2608.24329'
url: https://arxiv.org/abs/2608.24329
pdf_url: https://arxiv.org/pdf/2608.24329
published: '2026-08-25'
collected: '2026-08-26'
category: Eval
direction: AI生成广告 · 剪辑质量评估
tags:
- Video Ad Generation
- Human Evaluation
- Editing Quality
- LLM Planning
- Multimodal Content
one_liner: 通过专业剪辑师评测总结AI生成电影感视频广告剪辑质量的六大评估维度
practical_value: '- 做短视频信息流广告AI生成系统时，可直接复用本文提出的6个剪辑质量维度作为评测指标，替代模糊的主观打分，快速对齐专业内容生产标准，减少投放审核返工

  - 可参考「LLM先生成分镜计划+视频模型渲染」的两阶段生成架构，降低端到端生成视频广告的内容不可控风险，适配电商品宣、品牌种草等场景的批量广告生产需求

  - 专业从业者的定向评测反馈可直接作为训练数据，对生成模型做SFT或RLHF，快速提升AI生成内容的专业度，降低人力后期剪辑成本'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
当前AI已可自动生成带电影感剪辑的社交平台短视频广告，但缺乏细粒度的剪辑质量评估框架，无法对齐专业内容生产标准，难以落地到广告投放场景。
### 方法关键点
1. 对语料中的社交媒体广告做结构化分析，拆解时长、分镜结构、音视元素、剪辑技巧，设计**LLM生成分镜计划→视频模型渲染**的两阶段生成pipeline
2. 面向35个真实品牌生成70条电影感广告，邀请专业剪辑师对剪辑决策做系统性点评
### 关键结果
从专业点评中提炼出6个可落地的剪辑质量评估维度：叙事推进、音视频协调与音效设计、视觉构图与图形、镜头连续性、信息与品牌一致性、时间节奏与pacing，可直接指导AI生成优化、人工/自动化评测。
