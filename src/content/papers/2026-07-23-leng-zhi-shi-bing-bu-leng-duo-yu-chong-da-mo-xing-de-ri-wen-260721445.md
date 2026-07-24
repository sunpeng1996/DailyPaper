---
title: 'When Trivia Is Not Trivial: Everyday Knowledge Failures in Multilingual LLMs'
title_zh: 冷知识并不冷：多语种大模型的日常文化知识缺陷研究
authors:
- Anna Mosolova
- Djamé Seddah
affiliations:
- INRIA Paris
arxiv_id: '2607.21445'
url: https://arxiv.org/abs/2607.21445
pdf_url: https://arxiv.org/pdf/2607.21445
published: '2026-07-23'
collected: '2026-07-24'
category: Eval
direction: 多语种大模型 · 知识能力评测
tags:
- Multilingual-LLM
- Knowledge-Benchmark
- Cultural-Knowledge
- Long-tail-Knowledge
- LLM-Evaluation
one_liner: 构建覆盖6种欧洲语言的TriviaRoomQA基准，揭示多语种大模型的日常文化知识缺陷
practical_value: '- 跨语种电商/内容推荐Agent开发中，不可默认大模型对不同语言的本土流行文化知识掌握一致，需针对性补充对应语种的文化类RAG知识库

  - 本地化推荐的选品、文案生成场景中，涉及本土明星、影视、小众文化相关的内容，需单独增加知识校验逻辑，不可直接采信大模型输出

  - 可参考TriviaRoomQA的题型设计逻辑，构建面向业务的跨语种大模型知识校验集，提前排查不同语种下的大模型知识盲区'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有主流LLM评测基准多聚焦学术类、推理类任务，无法覆盖日常文化、本土长尾知识的能力评估，也不能体现大模型跨语种知识调用的真实差异。
### 方法关键点
构建TriviaRoomQA多语种知识评测基准，覆盖288个主题，包含6种欧洲语言的3300道平行选择题、额外5340道法语专属题，对30款参数量从7B到70B的全球开源大模型开展测评。
### 关键结果数字
大模型在历史、地理、数学等知识密集型主题表现优异，但在明星、音乐、影视、新闻等日常流行文化主题表现大幅下滑；同一问题不同语言下模型表现存在显著差异，说明事实知识访问并非跨语种独立，现有学术类基准存在明显知识覆盖缺口。
