---
title: 'Hopformer: Homogeneity-Pursuit Transformer for Time Series Forecasting'
title_zh: Hopformer：面向时序预测的同质性追寻Transformer架构
authors:
- Wan Zhang
- Qinjie Lin
- Chan Lee
- Weijian Li
- Han Liu
- Kai Zhang
affiliations:
- 中国科学院AMSS预测科学中心
- Northwestern University Department of Computer Science
- Northwestern University Department of Statistics and Data Science
- University of North Carolina at Chapel Hill Department of Statistics and Operations
  Research
arxiv_id: '2607.22299'
url: https://arxiv.org/abs/2607.22299
pdf_url: https://arxiv.org/pdf/2607.22299
published: '2026-07-24'
collected: '2026-07-27'
category: Other
direction: 时序预测 · 两阶段Transformer优化
tags:
- Time Series Forecasting
- Transformer
- LoRA
- Sparsity Pattern Aggregation
- MASE
one_liner: 提出两阶段时序预测框架，先提取公共低方差趋势再用LoRA微调Transformer拟合残差，性能达SOTA
practical_value: '- 可迁移到电商销量/流量/大促GMV预测场景，先用SPA模块提取行业/品类级公共趋势，降低时序建模噪声

  - 时序拟合时先拿通用Transformer基座做LoRA微调拟合残差，既能保留公共模式又适配单序列个性化特征，大幅降低训练成本

  - 高维协变量（如活动、折扣、节假日因子）可直接纳入SPA阶段做趋势融合，避免高维输入导致Transformer attention不稳定的问题'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
高维协变量下的多时序预测需同时兼顾通用时序模式学习与单序列个性化信息保留，传统Transformer处理高维输入时计算开销高、训练稳定性差，现有通用零-shot预测模型也难以适配高维协变量场景。
### 方法关键点
1. 两阶段框架：第一阶段通过Sparsity Pattern Aggregation（SPA）策略融合协变量，提取低方差公共趋势作为同质化层，理论上可实现接近最优的偏差-方差权衡；
2. 第二阶段采用LoRA微调的Transformer建模残差中的复杂依赖，针对时序依赖数据提供了泛化边界证明。
### 关键结果
在合成时序数据集与真实时序预测基准集上，平均MASE指标提升6.56%，达到当前SOTA水平。
