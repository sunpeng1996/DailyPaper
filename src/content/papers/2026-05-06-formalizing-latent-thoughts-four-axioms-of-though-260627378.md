---
title: 'Formalizing Latent Thoughts: Four Axioms of Thought Representation in LLMs'
title_zh: 'Formalizing Latent Thoughts: Four Axioms of Though'
authors:
- Fahd Seddik
- Fatemeh Fard
arxiv_id: '2606.27378'
url: https://arxiv.org/abs/2606.27378
pdf_url: https://arxiv.org/pdf/2606.27378
published: '2026-05-06'
collected: '2026-06-29'
category: Training
direction: Training
tags:
- Training
- LLM
one_liner: We introduce an axiomatic evaluation framework for latent thought representations
  in LLMs, comp...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: huggingface-daily
depth: abstract
---

### 摘要

We introduce an axiomatic evaluation framework for latent thought representations in LLMs, comprising metrics that are independent of downstream benchmark scores and reveal representational failures that benchmark accuracy masks. Existing evaluations conflate representation quality with model capacity. Therefore, failures cannot be attributed to the representation rather than to the model that processes it. We formalize four functional axioms (Causality, Minimality, Separability, and Stability) and define a quantitative measure for each, computed directly on the representation independently of downstream accuracy. We audit open-weight LLMs across 23 reasoning tasks (e.g., Spatial Reasoning, Factual QA). We find that no candidate satisfies all four axioms simultaneously, that the representations distinguish task type reliably but cannot distinguish between two questions within the same task, and that the representations encode little information beyond what is already present in the input embedding. The failure is consistent across dense, reasoning-distilled, and RL-trained model families, indicating that the gap is structural rather than a property of model size or training procedure.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
