---
title: 'Extracting Problem and Method Sentence from Scientific Papers: A Context-enhanced
  Transformer Using Formulaic Expression Desensitization'
title_zh: Extracting Problem and Method Sentence from Scient
authors:
- Yingyi Zhang
- Chengzhi Zhang
arxiv_id: '2606.26481'
url: https://arxiv.org/abs/2606.26481
pdf_url: https://arxiv.org/pdf/2606.26481
published: '2026-06-25'
collected: '2026-06-27'
category: LLM
direction: LLM
tags:
- LLM
- AI
one_liner: Billions of scientific papers lead to the need to identify essential parts
  from the massive tex...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 摘要

Billions of scientific papers lead to the need to identify essential parts from the massive text. Scientific research is an activity from putting forward problems to using methods. To learn the main idea from scientific papers, we focus on extracting problem and method sentences. Annotating sentences within scientific papers is labor-intensive, resulting in small-scale datasets that limit the amount of information models can learn. This limited information leads models to rely heavily on specific forms, which in turn reduces their generalization capabilities. This paper addresses the problems caused by small-scale datasets from three perspectives: increasing dataset scale, reducing dependence on specific forms, and enriching the information within sentences. To implement the first two ideas, we introduce the concept of formulaic expression (FE) desensitization and propose FE desensitization-based data augmenters to generate synthetic data and reduce models' reliance on FEs. For the third idea, we propose a context-enhanced transformer that utilizes context to measure the importance of words in target sentences and to reduce noise in the context. Furthermore, this paper conducts experiments using large language model (LLM) based in-context learning (ICL) methods. Quantitative and qualitative experiments demonstrate that our proposed models achieve a higher macro F1 score compared to the baseline models on two scientific paper datasets, with improvements of 3.71% and 2.67%, respectively. The LLM based ICL methods are found to be not suitable for the task of problem and method extraction.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。
