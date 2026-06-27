---
title: Understanding Domain-Aware Distribution Alignment in Budgeted Entity Matching
title_zh: Understanding Domain-Aware Distribution Alignment
authors:
- Nicholas Pulsone
- Gregory Goren
- Roee Shraga
arxiv_id: '2606.27342'
url: https://arxiv.org/abs/2606.27342
pdf_url: https://arxiv.org/pdf/2606.27342
published: '2026-06-25'
collected: '2026-06-27'
category: Training
direction: Training
tags:
- Training
- LLM
one_liner: Entity Matching (EM) is a core operation in the data integration pipeline,
  where records from d...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 摘要

Entity Matching (EM) is a core operation in the data integration pipeline, where records from different sources are compared to determine whether they refer to the same real-world entity. Recent work has incorporated domain information and low-resource learning techniques to better adapt EM systems to realistic settings. While these approaches have demonstrated strong performance, it remains unclear how they behave under varying data constraints and levels of supervision in practice. In this paper, we investigate a state-of-the-art method for low-resource, domain-aware EM--BEACON--and study how its performance is affected by different algorithmic choices and data availability conditions. We conduct a series of targeted experiments to evaluate these variations, providing deeper insight into the role of distribution alignment and the behavior of the BEACON framework.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
