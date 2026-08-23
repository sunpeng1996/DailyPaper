---
title: A Layered Simplex Architecture for Large Alphabets
title_zh: 面向大字符集的分层单纯形概率估计架构
authors:
- Meir Feder
- Yaniv Fogel
- Ruediger Urbanke
affiliations:
- Tel Aviv University
- EPFL
arxiv_id: '2608.19908'
url: https://arxiv.org/abs/2608.19908
pdf_url: https://arxiv.org/pdf/2608.19908
published: '2026-08-20'
collected: '2026-08-23'
category: Other
direction: 大字符集概率估计 · 贝叶斯方法优化
tags:
- Large Alphabet
- Probability Estimation
- Bayesian Estimator
- Log Loss
- Good-Turing
one_liner: 提出仅需深度参数的分层单纯形估计器，性能媲美Good-Turing等大字符集专业估计方法
practical_value: '- 电商/搜索大Query集、海量Item ID分布估计场景可尝试该极简估计器，替换Good-Turing降低调参成本

  - 该估计器regret显式可计算特性，可用于大Vocab下序列生成、分布预估的误差边界量化，辅助系统稳定性评估

  - 针对Zipf分布（搜索/推荐场景的点击、Query分布普遍符合）的scaling law结论，可直接用于预估采样数据量与未发现符号的对应关系，优化冷启动采样策略'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
大字符集下基于log loss的概率估计是经典问题，传统Laplace、Krichevsky–Trofimov等估计方法在稀疏、重尾分布场景表现不佳，Good-Turing等专业方法复杂度高、依赖调参，亟需简单高效的无调参方案。
### 方法关键点
提出分层单纯形贝叶斯估计器，仅需深度作为结构参数，构造逻辑为对概率单纯形的独立均匀采样结果按坐标相乘后重归一化，通过对不同深度的估计结果平均彻底消除调参需求；其regret（相对已知源编码的额外码长）支持显式高效计算。
### 关键结果
在合成、真实文本基准上性能与Good-Turing等专业方法相当；针对指数>1的Zipf分布，当样本仅覆盖小部分字符集时，regret接近已发现符号的描述长度，可直接推导数据量、字符集大小、深度的scaling law。
