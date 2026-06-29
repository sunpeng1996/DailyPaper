---
title: Can LLMs Judge Better Than They Generate? Evaluating Task Asymmetry, Mechanistic
  Interpretability and Transferability for In-Context QA
title_zh: Can LLMs Judge Better Than They Generate? Evaluati
authors:
- Sambaran Bandyopadhyay
arxiv_id: '2606.28050'
url: https://arxiv.org/abs/2606.28050
pdf_url: https://arxiv.org/pdf/2606.28050
published: '2026-06-26'
collected: '2026-06-29'
category: Training
direction: Training
tags:
- Training
- LLM
one_liner: LLM-as-a-Judge and self-evaluation pipelines implicitly assume that evaluation
  is easier than g...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 摘要

LLM-as-a-Judge and self-evaluation pipelines implicitly assume that evaluation is easier than generation. We test this in a controlled in-context QA setting where a context passage is the sole information source and each model judges the answer it generated, removing the parametric-knowledge confound of open-domain comparisons. Across four benchmarks (SQuAD 2.0, DROP, HotpotQA, MuSiQue) and two models, evaluation is not uniformly easier: generation accuracy exceeds self-evaluation on three of four, with multi-hop MuSiQue the exception. Attention analysis reveals why: evaluation attends to context 3--5x less than generation does and barely reads the candidate answer. LoRA fine-tuning confirms the asymmetry is not a training artifact: generation fine-tuning induces over-acceptance and evaluation fine-tuning degrades generation. These findings challenge core assumptions in self-evaluation pipelines.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
