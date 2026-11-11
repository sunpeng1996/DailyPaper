---
title: Data Quality Challenges in Multimodal Tourism Recommender Systems
title_zh: 多模态旅游推荐系统的数据质量挑战
authors:
- Zehui Wang
- Wolfram Höpken
- Dietmar Jannach
affiliations:
- University of Applied Sciences Ravensburg-Weingarten
- University of Klagenfurt
arxiv_id: '2611.13972'
url: https://arxiv.org/abs/2611.13972
pdf_url: https://arxiv.org/pdf/2611.13972
published: '2026-11-10'
collected: '2026-11-11'
category: RecSys
direction: 多模态推荐 · 数据质量优化
tags:
- Multimodal Recommendation
- Data Quality
- POI Recommendation
- Modality Fusion
- LLM Hallucination
one_liner: 梳理Yelp、Instagram真实数据集的多模态数据质量问题，给出多模态推荐系统优化方向
practical_value: '- 多模态推荐落地前需先做多源数据质量校验，重点排查虚假评论、LLM生成内容幻觉、跨模态矛盾、人群偏置四类问题

  - 跨模态融合模块可加入质量感知权重，对低质量模态数据降低贡献占比，避免噪声传导到排序结果

  - 引入LLM生成补充模态内容时，需增加结构化约束（如事实校验、格式限定）降低幻觉引入的噪声'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
当前多模态推荐系统普遍引入社交平台等多源异构数据提升效果，但底层多模态数据的质量问题长期被忽视，会引入噪声、偏置、矛盾，最终导致推荐结果可靠性差、鲁棒性低，旅游POI推荐等依赖多源UGC数据的场景问题尤为突出。
### 方法关键点
基于Yelp、Instagram两类真实公开数据集的落地实践，系统梳理出四大核心数据质量问题：1）虚假评论等人工引入的内容噪声；2）LLM生成补充内容的幻觉问题；3）图文等跨模态信息存在事实矛盾；4）用户人口统计特征分布偏置。针对性提出三大优化方向：质量感知的多模态融合策略、带结构化约束的可控LLM内容生成机制、用户群体分层建模方案。
### 关键结果
明确了多模态推荐落地时的核心数据风险点，提出的优化路径可有效降低数据噪声对推荐效果的负面影响，提升系统的鲁棒性与可靠性。
