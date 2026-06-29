---
title: 'SingGuard: A Policy-Adaptive Multimodal LLM Guardrail with Dynamic Reasoning'
title_zh: 'SingGuard: A Policy-Adaptive Multimodal LLM Guardr'
authors:
- SingGuard Team
arxiv_id: '2606.22873'
url: https://arxiv.org/abs/2606.22873
pdf_url: https://arxiv.org/pdf/2606.22873
published: '2026-06-21'
collected: '2026-06-29'
category: RecSys
direction: RecSys
tags:
- RecSys
- LLM
one_liner: Vision-language models (VLMs) are increasingly deployed in consumer, medical,
  financial, and en...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 10
source: huggingface-daily
depth: abstract
---

### 摘要

Vision-language models (VLMs) are increasingly deployed in consumer, medical, financial, and enterprise applications. This broad deployment expands the safety surface: risks can arise from multimodal question answering, assistant responses, and cross-modal composition, while moderation policies may vary across products, regions, and deployment stages. Most existing guardrails either rely on fixed taxonomies or target only a narrow set of interaction settings, which limits their adaptability when safety rules change at deployment time. We present SingGuard, a policy-adaptive multimodal guardrail model family for safety assessment in multimodal conversations. SingGuard treats the active policy as a runtime input: given natural-language rules, it checks the target content against the active policy rule by rule and predicts both the safety label and the triggered rule. To balance efficiency and interpretability, SingGuard supports fast, hybrid, and slow inference regimes along a fast-to-slow reasoning spectrum, ranging from direct safety judgments to policy-grounded deliberation. We further optimize this behavior with fast--slow decoupled reinforcement learning. We also introduce SingGuard-Bench, a multimodal guardrail benchmark with 56{,}340 examples spanning 80+ fine-grained risk types across multimodal QA, adversarial attack, and dynamic-rule evaluation settings, including cross-modal joint-risk cases where each modality is harmless in isolation but their composition implies unsafe intent. Across six benchmark families (35 datasets), SingGuard achieves state-of-the-art average F1 in every family. Dynamic-rule evaluation further shows improved policy-following accuracy from 0.6465 to 0.7415 under runtime policy shifts. Our code is available at https://github.com/inclusionAI/Sing-Guard.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
