---
title: 'Mind the Heads: Topological Representation Alignment for Multimodal LLMs'
title_zh: 'Mind the Heads: Topological Representation Alignme'
authors:
- Davide Caffagni
- Alberto Compagnoni
- Federico Melis
- Sara Sarto
- Pier Luigi Dovesi
- Mark Granroth-Wilding
- Marcella Cornia
- Lorenzo Baraldi
arxiv_id: '2606.23885'
url: https://arxiv.org/abs/2606.23885
pdf_url: https://arxiv.org/pdf/2606.23885
published: '2026-06-22'
collected: '2026-06-27'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: Representation alignment has emerged as an effective approach to improve
  Multimodal Large Langu...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 摘要

Representation alignment has emerged as an effective approach to improve Multimodal Large Language Models (MLLMs) by regularizing their internal representations toward those of an external vision encoder. However, existing methods typically align a fixed layer of the language backbone, overlooking the fine-grained structure of Transformer models. In this work, we propose Head-Wise Representation Alignment (HeRA), a method that enforces cross-modal alignment at the level of individual attention heads. Our approach is grounded in the Platonic Representation Hypothesis, focusing on preserving the topological structure of representations (i.e., their local neighborhood relationships) across modalities. Following the Mutual K-Nearest Neighbor (MKNN) alignment metric, we introduce a contrastive objective that acts as a differentiable proxy for matching local structures. HeRA applies this objective during multimodal training to specific attention heads in the LLM, selected by their alignment score according to the MKNN metric. Counterintuitively, we find that aligning the least aligned heads yields the largest gains. Extensive evaluations across multiple MLLMs and 18 benchmarks demonstrate that HeRA consistently improves performance on challenging vision-centric tasks and serves as an effective regularizer against visual hallucinations by naturally curbing the over-reliance on linguistic priors. Our code is publicly released.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
