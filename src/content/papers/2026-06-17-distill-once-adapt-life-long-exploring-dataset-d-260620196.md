---
title: 'Distill Once, Adapt Life-Long: Exploring Dataset Distillation for Continual
  Test-Time Adaptation'
title_zh: 'Distill Once, Adapt Life-Long: Exploring Dataset D'
authors:
- Hyun-Kurl Jang
- Jihun Kim
- Hyeokjun Kweon
- Kuk-Jin Yoon
arxiv_id: '2606.20196'
url: https://arxiv.org/abs/2606.20196
pdf_url: https://arxiv.org/pdf/2606.20196
published: '2026-06-17'
collected: '2026-06-26'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: Continual Test-Time Adaptation (CTTA) aims to maintain model performance
  under evolving target...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: huggingface-daily
depth: abstract
---

### 摘要

Continual Test-Time Adaptation (CTTA) aims to maintain model performance under evolving target domains by adapting online without labeled data. However, practical deployments often cannot retain the source dataset due to privacy or licensing constraints, and purely source-free CTTA methods tend to become unstable under long-term distribution shift, suffering from compounding self-training errors and catastrophic forgetting. We introduce DO-ALL (Distill Once, Adapt Life-Long), a plug-and-play framework that revisits source information in a compact and privacy-conscious form via Dataset Distillation (DD). Before deployment, DO-ALL performs DD to produce a small set of synthetic distilled anchors that summarize the source distribution. During adaptation, each target sample is matched with its most semantically aligned anchor, which provides a stable reference for various CTTA via source replay, representation alignment, and manifold-smoothing regularization. DO-ALL can be seamlessly integrated into existing CTTA algorithms, consistently improving long-term robustness across CIFAR100-C, ImageNet-C, and the CCC benchmark. This demonstrates the potential of leveraging DD to enable stable and continuous adaptation without retaining raw source data. The code is available at https://github.com/blue-531/DOALL.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。
