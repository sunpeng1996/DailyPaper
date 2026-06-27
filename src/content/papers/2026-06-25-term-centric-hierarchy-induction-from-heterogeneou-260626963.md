---
title: Term-Centric Hierarchy Induction from Heterogeneous Corpora
title_zh: Term-Centric Hierarchy Induction from Heterogeneou
authors:
- Elena Senger
- Yuri Campbell
- Jan-Peter Bergmann
- Rob van der Goot
- Barbara Plank
arxiv_id: '2606.26963'
url: https://arxiv.org/abs/2606.26963
pdf_url: https://arxiv.org/pdf/2606.26963
published: '2026-06-25'
collected: '2026-06-27'
category: Training
direction: Training
tags:
- Training
- LLM
one_liner: Organizing knowledge from diverse text sources into interpretable hierarchies
  is crucial for ta...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 摘要

Organizing knowledge from diverse text sources into interpretable hierarchies is crucial for tasks such as policy analysis, innovation monitoring, and exploratory domain mapping. Existing taxonomy induction methods typically rely on document-level representations that capture entire documents rather than the specific domain concepts relevant for knowledge organization, limiting their ability to generalize across heterogeneous sources. We propose a term-centric framework for inducing hierarchical taxonomies from heterogeneous corpora that scales to massive document collections. Our approach maps documents from diverse sources into a shared representation space using automatic term extraction, enabling robust cross-source alignment. Based on these representations, we construct interpretable hierarchies that integrate domain priors with datadriven clustering. Experiments on a novel English and German multi-source benchmark of over one million documents demonstrate that our method improves cross-source coherence and hierarchy quality over text- and summarybased baselines. A case study on German regional innovation analysis further demonstrates its practical utility for technology landscape mapping.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
