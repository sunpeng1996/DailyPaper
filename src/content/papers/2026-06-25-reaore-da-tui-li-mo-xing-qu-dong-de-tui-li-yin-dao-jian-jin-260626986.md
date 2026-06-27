---
title: 'ReaORE: Reasoning-Guided Progressive Open Relation Extraction Empowered by
  Large Reasoning Models'
title_zh: ReaORE：大推理模型驱动的推理引导渐进式开放关系抽取
authors:
- Xin Lin
- Liang Zhang
- Guoqi Ma
- Hongyao Tu
- Jinsong Su
affiliations:
- National Institute for Data Science in Health and Medicine, Xiamen University
- School of Informatics, Xiamen University
arxiv_id: '2606.26986'
url: https://arxiv.org/abs/2606.26986
pdf_url: https://arxiv.org/pdf/2606.26986
published: '2026-06-25'
collected: '2026-06-27'
category: LLM
direction: 大模型开放关系抽取 · 粗到细推理优化
tags:
- Open Relation Extraction
- LLM
- Coarse-to-Fine Reasoning
- Information Extraction
- Relation Prediction
one_liner: 提出粗到细两阶段推理的开放关系抽取框架ReaORE，解决泛化差与易混淆关系难区分问题
practical_value: '- 电商商品属性抽取、评论实体关系挖掘可复用两阶段架构：先召回候选关系再细粒度判定，提升抽取准确率

  - Query理解、用户意图识别场景中，易混淆意图区分可借鉴「embedding相似度召回+细粒度对比推理」组合方案，降低误判率

  - 电商领域知识图谱构建时，针对未定义的新型关系可复用该框架的泛化设计，减少人工标注成本'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
开放关系抽取（OpenRE）需从无结构文本中提取未知类型的实体间关系，现有两类方案均存在缺陷：聚类类方法无法生成可读关系标签、泛化性差；LLM直接生成方案对易混淆关系的区分度不足，难以落地实际场景。

### 方法关键点
提出ReaORE两阶段粗到细推理框架：
1. 关系过滤阶段：多维度推理生成初始候选关系集，再通过embedding相似度做补充过滤，确保目标关系落在候选范围内
2. 关系预测阶段：基于细粒度对比推理从候选集中识别最终目标关系，强化易混淆关系的区分能力

### 关键结果
在两个通用公开OpenRE数据集上，性能全面超越所有现有基线方案。
