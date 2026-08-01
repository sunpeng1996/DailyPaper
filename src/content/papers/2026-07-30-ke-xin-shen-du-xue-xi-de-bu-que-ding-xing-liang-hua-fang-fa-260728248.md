---
title: 'Uncertainty quantification for trustworthy deep learning: Methods and measures'
title_zh: 可信深度学习的不确定性量化：方法与度量综述
authors:
- H. Martin Gillis
- Thomas Trappenberg
affiliations:
- Faculty of Computer Science, Dalhousie University
arxiv_id: '2607.28248'
url: https://arxiv.org/abs/2607.28248
pdf_url: https://arxiv.org/pdf/2607.28248
published: '2026-07-30'
collected: '2026-08-01'
category: Training
direction: 深度学习可信性 · 不确定性量化综述
tags:
- Uncertainty_Quantification
- Deep_Ensemble
- Bayesian_Neural_Network
- OOD_Detection
- Calibration
one_liner: 系统梳理深度学习不确定性量化的五类方法与度量，重点覆盖高效集成与单通实现方案
practical_value: '- 推荐系统排序/召回模块可复用Deep Ensemble、MC Dropout等低成本UQ方案，识别高不确定性样本做兜底策略，降低bad
  case

  - LLM Agent调用决策时可直接复用论文整理的认知不确定性度量方法，优化OOD样本识别、选择性预测的判定阈值

  - 电商大模型语义匹配、召回环节可参考单通/最后层UQ方案，无需多推理步即可获得置信度，兼顾效果与推理效率'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
深度学习在安全关键场景落地缺乏原则性的预测置信度估计能力，现有UQ综述对高效集成、单通实现方案的覆盖深度不足，也未实现预测分布生成方法与不确定性度量的解耦梳理。
### 方法关键点
将UQ方法划分为贝叶斯神经网络、蒙特卡洛Dropout、深度集成、高效集成近似、最后层/单通方法五大类，同时覆盖证据网络、共形预测、事后校准等邻域方向，对比熵分解与成对散度等不确定性度量的差异，统一了不同方法的评估基准。
### 核心结论
梳理了UQ在LLM中的落地场景，提出分类任务高效认知度量、分布偏移下的多样性与校准、混合架构等开放研究方向。
