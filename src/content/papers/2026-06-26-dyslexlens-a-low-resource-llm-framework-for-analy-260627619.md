---
title: 'DysLexLens: A Low-Resource LLM Framework for Analysing Dyslexic Learners Insights
  from Online Forums'
title_zh: 'DysLexLens: A Low-Resource LLM Framework for Analy'
authors:
- Dana Rezazadegan
- Atie Kia
- Phongpadid Nandavong
- Dominique Carlon
- Jeremy Nguyen
- Abhik Banerjee
- James Marshall
- Anthony McCosker
- Yong-Bin Kang
arxiv_id: '2606.27619'
url: https://arxiv.org/abs/2606.27619
pdf_url: https://arxiv.org/pdf/2606.27619
published: '2026-06-26'
collected: '2026-06-29'
category: QueryRec
direction: QueryRec
tags:
- QueryRec
- LLM
one_liner: Dyslexic learners increasingly use artificial intelligence (AI) tools to
  support reading, writi...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 10
source: arxiv-cs.IR
depth: abstract
---

### 摘要

Dyslexic learners increasingly use artificial intelligence (AI) tools to support reading, writing, organisation, and study-related tasks. However, their lived experiences with these tools remain largely underexamined. This paper proposes DysLexLens, a low-resource LLM framework, designed to analyse dyslexic learners experience with AI through online forum discussions. DysLexLens is designed as an end-to-end, evidence-traceable architecture which transforms noisy social media posts into a dictionary-driven corpora, provides knowledge-graph (KG)-based question reasoning, generates verifiable query responses, and enables response evaluation through quantitative and human-grounded assessment. DysLexLens has four key features. First, it employs a dictionary-driven filtering method to construct a more focused Reddit corpus on dyslexia and AI, filtering out noisy and weakly related posts to improve the relevance of data collected from low-resource forum contexts. Second, it integrates LLM-assisted semantic analysis with KG-based query reasoning to uncover meaningful patterns. Third, it has quantitative evaluation metrics (RAGAS and Query Robustness) to measure LLM-generated response performance. Fourth, it provides structured qualitative validation guidelines for assessing response quality, with a specific focus on hallucination and evidence alignment. We demonstrate the effectiveness of DysLexLens using dyslexia-related Reddit forum data and 30 questions. The results show its potential generalisability to other low-resource forum data contexts. DysLexLens, sample data, questions and evaluation results are available at Github to support reproducibility.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
