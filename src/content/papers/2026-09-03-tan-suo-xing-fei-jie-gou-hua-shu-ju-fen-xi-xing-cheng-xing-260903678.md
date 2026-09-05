---
title: 'Exploratory Unstructured Data Analysis: A Formative Study and Implications
  for Human-AI Collaboration'
title_zh: 探索性非结构化数据分析：形成性研究及人机协作启示
authors:
- Johannes Eschner
- Dominik Eitler
- Max Irendorfer
- Patrick Kramml
- Matthias Zeppelzauer
- Manuela Waldner
affiliations:
- TU Wien
- University of Applied Sciences St. Pölten (USTP)
arxiv_id: '2609.03678'
url: https://arxiv.org/abs/2609.03678
pdf_url: https://arxiv.org/pdf/2609.03678
published: '2026-09-03'
collected: '2026-09-05'
category: Agent
direction: 人机协作 · 非结构化数据分析
tags:
- Human-AI Collaboration
- Unstructured Data Analysis
- CLIP
- Exploratory Data Analysis
- Few-shot Learning
one_liner: 提出非结构化数据探索分析框架EluDA，给出4个高价值人机协同优化方向
practical_value: '- 电商商品图/素材语义打标场景，可先用CLIP做语义分组，再补充用户自定义概念的few-shot标注，比纯zero-shot准确率提升40%以上

  - 搭建非结构化数据（商品图/用户评论）探索工具时，优先做自底向上的分面分类功能，无需投入资源做空间分类交互，用户需求极低

  - 设计数据分析类Agent的人机协同链路时，可直接复用4个优化方向：智能采样可视化、少样本增量学习、自动概念建议、信任校准'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
传统EDA仅适配结构化数据，大规模非结构化数据（如图像、用户评论、商品素材）缺乏可落地的探索分析框架，人工梳理结构效率极低。
### 方法关键点
1. EluDA概念框架融合传统EDA的查询、可视化能力与AI辅助的「结构搜索」流程，明确用户/AI驱动的任务边界；
2. 开展形成性用户研究，观测用户探索图像数据集时的结构构建行为模式；
3. 测评CLIP在零样本概念分配、语义分类两类任务的实用效果。
### 关键结果
- 90%以上用户采用自底向上的分面分类构建数据结构，仅不足10%用户会生成有意义的空间分类；
- CLIP零样本分配用户自定义概念准确率不足30%，达不到业务可用标准，但语义分组一致性可达75%以上；
- 提炼出4个高价值人机协同优化方向，可降低非结构化数据探索的人工成本70%以上
