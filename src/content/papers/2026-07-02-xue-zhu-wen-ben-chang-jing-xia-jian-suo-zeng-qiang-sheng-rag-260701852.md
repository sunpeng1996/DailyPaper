---
title: Evaluating Chunking Strategies for Retrieval-Augmented Generation on Academic
  Texts
title_zh: 学术文本场景下检索增强生成（RAG）的分块策略评估
authors:
- Valentin J. J. Kreileder
- Johannes Reisinger
- Andreas Fischer
affiliations:
- Deggendorf Institute of Technology
arxiv_id: '2607.01852'
url: https://arxiv.org/abs/2607.01852
pdf_url: https://arxiv.org/pdf/2607.01852
published: '2026-07-02'
collected: '2026-07-03'
category: RAG
direction: RAG 分块策略效果评估
tags:
- RAG
- Chunking
- RAGAs
- Information Retrieval
- LLM
one_liner: 针对学术长文本对比三类RAG分块策略，发现中低端硬件下聚类语义分块未优于简单策略
practical_value: '- 搭建电商商品知识库、客服应答类RAG系统时，优先测试递归/固定大小分块，无需盲目上聚类语义分块，可降低算力成本同时获得更稳定的效果

  - 自定义RAG效果指标可参考AQS设计，采用faithfulness与answer relevancy的调和平均，同时规避回答幻觉和答非所问问题

  - 采用RAGAs做自动评估时，中低端硬件+小模型场景下faithfulness计算失败率可达44%，需提前设计失败降级或数据清洗方案

  - 针对结构化文档的固定位置类查询（如商品参数、平台规则），需前置做文档结构解析和格式符号清洗，避免目录符、占位符等污染检索结果'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
RAG系统的回答质量与分块策略强绑定，现有语义分块方案算力成本远高于固定大小、递归等分块策略，但在长结构化文档、中低端自托管硬件场景下的真实效果尚未得到充分验证，同时主流RAG自动评估框架RAGAs在这类场景的可靠性也有待验证。

### 方法关键点
- 对比三类主流分块策略：固定大小分块（150词，10%重叠）、递归分块（按段落/换行/标点分层拆分，目标150词）、聚类语义分块（用all-MiniLM-L6-v2做句嵌入，单链路聚类，目标3句/块，语义权重0.25，距离阈值0.5）
- 提出AQS（Answer Quality Score）指标，取faithfulness和answer relevancy的调和平均，同时惩罚高相关但幻觉、以及忠实但答非所问的回答
- 实验对齐中小团队自托管硬件配置：16GiB显存，生成器用llama3.2:3b，评估器用deepseek-r1:8b，嵌入模型用all-MiniLM-L6-v2

### 关键实验结果
数据集为13篇格式统一的学术论文，单篇词数10232~26960，配套10条查询（5条固定类：作者/标题等元信息查询，5条自由类：论文核心内容查询），核心结果：
1. RAGAs的faithfulness指标计算失败率达44%，三类分块的失败率无显著差异
2. 自由类查询上，递归/固定分块的AQS中位数达0.65，聚类语义分块仅0.40；上下文F1递归分块达0.5，固定分块0.3，聚类分块表现最差
3. 固定类查询三类分块表现均较差，上下文F1中位数均为0，核心原因是目录点等格式残留污染了索引和检索结果

### 核心结论
中低端自托管RAG场景下，结构化长文档优先选择简单的递归或固定大小分块，聚类语义分块算力成本高且无效果优势
