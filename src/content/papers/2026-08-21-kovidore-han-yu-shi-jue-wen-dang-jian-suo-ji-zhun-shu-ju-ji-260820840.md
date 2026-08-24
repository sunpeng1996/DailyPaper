---
title: 'KoViDoRe: Korean Visual Document Retrieval'
title_zh: KoViDoRe：韩语视觉文档检索基准数据集
authors:
- Yongbin Choi
- Yongwoo Song
- Mujeen Sung
affiliations:
- Kyung Hee University
arxiv_id: '2608.20840'
url: https://arxiv.org/abs/2608.20840
pdf_url: https://arxiv.org/pdf/2608.20840
published: '2026-08-21'
collected: '2026-08-24'
category: RAG
direction: 多模态RAG · 视觉文档检索基准
tags:
- Multimodal Retrieval
- RAG
- Benchmark
- Visual Document
- Dataset
one_liner: 发布韩语复杂版式多页视觉文档检索基准及配套公开训练数据集
practical_value: '- 可复用其多阶段数据构造pipeline：结构化文档解析+摘要/上下文双策略合成查询+人工校验相关性，用于电商商品详情页、商家资质等多模态文档的检索数据集搭建

  - 其覆盖跨页证据聚合、复杂版式的评测设计思路，可迁移到自研多模态召回/RAG系统的业务评测集构建，更贴近真实使用场景

  - 面向韩语市场的跨境电商可直接复用配套公开训练集，优化韩语商品文档检索、智能客服RAG问答的模型效果'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有多模态文档检索基准以英文为核心，韩语相关资源仅支持单页检索，无法覆盖包含表格/图表/多栏布局、需跨页聚合证据的真实场景。
### 方法关键点
1. 构建KoViDoRe基准，样本取自公开韩语多版式文档，覆盖复杂结构化元素与多页场景；
2. 采用多阶段数据处理pipeline：结构化文档解析、摘要/上下文双策略合成查询、人工校验完成相关性映射；
3. 同步开源大规模训练集Ko-VDR Train Public，支撑韩语视觉文档检索模型定制开发。
### 关键结果
对主流多模态检索模型的评测显示，现有模型在韩语视觉文档检索任务上表现不佳，尤其在结构化内容检索、多类型查询场景下存在明显性能缺口。
