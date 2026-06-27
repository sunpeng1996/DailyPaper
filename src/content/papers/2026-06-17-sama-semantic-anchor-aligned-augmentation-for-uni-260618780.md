---
title: 'SAMA: Semantic Anchor-aligned Augmentation for Unified Low-Resource Multimodal
  Information Extraction'
title_zh: 'SAMA: Semantic Anchor-aligned Augmentation for Uni'
authors:
- Quanjiang Guo
- Chong Mu
- Jiazhou Pan
- Ming Jia
- Ling Tian
- Hui Gao
- Zhao Kang
arxiv_id: '2606.18780'
url: https://arxiv.org/abs/2606.18780
pdf_url: https://arxiv.org/pdf/2606.18780
published: '2026-06-17'
collected: '2026-06-27'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: Multimodal Information Extraction (MIE)-covering tasks such as Multimodal
  Named Entity Recognit...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: arxiv-cs.MM
depth: abstract
---

### 摘要

Multimodal Information Extraction (MIE)-covering tasks such as Multimodal Named Entity Recognition (MNER), Relation Extraction (MRE), and Event Extraction (MEE)-is essential for understanding multimedia content but remains constrained by severe data scarcity. Although data augmentation is a promising remedy, existing approaches are impeded by coarse cross-modal alignment and fragmented, task-specific designs that fail to exploit shared semantic knowledge. To overcome these limitations, we introduce Semantic Anchor-aligned Multimodal Augmentation (SAMA), a unified framework for generating high-fidelity, task-aware synthetic data. SAMA constructs structured semantic anchors from ground-truth labels to guide a Collaborative Multi-Experts Multimodal Large Language Model (CME-MLLM), which integrates a Universal Adapter for shared semantics with Task-Specific Adapters to produce diverse yet constraint-compliant textual samples. For image synthesis, SAMA employs an Anchor-Preserving Diffusion mechanism that uses anchor-weighted prompts and latent conditioning to maintain critical semantic anchors while diversifying visual contexts. To eliminate the need for manual verification, SAMA further introduces a Dual-Constraint Filtering module that selects synthetic samples based on both cross-modal consistency and anchor fidelity. Extensive experiments across benchmark datasets for MNER, MRE, and MEE demonstrate that SAMA consistently outperforms state-of-the-art augmentation baselines under both fully supervised and low-resource settings, underscoring its versatility, robustness, and effectiveness.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。
