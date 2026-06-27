---
title: Decision-Aligned Evaluation of Uncertainty Quantification
title_zh: Decision-Aligned Evaluation of Uncertainty Quantif
authors:
- Annika Schneider
- Tommy Rochussen
- Joshua Stiller
- Vincent Fortuin
arxiv_id: '2606.26990'
url: https://arxiv.org/abs/2606.26990
pdf_url: https://arxiv.org/pdf/2606.26990
published: '2026-06-25'
collected: '2026-06-27'
category: Training
direction: Training
tags:
- Training
- LLM
one_liner: Uncertainty estimates in machine learning are typically evaluated using
  generic metrics such as...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 摘要

Uncertainty estimates in machine learning are typically evaluated using generic metrics such as the negative log-likelihood and expected calibration error, yet good performance on such metrics does not necessarily imply high utility in downstream decisions. We introduce decision-alignment, a criterion that reveals which evaluation metrics meaningfully align with downstream utilities. Applying this framework, we show that many widely used uncertainty metrics are either misaligned with common decision problems or encode pathological prior beliefs about the downstream task. We then propose prior-weighted utility metrics, a special class of proper scoring rules that provides decision-aligned uncertainty evaluation. Across benchmark experiments and real-world case studies, our metrics consistently align with realized decision utility, while conventional metrics do not. Our results surface flaws in the current UQ evaluation protocol and offer a principled extension of existing metrics toward decision-relevant UQ evaluation.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
