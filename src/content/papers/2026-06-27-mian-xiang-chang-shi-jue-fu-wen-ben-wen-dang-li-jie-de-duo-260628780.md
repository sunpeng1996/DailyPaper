---
title: Multimodal Graph RAG for Long-range Visually Rich Document Understanding
title_zh: 面向长视觉富文本文档理解的多模态图RAG方法
authors:
- Yi-Cheng Wang
- Chu-Song Chen
affiliations:
- Department of Computer Science and Information Engineering, National Taiwan University
- FinTech Center, National Taiwan University
arxiv_id: '2606.28780'
url: https://arxiv.org/abs/2606.28780
pdf_url: https://arxiv.org/pdf/2606.28780
published: '2026-06-27'
collected: '2026-06-30'
category: RAG
direction: 多模态Graph RAG · 文档VQA
tags:
- Multimodal RAG
- Knowledge Graph
- VQA
- Long Document Understanding
- MLLM
one_liner: 提出多模态图RAG解决长视觉富文本文档全局VQA问题，同时发布DLVQA评测基准
practical_value: '- 处理电商场景下长多模态内容（如长商品详情页、商品说明书、多页直播图文稿）的问答/导购任务时，可借鉴用多模态知识图（MMKG）整合跨页文本、视觉、布局全局信息，解决纯检索MMRAG无法回答全局问题的缺陷

  - 构建需要全局理解、多跳推理的多模态Agent时，多模态Graph RAG比纯检索式RAG更适合长文档场景，可优先考虑该架构

  - 自研长多模态问答能力需要评测时，可参考本文思路，构造带支撑事实标注的文档级全局问题评测集'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
MLLM处理长视觉富文本文档受限于上下文窗口大小，现有多模态检索增强生成（MMRAG）仅能检索局部相关页面，无法解决需要全局文档理解的VQA问题；现有LLM构建知识图谱的方法仅支持文本模态，自动构建多模态知识图谱（MMKG）的方案未被充分探索，同时领域缺少带标注的综合文档级VQA评测基准。
### 方法关键点
提出多模态图RAG框架，将文档中的文本、图表、布局信息整合为统一的MMKG，建模文档全局知识，支撑跨页面的长程多跳VQA；同时发布新基准DLVQA，提供文档级全局问题的参考摘要与对应支撑事实标注。
### 结果
在公开多跳QA/VQA基准以及自研DLVQA基准上，性能均优于现有MMRAG和纯文本KG类RAG方法
