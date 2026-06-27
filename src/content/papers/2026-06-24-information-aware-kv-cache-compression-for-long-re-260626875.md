---
title: Information-Aware KV Cache Compression for Long Reasoning
title_zh: Information-Aware KV Cache Compression for Long Re
authors:
- Jushi Kai
- Zhuiri Xiao
- Alexandra Birch
- Zhouhan Lin
arxiv_id: '2606.26875'
url: https://arxiv.org/abs/2606.26875
pdf_url: https://arxiv.org/pdf/2606.26875
published: '2026-06-24'
collected: '2026-06-27'
category: Reasoning
direction: Reasoning
tags:
- Reasoning
- LLM
one_liner: Reasoning capability has advanced rapidly in large language models (LLMs),
  leading to an increa...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: huggingface-daily
depth: abstract
---

### 摘要

Reasoning capability has advanced rapidly in large language models (LLMs), leading to an increasing size of key-value (KV) cache in both prefilling and decoding stages. Existing KV cache compression methods mainly rely on attention weights to estimate token importance. While attention effectively captures contextual relevance, it overlooks complementary information-theoretic signals related to predictive uncertainty and token informativeness. In this paper, we revisit token importance from a forward-looking perspective and introduce Forward Influence, a metric that measures how compressed tokens affect future contexts. Our analysis reveals that tokens selected by attention scores mainly influence nearby contexts, whereas tokens associated with high predictive uncertainty exhibit substantially stronger influence on distant future contexts. Based on the observation, we propose InfoKV, an entropy-aware KV cache compression framework that incorporates information-theoretic signals. It combines token-level predictive uncertainty with layer-wise representation evolution and integrates the resulting entropy scores with attention scores during reasoning. Experiments on long-context reasoning benchmarks with Llama-3.1, Llama-3.2, and DeepSeek-R1 demonstrate that InfoKV consistently outperforms existing attention-based KV compression methods in both long prefilling and decoding scenarios.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。
