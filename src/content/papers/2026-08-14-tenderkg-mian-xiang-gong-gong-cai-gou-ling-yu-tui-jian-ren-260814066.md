---
title: TenderKG
title_zh: TenderKG：面向公共采购领域推荐任务的知识图谱数据集
authors:
- Yacine Mokhtari
- Véra Pukhkoy
- Grégory Smits
affiliations:
- IMT Atlantique, Lab-STICC, UMR 6285, CNRS
- Intescia Group
arxiv_id: '2608.14066'
url: https://arxiv.org/abs/2608.14066
pdf_url: https://arxiv.org/pdf/2608.14066
published: '2026-08-14'
collected: '2026-08-17'
category: RecSys
direction: 知识图谱推荐 · 高稀疏场景基准数据集
tags:
- Knowledge Graph
- Recommender System
- Dataset
- Sparse Interaction
- Side Information
one_liner: 发布覆盖2021-2023年法国公共采购的异构KG数据集，支持高约束场景知识感知推荐研究
practical_value: '- 面对仅存正样本、交互极度稀疏的推荐场景，可复用其融合文本、层级分类、地理特征等多源侧信息补全信号的思路

  - 构建面向强竞争、高风险匹配场景的KG时，可参考其异构实体（参与方、标的、类目taxonomy）+语义/结构关系的建模范式

  - 业务侧做推荐方法的鲁棒性验证时，可参考其针对结构属性、稀疏模式的数据分析维度设计评估指标'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
公共采购是核心经济活动，但该领域推荐研究长期不足，核心痛点是缺乏覆盖领域复杂度的公开数据集；且场景仅中标交互可见，显性信号极度稀疏，难以开展算法验证。
### 方法关键点
构建大规模KG数据集TenderKG，覆盖2021-2023年法国公共采购全量数据，建模异构实体（企业、标书、标段、领域专属工作类目taxonomy），关联丰富语义与结构关系；同时集成多维度侧信息（文本描述、层级分类、地理特征），解决稀疏信号问题，支撑高约束竞争场景下的知识感知推荐研究。
### 关键结果
完成数据集全维度统计分析，明确其结构属性、稀疏模式、领域专属特征，可作为投标人推荐、KG推荐、竞争感知匹配等任务的基准，支撑高风险真实决策场景的算法效果评估。
