---
title: Explaining Temporal Graph Neural Networks via Feature-induced Information Flow
title_zh: Explaining Temporal Graph Neural Networks via Feat
authors:
- Ping Xiong
- Thomas Schnake
- Klaus-Robert Müller
- Shinichi Nakajima
arxiv_id: '2606.27201'
url: https://arxiv.org/abs/2606.27201
pdf_url: https://arxiv.org/pdf/2606.27201
published: '2026-06-25'
collected: '2026-06-27'
category: RecSys
direction: RecSys
tags:
- RecSys
- LLM
one_liner: Event-based Temporal Graph Neural Networks (ETGNNs) have demonstrated strong
  performance across...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: arxiv-cs.LG
depth: abstract
---

### 摘要

Event-based Temporal Graph Neural Networks (ETGNNs) have demonstrated strong performance across a wide range of applications, including social network analysis, epidemic tracing, recommender systems, and political event forecasting. However, their increasing complexity poses significant challenges for explainability. Existing explanation methods focus only on a subset of the information flow within ETGNNs, typically tracing contributions from the event-related embeddings to the output. Consequently, they overlook the important pathways through event-induced variables, which mediate interactions between nodes and thereby play a central role in capturing long-range temporal dependencies. To overcome this limitation, we propose a novel attribution method that analyzes the \emph{entire} information flow through all event-associated variables. Our method is built upon the recent Normalized Relevance Measure (NRM) framework, which enables explicit quantification of information flow originating from event embeddings as well as information flow passing through event-induced variables. It also ensures comparability of latent variables across layers, and supports higher-order analysis of interactions between events. To handle the architectural complexity of ETGNNs, we extend the NRM framework with a modular decomposition procedure that facilitates the systematic construction of relevance structure for complex neural architectures. We evaluate our approach on two synthetic datasets for epidemic tracing and social dynamics, as well as a real-world dataset of political event networks. Our qualitative and quantitative experiments show that our method consistently outperforms existing explanation approaches while producing more human-interpretable explanations.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。
