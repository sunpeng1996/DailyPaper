---
title: On Same-Sample and Independent-Sample Stochastic Extragradient for Monotone
  Variational Inequalities
title_zh: 单调变分不等式的同样本与独立样本随机外梯度算法研究
authors:
- TaeHo Yoon
- Nicolas Loizou
arxiv_id: '2608.06182'
url: https://arxiv.org/abs/2608.06182
pdf_url: https://arxiv.org/pdf/2608.06182
published: '2026-08-06'
collected: '2026-08-09'
category: Other
direction: 随机优化 · 变分不等式求解理论
tags:
- Stochastic Extragradient
- Variational Inequality
- Convergence Analysis
- Stochastic Optimization
one_liner: 厘清同/独立样本随机外梯度收敛边界，明确两类算法假设与步长策略适用范围
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
随机外梯度（SEG）是求解单调变分不等式（VIP）的核心算法，但现有分析多聚焦独立样本SEG（I-SEG），对同样本SEG（S-SEG）的收敛特性研究不足，且普遍依赖紧致域、随机算子方差一致有界等强假设，适用场景受限。
### 方法关键点
1. 分析样本级Lipschitz参数对S-SEG收敛性的影响，放宽既有算法的假设约束；
2. 针对无界域场景推导两类SEG变体的高概率受限间隙收敛界；
3. 对比验证不对称双步长策略对两类SEG的适用差异。
### 关键结果
1. 仅均值Lipschitz与方差有界无法保证S-SEG在紧致域收敛；
2. 无界域下两类SEG的高概率收敛界无法进一步泛化改进；
3. 保证I-SEG几乎必然最后迭代收敛的不对称双步长策略，会导致S-SEG在部分单调VIP场景下几乎必然发散。
