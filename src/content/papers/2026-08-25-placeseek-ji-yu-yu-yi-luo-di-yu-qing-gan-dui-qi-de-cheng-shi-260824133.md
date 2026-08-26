---
title: 'PlaceSeek: Human-Centered Geospatial Retrieval of Urban Outdoor Places via
  Semantic Grounding and Affective Alignment'
title_zh: PlaceSeek：基于语义落地与情感对齐的城市户外场所检索框架
authors:
- Ziqi Cui
- Shangyu Lou
affiliations:
- University of British Columbia
- University of California, Santa Barbara
- San Diego State University
arxiv_id: '2608.24133'
url: https://arxiv.org/abs/2608.24133
pdf_url: https://arxiv.org/pdf/2608.24133
published: '2026-08-25'
collected: '2026-08-26'
category: RecSys
direction: 地理空间检索 · 多模态语义对齐
tags:
- Semantic Grounding
- LoRA
- Vision-Language Model
- POI Retrieval
- Affective Alignment
one_liner: 提出融合语义落地与情感对齐的人文导向城市户外场所检索框架，性能优于多类基线
practical_value: '- 意图拆分思路可复用：将用户自然语言查询拆分为功能需求+情感偏好两个子维度，先做有效性过滤再做偏好排序，可直接迁移到到店推荐、本地生活服务搜索场景

  - 多模态微调降本trick：用LoRA微调多模态模型适配人类感知标注数据，无需全量微调即可显著提升匹配精度，大幅降低工程落地成本

  - 召回校验逻辑可借鉴：新增前置有效性校验模块过滤不满足核心功能需求的候选，再进行个性化排序，可大幅减少无效结果透出，提升用户满意度'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有地理空间检索以POI元数据为核心，无法匹配用户开放式、情感类、活动导向的场所查询需求。
### 方法关键点
1. 设计意图感知检索机制，将用户自然语言查询拆分为功能、情感两类子意图
2. 语义落地模块验证候选街景是否具备支撑目标活动的物理要素，过滤无效候选
3. 情感对齐模块采用基于人类城市感知标注数据LoRA微调的多模态模型，对有效候选重排
### 关键结果
在米兰31956个街视点数据集上测试，Precision@5达88.0%，平均匹配得分3.39/4，nDCG@5达0.920，全面优于CLIP、微调CLIP、SigLIP、VQA基线；消融实验验证语义落地是结果有效性的核心，情感对齐可进一步提升有效候选的排序质量。
