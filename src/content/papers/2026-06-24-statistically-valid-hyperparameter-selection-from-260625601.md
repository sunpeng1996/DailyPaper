---
title: 'Statistically Valid Hyperparameter Selection: From Tuning to Guarantees'
title_zh: 'Statistically Valid Hyperparameter Selection: From'
authors:
- Amirmohammad Farzaneh
- Osvaldo Simeone
arxiv_id: '2606.25601'
url: https://arxiv.org/abs/2606.25601
pdf_url: https://arxiv.org/pdf/2606.25601
published: '2026-06-24'
collected: '2026-06-27'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: Hyperparameter selection is a critical step in the deployment of modern
  artificial intelligence...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 摘要

Hyperparameter selection is a critical step in the deployment of modern artificial intelligence systems, given the need to tune degrees of freedom such as inference-time parameters, implementation-level settings, and thresholds driving decision rules. Despite its practical importance, hyperparameter selection is typically performed using best-effort empirical methods such as grid search or Bayesian optimization, which provide no formal statistical guarantees on reliability or safety. This monograph presents a unified statistical framework for reliable hyperparameter selection, centered on the learn-then-test (LTT) paradigm, which formulates the problem as multiple hypothesis testing over a candidate set of hyperparameters. The framework enables the selection of hyperparameters that provably satisfy application-specific reliability requirements -- such as bounds on average risk, quantile risk, or information-theoretic constraints -- with explicit, finite-sample control of error probabilities. The supporting statistical machinery, namely p-values, e-values, and concentration inequalities, is developed from first principles in a dedicated appendix.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
