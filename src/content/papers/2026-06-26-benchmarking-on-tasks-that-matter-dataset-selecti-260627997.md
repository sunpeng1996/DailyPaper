---
title: 'Benchmarking on Tasks That Matter: Dataset Selection for Preserving Model
  Rankings'
title_zh: 'Benchmarking on Tasks That Matter: Dataset Selecti'
authors:
- Rostislav Gusev
- Alexey Zaytsev
arxiv_id: '2606.27997'
url: https://arxiv.org/abs/2606.27997
pdf_url: https://arxiv.org/pdf/2606.27997
published: '2026-06-26'
collected: '2026-06-29'
category: RecSys
direction: RecSys
tags:
- RecSys
- LLM
one_liner: Benchmarks of machine learning models often include many datasets, making
  evaluation expensive....
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: arxiv-stat.ML
depth: abstract
---

### 摘要

Benchmarks of machine learning models often include many datasets, making evaluation expensive. For efficiency, it is preferable to perform evaluations on small, representative datasets instead. The selection of such subsets typically relies on heuristics and is rarely analyzed for the robustness of the resulting model rankings. We introduce a framework to perform the task of selecting datasets subsets with an evaluation of how different selection strategies preserve the global model rankings. Our framework includes bootstrap aggregation, which provides valid confidence intervals, allowing a principled comparison of selection strategies. We consider clustering, design criteria (A/D-optimality), random baselines, and greedy farthest-first (FAFI). For the latter, we derive upper bounds on selection quality in terms of ranking errors as a function of the number of selected datasets. Empirically, in time series classification (TSC, 112 datasets) and in a supplementary natural language processing benchmark derived from MTEB (57 tasks), several selection strategies improve rank preservation compared with random subsets, including simple FAFI. In contrast, in recommender systems (30 datasets), the improvement of strategies over random selection is small and typically statistically insignificant. For TSC, our best-performing strategy achieves a Spearman correlation of 0.95 with the full benchmark model rankings using only five selected datasets. Additional experiments indicate that the effectiveness of selection approaches depends on both the quality of dataset representations and the scale of the benchmarking regime.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
