---
title: 'NuclearQAv2: A Structured Benchmark for Evaluating Domain-Science Competence
  in Large Language Models'
title_zh: 'NuclearQAv2: A Structured Benchmark for Evaluating'
authors:
- Henry Shaowu Yuchi
- Michal Kucer
- Benjamin H. Sims
- Selma Peterson
- Emily Taylor
arxiv_id: '2606.27047'
url: https://arxiv.org/abs/2606.27047
pdf_url: https://arxiv.org/pdf/2606.27047
published: '2026-06-25'
collected: '2026-06-27'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: Large language models (LLMs) have demonstrated strong performance across
  a wide range of tasks,...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 摘要

Large language models (LLMs) have demonstrated strong performance across a wide range of tasks, but ensuring their reliability in highly technical domains remains a significant challenge. In nuclear engineering, problem solving often requires not only factual knowledge but also quantitative reasoning and conceptual understanding. To address the need for systematic evaluation in this domain, we introduce NuclearQAv2, a benchmark for assessing LLMs on nuclear engineering knowledge. The benchmark comprises approximately 1,240 question-answer pairs spanning three categories: boolean, numeric, and verbal. NuclearQAv2 is constructed using a hybrid pipeline that combines expert-authored questions, existing datasets, and LLM-assisted generation from domain-specific technical corpora. By leveraging structured prompting for both automated question generation and response evaluation, the proposed framework enables scalable benchmark construction and evaluation. We evaluate a diverse set of LLMs using NuclearQAv2 and observe substantial performance differences across task types. While the models generally perform well on factual questions, quantitative reasoning and conceptual understanding remain considerably more challenging. These results highlight the importance of multi-faceted evaluation frameworks and establish NuclearQAv2 as a scalable benchmark for assessing LLM capabilities in technical domains.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
