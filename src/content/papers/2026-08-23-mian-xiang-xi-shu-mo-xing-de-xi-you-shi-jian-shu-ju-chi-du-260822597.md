---
title: Scale-invariant Optimal Sampling for Rare-events Data with Sparse Models
title_zh: 面向稀疏模型的稀有事件数据尺度不变最优采样方法
authors:
- Jing Wang
- HaiYing Wang
- Qiang Zhang
- Hao Helen Zhang
affiliations:
- University of Connecticut
- Wills Eye Hospital Thomas Jefferson University
- University of Arizona
arxiv_id: '2608.22597'
url: https://arxiv.org/abs/2608.22597
pdf_url: https://arxiv.org/pdf/2608.22597
published: '2026-08-23'
collected: '2026-08-25'
category: Training
direction: 不平衡数据采样 · 稀疏模型训练优化
tags:
- Rare-event Sampling
- Sparse Model
- Imbalanced Data
- Adaptive Lasso
- Subsampling
one_liner: 提出尺度不变的稀有事件最优子采样方法，降低稀疏模型预测误差与采样信息损失
practical_value: '- 电商推荐/广告的点击、转化等稀有正样本不平衡训练场景，可复用该尺度不变采样策略，避免特征缩放干扰采样效果，降低采样带来的预测偏差

  - 高维稀疏特征场景下做子采样加速训练时，可结合IPW自适应Lasso与MSCL估计器提升样本利用效率，避免过度采样丢失有效信息

  - 针对稀疏特征的用户行为建模，可参考本文的oracle性质验证思路，评估子采样方案的有效性'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有稀有事件数据最优子采样概率依赖数据尺度，不当特征缩放会放大无效特征对采样的影响，导致采样效率低、信息损失大，该问题在高维稀疏特征场景尤为突出。
### 方法关键点
1. 基于自适应Lasso构建稀有事件数据估计器，验证其oracle性质为子采样提供理论支撑；
2. 推导尺度不变的最优子采样函数，最小化逆概率加权（IPW）自适应Lasso的预测误差；
3. 提出基于最大采样条件似然（MSCL）的估计器，进一步提升参数估计效率。
### 关键结果
仿真和真实数据集实验验证，所提方法不受特征缩放影响，相比现有最优采样方案预测误差更低、参数估计效率更高，在稀疏特征场景优势更显著。
