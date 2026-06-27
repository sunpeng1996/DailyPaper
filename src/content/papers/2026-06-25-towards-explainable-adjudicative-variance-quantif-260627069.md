---
title: 'Towards Explainable Adjudicative Variance: Quantifying Judicial Discretion
  via Gated Multi-Task Learning'
title_zh: 'Towards Explainable Adjudicative Variance: Quantif'
authors:
- Stanisław Sójka
- Felix Steffek
- Matthias Grabmair
arxiv_id: '2606.27069'
url: https://arxiv.org/abs/2606.27069
pdf_url: https://arxiv.org/pdf/2606.27069
published: '2026-06-25'
collected: '2026-06-27'
category: Training
direction: Training
tags:
- Training
- LLM
one_liner: Legal outcome prediction must disentangle objective case facts from adjudicative
  context. Merit...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 5
source: arxiv-cs.CL
depth: abstract
---

### 摘要

Legal outcome prediction must disentangle objective case facts from adjudicative context. Merit-based rulings rely on factual evidence while technical disposals may hinge on judicial discretion. We propose a Judge-Aware Gated Multi-Task Learning architecture that explicitly models this distinction. We introduce a fine-grained outcome taxonomy to supervise the encoder, enforcing a structural regularization that disentangles distinct semantic pathways. This granular legal curriculum enables our Gated Fusion mechanism to dynamically modulate reliance on judge identity. We evaluate our approach on 13,937 UK Employment Tribunal decisions. We benchmark our design against supervised fine-tuning (SFT) of a Gemma-4 26B-A4B backbone, in which judge identity and the taxonomy are injected as prompt tokens or autoregressive output targets. The two contextual signals compose only weakly when forced through a single autoregressive channel. In contrast, coupling a LoRA-adapted Gemma-4 encoder with our gated architecture defines a new state of the art on this benchmark while requiring an order of magnitude fewer trainable parameters than the generative SFT baselines, with gains concentrated on the most ambiguous and rarest outcome classes. Beyond accuracy, the architecture is interpretable; learned judge embeddings and calibration profiles localize the cases where adjudicative context drives the prediction. These results indicate that, for identity-conditioned classification of legal outcomes, the choice of conditioning interface dominates scale: differentiable structured composition yields more accurate, more parameter-efficient models than prompt-based composition over a substantially larger backbone.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
