---
title: Discovery-Driven Integration of Disjoint Tables via Text
title_zh: 基于文本的无关联表发现驱动集成方法
authors:
- Md Ataur Rahman
- Dimitris Sacharidis
- Oscar Romero
- Sergi Nadal
affiliations:
- UPC, BarcelonaTech
- Université Libre de Bruxelles
arxiv_id: '2609.26658'
url: https://arxiv.org/abs/2609.26658
pdf_url: https://arxiv.org/pdf/2609.26658
published: '2026-09-22'
collected: '2026-09-23'
category: Other
direction: 异构数据湖 · 文本介导跨表关联发现
tags:
- DataIntegration
- ContrastiveLearning
- CrossAttention
- UnsupervisedLearning
- DataLake
one_liner: 双向交叉注意力架构LOKI实现无监督文本介导跨表关联发现，成本比直接Prompt低40倍
practical_value: '- 电商多源异构数据（用户行为表、商品表、评论/客服文本）关联场景，可复用LOKI的行-文本细粒度无监督对齐方法，无需人工标注关联关系

  - 跨模态数据对齐场景可复用全局对比学习替代LLM直接Prompt的思路，最高降低97.5%的API调用成本

  - 可解释的细粒度关联路径能力可迁移到推荐归因场景，用于打通用户行为数据与评论/客服文本的归因链路'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
数据湖内大量异构结构化表无显式可Join属性，现有多模态发现方法仅支持粗粒度列-文本关联，集成系统依赖预定义的行-文本链接、Schema或查询，无法落地无监督的细粒度行级跨表关联。
### 方法关键点
1. 任务被形式化为文本介导的Join路径发现任务，目标是通过文本为无关联表建立行级关联
2. 横向双向交叉注意力架构LOKI可学习表行与文本句子的上下文表示
3. 采用全局表-文本对比学习目标，无需局部显式监督即可挖掘细粒度行-句子关联
4. 隐式关联可自动转化为可解释Join路径，最终生成带句子级来源标注的类型化集成表
### 关键结果
在真实基准数据集上Macro类型对精度达0.982，效果优于现有SOTA多模态数据发现方法，LLM API成本仅为直接Prompt的1/40。
