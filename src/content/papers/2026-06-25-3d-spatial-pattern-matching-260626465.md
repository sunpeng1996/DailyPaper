---
title: 3D Spatial Pattern Matching
title_zh: 3D Spatial Pattern Matching
authors:
- Nicole R. Schneider
- Avik Das
- Lukas Arzoumanidis
- Abhijeet Ghodgaonkar
- Hanan Samet
- Youness Dehbi
arxiv_id: '2606.26465'
url: https://arxiv.org/abs/2606.26465
pdf_url: https://arxiv.org/pdf/2606.26465
published: '2026-06-25'
collected: '2026-06-26'
category: QueryRec
direction: QueryRec
tags:
- QueryRec
- LLM
one_liner: Spatial pattern matching is the process of matching query entities and
  constraints with databas...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 摘要

Spatial pattern matching is the process of matching query entities and constraints with database entities and relations. It has many applications, including similar region search, housing market search, landmark search, and road network matching. To our knowledge, all existing spatial pattern matching approaches frame the problem in a 2 dimensional space, where entities lie in a cartesian plane and relationships defined between them are contained in 2 dimensions. However, this problem framing has significant limitations when searching for real world entities that have height in addition to position. To address this limitation, we extend spatial pattern matching to 3 dimensions and provide a generalized definition of the problem. We describe a subgraph matching algorithm capable of resolving 3D spatial patterns over distance relations and release two 3D spatial pattern matching datasets, one synthetic and one containing real 3D building data from the city of Hamburg, Germany. We test our subgraph matching algorithm on both datasets and present results as a baseline for future methods to build upon.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。
