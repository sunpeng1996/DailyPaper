---
title: 'When the tail is earned by its companions: measuring label dependence in long-tailed
  multi-label classification'
title_zh: 长尾多标签分类标签依赖度量：基于共现同伴的尾标签召回分析
authors:
- Christoffer Löffler
affiliations:
- Pontificia Universidad Católica de Valparaíso, School of Computer Engineering
arxiv_id: '2611.22859'
url: https://arxiv.org/abs/2611.22859
pdf_url: https://arxiv.org/pdf/2611.22859
published: '2026-11-17'
collected: '2026-11-18'
category: Eval
direction: 长尾多标签分类 · 评估度量优化
tags:
- long-tailed classification
- multi-label classification
- macro-F1
- label co-occurrence
- evaluation metric
one_liner: 提出无需训练的标签依赖统计量，揭示长尾多标签分类中Macro-F1对尾召回的高估问题
practical_value: '- 电商商品标签打标、长尾内容/商品召回场景，不要仅用Macro-F1评估模型效果，需补充无共现同伴样本的尾标签召回率作为辅助指标，避免高估长尾性能

  - 训练多标签分类模型前，可先统计训练集标签共现统计量，提前预估模型尾标签召回的上限，规避无效调优

  - 若业务要求尾标签独立识别能力，优先选择不依赖其他标签预测的单标签分支架构，依赖标签关联的架构会放大尾标签依赖问题'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
长尾多标签分类中尾标签常与高频标签共现，模型易通过共现关系「伪召回」尾标签，现有Macro-F1等指标无法区分这类依赖共现的召回，且过往诊断方法需完成模型训练才能输出结果，无法提前预判数据集风险。

### 方法关键点
1. 提出标签内估计量，拆分尾标签召回为「有共现同伴」「无共现同伴」两类；
2. 定义评估规则：仅当无共现召回提升时，才判定标签依赖度有效下降；
3. 提出无需训练的训练集标签统计量，可提前预估报告召回率与无共现召回率的差值上限。

### 关键结果数字
在23个数据集、7种训练目标、5类标签关联机制上验证：最多18.4%的Macro-F1统计的尾标签真阳性依赖共现得到，无共现时会消失；现有长尾优化目标均无法降低标签依赖，仅架构调整可影响，依赖其他标签预测做尾标签打分的模型依赖度极高。
