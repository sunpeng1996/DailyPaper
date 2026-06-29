---
title: An Empirical Analysis of Factual Errors in Human-Written Text and its Application
title_zh: An Empirical Analysis of Factual Errors in Human-W
authors:
- Kazuma Iwamoto
- Kazumasa Omura
- Shotaro Ishihara
arxiv_id: '2606.27959'
url: https://arxiv.org/abs/2606.27959
pdf_url: https://arxiv.org/pdf/2606.27959
published: '2026-06-26'
collected: '2026-06-29'
category: Training
direction: Training
tags:
- Training
- LLM
one_liner: Factual Error Detection (FED), which is the task of identifying factually
  incorrect spans in a...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 摘要

Factual Error Detection (FED), which is the task of identifying factually incorrect spans in a given text, has long been recognized as an important research problem. However, with the rapid rise of large language models (LLMs), research attention has shifted toward factual errors specific to LLM-generated text (hallucinations) and their detection. As a result, the detection of factual errors in human-written text has been relatively neglected. To address this gap, we first distill a taxonomy of human-induced factual errors by analyzing corrections of newspaper articles, a representative source of text that is guaranteed to be human-written and contains few grammatical errors. Our analysis revealed that there are characteristic categories such as kanji misconversions and numeral classifier errors, which are not focused in existing hallucination benchmarks. Based on the taxonomy, we then evaluate the FED capability of vanilla LLMs on synthesized realistic test cases and real corrections. Experimental results demonstrated that even high-performance LLMs such as GPT-5.4 achieved only word-level F1 score of 52% on the synthetic evaluation data, highlighting the task difficulty. Furthermore, a detailed analysis by detection difficulty revealed the current state of FED.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
