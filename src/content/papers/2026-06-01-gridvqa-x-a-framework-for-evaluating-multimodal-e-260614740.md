---
title: 'GridVQA-X: A Framework for Evaluating Multimodal Explainability Methods'
title_zh: 'GridVQA-X: A Framework for Evaluating Multimodal E'
authors:
- Sujay Belsare
- Sudarshan Nikhil
- Sushant Kumar
- Ponnurangam Kumaraguru
- Chirag Agarwal
arxiv_id: '2606.14740'
url: https://arxiv.org/abs/2606.14740
pdf_url: https://arxiv.org/pdf/2606.14740
published: '2026-06-01'
collected: '2026-06-26'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: With the increasing development of Vision-Language Models, it becomes imperative
  that their pre...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 9
source: huggingface-daily
depth: abstract
---

### 摘要

With the increasing development of Vision-Language Models, it becomes imperative that their predictions are readily explainable to relevant stakeholders. However, the field of explainability has not kept pace with the multimodal surge. While recent Multimodal Explainable AI (MxAI) methods generate explanations to attribute the interaction between different modalities, current evaluation protocols lack the ground truth required to distinguish between true cross-modal reasoning (e.g., spatial composition) and shallow cross-modal shortcuts (e.g., Bag-of-Words attribute matching). It remains unknown whether MxAI methods faithfully capture synergistic interactions or merely hallucinate reasoning on models acting as simple feature detectors. In this paper, we introduce GridVQA-X, the first diagnostic framework specifically designed to evaluate cross-modal explainability. Unlike natural datasets, GridVQA-X leverages a closed-world synthesis logic to generate unique, mathematically guaranteed explanations. We utilize this controlled environment to train paired ground-truth models on identical architectures: M_{pure}, which learns robust spatial-relational reasoning and M_{spur}, which is structurally forced to rely on cross-modal shortcuts. This behavioral divergence creates a rigorous testbed: a faithful explainer must report distinct reasoning pathways for each model. Our findings reveal that widely used methods fail to distinguish between models relying on genuine spatial-relational reasoning and those exploiting cross-modal shortcuts, highlighting a critical gap in capturing true cross-modal synergy and misrepresenting how multimodal models actually make decisions.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。
