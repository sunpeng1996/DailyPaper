---
title: 'RSPC: A Benchmark for Modeling Stress and Psychiatric Conditions in Digitally
  Mediated Relationships using Psychiatrist Annotations'
title_zh: 'RSPC: A Benchmark for Modeling Stress and Psychiat'
authors:
- Parmitha Vangapandu
- Sai Ganesh Mokkapati
- Sathwik Narkedimilli
- MSVPJ Sathvik
- Timothy Liu
- Simon See
- Johannes C. Eichstaedt
arxiv_id: '2606.27247'
url: https://arxiv.org/abs/2606.27247
pdf_url: https://arxiv.org/pdf/2606.27247
published: '2026-06-25'
collected: '2026-06-27'
category: LLM
direction: LLM
tags:
- LLM
- AI
one_liner: In NLP, mental health conditions are often modeled as isolated phenomena,
  without interpersonal...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 摘要

In NLP, mental health conditions are often modeled as isolated phenomena, without interpersonal context. We use Reddit posts about long-distance relationships to capture both mental health distress and associated relational triggers. We introduce the Relational Stress and Psychiatry Corpus (RSPC) containing 1,799 Reddit posts annotated by psychiatrists for diagnostic categories, including the most prevalent mood disorders (anxiety and depression), relational stressor triggers, and indications of relationship phase. We benchmark seven fine-tuned transformer models and five large language models across multi-label disorder classification, relational trigger detection, and temporal phase prediction tasks. We find clear task-dependent differences between model families, with Claude-3-Haiku achieving the best disorder classification performance (Macro-F1 = 0.538) and GPT-4o obtaining the strongest relational trigger detection performance (Macro-F1 = 0.519), suggesting distinct model capabilities. We further find strong associations between anxiety disorders and chronic relational uncertainty. Overall, RSPC establishes a benchmark for NLP tasks that consider relational context and supports a shift from individual-centric to context-aware mental health modeling that captures the social and temporal dynamics of distress.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
