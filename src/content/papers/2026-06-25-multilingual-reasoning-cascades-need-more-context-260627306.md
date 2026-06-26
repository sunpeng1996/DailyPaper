---
title: Multilingual Reasoning Cascades Need More Context
title_zh: Multilingual Reasoning Cascades Need More Context
authors:
- Arnav Mazumder
- Dengjia Zhang
- Shuyue Stella Li
- Yulia Tsvetkov
- Niyati Bafna
arxiv_id: '2606.27306'
url: https://arxiv.org/abs/2606.27306
pdf_url: https://arxiv.org/pdf/2606.27306
published: '2026-06-25'
collected: '2026-06-26'
category: QueryRec
direction: QueryRec
tags:
- QueryRec
- LLM
one_liner: Translation cascades for reasoning translate the query from another language
  to English, reason...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 9
source: arxiv-cs.CL
depth: abstract
---

### 摘要

Translation cascades for reasoning translate the query from another language to English, reason in English, and translate the answer back to the original language. This is a competitive approach to multilingual reasoning, but structurally lossy, since each stage discards information later stages may need, including cues for cultural grounding, register, and disambiguation. We examine the benefits of a simple and training-free intervention: a context-aware translation cascade, which additionally provides the original question, the English translated question, and the reasoning trace to the context of the final translation module. We evaluate gains across nine multilingual benchmarks including various task types, three backbone models, and 285 high-, mid-, and low-resource languages, and demonstrate strong gains for open-ended generation across models and resource regimes. We show that the original language question carries most of the beneficial context. Our study emphasizes the need to better design information flow in machine translation cascades for mitigating error propagation, and provides a simple and actionable default strategy: preserve the original user question until the end of the pipeline.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。
