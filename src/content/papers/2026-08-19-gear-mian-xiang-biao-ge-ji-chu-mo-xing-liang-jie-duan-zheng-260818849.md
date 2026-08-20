---
title: 'GEAR: Generative Expansion and Real Anchoring for Two-Stage Distillation of
  Tabular Foundation Models'
title_zh: GEAR：面向表格基础模型两阶段蒸馏的生成式扩展与真实锚定
authors:
- Qi Qin
- Jiajie Zhu
- Dali Chen
- Yuzhao Zhang
- Jia-Xing Han
- Yu Su
- Peng Zhang
- Ying Yan
- Yifan Sun
affiliations:
- Renmin University of China
- Ant Digital Technologies, Ant Group
- Nanjing University
arxiv_id: '2608.18849'
url: https://arxiv.org/abs/2608.18849
pdf_url: https://arxiv.org/pdf/2608.18849
published: '2026-08-19'
collected: '2026-08-20'
category: Training
direction: 表格基础模型蒸馏 · 轻量落地优化
tags:
- Tabular Foundation Model
- Knowledge Distillation
- Model Compression
- LightGBM
- MLP
one_liner: 提出两阶段蒸馏框架GEAR，将表格基础模型压缩为可CPU部署的轻量预测器，大幅降本提效
practical_value: '- 电商CTR/CVR等表格类预测任务可直接复用GEAR框架，将表格大模型蒸馏为MLP/LightGBM，既能保留大模型效果，又可在CPU上低时延部署，适配线上高吞吐要求

  - 蒸馏流程可复用两阶段trick：第一阶段用合成样本扩充分布覆盖学习大模型软标签，第二阶段用真实样本+折外教师预测锚定分布，避免标签泄漏，可迁移到任意大模型蒸馏任务

  - 可参考论文给出的生成查询量与保真度的权衡公式，合理控制合成样本规模，避免不必要的训练成本浪费'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
表格基础模型（TFM）依托上下文学习效果优异，但上下文依赖的推理带来极高时延与内存开销，难以适配电商等场景的大规模线上部署需求。

### 方法关键点
提出模块化两阶段蒸馏框架GEAR：1. 第一阶段用合成协变量作为教师查询位置，让学生模型学习TFM输出的软标签，突破观测样本的分布覆盖限制；2. 第二阶段用真实标签和折外教师预测锚定学生模型到目标分布，避免自标注泄漏；同时推导了生成查询量与生成保真度的权衡风险证明。

### 关键结果
两阶段MLP相比监督MLP，二分类任务AUC提升1.81~2.00个点，多分类提升1.19~1.35个点，比仅用真实数据蒸馏分别高1.76~2.19、2.09~2.40个点；二分类增益可迁移到LightGBM、XGBoost，三类学生模型平均AUC均超过最优非TFM基线CatBoost；推理中值时延降低57~2866倍，峰值内存降低1.9~3.3倍，同时AUC高于同规模监督基线。
