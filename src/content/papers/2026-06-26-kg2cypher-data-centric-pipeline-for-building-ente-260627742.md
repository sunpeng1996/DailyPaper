---
title: 'KG2Cypher: Data-Centric Pipeline for Building Enterprise Text-to-Cypher Systems'
title_zh: 'KG2Cypher: Data-Centric Pipeline for Building Ente'
authors:
- Minjun Choi
- Yerin Kim
- Junghyuk Seo
- Sujin Mo
- Hyemin Lee
- Youngjoong Ko
arxiv_id: '2606.27742'
url: https://arxiv.org/abs/2606.27742
pdf_url: https://arxiv.org/pdf/2606.27742
published: '2026-06-26'
collected: '2026-06-29'
category: QueryRec
direction: QueryRec
tags:
- QueryRec
- LLM
one_liner: Enterprise Knowledge Graphs (KGs) are increasingly used for internal search,
  analytics, and que...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 9
source: arxiv-cs.CL
depth: abstract
---

### 摘要

Enterprise Knowledge Graphs (KGs) are increasingly used for internal search, analytics, and question answering, but building natural-language interfaces for private enterprise graphs remains costly. We present KG2Cypher, a data-centric pipeline for building enterprise text-to-Cypher systems from existing KGs. KG2Cypher first constructs an executable Cypher query from observed graph facts and then uses LLMs to generate its associated natural-language question. The resulting Text-Cypher pairs are validated with an LLM judge and human validation, and are converted into candidate-aware SFT data. The trained generator is served with class-conditioned schema prompting, entity retrieval, and LoRA-based inference. We evaluate KG2Cypher in Korean enterprise settings, where short search-style queries and schema paraphrases make language grounding difficult. LoRA SFT improves execution-result F1 from 0.806 to 0.950 on broadcast-program queries and from 0.70 to 0.92 on company queries. In an 11-class setting, KG2Cypher achieves 95.2% exact match, 99.9% execution rate, and 0.964 execution-result F1.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
