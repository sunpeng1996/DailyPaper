---
title: 'Fast and Feasible: Permutation-based Constrained Reranking for Revenue Maximization'
title_zh: 'Fast and Feasible: Permutation-based Constrained R'
authors:
- Svetlana Shirokovskikh
- Anastasiia Soboleva
- Ekaterina Solodneva
- Aleksandr Katrutsa
- Roman Loginov
- Egor Samosvat
arxiv_id: '2606.28059'
url: https://arxiv.org/abs/2606.28059
pdf_url: https://arxiv.org/pdf/2606.28059
published: '2026-06-26'
collected: '2026-06-29'
category: RecSys
direction: RecSys
tags:
- RecSys
- LLM
one_liner: Search and recommender systems have produced highly relevant search results.
  A natural next ste...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 摘要

Search and recommender systems have produced highly relevant search results. A natural next step in the development of such systems in e-commerce is to rerank these results to increase the platform's revenue from paid promotion products. However, maximizing revenue alone may degrade the user experience by reducing relevance or increasing fraud risk. To avoid this, we state the reranking problem as an integer linear program ($ILP$) that maximizes revenue subject to per-query constraints on other metrics, e.g., relevance. Since solving $ILP$ exactly for every query is slow for deployment to the online service, we propose a lightweight permutation-based reranking approximation algorithm PermR. At each step, the algorithm selects a pair of neighboring items and swaps them to either improve the objective or repair a violated constraint. We evaluate PermR across multiple categories of a large classified platform in offline and online settings. PermR achieves about 63\% of the ILP revenue improvement, within production latency limits, preserving all constraints. In a 14-day online A/B test over 56 million search queries, PermR increased revenue by $2$\%.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
