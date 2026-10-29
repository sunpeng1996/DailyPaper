---
title: LLM knowledge for improved Out-of-Distribution Tabular Prediction - A Cross-Validated
  Regularisation Approach
title_zh: 利用LLM先验知识优化分布外表格预测的交叉验证正则化方法
authors:
- Sølve Langseth
- Kristoffer Herland Hellton
- Hugo L. Hammer
affiliations:
- Oslo Metropolitan University
- SimulaMet
- Oslo University Hospital
arxiv_id: '2610.36806'
url: https://arxiv.org/abs/2610.36806
pdf_url: https://arxiv.org/pdf/2610.36806
published: '2026-10-27'
collected: '2026-10-29'
category: Training
direction: LLM增强模型训练 · 分布外泛化优化
tags:
- OOD Generalization
- Regularization
- Prior Elicitation
- Tabular Prediction
- Distribution Shift
- LLM
one_liner: 将LLM提取的特征系数先验作为正则化收缩目标，优化表格数据的分布外预测性能
practical_value: '- 推荐/广告场景冷启动、跨域预测等OOD任务，可尝试从LLM提取特征权重先验，替代正则化默认零收缩目标，降低分布偏移带来的性能衰减

  - 先验选择阶段无需追求最优先验，仅通过源域交叉验证筛选即可，核心目标是规避最差先验即可拿到大部分收益

  - 训练样本量较小时，引入LLM先验可同时收获域内+OOD精度提升；仅当训练数据量足够大、域内增益消失时，先验的知识迁移收益才会显性体现'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
表格预测模型在部署场景与训练分布不一致时性能衰减严重，传统人工专家先验提取效率低、扩展性差，无法适配大规模业务需求。
### 方法关键点
1. 从LLM中提取特征-响应关系的系数先验，作为正则化回归的收缩目标替代传统零值
2. 仅通过源域交叉验证完成LLM提供商、先验结构的选择，无需目标域数据参与
3. 设置损坏先验的对照实验，隔离先验内容与尺度的影响
### 关键结果数字
- 5个真实表格数据集上，4个实现OOD MSE下降，最高降幅达7.9%
- 24组先验实验中10组在常规置信度下实现显著提升，分类任务收益主要体现在概率精度而非排序效果
- 3个数据集上域内精度提升幅度与OOD相当，仅当训练数据量足够大时先验的知识迁移作用才会显性体现
