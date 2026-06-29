---
title: Context-Aware Explanations for Spatialized Document Layouts
title_zh: Context-Aware Explanations for Spatialized Documen
authors:
- Wei Liu
- John Wenskovitch
- Chris North
- Rebecca Faust
arxiv_id: '2606.28081'
url: https://arxiv.org/abs/2606.28081
pdf_url: https://arxiv.org/pdf/2606.28081
published: '2026-06-26'
collected: '2026-06-29'
category: LLM
direction: LLM
tags:
- LLM
- AI
one_liner: Spatialized document layouts are widely used for exploratory analysis of
  text corpora, but inte...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 摘要

Spatialized document layouts are widely used for exploratory analysis of text corpora, but interpreting the spatial organization of documents and the relationships between regions remains challenging. Existing approaches primarily summarize document content or explain how layouts are generated, providing limited support for understanding spatial relationships within the layout itself. We present CAPE, a context-aware explanation framework that generates natural-language explanations grounded in both document semantics and layout-derived spatial context. CAPE identifies salient spatial patterns (e.g., clusters, subgroups, outliers, and bridging documents) and constructs multi-level contextual representations to guide LLM-based explanation generation. It supports both AI-guided overview and user-driven exploration, with explanations available at multiple levels of detail. We demonstrate CAPE on news and scholarly document layouts and evaluate it in a controlled user study against keyword-based and content-only LLM baselines. Our results suggest that spatially grounded explanations are perceived as more helpful than content-only baselines for interpreting the spatial organization of document layouts.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
