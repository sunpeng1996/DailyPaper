---
title: Unified Multimodal Model for Brain MRI Imputation and Understanding
title_zh: Unified Multimodal Model for Brain MRI Imputation
authors:
- Zhiyun Song
- Che Liu
- Tian Xia
- Avinash Kori
- Wenjia Bai
arxiv_id: '2606.16484'
url: https://arxiv.org/abs/2606.16484
pdf_url: https://arxiv.org/pdf/2606.16484
published: '2026-06-15'
collected: '2026-06-27'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: Multimodal large language models (MLLMs) hold great potential for medicine,
  as they inherit kno...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: arxiv-cs.MM
depth: abstract
---

### 摘要

Multimodal large language models (MLLMs) hold great potential for medicine, as they inherit knowledge from LLM and allow multiple data modalities to be integrated, analysed and interpreted in natural language. However, the field of medical MLLMs is constrained by non-trivial challenges, notably the scarcity of high-quality training data and the frequent occurrence of missing data in the real-world clinical setting. Here, we propose a novel unified multimodal model, UniBrain, for brain magnetic resonance image (MRI) analysis. To address potential missing brain MRI modalities, we employ a unified training strategy to perform joint imaging modality imputation and brain image understanding. During training, an interleaved and description-enriched data flow is constructed to train the model in an autoregressive manner, enabling medical reasoning with generated multimodal data. A self-alignment strategy is introduced to leverage dense image embeddings to learn fine-grained anatomical features without requiring detailed image captions. Furthermore, we propose a dynamic hidden state mechanism to alleviate the exposure bias during long-context multimodal inference. Extensive experiments on multi-disease brain MRI dataset demonstrate that UniBrain achieves high performance for brain image imputation, understanding, and disease diagnosis under various extents of modality incompleteness.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。
