---
title: Mapping Political-Elite Networks in Europe with a Multilingual Joint Entity-Relation
  Extraction Pipeline
title_zh: Mapping Political-Elite Networks in Europe with a
authors:
- Kirill Solovev
- Jana Lasser
arxiv_id: '2606.27347'
url: https://arxiv.org/abs/2606.27347
pdf_url: https://arxiv.org/pdf/2606.27347
published: '2026-06-25'
collected: '2026-06-27'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: Whether political elites organise into rent-seeking coalitions that capture
  public resources or...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 摘要

Whether political elites organise into rent-seeking coalitions that capture public resources or civic networks that sustain governance is a central question in comparative politics. Yet observing these complex, informal, and adversarial ties at scale has historically required intensive manual coding, while automated text-as-data methods have largely been limited to simple co-occurrence. Recent large language model (LLM) approaches offer a path forward but often rely on proprietary APIs, lack cross-lingual capability, and struggle with scalable entity resolution. We present a modular, fully open-weight pipeline for multilingual joint entity-relation extraction that builds signed, temporal knowledge graphs from massive unstructured news corpora. It combines span-based named-entity recognition (NER) with a three-stage linking cascade mapping mentions to language-independent Wikidata identifiers; a high-throughput, ontology-constrained mixture-of-experts model then uses guided decoding to extract directed, signed relationships grounded in a domain ontology. A full-coverage spot-check against a 3491-relation gold standard shows high textual correctness (68.2% strict to 93.7% lenient). Two large-scale case studies validate the pipeline against the public record. In Austria, it reconstructs a political party's complete lifecycle, dating internal fractures and tracking personnel into successor factions and court convictions. In a Polish corpus, it uncovers the overlapping economic and governance networks of state-enterprise patronage, alongside the structurally balanced, signed conflict network of the polarized Civic Platform (Platforma Obywatelska, PO)--Law and Justice (Prawo i Sprawiedliwość, PiS) duopoly. By bridging raw multilingual text and structured relational data, our framework provides a robust, replicable foundation for cross-national empirical computational social science.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
