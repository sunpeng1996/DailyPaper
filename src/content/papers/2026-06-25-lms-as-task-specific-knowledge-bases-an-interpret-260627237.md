---
title: 'LMs as Task-Specific Knowledge Bases: An Interpretability Analysis'
title_zh: 'LMs as Task-Specific Knowledge Bases: An Interpret'
authors:
- Amit Elhelo
- Amir Globerson
- Mor Geva
arxiv_id: '2606.27237'
url: https://arxiv.org/abs/2606.27237
pdf_url: https://arxiv.org/pdf/2606.27237
published: '2026-06-25'
collected: '2026-06-27'
category: Training
direction: Training
tags:
- Training
- LLM
one_liner: Language models (LMs) capture large amounts of factual knowledge applicable
  to a wide range of...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 摘要

Language models (LMs) capture large amounts of factual knowledge applicable to a wide range of tasks, motivating the view of their parameters as a knowledge base. An important property of knowledge bases is that different queries for the same fact return consistent results, drawing on a single source of truth. We investigate whether LMs satisfy this property through behavioral and mechanistic analyses. Our results suggest that they encode knowledge in a task-specific manner. Behaviorally, facts acquired on one task frequently fail to co-emerge on others during training. Parameter localization experiments suggest a mechanistic explanation, revealing distinct parameter subsets underlying different tasks for the same fact. Finally, we show that chain-of-thought reasoning draws part of its effectiveness from engaging task-specific parameters beyond those tied to the evaluation task. Our findings suggest that what the model knows and how it is asked are intertwined in parameter space, undermining the "knowledge base" analogy and carrying implications for the reliability and controllability of factual knowledge in LMs.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
