---
title: Cognitive Episodes in LLM Reasoning Traces Enable Interpretable Human Item
  Difficulty Prediction
title_zh: Cognitive Episodes in LLM Reasoning Traces Enable
authors:
- Chenguang Wang
- Ming Li
- Xinyue Zeng
- Zhuochun Li
- Hong Jiao
- Tianyi Zhou
- Dawei Zhou
arxiv_id: '2606.28186'
url: https://arxiv.org/abs/2606.28186
pdf_url: https://arxiv.org/pdf/2606.28186
published: '2026-06-26'
collected: '2026-06-29'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: Predicting human item difficulty is central to educational assessment,
  where reliable estimates...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 摘要

Predicting human item difficulty is central to educational assessment, where reliable estimates support fairness and effective test construction. Existing methods often depend on costly human calibration or item-level textual representations, providing limited evidence about the cognitive processes that make items difficult. We argue that difficulty should be viewed not only as a property of item text, but also as an observable consequence of the problem-solving burden an item induces. Large Reasoning Models (LRMs) offer scalable process evidence through reasoning traces, but such evidence must be structured to support interpretable modeling. To this end, we introduce Epi2Diff (Episode to Difficulty), a framework that maps LRM reasoning traces into cognitively grounded episode sequences. These episodes group trace segments into functional problem-solving states, enabling difficulty to be modeled through reasoning scale, effort allocation, and state transitions. Epi2Diff extracts compact episode-dynamic features and combines them with semantic item representations for human difficulty prediction. Experiments on four real-world human difficulty datasets show that Epi2Diff consistently outperforms strong baselines, including fine-tuned small language models, LLM in-context learning, and supervised LLM adaptation. On SAT-derived classification benchmarks, Epi2Diff achieves an 8.1% average relative gain over supervised LLM fine-tuning baselines. Further analyses show that harder items induce more effortful, iterative, and implementation-centered episode dynamics, rather than merely longer responses. These results demonstrate that cognitive episodes in LRM reasoning traces provide a predictive and interpretable process representation for human item difficulty, offering a new lens for educational measurement with reasoning models.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
