---
title: 'BUMP: Brief Unexpected Mid-Interpolation Peak'
title_zh: BUMP：排列对齐神经网络线性插值的短时意外峰值现象
authors:
- Melinda Flóra Kiss
- Márton Muntag
- Adrián Csiszárik
- Dániel Varga
affiliations:
- HUN-REN Alfréd Rényi Institute of Mathematics, Budapest, Hungary
- Eötvös Loránd University, Budapest, Hungary
arxiv_id: '2611.08182'
url: https://arxiv.org/abs/2611.08182
pdf_url: https://arxiv.org/pdf/2611.08182
published: '2026-11-05'
collected: '2026-11-07'
category: Training
direction: 神经网络训练 · 模型集成优化
tags:
- Model Ensemble
- Linear Interpolation
- Weight Averaging
- Logit Ensemble
- Loss Landscape
one_liner: 发现排列对齐神经网络线性插值的BUMP现象，衍生权重-预测混合集成方法超越标准logit集成
practical_value: '- 推荐/广告多模型集成场景可替换原有纯logit集成，采用权重-预测混合集成方案，同时提升离线准确率与输出校准性

  - 模型迭代时可对多个对齐的训练checkpoint做权重插值，利用BUMP效应选取最优权重，零额外训练成本获得性能增益

  - LLM/LoRA微调的推荐/Agent场景，可对多个微调后的对齐权重做插值，低成本提升下游任务效果'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有神经网络线性模式连通性研究聚焦插值中点的损失屏障特征，普遍忽略端点附近的短暂性能增益现象，此前无针对性的系统分析与应用落地。
### 方法关键点
1. 首次明确命名并系统验证BUMP效应：排列对齐的独立训练神经网络做线性插值时，靠近端点的位置会出现精度短暂上升后向中点下降的特征，该效应跨数据集、模型架构、训练范式稳定存在，不受早停、极端剪枝扰动，也不属于普通正则效应。
2. 基于该效应衍生的权重-预测混合集成方案，结合权重空间插值混合与预测空间logit混合的互补优势。
### 关键结果
该集成方案对比标准logit集成，测试准确率稳定提升，同时输出校准trade-off更优。
