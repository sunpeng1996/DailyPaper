---
title: 'PAD: Policy-Aware Data Valuation for Autonomous Driving'
title_zh: PAD：面向自动驾驶的策略感知数据估值框架
authors:
- Chengkai Xu
- Yicheng Guo
- Jiaqi Liu
- Yiming Cui
- Shiyu Fang
- Peng Hang
- Hao Zhang
- Jian Sun
affiliations:
- College of Transportation, Tongji University
- Department of Computer Science, UNC Chapel Hill
- Department of Control Science and Engineering, Tongji University
arxiv_id: '2611.25604'
url: https://arxiv.org/abs/2611.25604
pdf_url: https://arxiv.org/pdf/2611.25604
published: '2026-11-18'
collected: '2026-11-22'
category: Training
direction: 模型训练 · 策略感知高价值样本筛选
tags:
- Data Valuation
- Policy Optimization
- Training Data Curation
- Influence Function
- Autonomous Driving
one_liner: 提出策略感知的自动驾驶训练数据估值方法，精准筛选高价值样本提升策略性能
practical_value: '- 做LLM4Rec/Agent策略训练时，可迁移PAD思路，针对目标模型做训练样本价值打分，替代盲目堆数据的做法，降低训练成本同时提升业务效果

  - 样本价值评估可复用「梯度反馈+局部训练几何正则近似」的方案，比仅依赖样本固有属性的打分逻辑更贴合下游任务的真实收益

  - 跨模型场景（如不同召回/排序模型）可借鉴PAD的策略专属估值思路，避免通用样本筛选规则对特定模型无效的问题'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
端到端自动驾驶策略训练依赖大规模演示数据，但数据量增长不代表性能线性提升，不同样本对不同策略的效用差异极大，现有数据筛选方法仅依赖样本固有属性或训练代理指标，无法匹配下游策略的真实收益。

### 方法关键点
- PAD框架为每个候选演示数据生成针对目标驾驶策略的专属效用分
- 融合场景级校准反馈、投影策略梯度与局部训练几何正则近似，实现可扩展的基于影响力的价值计算

### 关键结果
- 在DiffusionDrive上，相比仅用真实数据训练，NavTest集EPDMS提升3.5个点，NavHard集提升5.0个点
- 在扩散、回归、流匹配三类planner上，基于PAD的策略专属数据筛选效果均优于全量/真实数据训练，同时显著降低场景级性能退化
