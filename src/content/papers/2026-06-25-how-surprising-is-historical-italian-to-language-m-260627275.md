---
title: How Surprising Is Historical Italian to Language Models? Tokenization Tax,
  Comprehension Tax, and a Simple Mitigation
title_zh: How Surprising Is Historical Italian to Language M
authors:
- Maria Levchenko
arxiv_id: '2606.27275'
url: https://arxiv.org/abs/2606.27275
pdf_url: https://arxiv.org/pdf/2606.27275
published: '2026-06-25'
collected: '2026-06-27'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: Large language models (LLMs) are increasingly critical to digital library
  workflows, yet their...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 摘要

Large language models (LLMs) are increasingly critical to digital library workflows, yet their ability to process historical language remains poorly understood. Historical difficulty is typically treated as a monolithic barrier, conflating orthographic variation, linguistic distance, and pretraining exposure. In this paper, we propose a diagnostic framework that decomposes this difficulty into four distinct dimensions: tokenization cost, predictive uncertainty (surprisal), semantic robustness, and context sensitivity. We evaluate this framework on three datasets spanning three centuries: (1) a newly curated corpus of 17th-century Italian texts (1610-1689) digitized from original page images; (2) canonical 19th-century Italian "I Promessi Sposi" serving as a high-exposure control; and (3) 18th-century Russian civil print books as a contrastive orthographic stress test. Our results reveal a distinct dissociation between encoding cost and comprehension. While Russian and early modern Italian incur comparable tokenization penalties (25-30% inflation), their predictive difficulty diverges sharply. 17th-century Italian is on average 2.4 times more surprising than its modern equivalent - with academic prose reaching 3.2 times - whereas Russian shows only a modest increase. But predictive uncertainty does not imply representational degradation: embedding similarity remains robust (> 0.85) across all datasets, confirming that models can represent historical meaning even when generation is unstable. Finally, we demonstrate that a minimal temporal context prompt reduces historical surprisal by approximately 60%, offering a simple, model-agnostic mitigation. These findings suggest that while historical text imposes a consistent encoding tax, digital libraries can safely deploy LLMs for semantic retrieval tasks, provided that generative applications are carefully adapted.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
