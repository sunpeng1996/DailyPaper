---
title: 'ToxiREX: A Dataset on Toxic REasoning in ConteXt'
title_zh: 'ToxiREX: A Dataset on Toxic REasoning in ConteXt'
authors:
- Stefan F. Schouten
- Ilia Markov
- Piek Vossen
arxiv_id: '2606.27981'
url: https://arxiv.org/abs/2606.27981
pdf_url: https://arxiv.org/pdf/2606.27981
published: '2026-06-26'
collected: '2026-06-29'
category: Training
direction: Training
tags:
- Training
- LLM
one_liner: 'We introduce a new, contextual, multilingual dataset called ToxiREX: Toxic
  REasoning in ConteXt...'
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 摘要

We introduce a new, contextual, multilingual dataset called ToxiREX: Toxic REasoning in ConteXt. The dataset consists of threads of Reddit comments and structured characterizations of what the comments imply, following a systematic toxic reasoning schema developed in a previous paper. Using the schema allows us to capture and explain implicit and context-dependent toxicity, while supporting mappings to existing toxicity taxonomies. The dataset includes comments in six languages (English, Arabic, Turkish, Spanish, German, and Dutch), collected from posts connected to specific major events (e.g. the 2023 Turkey earthquakes; the Russian invasion of Ukraine). We describe the context-preserving preprocessing of the threads. We create a training set of 125 thousand comments which is annotated by a commercially available LLM, and a test set of just under three thousand comments that is annotated by native speakers. We show that apparent disagreements in the test set annotations often reflect defensible alternative interpretations rather than noise. Finally, we provide baseline results by prompting and fine-tuning language models. To produce these results, we develop evaluation strategies for our hierarchical, schema-based predictions. While models perform better than random, there remains a lot of room for improvement, showing the task to be challenging. ToxiREX is the first dataset to simultaneously incorporate multiple languages, conversational context, and implicit toxicity, while using the toxic reasoning schema for rich, structured annotations. Dataset available at: https://github.com/cltl/toxirex

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
