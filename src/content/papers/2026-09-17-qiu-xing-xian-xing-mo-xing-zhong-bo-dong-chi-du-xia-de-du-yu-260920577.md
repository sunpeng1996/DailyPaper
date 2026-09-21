---
title: TAP Accuracy Below the Fluctuation Scale and Universal Posterior Geometry in
  Spherical Linear Models
title_zh: 球形线性模型中波动尺度下的TAP精度与通用后验几何
authors:
- Jingbo Liu
- Zhiyuan Yu
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2609.20577'
url: https://arxiv.org/abs/2609.20577
pdf_url: https://arxiv.org/pdf/2609.20577
published: '2026-09-17'
collected: '2026-09-21'
category: Other
direction: 高维统计 · 后验近似理论
tags:
- High-dimensional Statistics
- TAP Approximation
- Posterior Geometry
- Random Matrix Theory
- Bayesian Regression
one_liner: 在马琴科-帕斯特谱正则条件下推导球形线性模型TAP近似误差边界与后验几何量化特性
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
高维线性回归是信号恢复、逆问题的核心基础框架，现有TAP近似与后验几何量化研究对设计矩阵的逐元素独立性假设过强，缺乏普适性的误差边界刻画。
### 方法关键点
放宽设计矩阵的独立性约束，仅要求满足定量Marchenko–Pastur谱正则条件，推导全温度下的TAP近似量化边界，系统刻画球形先验下的后验质量集中特性。
### 关键结果数字
1. 归一化球形自由能与TAP最优值的误差为$O_P(p^{-1})$，二者与确定性等价量的误差均为$O_P(p^{-1/2})$，该波动尺度是紧的；
2. 所有全局TAP最大值与球形后验均值的归一化平方欧氏距离为$O_P(p^{-1})$；
3. 岭估计器定义的带外后验质量的对数上界为$-cp\varepsilon^2+O_P(1)$，当$\varepsilon_p \gg p^{-1/2}$时，对应带可捕获所有渐近后验质量。
