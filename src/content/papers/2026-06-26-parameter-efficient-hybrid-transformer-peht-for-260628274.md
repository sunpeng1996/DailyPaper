---
title: Parameter Efficient Hybrid Transformer (PEHT) for Network Traffic Prediction
  via Dynamic Urban Congestion Integration
title_zh: Parameter Efficient Hybrid Transformer (PEHT) for
authors:
- Abdolazim Rezaei
- Mehdi Sookhak
- Mahboobeh Haghparast
arxiv_id: '2606.28274'
url: https://arxiv.org/abs/2606.28274
pdf_url: https://arxiv.org/pdf/2606.28274
published: '2026-06-26'
collected: '2026-06-29'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: Accurate network traffic prediction is a critical element for efficient
  resource allocation in...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 摘要

Accurate network traffic prediction is a critical element for efficient resource allocation in dynamic urban cellular networks. However, prediction remains challenging because network demand is influenced by complex mobility patterns, congestion dynamics, and heterogeneous user behavior. This paper introduces the Parameter-Efficient Hybrid Transformer (PEHT), a network traffic prediction framework that integrates urban mobility and congestion information into a Transformer-based architecture. PEHT separates primary network communication features from secondary urban mobility features and incorporates Low-Rank Adaptation (LoRA) into the Transformer encoder to reduce the number of trainable parameters while maintaining high predictive accuracy. A multimodal fusion strategy then injects external mobility and congestion features into the decoder to improve traffic forecasting. Experiments on the Telecom Italia Milan dataset and multiple synthetic congestion scenarios show that PEHT outperforms state-of-the-art baselines in terms of RMSE, MAE, and $R^2$. The implementation is available in the GitHub repository.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
