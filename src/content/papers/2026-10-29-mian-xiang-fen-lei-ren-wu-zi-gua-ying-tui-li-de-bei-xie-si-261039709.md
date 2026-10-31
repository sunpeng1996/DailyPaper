---
title: Bayes-Consistent Losses for Adaptive Inference in Classification
title_zh: 面向分类任务自适应推理的贝叶斯一致损失函数
authors:
- Shirley Xiaoqi Liu
- Florence Regol
- Antonios Valkanas
- Patrick Rebeschini
- Mark Coates
arxiv_id: '2610.39709'
url: https://arxiv.org/abs/2610.39709
pdf_url: https://arxiv.org/pdf/2610.39709
published: '2026-10-29'
collected: '2026-10-31'
category: Training
direction: 模型训练 · 自适应推理路由优化
tags:
- Adaptive Inference
- Loss Function
- Bayesian Consistency
- Model Routing
- Semi-supervised Learning
one_liner: 提出贝叶斯一致的成本敏感铰链损失，及基于无标签数据优化路由的PPI流程
practical_value: '- 多模型混合部署（如MoE、大小模型 cascade 推理）场景可直接复用成本敏感铰链损失做联合训练，平衡精度与推理耗时，适配电商搜索/推荐高吞吐要求

  - 路由模块标注数据不足时，可复用PPI流程用海量无标签用户行为数据优化路由策略，降低标注成本

  - 分类类任务（如用户意图识别、商品类目预测）的自适应推理系统可直接套用本文证明的贝叶斯一致理论边界做训练效果校验'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
自适应推理系统通过路由为输入匹配不同成本-精度的模型，平衡推理效果与耗时，是高吞吐场景（如推荐、搜索）的核心优化方向，但现有模型与路由联合训练缺乏有理论支撑的损失函数，且路由训练标注数据需求远高于分类器，标注成本高。
### 方法关键点
1. 提出成本敏感铰链损失，支持单阶段路由、级联路由两种场景的分类器+路由联合训练，理论证明该损失满足贝叶斯一致性，最小化该损失可收敛到成本敏感0-1损失下的贝叶斯最优风险；
2. 提出训练后预测驱动推理（PPI）流程，用无标签数据微调已训练的单阶段路由，降低标注依赖。
### 关键结果
实验在合成与真实分类数据集上验证，所提铰链损失联合训练效果优于传统独立训练方案，标注数据稀缺场景下PPI可有效降低路由错误率
