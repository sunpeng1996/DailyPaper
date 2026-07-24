---
title: 'AutoJourn: Multi-Perspective Summarisation, Bias Detection and Bias Neutralisation
  for LLM-Generated News in Automated Journalism'
title_zh: AutoJourn：面向自动化新闻的多视角摘要、偏见检测与消除系统
authors:
- Himel Ghosh
- Ahmed Mosharafa
- Georg Groh
affiliations:
- Technical University of Munich
- Sapienza University of Rome
arxiv_id: '2607.18983'
url: https://arxiv.org/abs/2607.18983
pdf_url: https://arxiv.org/pdf/2607.18983
published: '2026-07-21'
collected: '2026-07-24'
category: LLM
direction: LLM 负责任文本生成与偏见治理
tags:
- LLM
- Bias Mitigation
- Multi-Perspective Summarization
- RAG
- Prompt Engineering
one_liner: 面向自动化新闻领域的多视角LLM生成、偏见检测与消除演示系统
practical_value: '- 多视角内容生成的prompt工程+RAG组合方案可直接迁移到商品评价多观点摘要、用户评论结构化生成场景，避免生成内容过于片面

  - 句子级偏见检测与自动中立化改写流程可复用在营销文案、商品种草内容合规性检查与修改环节，降低内容违规风险

  - 视角聚类+分立场摘要对比的评估框架可迁移到UGC/PGC内容质量评估、生成式推荐内容多样性校验场景'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
自动化新闻场景下LLM生成内容易出现视角单一、继承源数据或训练偏见的问题，而社媒来源的公共讨论本身碎片化、极化严重，现有方案无法兼顾内容多样性与中立性。
### 方法关键点
1. 全链路融合prompt工程与可选RAG模块，从非结构化社媒讨论中提取生成语义多样的视角集合
2. 多视角摘要模块整合冲突观点输出平衡摘要
3. 偏见分析套件支持句子级偏见检测、类型分类与自动中立化改写，配套交互界面支持视角聚类查看、分立场摘要对比等操作
### 关键结果
各模块在语义多样性、摘要质量、偏见降低指标上均优于强基线，同时保持高内容保真度，已上线公开可访问Demo支持复现与后续研究。
