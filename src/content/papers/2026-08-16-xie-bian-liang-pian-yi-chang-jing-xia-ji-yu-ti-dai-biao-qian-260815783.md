---
title: Inferential Evaluation of Surrogate-Derived Models under Covariate Shift
title_zh: 协变量偏移场景下基于替代标签训练模型的推断评估方法
authors:
- Longtian Shi
- Molei Liu
- Doudou Zhou
affiliations:
- National University of Singapore Department of Statistics and Data Science
- Peking University Health Science Center Department of Biostatistics
- Beijing International Center for Mathematical Research, Peking University
arxiv_id: '2608.15783'
url: https://arxiv.org/abs/2608.15783
pdf_url: https://arxiv.org/pdf/2608.15783
published: '2026-08-16'
collected: '2026-08-18'
category: Eval
direction: 模型评估 · 迁移学习域适配
tags:
- Covariate Shift
- Transfer Learning
- Model Evaluation
- Surrogate Label
- Statistical Inference
one_liner: 面向三样本迁移场景，提出无金标目标域下替代标签训练模型的性能评估与统计推断框架
practical_value: '- 跨域迁移的召回/排序模型上线前无目标域金标时，可复用三样本评估框架估算真实性能，降低上线风险

  - 点击、短会话等替代标签训练的模型效果校准，可复用文中密度比校正方法降低标签偏差带来的评估误差

  - 模型AUC/TPR/FPR等核心指标的统计推断方法可直接复用，量化小样本金标下的评估置信区间，辅助决策'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
迁移学习场景下通常用低成本易得的替代标签（如弱监督标注、自动标注）训练模型，但目标域无金标、存在协变量偏移时，无法准确评估模型对真实金标任务的性能，现有方案缺少带统计保证的评估能力。
### 方法关键点
设定三样本场景：小批量金标源域、大批量替代标签源域、无标注目标域，基于条件可迁移性假设，通过源域特定密度比迁移双源域信息，提出交叉拟合估计器，结合结果回归增强与核校正处理阈值附近的估计偏差，同时覆盖三个样本的不确定性。
### 关键结果
推导得到TPR/FPR的渐近线性推断、ROC曲线一致性与逐点推断、AUC的渐近正态推断；Chatbot Arena时序验证与ACS-Income半合成实验中，指标估计偏差<1%，95%置信区间覆盖率达94%以上
