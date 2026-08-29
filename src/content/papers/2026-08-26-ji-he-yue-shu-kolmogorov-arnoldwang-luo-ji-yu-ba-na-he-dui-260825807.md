---
title: 'Geometry-Constrained Kolmogorov-Arnold Networks: Learning Edge Geometry via
  Banach Duality'
title_zh: 几何约束Kolmogorov-Arnold网络：基于巴拿赫对偶学习边几何特征
authors:
- K S Sesh Kumar
affiliations:
- Brevan Howard Centre for Financial Analysis
- Imperial Business School
arxiv_id: '2608.25807'
url: https://arxiv.org/abs/2608.25807
pdf_url: https://arxiv.org/pdf/2608.25807
published: '2026-08-26'
collected: '2026-08-29'
category: Training
direction: KAN架构优化 · 可学习边参数化
tags:
- KAN
- Symbolic Regression
- Neural Architecture
- Banach Duality
- Small Sample Learning
one_liner: 提出基于巴拿赫对偶的几何约束KAN，在噪声、小样本符号回归任务上性能优于固定基KAN
practical_value: '- 推荐场景特征非线性拟合可替换固定激活KAN为巴拿赫KAN，提升噪声数据鲁棒性，降低特征清洗成本

  - 新用户/新商品冷启动等小样本场景可引入可学习几何参数的边激活设计，降低小样本下拟合误差

  - 广告投放等高可解释性需求场景，可复用可学习指数p作为特征作用模式的解释信号，提升策略可解释性'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有KAN采用固定基（样条、多项式、傅里叶特征）参数化边函数，提前预设函数空间几何特征，无法适配不同数据分布，在噪声、小样本场景表现受限。
### 方法关键点
基于巴拿赫对偶映射设计边激活，为每条边引入可学习标量指数$p>1$：$p<2$对应类$ℓ_1$的sharp阈值行为，$p=2$为线性regime，$p>2$为原点附近平缓响应。
### 关键结果
- 50个符号回归任务上，Banach-KAN中位NRMSE达0.030，与Chebyshev基持平、优于样条基；18个核心方程任务平均排名2.00位列第一，全基准平均排名2.32与最优样条基持平。
- 噪声场景下$σ$从0升至1时，$ℓ^p$-KAN性能仅下降3.7×，远低于交叉验证样条的≈11×、无正则样条的21.6×；Banach-KAN下降8.8×，与调优样条持平，稳定性远超无正则样条。
- 小样本场景下Banach-KAN单任务获胜次数最多，固定基模型仅在训练样本量增大后追平效果；可学习$p$值可作为可解释信号，反映不同任务的特征作用模式。
