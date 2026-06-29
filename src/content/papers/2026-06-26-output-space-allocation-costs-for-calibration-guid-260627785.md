---
title: 'Output-Space Allocation Costs for Calibration-Guided LLM Compression: An Empirical
  Study'
title_zh: Output-Space Allocation Costs for Calibration-Guid
authors:
- Qiong Tang
- Xiangkun Hu
- Xiangyang Liu
- Yiran Chen
- Yunfan Shao
arxiv_id: '2606.27785'
url: https://arxiv.org/abs/2606.27785
pdf_url: https://arxiv.org/pdf/2606.27785
published: '2026-06-26'
collected: '2026-06-29'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: Training-free compression methods for large language models (LLMs) often
  use calibration data t...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 摘要

Training-free compression methods for large language models (LLMs) often use calibration data to guide compression decisions. ROCKET, a recent method combining sparse-dictionary factorization with multi-choice knapsack problem (MCKP) allocation, derives its per-layer factorization from an output reconstruction objective but uses weight-space Frobenius error as the MCKP allocation cost. We investigate whether aligning the allocation cost with the output-space objective improves compressed model fidelity. On Qwen3-8B at 50\% compression, our ROCKET-ActCost achieves +0.8 percentage points higher average accuracy across 8 zero-shot benchmarks (53.1\% vs 52.3\%), but increases WikiText perplexity by 16\% (61.46 vs 52.98). This accuracy-perplexity tradeoff reveals that different allocation objectives favor different downstream metrics. The high correlation ($>$0.99) between weight-space and output-space errors limits allocation divergence, explaining the modest effect size. On Llama-3.2-1B at 20\% compression, the two methods produce near-identical results (53.3\% vs 53.5\% accuracy, 14.45 vs 14.66 PPL), suggesting that the effect of the cost function is minor at lower compression ratios.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
