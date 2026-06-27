---
title: 'DnA: Denoising Attention for Visual Tasks'
title_zh: 'DnA: Denoising Attention for Visual Tasks'
authors:
- Ron Campos
- Subhajit Maity
- Xin Li
- Srijan Das
- Aritra Dutta
arxiv_id: '2606.27372'
url: https://arxiv.org/abs/2606.27372
pdf_url: https://arxiv.org/pdf/2606.27372
published: '2026-06-25'
collected: '2026-06-27'
category: QueryRec
direction: QueryRec
tags:
- QueryRec
- LLM
one_liner: The softmax activation in multihead attention (MHA) is the de facto standard
  for attention-base...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: arxiv-cs.CV
depth: abstract
---

### 摘要

The softmax activation in multihead attention (MHA) is the de facto standard for attention-based models in visual perception tasks. However, standard softmax can produce noisy attention patterns that dilute relevant features and degrade its performance. In this paper, we propose Denoising Attention or DnA, in which, first, a positive query identifies which image features belong to the correct class, and a negative query identifies closely associated but irrelevant image features. DnA then projects these interactions into two distinct subspaces with larger principal angles, promoting subspace separation and improved discriminability. Using a ViT-B backbone, our proposed DnA achieves an absolute gain of 0.8% on ImageNet-1K compared to the baseline. We further show improvements across multiple visual understanding tasks, including video understanding with video transformers (1.8%) and video LLMs (0.5%). Our extensive empirical analyses justify the design choices involving two interacting subspaces and the denoising effect of DnA.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。
