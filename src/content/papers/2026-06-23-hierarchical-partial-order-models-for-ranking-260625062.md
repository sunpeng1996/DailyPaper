---
title: Hierarchical Partial-Order Models for Ranking
title_zh: Hierarchical Partial-Order Models for Ranking
authors:
- Dongqing Li
- Geoff K. Nicholls
- Jeong Eun Lee
- Chuxuan
- Jiang
arxiv_id: '2606.25062'
url: https://arxiv.org/abs/2606.25062
pdf_url: https://arxiv.org/pdf/2606.25062
published: '2026-06-23'
collected: '2026-06-26'
category: RecSys
direction: RecSys
tags:
- RecSys
- LLM
- Agent
one_liner: Rank aggregation combines information from ordered lists ranking items
  by preference. Classical...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 10
source: arxiv-stat.ML
depth: abstract
---

### 摘要

Rank aggregation combines information from ordered lists ranking items by preference. Classical parametric models for such data, including the Mallows and Plackett-Luce models, assume the orders concentrate around one or more complete consensus rankings. Recent work relaxes the total-order assumption by allowing the consensus structure to be a partial order (poset), allowing for incomparabilities in preferences. However, in many applications preference data exhibit group structure. We introduce hierarchical partial order (HPO) models, which extend poset-based models to accommodate grouped data through a hierarchy of latent posets. This framework, which parallels mixture model extensions of the Mallows and Plackett-Luce models, enables principled sharing of information across groups while preserving partial-order structure. We show that the Plackett-Luce model and its hierarchical variants are special cases of HPO-models. We develop a hierarchical clustering extension (HCPO) for unsupervised clustering in settings where group labels are unknown. Bayesian inference for the latent poset hierarchy is performed using Markov chain Monte Carlo methods. Experiments on synthetic and real-world datasets, including pairwise acoustic preference data and LLM agent traces, demonstrate that the proposed HPO and HCPO models outperform existing approaches in both predictive performance and structural interpretability.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。
