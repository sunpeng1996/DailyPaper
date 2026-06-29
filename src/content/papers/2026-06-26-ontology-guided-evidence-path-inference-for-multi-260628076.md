---
title: Ontology-Guided Evidence Path Inference for Multi-hop Knowledge Graph Question
  Answering
title_zh: Ontology-Guided Evidence Path Inference for Multi-
authors:
- Yongxue Shan
- Meihan Wu
- Cundi Fang
- Jie Peng
- Xiaodong Wang
arxiv_id: '2606.28076'
url: https://arxiv.org/abs/2606.28076
pdf_url: https://arxiv.org/pdf/2606.28076
published: '2026-06-26'
collected: '2026-06-29'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: Knowledge graph question answering (KGQA) aims to answer natural-language
  questions by reasonin...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 9
source: arxiv-cs.AI
depth: abstract
---

### 摘要

Knowledge graph question answering (KGQA) aims to answer natural-language questions by reasoning over structured facts. Existing multi-hop KGQA methods mainly rely on topic-centered expansion, which faces two key challenges: the search space rapidly grows with noisy mixed-type paths, and retrieved paths may fail to satisfy the semantic constraints of complex questions. To address these challenges, we propose OPI, an ontology-guided evidence path inference framework for multi-hop KGQA. OPI introduces a relation-centric ontology graph to capture the head-tail type constraints of relations, providing a compact interface for answer-side constraints. Based on this ontology graph, OPI first introduces a bidirectional retrieval mechanism by mapping the predicted answer type to compatible final-hop relations and combining topic-side prefix expansion with answer-side final-hop matching, thereby suppressing noisy mixed-type expansion. OPI further adopts an iterative refinement strategy to reassess retrieved paths and candidate answers under the question context, filtering type-compatible but question-irrelevant evidence for more reliable answer prediction. Experiments on WebQSP, CWQ, and MetaQA show that OPI substantially reduces the search space, improves Hit@1/F1 by 4.6/5.0 points on WebQSP and 8.9/3.3 points on CWQ over the strongest prior results, and achieves near-saturated Hit@1 on MetaQA with the retrieval module alone.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
