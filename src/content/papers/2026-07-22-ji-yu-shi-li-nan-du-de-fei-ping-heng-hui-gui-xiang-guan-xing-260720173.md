---
title: Instance Hardness-Based Relevance for Imbalanced Regression
title_zh: 基于实例难度的非平衡回归相关性计算方法
authors:
- Vitor M. Leitao
- Juscimara G. Avelino
- George D. C. Cavalcanti
- Rafael M. O. Cruz
affiliations:
- Universidade Federal de Pernambuco, Brazil
- École de Technologie Supérieure, University of Quebec, Canada
arxiv_id: '2607.20173'
url: https://arxiv.org/abs/2607.20173
pdf_url: https://arxiv.org/pdf/2607.20173
published: '2026-07-22'
collected: '2026-07-23'
category: Training
direction: 非平衡回归 · 训练样本权重优化
tags:
- Imbalanced Regression
- Instance Hardness
- Relevance Function
- Resampling
- Model Training
one_liner: 提出融合实例学习难度的相关性函数InHaR，解决非平衡回归复杂场景下稀有样本识别偏差问题
practical_value: '- 电商推荐的GMV预估、高价值用户转化预测等非平衡回归任务，可替换传统仅按标签值加权的方案为InHaR，提升稀有高价值样本的识别精度

  - 做非平衡数据过采样、噪声增强等预处理时，可结合InHaR输出的相关性调整采样权重，减少对伪稀有样本的过度加权，降低模型过拟合风险

  - 针对用户行为标签常见的双峰分布（如极低频/极高客单价订单），可复用InHaR的「分布稀有性+学习难度」双维度判定逻辑优化样本权重分配'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
非平衡回归任务中目标变量分布不对称，部分取值区间样本量极低。传统相关性函数仅基于目标值固定分配样本权重，在双峰分布等复杂场景下无法区分真稀有样本与普通样本，直接限制了不平衡感知学习方法的效果。
### 方法关键点
提出基于实例难度的相关性函数InHaR，同时融合目标分布的稀有性、模型对当前实例的学习难度两个维度判定样本相关性，突破仅依赖目标值固定赋值的局限；可直接对接随机过采样（RO）、高斯噪声增强（GN）等主流重采样策略，优化非平衡回归的训练过程。
### 关键结果
在双峰分布数据集上可精准识别稀有区域，搭配重采样策略时预测性能较传统相关性方法有显著提升，相关代码、数据集已完全开源，可直接二次开发。
