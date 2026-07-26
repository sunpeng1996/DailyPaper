---
title: slang.gr as a Large-Scale Crowdsourced Resource for Non-Standard Greek
title_zh: slang.gr：面向希腊非标准口语的大规模众包语言资源
authors:
- Panagiotis Papadakos
- Katerina Papantoniou
- Dimitris Plexousakis
affiliations:
- ICS-FORTH, Heraklion, Greece
arxiv_id: '2607.21255'
url: https://arxiv.org/abs/2607.21255
pdf_url: https://arxiv.org/pdf/2607.21255
published: '2026-07-23'
collected: '2026-07-26'
category: Other
direction: 非标准语言资源 · 俚语计算建模
tags:
- Slang Resource
- Crowdsourced NLP
- Folksonomy
- Taxonomy Construction
- Non-standard Language
one_liner: 构建希腊非标准语大规模众包资源，实现噪声标签到多层分类体系映射并提出社区式定义置信度评分
practical_value: '- 处理UGC内容标签噪声时，可借鉴将无结构民间标签映射到多层分类体系的方法，提升标签可解释性

  - 众包内容质量评估可复用融合用户角色、交互行为、审核信号的置信度打分方案，降低低质量内容占比

  - 优化搜索/推荐场景的网络热词、俚语识别能力时，可参考该研究的俚语语义分类框架提升query理解准确率'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
俚语等非标准语言具备强动态性、非标准化特征，计算建模难度极高，希腊语领域长期缺乏可支撑下游NLP任务的大规模可计算俚语资源。

### 方法关键点
1. 整合众包平台slang.gr的词汇内容、UGC标签、用户交互数据，将噪声民间标签映射到同时覆盖语义分类、社会语言学元数据的多层结构化分类体系；
2. 分析希腊俚语语言结构与贡献者社区行为特征，融合用户角色、交互模式、审核信号，提出基于社区的俚语定义置信度评分。

### 关键结果
分类体系表征在保留行为结构有效信息的同时显著提升可解释性，置信度信号分析的结构化程度大幅优化，已产出首个可计算的希腊非标准语言资源，可支撑社会语言学NLP、LLM非正式语言建模、偏见分析等下游任务。
