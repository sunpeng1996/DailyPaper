---
title: How Good Can Linear Models Be for Time-Series Forecasting?
title_zh: How Good Can Linear Models Be for Time-Series Fore
authors:
- Lang Huang
- Jinglue Xu
- Luke Darlow
arxiv_id: '2606.27282'
url: https://arxiv.org/abs/2606.27282
pdf_url: https://arxiv.org/pdf/2606.27282
published: '2026-06-25'
collected: '2026-06-26'
category: LLM
direction: LLM
tags:
- LLM
- AI
one_liner: Time-series forecasting research has been moving steadily toward larger
  architectures, from spe...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: arxiv-cs.LG
depth: abstract
---

### 摘要

Time-series forecasting research has been moving steadily toward larger architectures, from specialized transformers to general-purpose foundation models, on the assumption that capacity is what unlocks accuracy. We take the opposite position: most of the gap can be closed at far lower cost by tuning preprocessing rather than scaling models. We use Ridge regression as the testbed, since it has a closed-form solution and interpretable weights, which let the optimal hyperparameters be read off the search directly. We search over context length, local normalization, regularization, and augmentation on eight standard benchmarks and find three patterns. (1) Optimal lookback is strongly series-specific and often non-monotonic in forecast horizon, with fitted power-law exponents ranging from $+0.46$ on ETTm2 to $-0.19$ on Exchange and Traffic, challenging the convention that longer horizons need longer history. (2) Normalizing over a learned trailing fraction of the context, rather than its entirety, is almost universally preferred. (3) Series within the same dataset often disagree on hyperparameters; the optimal degree of cross-series sharing varies from fully shared to fully per-series. The resulting models beat prior linear forecasters on most dataset-horizon entries and exceed Transformer, MLP, and CNN baselines on six of eight benchmarks. The optimized hyperparameters also serve as a diagnostic on the data itself, revealing structures that larger models absorb silently into their learned parameters.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。
