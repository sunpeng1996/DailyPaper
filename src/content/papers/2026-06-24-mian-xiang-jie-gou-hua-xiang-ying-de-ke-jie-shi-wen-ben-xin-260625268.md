---
title: Learning Interpretable Text Signals for Structured Responses
title_zh: 面向结构化响应的可解释文本信号学习方法
authors:
- Cixiao Jiang
- Ben Powell
- Niall MacKay
affiliations:
- University of York
arxiv_id: '2606.25268'
url: https://arxiv.org/abs/2606.25268
pdf_url: https://arxiv.org/pdf/2606.25268
published: '2026-06-24'
collected: '2026-06-27'
category: RecSys
direction: 可解释文本表征 · 评论评分预测
tags:
- interpretable text
- NMF
- supervised representation learning
- review rating prediction
- topic modeling
one_liner: 提出非负矩阵分解与二项回归联合模型，学习同时对齐语义和外部响应的可解释文本表征
practical_value: '- 电商场景可复用该联合建模框架，从商品/商家评论中同时学习语义主题与评分关联信号，替代传统分阶段的主题提取+评分回归方案，提升可解释性

  - 可迁移到好评/差评原因自动挖掘、商品舆情预警任务，无需额外标注即可得到和评分强关联的文本特征

  - 做评论相关的可解释推荐时，可直接用该模型输出的响应相关主题作为解释依据，解决传统主题模型输出和用户评分关联度低的问题'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有文本-结构化响应建模通常将预测与可解释性拆分为独立步骤，输出的文本表征要么语义一致性差，要么和外部结构化响应（如电商评分、风险等级）对齐度低，无法同时满足预测精度与可解释需求。
### 方法关键点
提出非负矩阵分解（NMF）与二项回归联合训练框架，文档-主题表征同时接受文本重构损失、评分预测损失的双重监督，既保证主题的语义可解释性，又强制文本特征和外部响应强关联。
### 关键结果
仿真实验与真实评论数据集测试显示，模型可稳定提取与响应强相关的文本信号，评分预测性能优于线性回归、岭回归基线，可解释性显著优于无监督主题建模方案。
