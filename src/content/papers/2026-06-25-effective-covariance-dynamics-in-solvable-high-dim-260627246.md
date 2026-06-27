---
title: Effective Covariance Dynamics in Solvable High-Dimensional GANs
title_zh: Effective Covariance Dynamics in Solvable High-Dim
authors:
- Andrew Bond
- Zafer Doğan
arxiv_id: '2606.27246'
url: https://arxiv.org/abs/2606.27246
pdf_url: https://arxiv.org/pdf/2606.27246
published: '2026-06-25'
collected: '2026-06-27'
category: Training
direction: Training
tags:
- Training
- LLM
one_liner: We study a solvable high-dimensional model of generative adversarial network
  (GAN) training in...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 摘要

We study a solvable high-dimensional model of generative adversarial network (GAN) training in which a linear generator learns a low-dimensional subspace from data with structured latent covariance. Prior solvable GAN analyses assume unconditional signals with diagonal latent covariance; we extend the multi-feature discriminator setting to class-dependent, correlated, and non-zero-mean latent structure. For the quadratic energy discriminator, all such heterogeneity enters the dynamics through a probability-weighted effective second moment. We prove that the stochastic microscopic training process converges, in the high-dimensional limit, to deterministic ordinary differential equations governed by this effective covariance. In the matched-covariance specialization, the stability analysis yields a mode-wise solvable interval determined by the learning rates and noise level: learning begins when the leading effective eigenvalue crosses the lower threshold, while full recovery requires all relevant effective modes to remain within the interval. This reveals a signal-boosting mechanism: low-rank correlations can lift weak directions above the learnability threshold, whereas overly strong correlations destabilize recovery. Numerical simulations validate the ODE, phase boundary, and boosting mechanism. Experiments on MNIST, FashionMNIST, and CIFAR-10 further show that informed generator covariance improves alignment with the data-driven reference subspace.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
