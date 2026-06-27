---
title: 'DomainShuttle: Freeform Open Domain Subject-driven Text-to-video Generation'
title_zh: 'DomainShuttle: Freeform Open Domain Subject-driven'
authors:
- Nan Chen
- Yiyang Cai
- Rongchang Xie
- Junwen Pan
- Cheng Chen
- Weinan Jia
- Zhuowei Chen
- Wen Zhou
- Zhenbang Sun
- Wenhan Luo
arxiv_id: '2606.26058'
url: https://arxiv.org/abs/2606.26058
pdf_url: https://arxiv.org/pdf/2606.26058
published: '2026-06-23'
collected: '2026-06-27'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: Open domain subject-driven text-to-video (S2V) generation has drawn significant
  interest in aca...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: huggingface-daily
depth: abstract
---

### 摘要

Open domain subject-driven text-to-video (S2V) generation has drawn significant interest in academia and industry. Open domain S2V mainly involves two scenarios: in-domain, which requires retaining the reference subject features as much as possible, and cross-domain, which preserves the intrinsic features of the subject while allowing subject-irrelevant properties to vary flexibly according to the text prompt. Existing methods primarily focus on maximizing subject fidelity in in-domain scenarios, which limits their editability and adaptability in cross-domain scenarios, such as novel styles, semantic combinations, or domain attributes. In this study, we propose that an ideal S2V method should flexibly shuttle between different domains, achieving strong performance in both in-domain and cross-domain scenarios. To this end, we propose DomainShuttle, which could achieve high fidelity and generative flexibility for open domain video personalization. Specifically, we introduce Domain-MoT, which decouples videos and reference features and introduces the domain-aware AdaLN for domain-specific modeling of reference images. We then introduce the Video-Reference DualRoPE scheme, which places reference image tokens and video tokens in separate RoPE spaces to enable precise subject-level spatial modeling, and Cross-Pair Consistent Loss, which aims to extract intrinsic subject features unaffected by irrelevant features. Extensive experiments demonstrate that DomainShuttle achieves significant performance improvements over existing methods, exhibiting high subject fidelity and generative flexibility across diverse open domain application scenarios.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。
