---
title: 'See & Sniff: Learning Visuo-Olfactory Representations'
title_zh: 'See & Sniff: Learning Visuo-Olfactory Representati'
authors:
- Seongyu Kim
- Seungwoo Lee
- Hyeonggon Ryu
- Joon Son Chung
- Arda Senocak
arxiv_id: '2606.27307'
url: https://arxiv.org/abs/2606.27307
pdf_url: https://arxiv.org/pdf/2606.27307
published: '2026-06-25'
collected: '2026-06-26'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: While modern multimodal models integrate vision with language, audio, or
  touch, olfaction remai...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 10
source: arxiv-cs.CV
depth: abstract
---

### 摘要

While modern multimodal models integrate vision with language, audio, or touch, olfaction remains largely unexplored due to the lack of paired visuo-olfactory data. We introduce SmellNet-V, a scalable visuo-olfactory dataset built on the insight that odor identity is largely invariant to visual transformations within a semantic category. This allows us to synthetically pair smell-only samples with semantically aligned in-the-wild web images, converting a unimodal olfactory dataset into a cross-modal benchmark without costly co-collection. Building on this dataset, we propose See & Sniff, a self-supervised framework that learns joint visuo-olfactory representations via dense local alignment and naturally produces smell saliency maps for spatial grounding of odor sources. We further introduce pixel-level smell localization task and a benchmark for evaluation. Our method surpasses smell-only baselines by 7% in smell classification from smell alone and generalizes to cross-modal retrieval and smell localization, establishing visuo-olfactory learning as a new direction in multimodal perception.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。
