---
title: Investigating the Impact of Learner Errors on Social Bias in Large Language
  Models
title_zh: 学习者语法错误对大语言模型社会偏见的影响研究
authors:
- Federico Marcuzzi
- Martin Christoph
- Iryna Gurevych
- Alla Rozovskays
affiliations:
- INSAIT, Sofia University "St. Kliment Ohridski"
- Ubiquitous Knowledge Processing Lab (UKP Lab), TU Darmstadt
- National Research Center for Applied Cybersecurity ATHENE
- Queens College, City University of New York (CUNY)
arxiv_id: '2610.29896'
url: https://arxiv.org/abs/2610.29896
pdf_url: https://arxiv.org/pdf/2610.29896
published: '2026-10-21'
collected: '2026-10-23'
category: LLM
direction: 大语言模型 · 社会偏见评估与缓解
tags:
- LLM Bias
- Prompt Evaluation
- Social Bias
- Fine-tuning
- Non-native Input
one_liner: 发现非母语用户prompt语法错误会放大LLM社会偏见，给出量化结论及微调缓解方案
practical_value: '- 做跨境电商LLM客服、海外搜索Query理解模块时，需针对非母语用户的语法错误输入做专项偏见测试，避免输出刻板印象内容引发用户投诉

  - 面向多语言/非母语用户的LLM应用，可采集真实用户含语法错误的输入数据做微调，降低错误输入引发的偏见放大问题

  - 做LLM偏见评估时，不能仅用标准书面语测试集，需加入不同错误率、错误类型的测试case，更全面覆盖真实用户场景'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM社会偏见评估基准均基于标准流利英语构建，未覆盖非母语用户带语法错误的输入场景，会低估真实场景下的偏见暴露水平。
### 方法关键点
1. 搭建可控的学习者高频错误注入框架，覆盖介词、拼写、主谓一致等4类常见错误，支持自定义错误率；
2. 基于性别、种族、宗教三类偏见基准开展对照实验，对比标准prompt与带错误prompt的输出偏见差异。
### 关键结果
- 语法错误会显著提升LLM刻板印象对齐率，错误率每提升20%，偏见水平平均上升15%；
- 4类错误中，介词错误引发的偏见增幅最大，较其他错误类型高8~12pct；
- 基于含错误文本微调，可降低80%以上错误输入引发的偏见增幅。
