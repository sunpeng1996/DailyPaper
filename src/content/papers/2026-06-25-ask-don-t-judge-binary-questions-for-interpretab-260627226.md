---
title: 'Ask, Don''t Judge: Binary Questions for Interpretable LLM Evaluation and Self-Improvement'
title_zh: 'Ask, Don''t Judge: Binary Questions for Interpretab'
authors:
- Sangwoo Cho
- Kushal Chawla
- Pengshan Cai
- Zefang Liu
- Chenyang Zhu
- Shi-Xiong Zhang
- Sambit Sahu
arxiv_id: '2606.27226'
url: https://arxiv.org/abs/2606.27226
pdf_url: https://arxiv.org/pdf/2606.27226
published: '2026-06-25'
collected: '2026-06-27'
category: Training
direction: Training
tags:
- Training
- LLM
one_liner: 'Evaluating LLM outputs remains a major bottleneck in NLP: human evaluation
  is expensive and slo...'
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 摘要

Evaluating LLM outputs remains a major bottleneck in NLP: human evaluation is expensive and slow, lexical metrics correlate poorly with human judgments on open-ended generation, and holistic LLM judges often produce opaque scores that are hard to debug. We propose BINEVAL, a framework that decomposes evaluation criteria into atomic binary questions and aggregates the resulting verdicts into interpretable, multi-dimensional scores. Given a task prompt, a meta-prompt generates fine-grained evaluation questions, and an LLM answers them independently for each output, yielding transparent question-level feedback together with calibrated overall scores. This decomposition makes evaluation easier to inspect, easier to diagnose, and directly usable for prompt improvement. Across SummEval, Topical-Chat, and QAGS, BINEVAL matches or outperforms strong baselines including UniEval and G-Eval, with especially strong results on factual consistency benchmarks such as QAGS. Beyond competitive correlation with human judgments, BINEVAL better matches human score distributions and avoids the ceiling effects common in prior LLM judges, leading to better discrimination between borderline and clearly flawed outputs. We further show that the same question-level feedback supports iterative prompt optimization, improving evaluator prompts on summarization and generation prompts on IFBench under both self-update and cross-model update settings. Overall, BINEVAL provides a task-agnostic, training-free, and interpretable evaluation framework that combines strong empirical performance with practical diagnostic and optimization value.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
