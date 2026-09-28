---
title: 'Statistical Foundations for a Google Play User-Review Sentiment Index: Signal
  Fusion, Shrinkage, Distributional Validation, and Dynamic Smoothing'
title_zh: 谷歌Play用户评论情感指数的统计基础：信号融合、收缩与动态平滑
authors:
- Marco Mandap
affiliations:
- Bulacan State University
arxiv_id: '2609.31513'
url: https://arxiv.org/abs/2609.31513
pdf_url: https://arxiv.org/pdf/2609.31513
published: '2026-09-25'
collected: '2026-09-28'
category: RecSys
direction: 用户评论情感指数 · 多信号融合
tags:
- sentiment_analysis
- signal_fusion
- empirical_bayes
- kalman_filter
- user_review
one_liner: 提出融合星级与文本情感的统计严谨的用户评论情感指数构建框架
practical_value: '- 电商商品评价、App评论的情感评分可复用协方差感知的逆方差加权方法融合星级与文本情感信号，比单一评分更准确

  - 低评论量商品的情感评分可采用高斯共轭收缩向总体均值偏移，替代人工设定的评论量阈值，解决冷启动下评分波动问题

  - 时序化的用户满意度趋势可引入Kalman滤波做动态平滑去噪，区分真实趋势与采样噪声，适合评价分时序监控场景'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有用户评论情感聚合要么仅用星级忽略文本信息，要么用固定阈值处理低评论量样本，时序波动易受噪声干扰，缺乏统计严谨的融合框架。
### 方法关键点
1. 将归一化星级与文本情感分作为潜在评价效价的带噪观测，用协方差感知的逆方差加权做信号融合；
2. 聚合时加入有界的有用性、新鲜度权重，再用估计精度替代任意评论数阈值向总体均值做贝叶斯收缩；
3. 针对离散星级分布修正KS检验做样本有效性校验，用状态空间模型+Kalman滤波生成去噪的时序趋势。
### 关键结果
整套框架有完整的统计理论证明支撑，案例验证仅3条带负面文本的评论就能将看似满分的纯星级评分显著拉低。
