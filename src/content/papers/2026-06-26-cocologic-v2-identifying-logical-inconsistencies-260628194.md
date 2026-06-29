---
title: 'COCOLogic-V2: Identifying Logical Inconsistencies via Truly Hard-Negatives'
title_zh: 'COCOLogic-V2: Identifying Logical Inconsistencies'
authors:
- David Steinmann
- Antonia Wüst
- Kristian Kersting
- Wolfgang Stammer
arxiv_id: '2606.28194'
url: https://arxiv.org/abs/2606.28194
pdf_url: https://arxiv.org/pdf/2606.28194
published: '2026-06-26'
collected: '2026-06-29'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: While interpretable models such as concept bottleneck models (CBMs) and
  program synthesis metho...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 10
source: arxiv-cs.LG
depth: abstract
---

### 摘要

While interpretable models such as concept bottleneck models (CBMs) and program synthesis methods enable verification of model decisions, their evaluation is typically limited to simple tasks, leaving complex reasoning on real-world images largely unexplored. We introduce COCOLogic-V2, an object-centric dataset for visual inductive reasoning on real-world images covering a broad subset of first-order logic. By categorizing samples into positive variants, near-boundary (NB), and far-from-boundary (FB) negatives, COCOLogic-V2 enables fine-grained diagnosis of model accountability. Our evaluations show that models tend to separate positive and FB samples well but fail on NB samples, while perceptual noise and large rule-induced search spaces pose additional challenges in few-shot settings. Together, these results highlight that visual inductive reasoning remains an open challenge and COCOLogic-V2 provides a concrete foundation for advancing methods in this direction.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
