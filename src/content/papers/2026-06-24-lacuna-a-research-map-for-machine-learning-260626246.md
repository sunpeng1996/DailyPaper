---
title: 'Lacuna: A Research Map for Machine Learning'
title_zh: 'Lacuna: A Research Map for Machine Learning'
authors:
- Martin Weiss
- Miles Q. Li
- Alejandro H. Artiles
- Yacine Mkhinini
- Chris Pal
- Hugo Larochelle
- Nasim Rahaman
arxiv_id: '2606.26246'
url: https://arxiv.org/abs/2606.26246
pdf_url: https://arxiv.org/pdf/2606.26246
published: '2026-06-24'
collected: '2026-06-26'
category: Agent
direction: Agent
tags:
- Agent
- LLM
one_liner: Lacuna is a research map for machine learning that uses LLMs to turn papers
  and scholarly metad...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 10
source: arxiv-cs.IR
depth: abstract
---

### 摘要

Lacuna is a research map for machine learning that uses LLMs to turn papers and scholarly metadata into markdown summaries, concept elements, research directions, and research proposals. Each item keeps links to the primary source records and papers that support it. We release the map with web, markdown, and MCP interfaces. Across LitSearch, Multi-XScience-CS/ML, and ScholarQA-CS-ML, Lacuna outperforms OpenScholar with the strongest gains on LitSearch retrieval (Recall@10 0.538 vs. 0.424 for OpenScholar v3). We also evaluate Lacuna Deep Research, a multi-stage report agent over the map, on 25 ReportBench-ML survey tasks: Lacuna Deep Research reaches 0.052 citation F1, 0.339 citation precision, 99 expert-reference hits, and 7.82/10 RACE report quality, while GPT-Researcher reaches 0.039 F1, 0.290 precision, 72 hits, and 5.24/10 RACE.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。
