---
title: 'STAG: Spatio-temporal Evolving Structural Representation of Action Units for
  Micro-expression Recognition'
title_zh: 'STAG: Spatio-temporal Evolving Structural Represen'
authors:
- Nandani Sharma
- Varun Sharma
- Dinesh Singh
arxiv_id: '2606.28083'
url: https://arxiv.org/abs/2606.28083
pdf_url: https://arxiv.org/pdf/2606.28083
published: '2026-06-26'
collected: '2026-06-29'
category: Reasoning
direction: Reasoning
tags:
- Reasoning
- LLM
one_liner: Micro-expression recognition is challenging due to subtle and short-lived
  facial muscle movemen...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 摘要

Micro-expression recognition is challenging due to subtle and short-lived facial muscle movements. Existing methods rely heavily on apex-onset frames, overlook fine-grained inter-frame dynamics, and separately model spatial and temporal information, limiting generalization across datasets. To address these challenges, we propose STAG, a dynamic ROI-AU-coupled spatial-temporal network that jointly models motion flow and adaptive facial connectivity. The framework extracts optical flow from discriminative frames using magnitude-based selection and temporal attention. A dual-branch architecture combines an enhanced graph attention network for structured spatial reasoning with a transformer encoder for temporal modeling. A bidirectional cross-attention module enables mutual refinement of spatial and temporal features, while AU-guided dynamic connectivity adapts facial region interactions according to muscle activation patterns. The transformer captures subtle temporal dynamics beyond apex-based approaches, improving semantic consistency and interpretability for explainable micro-expression recognition. The fused representation is optimized using focal loss and evaluated on CASME II, 4DME, DFME, NaME, SAMM, and SMIC-HS. Extensive experiments demonstrate improved robustness, generalization, interpretability, and computational efficiency, confirming the effectiveness of adaptive relational reasoning, AU-guided dynamic connectivity, and deep spatial-temporal feature fusion for accurate cross-dataset micro-expression recognition.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
