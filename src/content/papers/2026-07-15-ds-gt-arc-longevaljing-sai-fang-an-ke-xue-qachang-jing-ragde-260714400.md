---
title: 'DS@GT ARC at LongEval: Citation Integrity and Factual Grounding in Scientific
  QA'
title_zh: DS@GT ARC LongEval竞赛方案：科学QA场景RAG的引文完整性与事实对齐研究
authors:
- Brandon Michaels
- Brendon Johnson
affiliations:
- Georgia Institute of Technology
arxiv_id: '2607.14400'
url: https://arxiv.org/abs/2607.14400
pdf_url: https://arxiv.org/pdf/2607.14400
published: '2026-07-15'
collected: '2026-07-17'
category: RAG
direction: 可信RAG · 事实对齐与引文校验
tags:
- RAG
- Fact Grounding
- Citation Integrity
- LLM-as-Judge
- Scientific QA
one_liner: 对比多套RAG方案的生成质量与引文忠实度差异，提出可信RAG需配套事实对齐评估指标
practical_value: '- 电商商品问答/活动规则生成类业务可复用CRAG+CiteFix组合框架：生成前过滤低相关召回块，生成后校验内容与召回素材的一致性，减少虚假宣传、参数报错问题

  - RAG系统评估不能仅关注query相关性/内容流畅度，需引入RAGAs的全局忠实度、引文忠实度双维度指标，避免大模型依赖参数记忆而非业务素材生成内容

  - 前沿大模型优先依赖参数记忆而非给定上下文的现象具有普适性，合规要求高的场景（如美妆/医药宣传、售后规则解答）必须加事后校验环节，不能直接信任大模型输出'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
科学领域QA要求回答必须100%基于给定文献、引文准确，但现有RAG评估多侧重内容流畅度与query相关性，忽视事实对齐与引文可信度；同时前沿大模型常依赖参数记忆而非给定上下文生成，导致引文造假、事实错误，亟需明确可信RAG的优化与评估方向。

### 方法关键点
- 输入处理：将官方提供的10篇预检索文档切分为语义块，用BM25+BGE混合召回Top-k块作为生成基础输入
- 三套生成方案对比：1）混合基线：直接将召回块输入Gemma-4-31B生成回答；2）校正Pipeline：生成前用轻量交叉编码器过滤低蕴涵召回块，生成后用CiteFix剪去无证据支撑的引文；3）前沿模型基准：直接用GPT-5.5 Thinking、Claude Opus 4.7基于原始10篇文档生成
- 双维度评估：官方指标（ROUGE、BERTScore、引文准确率）+ RAGAs自定义评估（全局忠实度、引文忠实度、回答相关性）

### 关键实验
基于LongEval提供的CORE科学文献数据集共47个测试query，对比4类方案表现：① 前沿模型官方指标领先，GPT-5.5 ROUGE F1达0.188、BERT F1达0.227，Claude Opus引文准确率达1.0；② 校正Pipeline忠实度最优，全局忠实度0.784、引文忠实度0.758，较混合基线分别提升4.3pct、1.7pct；③ 前沿模型忠实度极低，GPT-5.5引文忠实度仅0.417，多数回答依赖参数记忆而非给定文献。

### 核心结论
可信RAG的评估不能只关注生成内容的流畅度与相关性，必须配套奖励事实对齐的指标，否则越强的大模型越容易出现「回答对但来源错」的不可信问题。
