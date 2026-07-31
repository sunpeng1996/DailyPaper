---
title: 'TreeCCA: Canonical Correlation Analysis via Gradient-Boosted Trees'
title_zh: TreeCCA：基于梯度提升树的典型相关性分析
authors:
- James Chapman
arxiv_id: '2607.27027'
url: https://arxiv.org/abs/2607.27027
pdf_url: https://arxiv.org/pdf/2607.27027
published: '2026-07-29'
collected: '2026-07-31'
category: Training
direction: 多视图关联分析 · GBT自定义训练目标
tags:
- Gradient Boosted Trees
- Canonical Correlation Analysis
- Feature Fusion
- Interpretable ML
- Tabular ML
one_liner: 首个用梯度提升树作为端到端CCA编码器的方法，兼顾非线性精度、可解释性与低计算成本
practical_value: '- 做多视图特征融合（如用户行为+商品属性+搜索query关联挖掘）时，可直接复用TreeCCA的Eckart-Young损失作为XGBoost/LightGBM自定义目标，无需设计复杂神经网络，默认超参数即可获得不错效果

  - 需特征可解释性的场景（如推荐归因、广告特征重要性分析），可复用TreeCCA原生特征重要性计算逻辑，零额外成本定位驱动跨视图关联的核心特征

  - 低延迟推荐/广告排序场景下，TreeCCA比Deep CCA计算成本低5倍且精度相当，可替换现有神经网络多视图融合方案降本提效'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
梯度提升树（GBT）是表格数据建模的主流方案，但传统典型相关性分析（CCA）一直依赖线性或神经编码器，无法复用GBT的易用性、高性能与原生可解释性优势。
### 方法关键点
提出TreeCCA，基于Eckart-Young（EY）损失生成闭格式逐样本梯度，可直接作为自定义目标接入XGBoost、LightGBM等标准GBT库，无需额外架构设计，超参数与常规GBT一致，默认配置即可获得良好效果，原生支持特征重要性解释。
### 关键结果
- 合成基准上性能超过Deep CCA：Signed Power数据集得分2.61 vs 2.43，Hermite数据集得分2.93 vs 2.89
- 稀疏基准下p=50时Precision@S=1.00，远优于无信号输出的PMD方法
- UCI HAR传感器融合基准上精度与Deep CCA相当，计算成本低5倍
- 5个通用表格多视图数据集上，TreeMCCA的非线性关联提取能力、下游分类精度均优于或持平线性CCA
