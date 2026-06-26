---
title: 'ProvenAI: Provenance-Native Traces of Evidence in Generated Answers'
title_zh: 'ProvenAI: Provenance-Native Traces of Evidence in'
authors:
- Mohammad Faizan
- Dalal Alharthi
arxiv_id: '2606.26449'
url: https://arxiv.org/abs/2606.26449
pdf_url: https://arxiv.org/pdf/2606.26449
published: '2026-06-24'
collected: '2026-06-26'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: Retrieval-augmented systems routinely present citations alongside generated
  answers, yet a cita...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: arxiv-cs.IR
depth: abstract
---

### 摘要

Retrieval-augmented systems routinely present citations alongside generated answers, yet a citation does not confirm that the corresponding source meaningfully shaped the output. This paper introduces ProvenAI, a framework that decomposes transparency in multi-hop question answering into three independently measurable layers: answer correctness, citation fidelity against benchmark supporting evidence, and per-document influence under leave-one-resource-out intervention. Targeting the HotpotQA distractor benchmark through a seven-stage pipeline covering data normalisation, retrieval indexing, citation-aware answer generation, attribution auditing, ablation-based influence estimation, batch evaluation, and interactive inspection, ProvenAI evaluates 7,405 validation examples drawn from a canonical corpus of 509,300 passages. The system achieves 53.53% answer accuracy alongside a mean citation-fidelity score of 71.55%, and a worked example surfaces what we call the citation-influence gap: a clean citation audit co-occurring with a profile in which one cited source registers only weak influence while seven uncited sources demonstrably shift the output. We formalise the relationship between the implemented surface proxy and a token-level KL-divergence target through a stated faithfulness condition, ground the framework in causal-mediation analysis and database-provenance theory, and discuss how the three measurement layers compose with cryptographic provenance architectures emerging in autonomous scientific discovery. ProvenAI establishes that meaningful transparency in retrieval-grounded QA requires traceable links across retrieved, cited, and behaviourally influential evidence as three distinct, independently measured layers.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。
