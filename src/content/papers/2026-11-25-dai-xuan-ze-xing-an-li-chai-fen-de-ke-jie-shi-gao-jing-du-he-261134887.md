---
title: Interpretable and Accurate Hybrid Decision Trees with Selective Case-Based
  Splits
title_zh: 带选择性案例拆分的可解释高精度混合决策树
authors:
- Cristiano Landi
- Alessio Cascione
- Riccardo Guidotti
affiliations:
- University of Pisa
- ISTI-CNR
arxiv_id: '2611.34887'
url: https://arxiv.org/abs/2611.34887
pdf_url: https://arxiv.org/pdf/2611.34887
published: '2026-11-25'
collected: '2026-11-26'
category: Training
direction: 可解释机器学习 · 决策树优化
tags:
- DecisionTree
- ExplainableAI
- InterpretableML
- HybridModel
- CaseBasedLearning
one_liner: 提出融合特征与案例拆分的混合决策树及选择性拆分策略，精度比肩集成模型且树更浅可解释性强
practical_value: '- 推荐/广告强解释性场景的轻量模型选型：可替换原有单结构决策树，在不损失精度的前提下得到更浅的树结构，满足风控、广告投放合规等强解释要求的业务场景

  - 粗排树模型优化：拆分思路可迁移到召回粗排的树模型训练，针对用户行为、商品属性等异构特征，动态选择最优特征子集做节点拆分，提升粗排的划分效率与精度

  - 用户分群场景复用：混合拆分逻辑可复用到用户分层运营场景，融合规则特征与相似用户案例做划分，得到的分群规则更简洁易落地，同时分群精准度比肩集成模型'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
决策树是经典可解释机器学习模型，现有轴平行、斜向、基于样例的拆分策略各有优劣，无通用最优方案；常规单结构决策树精度难对标集成模型，深度过大也会损失可解释性，无法满足强监管场景需求。
### 方法关键点
1. 混合树架构：整合同构特征拆分与异构案例拆分逻辑，树的各节点可自适应选择拆分方式，支持全树异构拆分
2. 选择性案例拆分策略：每次拆分时自动搜索信息量最高的特征子集定义拆分规则，平衡案例方法的特异性与特征方法的简洁性
### 关键结果
在多组公开表格数据集上，精度优于标准决策树，达到集成模型同等水平，同时生成的树结构更浅，可解释性显著优于常规决策树与集成模型。
