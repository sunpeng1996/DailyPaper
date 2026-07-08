---
title: 'CMDR: Contextual Multimodal Document Retrieval'
title_zh: CMDR：上下文感知多模态文档检索方法
authors:
- Ryota Tanaka
- Taku Hasegawa
- Kyosuke Nishida
affiliations:
- Human Informatics Labs., NTT, Inc., Tokyo, Japan
arxiv_id: '2607.05927'
url: https://arxiv.org/abs/2607.05927
pdf_url: https://arxiv.org/pdf/2607.05927
published: '2026-07-07'
collected: '2026-07-08'
category: RAG
direction: 多模态文档检索 · RAG召回优化
tags:
- Multimodal Retrieval
- Contrastive Learning
- Embedding
- RAG
- Benchmark
one_liner: 提出上下文感知多模态文档检索框架、配套基准与对比学习目标，显著优化跨页聚合类查询检索效果
practical_value: '- 电商多模态商品手册/详情页检索场景，可复用多页联合编码思路，解决跨详情页/跨规格参数的信息聚合查询需求

  - RAG系统的多模态文档召回模块，可借鉴CMCL对比学习目标，平衡上下文建模与单页粒度的判别性，提升召回准确率

  - 多模态embedding训练时，可采用共享上下文表征派生单页嵌入的方案，降低多模态长文档的编码开销'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有多模态文档检索方法多独立编码单页内容，忽略文档全局上下文，无法支撑需跨多页聚合信息的复杂查询；且现有评估基准仅验证简单词汇/语义匹配能力，与真实场景需求脱节。

### 方法关键点
1. 发布CMDR-Bench专用基准，聚焦需建模文档上下文的多模态检索任务评估；
2. 提出CMDR-Embed上下文多模态嵌入框架，联合编码同文档多页内容，从共享全局上下文表征派生单页级嵌入，显式引入上下文信息；
3. 设计CMCL上下文多模态对比学习目标，平衡全局上下文建模能力与单页粒度的判别性，提升训练效率。

### 关键结果
实验显示CMDR-Embed相对无上下文的基线嵌入方案检索效果提升显著，充分验证了上下文感知多模态嵌入对长文档检索的增益价值。
