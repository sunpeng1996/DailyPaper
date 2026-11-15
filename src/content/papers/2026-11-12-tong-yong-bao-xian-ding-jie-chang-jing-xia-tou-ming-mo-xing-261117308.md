---
title: Quantifying structural stability of transparent models for general insurance
  pricing
title_zh: 通用保险定价场景下透明模型的结构稳定性量化方法
authors:
- Félix Côté
- Marie-Pier Côté
affiliations:
- École d’actuariat, Université Laval, Canada
arxiv_id: '2611.17308'
url: https://arxiv.org/abs/2611.17308
pdf_url: https://arxiv.org/pdf/2611.17308
published: '2026-11-12'
collected: '2026-11-15'
category: Eval
direction: 可解释模型迭代稳定性评估
tags:
- Model Stability
- Explainable AI
- Model Retraining
- EBM
- XGBoost
one_liner: 提出功能透明模型定义与均方形状函数距离指标，量化模型迭代时的结构稳定性
practical_value: '- 迭代模型结构稳定性评估可参考MSS距离指标，优先选择更新后结构波动小的模型架构，降低业务侧规则适配、用户解释成本

  - 模型迭代时采用固定超参数、序列建模的稳定策略，可在几乎不损失效果的前提下大幅提升EBM、XGBoost类树模型的结构稳定性，适合广告定价、人群分层等需稳定输出的场景

  - 对可解释性要求高的业务（如电商营销预算分配、广告出价），可优先选择带中心化数值协变量的GLM或EBM，兼顾稳定性、效果与可解释性'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
财险合同周期短，数据分布漂移快，需频繁更新模型适配新数据，但现有结构稳定性指标仅适用于简单决策树，无法衡量更新前后模型的结构差异，而结构稳定性是预测稳定性的上游核心前提。
### 方法关键点
1. 定义功能透明模型：预测函数可拆分为主效应单变量函数+成对交互双变量函数之和的模型，覆盖GLM、EBM等常用可解释模型
2. 提出均方形状函数（MSS）距离指标，量化功能透明模型更新前后的结构差异程度
### 关键结果
在3个公开车险数据集上测试：① 带中心化数值协变量的GLM稳定性最优；② EBM可兼顾稳定性与预测效果；③ 固定超参数、序列建模的稳定策略可将EBM、XGBoost的结构稳定性大幅提升，且预测效果损失可忽略
