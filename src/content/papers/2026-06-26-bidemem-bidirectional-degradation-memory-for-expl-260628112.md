---
title: 'BiDeMem: Bidirectional Degradation Memory for Explainable Image Restoration'
title_zh: 'BiDeMem: Bidirectional Degradation Memory for Expl'
authors:
- Xinrui Wu
- Lichen Huang
arxiv_id: '2606.28112'
url: https://arxiv.org/abs/2606.28112
pdf_url: https://arxiv.org/pdf/2606.28112
published: '2026-06-26'
collected: '2026-06-29'
category: QueryRec
direction: QueryRec
tags:
- QueryRec
- LLM
one_liner: Degradation-aware prompts, conditions, and latent priors are increasingly
  used in image restora...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 10
source: arxiv-cs.AI
depth: abstract
---

### 摘要

Degradation-aware prompts, conditions, and latent priors are increasingly used in image restoration, yet they are usually judged by a single endpoint: whether the restored image obtains higher PSNR. This is a weak test of semantics. A condition can help by adding capacity, acting as a global correction bias, or exploiting dataset shortcuts, without becoming an interpretable degradation prior. We propose BiDeMem, a bidirectional degradation memory for explainable image restoration. A query built from restoration features and input statistics retrieves a compact top-k subset of memory slots. The same selected slot identity supports the restoration path at inference time and a training-only forward-degradation explanation path. The study centers on verifiability in a controlled multi-degradation NAFNet setting. New controls separate the gain from a correction head alone, a dense query prior, and a static global prior: these variants are 0.2588, 0.2586, and 0.2839 dB below BiRank, respectively. Strong residual supervision and a wider degradation head also remain below the full bidirectional memory model. Intervention probes show that BiRank preserves restoration quality while increasing wrong-prior and native-prior sensitivity, framing degradation memory as both a restoration module and a falsifiable explanation mechanism.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
