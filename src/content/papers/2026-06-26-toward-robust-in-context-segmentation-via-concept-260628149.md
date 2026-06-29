---
title: Toward Robust In-Context Segmentation via Concept Guidance
title_zh: Toward Robust In-Context Segmentation via Concept
authors:
- Zhigang Chen
- Xiawu Zheng
- Rongrong Ji
arxiv_id: '2606.28149'
url: https://arxiv.org/abs/2606.28149
pdf_url: https://arxiv.org/pdf/2606.28149
published: '2026-06-26'
collected: '2026-06-29'
category: QueryRec
direction: QueryRec
tags:
- QueryRec
- LLM
one_liner: In-context segmentation (ICS) requires a model to segment target regions
  in a query image using...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 10
source: arxiv-cs.AI
depth: abstract
---

### 摘要

In-context segmentation (ICS) requires a model to segment target regions in a query image using only a few reference images and their corresponding masks, without updating any parameters. Despite recent progress, prior ICS studies have largely overlooked a critical aspect: system robustness, ie, whether the model can produce stable segmentation results for the same query under different references. In this work, we revisit ICS from the robustness perspective and introduce a novel paradigm, Concept-Guided In-Context Segmentation (CG-ICS), which performs segmentation by extracting high-level semantic concepts from references rather than relying solely on low-level visual matching. Specifically, CG-ICS introduces a concept reasoning module that uses an MLLM to propose candidates and a SAM3-driven scoring function with tree-search refinement to select reliable textual concepts, together with a parallel visual exemplar route that provides query-side spatial grounding via a simple context construction. Both the textual concept and the visual exemplar are then used to activate the segmentation capability of a frozen SAM3 backbone. Extensive experiments on standard ICS benchmarks demonstrate that CG-ICS not only achieves state-of-the-art accuracy but also substantially improves robustness, yielding a more reliable ICS system with significantly reduced variance across diverse reference choices.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
