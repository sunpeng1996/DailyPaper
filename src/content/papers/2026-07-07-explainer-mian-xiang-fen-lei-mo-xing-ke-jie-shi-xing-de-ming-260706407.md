---
title: 'ExplAIner: A Declarative Query Language for Explaining Classification Models'
title_zh: ExplAIner：面向分类模型可解释性的声明式查询语言
authors:
- Marcelo Arenas
- Pablo Barceló
- Diego Bustamante
- Jose Caraball
- María Alejandra Schild
- Bernardo Subercaseaux
affiliations:
- Pontificia Universidad Católica de Chile
- Carnegie Mellon University
arxiv_id: '2607.06407'
url: https://arxiv.org/abs/2607.06407
pdf_url: https://arxiv.org/pdf/2607.06407
published: '2026-07-07'
collected: '2026-07-09'
category: Other
direction: 分类模型可解释性 · 声明式查询语言
tags:
- XAI
- Declarative Query
- Model Interpretability
- Classification
- Complexity Analysis
one_liner: 针对原有可解释性查询语言FOIL的缺陷，提出分层结构的ExplAIner，覆盖多类XAI解释需求且复杂度可控
practical_value: '- 电商推荐/广告分类模型的可解释性工具建设可复用ExplAIner分层结构，统一封装归因、对比等多类解释需求，避免重复开发

  - 需向运营/用户输出模型决策的核心特征时，可直接套用Opt-FOIL的最小解释逻辑，仅通过多项式次SAT求解器调用即可得到最优解，降低工程成本

  - 复杂度结论可直接参考：只要模型基础谓词可多项式时间计算，布尔分类模型（如LR、决策树类排序分支模型）的解释查询都可套用该框架保证落地性'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有XAI领域解释指标、查询类型零散，原有黑盒可解释性查询语言FOIL存在两大核心缺陷：无法表达基于最优性的解释查询，且在决策树上的计算复杂度极高，多项式层级每一层都难解，缺少统一的声明式框架实现多类解释需求的统一配置、组合与分析。
### 方法关键点
1. 基于FOIL扩展词汇表与分层结构，推出ExplAIner声明式查询语言，覆盖溯因、对比、基于特征、基于距离等全类别解释需求；
2. 推出面向优化的子语言Opt-FOIL，支持严格偏序下的最小解释计算。
### 关键结果
固定ExplAIner查询仅需固定次数调用SAT求解器即可完成计算；Opt-FOIL定义的最优解释仅需多项式次SAT调用即可得到。针对可多项式时间计算基础谓词的布尔模型，ExplAIner查询评估属于布尔层级，Opt-FOIL评估复杂度为$
\mathrm{FP}^{\mathrm{NP}}$
