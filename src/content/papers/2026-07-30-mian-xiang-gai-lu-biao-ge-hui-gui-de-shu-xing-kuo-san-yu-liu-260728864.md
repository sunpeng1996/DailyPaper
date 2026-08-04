---
title: Conditioning Tree-Based Diffusions and Flows for Probabilistic Tabular Regression
title_zh: 面向概率表格回归的树型扩散与流模型条件化方法
authors:
- Silas Koemen
affiliations:
- Independent Researcher
arxiv_id: '2607.28864'
url: https://arxiv.org/abs/2607.28864
pdf_url: https://arxiv.org/pdf/2607.28864
published: '2026-07-30'
collected: '2026-08-04'
category: Training
direction: 树型扩散优化 · 表格概率回归
tags:
- Diffusion Model
- Flow Matching
- LightGBM
- Tabular Data
- Probabilistic Regression
one_liner: 提出DiffGBM框架，优化树扩散默认配置，实现更高精度更快的表格概率回归
practical_value: '- 电商转化率、pCVR等概率预估任务，可直接复用DiffGBM的流匹配训练逻辑，在现有LightGBM基线基础上低成本实现概率分布输出，无需引入神经网络组件

  - 推荐/广告场景的不确定性量化（如冷启动置信度评估、出价风险判定），可参考score-flex可调参数集，联合调优残差、EDM预条件等模块提升预估精度

  - 低延迟要求的实时场景（如实时推荐的不确定性过滤）可优先选择确定性ODE采样方案，比传统树扩散采样快5.2倍，满足线上延迟约束'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有基于树的扩散模型直接照搬神经扩散的默认设计（噪声音路、采样器、参数化方式等），未适配树模型特性，是性能提升的核心约束。
### 方法关键点
1. 提出DiffGBM框架，基于LightGBM设计两个可调优化轴：一是高斯路径流匹配训练器，直接学习速度场，支持少步确定性ODE采样；二是将score侧的残差处理、EDM预条件、log-sigma时间采样、噪声水平特征、损失加权、直方图分辨率等参数全部开放为联合可调空间，原有固定配置仅为其中一个特例。
### 关键结果
11个表格基准数据集上优化后的配置全量优于原树扩散基线（Wilcoxon检验p<1e-3），整体CRPS从0.699提升至0.725；流匹配版本采样速度比基线快5.2倍，校准效果最优；score-flex版本精度最高但采样速度最慢。
