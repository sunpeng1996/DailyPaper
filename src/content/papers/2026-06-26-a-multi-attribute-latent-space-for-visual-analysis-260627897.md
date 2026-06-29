---
title: A Multi-Attribute Latent Space for Visual Analysis of Watches
title_zh: A Multi-Attribute Latent Space for Visual Analysis
authors:
- Kai Lawonn
- Tobias Günther
- Monique Meuschke
arxiv_id: '2606.27897'
url: https://arxiv.org/abs/2606.27897
pdf_url: https://arxiv.org/pdf/2606.27897
published: '2026-06-26'
collected: '2026-06-29'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: We present a design rationale, embedding model, and interactive visual-analysis
  system for expl...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: arxiv-cs.HC
depth: abstract
---

### 摘要

We present a design rationale, embedding model, and interactive visual-analysis system for exploring large wristwatch collections through heterogeneous visual and semantic attributes. The system addresses a common limitation of catalog and e-commerce interfaces: users can filter by metadata, but they receive little support for open-ended exploration of visual similarity, stylistic alternatives, and mixed aesthetic-functional criteria. We therefore represent watches with separate attribute graphs for dial color and dial design, while using watch type as an explicit semantic organizer. Dials are segmented with a U-Net, watch types are predicted with a Vision Transformer, colors are represented through a shared CIELAB reference palette, and dial structure is described with a gradient-based image descriptor. We extend UMAP by combining attribute-specific neighborhood graphs in a unified probabilistic objective and by adding a class-aware layout term that separates global type structure from local visual neighborhoods. The resulting map is exposed in an interactive interface with spatial navigation, metadata filtering, detail inspection, and search-by-example insertion. We evaluate the approach through parameter analysis, runtime measurements, and a qualitative pilot study with watch experts and novices. The results suggest that the system supports discovery and comparison, while also revealing limitations in scalability assessment, search-by-example validation, and the need for broader domain studies. We explicitly discuss these limitations and derive design implications for multi-attribute latent-space visualization across heterogeneous visual collections.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
