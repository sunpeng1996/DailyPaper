---
title: Statistical Inference with Ill-Conditioned Random Weight Neural Network Sieves
title_zh: 病态随机权神经网络筛的统计推断
authors:
- Giovanni Ballarin
- Lukas Gonon
- Lyudmila Grigoryeva
affiliations:
- University of St. Gallen
- University of Warwick
arxiv_id: '2611.26410'
url: https://arxiv.org/abs/2611.26410
pdf_url: https://arxiv.org/pdf/2611.26410
published: '2026-11-19'
collected: '2026-11-22'
category: Other
direction: 随机权神经网络 · 统计推断理论
tags:
- RWNN
- statistical_inference
- ridge_regression
- ill_conditioning
- nonparametric_estimation
one_liner: 揭示随机权神经网络维度升高时的病态特性，构建适配的近似、估计与推断理论框架
practical_value: '主要是学术贡献，业务可借鉴点有限，RWNN相关工程可参考：

  - RWNN随维度升高必然出现病态问题，训练时需提前加入岭正则化避免不稳定

  - 采用分层采样优化RWNN特征，可同时提升L²与L∞近似精度'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
随机权神经网络（RWNN）仅训练输出层、计算效率高，但维度升高时的病态问题缺乏系统性的统计推断理论支撑，限制其在高维任务中的可靠性。
### 方法关键点
1. 证明满足多项式覆盖与Lipschitz条件的特征族的总体协方差矩阵特征值存在多项式上界，最小特征值随维度升高趋近于0；
2. 基于β-Hölder源条件推导分层采样下的L²、L∞近似界；
3. 给出岭正则化最小二乘的一致性保证，建立线性泛函的渐近线性与高斯极限结论，验证岭调整方差估计的一致性。
### 关键结果
分层采样下L²近似速率优于蒙特卡洛方法，实验验证了随机特征的条件恶化现象与所提估计、推断流程的有限样本有效性。
