---
title: 'Sinkhorn Linearization and the Spectral Proxy: Unifying the Statistical and
  Algorithmic Theory of Feature-Parameterized Inverse Optimal Transport via a Single
  Spectral Sandwich'
title_zh: Sinkhorn线性化与谱代理：统一特征参数化逆最优传输的统计与算法理论
authors:
- Han Dong
- Jiaming Li
- Yongqiang Gong
- Ruixi Li
- Yin Liu
affiliations:
- Nankai University School of Medicine
- Nankai University College of Artificial Intelligence
arxiv_id: '2608.13201'
url: https://arxiv.org/abs/2608.13201
pdf_url: https://arxiv.org/pdf/2608.13201
published: '2026-08-13'
collected: '2026-08-16'
category: Other
direction: 逆最优传输 · 统计算法理论统一
tags:
- Inverse-Optimal-Transport
- Sinkhorn-Algorithm
- Spectral-Analysis
- Optimization-Theory
- Statistical-Learning
one_liner: 提出Sinkhorn线性化与谱代理，通过单谱夹界统一特征参数化逆最优传输的统计与算法理论
practical_value: '- 业务中用最优传输(OT)做用户-物品分布匹配、跨域推荐适配的场景，可直接复用Sinkhorn线性化推导实现OT成本函数端到端训练

  - 本文给出的Hessian谱界可用于OT类匹配算法梯度下降的学习率上下界设定，降低调参试错成本

  - 无OT相关落地需求的电商/推荐业务可借鉴价值极低，以学术理论贡献为主'
score: 4
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有特征参数化逆最优传输（IOT）领域的统计性质、算法收敛性研究分散，缺乏统一核心理论框架支撑IOT的落地与性能分析。
### 方法关键点
1. 提出Sinkhorn线性化技术，通过对KKT条件求导得到熵正则OT方案对成本参数的隐函数敏感度；
2. 设计谱代理公式，推导得到切空间受限Hessian的谱夹界，以此单核心界支撑所有理论结论推导。
### 关键结果
1. 证明参数可识别性，参数维度上界满足F≤(K-1)²；
2. L1正则化估计器可指数级低失败概率恢复参数真实支撑；
3. 特征矩映射满足强单调性，逆映射Lipschitz常数有明确可计算上界，局部强凸性保证梯度下降单调收敛；
4. 模型误配场景下估计器收敛到真实分布的OT投影，经验Holder指数介于(0,1)区间。
