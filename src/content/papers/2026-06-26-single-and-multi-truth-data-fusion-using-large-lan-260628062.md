---
title: Single and Multi Truth Data Fusion using Large Language Models
title_zh: Single and Multi Truth Data Fusion using Large Lan
authors:
- Hira Beril Kucuk
- Norman W Paton
- Jiaoyan Chen
- Zhenyu Wu
arxiv_id: '2606.28062'
url: https://arxiv.org/abs/2606.28062
pdf_url: https://arxiv.org/pdf/2606.28062
published: '2026-06-26'
collected: '2026-06-29'
category: LLM
direction: LLM
tags:
- LLM
- AI
one_liner: Data fusion, also known as truth discovery, is a data integration problem
  that aims to determin...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 摘要

Data fusion, also known as truth discovery, is a data integration problem that aims to determine the correct value or set of values for each attribute of an object when presented with potentially conflicting values from multiple sources. Data fusion tasks belong to two main categories: single-truth scenarios, where each attribute has only one correct value, and multi-truth scenarios, where multiple values can be valid simultaneously. This paper investigates the use of Large Language Models (LLMs) in data fusion tasks for tabular data. Various prompting strategies, encompassing both single-truth and multi-truth scenarios, are investigated empirically. Domain-dependent, domain-independent, zero-shot and one-shot prompts are evaluated on three different benchmark datasets. Experimental results demonstrate that LLM-based approaches outperform traditional unsupervised truth discovery methods, such as DART and LTM, across all datasets. The codebase of this study has been made publicly available on GitHub.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
