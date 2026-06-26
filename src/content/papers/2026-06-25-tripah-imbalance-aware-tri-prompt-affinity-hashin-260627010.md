---
title: 'TriPAH: Imbalance-Aware Tri-Prompt Affinity Hashing for Cross-Modal Medical
  Retrieval'
title_zh: 'TriPAH: Imbalance-Aware Tri-Prompt Affinity Hashin'
authors:
- Jiaming Bian
- Songming Li
- Yurui Song
- Yunfei Chen
- Yichao Cao
- Jun Long
arxiv_id: '2606.27010'
url: https://arxiv.org/abs/2606.27010
pdf_url: https://arxiv.org/pdf/2606.27010
published: '2026-06-25'
collected: '2026-06-26'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: In the era of big medical data, efficient cross-modal retrieval is pivotal
  for evidence-based d...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 10
source: arxiv-cs.IR
depth: abstract
---

### 摘要

In the era of big medical data, efficient cross-modal retrieval is pivotal for evidence-based diagnosis and large-scale case management. Cross-modal medical hashing retrieval aims to enable efficient image-text search and support downstream tasks such as case-based reasoning and decision support by learning compact, semantically aligned binary codes. However, current methods suffer from semantic fragmentation due to noisy clinical language, long-tailed labels, and brittle quantization that weakens alignment. We propose TriPAH, a Tri-Prompt Affinity Hashing framework. TriPAH synthesizes ontology-grounded, patient-level prompts conditioned on normalized clinical cues to yield low-noise textual representations for initial alignment. A lightweight prompt-token mixer performs hierarchical, multi-granularity alignment and produces quantization-ready features under an asymmetric multi-task objective coupling multi-positive contrastive alignment, imbalance-aware classification, and progressive quantization regularization. A patient-level consistency module further stabilizes codes across complementary views. Extensive experiments on three public datasets demonstrate that TriPAH significantly outperforms state-of-the-art methods.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。
