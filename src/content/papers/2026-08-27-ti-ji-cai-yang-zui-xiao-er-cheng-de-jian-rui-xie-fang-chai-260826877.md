---
title: When Is the Sharp Covariance Envelope Tight? Feature-Only Geometry for Volume-Sampled
  Least Squares
title_zh: 体积采样最小二乘的尖锐协方差包络紧性条件：仅基于特征的几何分析
authors:
- Kihun Rhee
affiliations:
- Seoul National University
arxiv_id: '2608.26877'
url: https://arxiv.org/abs/2608.26877
pdf_url: https://arxiv.org/pdf/2608.26877
published: '2026-08-27'
collected: '2026-08-30'
category: Other
direction: 机器学习理论 · 最小二乘采样方差分析
tags:
- Least-Squares
- Volume-Sampling
- Covariance-Analysis
- Loewner-Envelope
- Feature-Geometry
one_liner: 推导体积采样下OLS系数协方差的尖锐Loewner包络，给出仅用特征的紧性判定阈值
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-stat.ML
depth: abstract
---

### 动机
此前体积采样下的最小二乘（OLS）损失、协方差分析仅覆盖采样规模等于特征秩的端点场景，缺乏任意合法采样规模下的协方差边界及紧性判定方法。

### 方法关键点
1. 推导任意全秩特征池、合法采样规模下，中心化系数协方差的全局尖锐Loewner包络；
2. 提出仅依赖特征的余量指标ν_A，直接判定协方差包络的谱紧性：ν_A>0时对所有兼容残差包络严格，ν_A=0时存在残差达到紧边界，且该残差在所有内部采样规模下均保持紧性；
3. 通过残差增广测度变换、支撑饱和分析分别给出松弛界与可达性证明。

### 关键结果
给出的协方差包络在全秩类下全局最优，特征余量阈值可实现无偏的采样规模保守决策，冻结特征实验验证了下界证书的有效性，结论仅适用于条件中心化的协方差分析，不涉及泛化性。
