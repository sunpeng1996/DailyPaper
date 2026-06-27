---
title: 'Continuous Behavioral Synthesis for Adaptive Health Dashboards: An LLM-Mediated
  Architecture Integrating Explicit Preference, Spatial Reorganization, and Attention
  Allocation Signals'
title_zh: Continuous Behavioral Synthesis for Adaptive Healt
authors:
- Tiziano Santilli
- Mina Alipour
- Mahyar T. Moghaddam
arxiv_id: '2606.26937'
url: https://arxiv.org/abs/2606.26937
pdf_url: https://arxiv.org/pdf/2606.26937
published: '2026-06-25'
collected: '2026-06-27'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: The engineering of adaptive user interfaces has traditionally relied on
  either rule-based syste...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 摘要

The engineering of adaptive user interfaces has traditionally relied on either rule-based systems encoding designer intuitions about user needs or machine learning approaches requiring substantial historical data before achieving effective personalization. We present a technical architecture that leverages Large Language Models as behavioral synthesis engines to enable immediate adaptation from sparse, heterogeneous user signals. Our system integrates three distinct behavioral channels, i) explicit micro-feedback on individual interface elements, ii) spatial priority inferred from manual widget reorganization through drag-and-drop interaction, iii) and attentional investment measured through dwell time during hover events, within a structured prompt engineering framework that continuously regenerates dashboard layouts while maintaining explanatory coherence. The architecture addresses the technical challenge of translating low-level interaction patterns into high-level design decisions through a layered prompt construction methodology that separates temporal context determination, behavioral signal extraction, explicit preference enforcement, and user profile synthesis. The approach combines manually specified behavioral interpretations and temporal heuristics with LLM-mediated synthesis, enabling the reconciliation of multiple simultaneous signals that would be difficult to encode through explicit rules alone. We demonstrate the system through an instantiation in the personal health monitoring domain, including an analytical evaluation of adaptation behavior across multiple scenarios and a working implementation managing fourteen distinct health metrics across seven widget visualization modalities. The evaluation compares profile-driven initialization, multi-signal behavioral adaptation, and presents the resulting interfaces through representative post-adaptation screenshots.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
