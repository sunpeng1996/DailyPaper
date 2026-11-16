---
title: 'Where Tree Ensembles Decide: Structural Local Explanation with Decision Predicate
  Graphs'
title_zh: 基于决策谓词图的树集成模型局部结构解释方法
authors:
- Sylvio Barbon Junior
- Luca Longo
affiliations:
- University of Trieste
- University College Cork
arxiv_id: '2611.18382'
url: https://arxiv.org/abs/2611.18382
pdf_url: https://arxiv.org/pdf/2611.18382
published: '2026-11-13'
collected: '2026-11-16'
category: Other
direction: 树模型可解释 · 决策谓词图
tags:
- Tree Ensemble
- XAI
- Local Explanation
- Decision Predicate Graph
- Model Debugging
one_liner: 提出局部决策谓词图框架定位树集成预测的关键决策阈值，效果优于TreeSHAP等基准
practical_value: '- 电商粗排/精排的树模型bad case分析可复用DPG方法，快速定位导致预测错误的具体决策阈值，替代传统仅看特征重要性的分析方式

  - 树模型在线debug时可基于关键谓词快速定位异常分支，适合广告投放、推荐排序的实时异常排查场景

  - 可与TreeSHAP等特征归因方法互补，输出面向运营/产品的可解释规则（如用户客单价>X时触发高优推荐），提升推荐逻辑透明度'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
树集成（XGBoost、LightGBM、随机森林等）是电商排序、广告预估的主流模型，现有TreeSHAP等特征归因、反事实解释仅能输出特征重要性，无法定位预测对应的具体决策阈值，结构化解释又会丢失树的原始结构信息。

### 方法关键点
1. 提出局部Decision Predicate Graph（DPG），聚合单样本触发的所有决策规则，保留完整的树计算路径，可复现所有预测结果；
2. 从规则中筛选关键谓词，即对目标类别预测影响最大的决策阈值，无需外部解释器即可输出阈值及共享该阈值的所有树。

### 关键结果数字
在16个数据集、4种树集成架构上验证：
- 单阈值修正可修复46-69%的错误预测，比TreeSHAP选Top特征修正的效果（29-50%）高17-19pct；
- 注入故障的场景下，可定位46-71%的错误阈值，远高于随机选择的6-21%。
