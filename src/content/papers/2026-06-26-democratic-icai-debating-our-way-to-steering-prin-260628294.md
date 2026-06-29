---
title: 'Democratic ICAI: Debating Our Way to Steering Principles from Preferences'
title_zh: 'Democratic ICAI: Debating Our Way to Steering Prin'
authors:
- Kevin Kingslin
- Anish Natekar
- Ashutosh Ranjan
- Vivek Srivastava
- Savita Bhat
- Shirish Karande
arxiv_id: '2606.28294'
url: https://arxiv.org/abs/2606.28294
pdf_url: https://arxiv.org/pdf/2606.28294
published: '2026-06-26'
collected: '2026-06-29'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: Preference-based alignment often struggles to capture the reasoning that
  underlies human judgme...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 摘要

Preference-based alignment often struggles to capture the reasoning that underlies human judgments. Many evaluations rely on multiple interacting criteria, yet pairwise labels reveal only the final choice rather than the considerations that shape preferences. Inverse Constitutional AI (ICAI) improves interpretability in decision making by summarizing preferences into natural-language principles, but its single-pass explanations miss much of the nuance involved in complex decisions. We introduce Democratic ICAI, a novel approach that gathers multiple competing rationales through structured persona debate, offering a broader and more expressive account of the factors influencing each comparison. From these richer signals, we derive clearer and more comprehensive steering principles and use them to guide decision modeling through both LLM-based and decision-tree judges. Experiments on creative preference benchmarks, MuCE-Pref and LiTBench, across multiple creative task categories show that Democratic ICAI yields a more faithful preference structure. It improves average preference prediction across tasks relative to deliberative prompting and principle-based baselines, while producing constitutions that LLM annotators prefer.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
