---
title: 'Robust Harmful Features Under Jailbreak Attacks: Mechanistic Evidence from
  Attention Head Specialization in Large Language Models'
title_zh: 'Robust Harmful Features Under Jailbreak Attacks: M'
authors:
- Yanchen Yin
- Dongqi Han
- Linghui Li
arxiv_id: '2606.28153'
url: https://arxiv.org/abs/2606.28153
pdf_url: https://arxiv.org/pdf/2606.28153
published: '2026-06-26'
collected: '2026-06-29'
category: Training
direction: Training
tags:
- Training
- LLM
one_liner: Jailbreak attacks bypass LLM safety alignment, yet their mechanisms remain
  poorly understood. W...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 摘要

Jailbreak attacks bypass LLM safety alignment, yet their mechanisms remain poorly understood. We provide evidence that attacks do not comprehensively eliminate safety features, but instead selectively suppress specific attention heads. We identify two functionally differentiated types: Adversarially Compromised Heads (ACHs) concentrated in early layers, which are suppressed under attacks, and Safety-Aligned Heads (SAHs) in mid-layers, which maintain robust activations even when attacks succeed. Ablation studies support the causal role of ACHs and the contribution of SAHs to robust activations: suppressing a small number of ACHs is sufficient to induce jailbreak-like behavior on normally refused inputs, while removing SAHs substantially weakens mid-layer safety activations. Token-level attribution further shows that ACH suppression is driven specifically by attack-template tokens, providing a mechanistic account of why attacks can bypass refusal decisions through ACH suppression while leaving internal safety signals sustained by SAHs -- a phenomenon we term Robust Harmful Features. To validate the practical significance of this robustness, we show that simply reading these persistent activations -- without any training -- yields competitive aggregate detection performance with strong adversarial robustness.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
