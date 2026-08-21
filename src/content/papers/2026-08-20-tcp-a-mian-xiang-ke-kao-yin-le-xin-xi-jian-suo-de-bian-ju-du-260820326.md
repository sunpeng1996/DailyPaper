---
title: '$TCP_α$: Margin-Controlled Confidence estimation for reliable Music Information
  Retrieval'
title_zh: TCP_α：面向可靠音乐信息检索的边距控制置信度估计
authors:
- Parampreet Singh
- Anushka Singh
- Sumit Kumar
- Vipul Arora
affiliations:
- Indian Institute of Technology Kanpur
arxiv_id: '2608.20326'
url: https://arxiv.org/abs/2608.20326
pdf_url: https://arxiv.org/pdf/2608.20326
published: '2026-08-20'
collected: '2026-08-21'
category: Eval
direction: 置信度估计 · 模型故障预测优化
tags:
- Confidence Estimation
- Failure Prediction
- Margin Control
- Post-hoc Calibration
- Imbalanced Regression
one_liner: 提出带边距惩罚的置信度目标TCP_α，解决分类模型过置信问题，提升故障预测性能
practical_value: '- 推荐/搜索的分类类模型（如类目预测、意图识别）可复用TCP_α的边距控制置信度目标，解决过置信问题，快速过滤低置信预测降低badcase

  - 可复用论文针对置信度头训练的不平衡回归优化策略，无需改动base模型结构，仅加轻量头即可快速上线置信度评估能力

  - 跨域场景下仅用5%目标域标注样本微调置信度头即可恢复性能的经验，可迁移到推荐系统跨域冷启动的置信度校准场景'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
DNN分类模型普遍存在过置信问题，错误预测也会被分配高置信，现有后验置信度估计方法的置信值在对错样本上重叠，决策边界附近错误样本的置信度和正确样本无法区分，无法可靠判断预测是否可信。

### 方法关键点
1. 提出TCP_α置信度目标，对错误样本引入边距控制惩罚，从理论上保证对错样本的目标值完全可分，分离边距和类别数无关，随惩罚参数单调递增
2. 针对置信度头训练中错误样本少导致的严重不平衡回归问题，通过 ablation 筛选出最优训练配置

### 关键结果
- 所有实验场景下TCP_α的故障预测性能均优于现有置信度目标
- 仅拒绝置信度最低的8%预测，即可将基础模型macro-F1从0.89提升至0.98
- 跨域场景下仅用5%新域标注样本微调置信度头，即可有效恢复性能
