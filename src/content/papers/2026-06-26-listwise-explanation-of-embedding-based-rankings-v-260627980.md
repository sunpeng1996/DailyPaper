---
title: Listwise Explanation of Embedding-Based Rankings via Semantic Chunk Grouping
title_zh: Listwise Explanation of Embedding-Based Rankings v
authors:
- Hyunkyu Kim
- Yeeun Yoo
- Youngjun Kwak
arxiv_id: '2606.27980'
url: https://arxiv.org/abs/2606.27980
pdf_url: https://arxiv.org/pdf/2606.27980
published: '2026-06-26'
collected: '2026-06-29'
category: RecSys
direction: RecSys
tags:
- RecSys
- LLM
one_liner: Dense embedding rankers score documents through contextual sentence- and
  passage-level represen...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 摘要

Dense embedding rankers score documents through contextual sentence- and passage-level representations. Yet many listwise explanation methods still attribute rankings to isolated words. This feature-unit mismatch leaves word-level features too fragmented for dense semantic ranking. We introduce ChunkGroupSHAP, a listwise Shapley method that clusters semantically related chunks into shared cross-document features. Masking a group perturbs all documents with related evidence, attributing rankings at a granularity closer to dense representations while preserving the listwise setup. Our findings across MS MARCO, FinanceBench, AILACaseDocs, and FinQA with E5 rankers and BM25 show that the best explanation unit is setting-dependent: word features for lexical BM25, corpus-level groups for dense rankers, and query-local grouping for heterogeneous web retrieval. Feature units should thus follow both the ranker's representational granularity and the structure of the retrieved corpus.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
