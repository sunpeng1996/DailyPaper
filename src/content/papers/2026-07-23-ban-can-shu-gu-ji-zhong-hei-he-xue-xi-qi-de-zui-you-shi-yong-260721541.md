---
title: Optimal use of a black-box learner in semiparametric estimation
title_zh: 半参数估计中黑盒学习器的最优使用方法
authors:
- Yihong Gu
affiliations:
- Harvard University
arxiv_id: '2607.21541'
url: https://arxiv.org/abs/2607.21541
pdf_url: https://arxiv.org/pdf/2607.21541
published: '2026-07-23'
collected: '2026-07-25'
category: Other
direction: 半参数因果估计 · 黑盒模型优化
tags:
- Causal Inference
- Semi-parametric Estimation
- DML
- Black-box Model
- Adversarial Calibration
one_liner: 提出优于DML的半参数黑盒估计器与通用TAME校准框架，消除DML次优误差项，达理论最优下界
practical_value: '- 做Uplift建模、因果效应评估时，可用TAME框架替换原有DML流程，在nuisance函数拟合难度不均的场景下降低估计误差

  - 黑盒模型做因果相关半参数估计时，可复用本文误差率下界结论指导模型选型，优先降低易拟合nuisance的误配误差

  - 广告/推荐策略效果量化场景，可引入TAME的局部对抗矩校准方法修正黑盒预测的偏差权重，提升估计准确性'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有半参数估计主流DML框架存在次优误差项，当两个 nuisance 函数拟合难度不均衡时，误差传播效率低，无法最优利用黑盒学习器的拟合能力

### 方法关键点
1. 针对部分线性模型构造全新估计器，误差率优化为$1/\sqrt{n} + \delta_{a,\mu} \cdot \delta_{a,\pi} + \delta_s^2$，严格消除DML中原有的$\max(\delta_{a,\mu}, \delta_{a,\pi}) \cdot \delta_s$次优项，且匹配理论下界，速率不可改进
2. 推出通用TAME框架，通过对抗条件矩校准局部修正黑盒回归得到的去偏权重，可兼容任意初始黑盒估计结果，无需额外假设或计算开销

### 关键结果
当 nuisance 拟合难度不均衡时，相对DML估计误差可降低最多$\delta_s \cdot \max(\delta_{a,\mu}, \delta_{a,\pi})$量级，适配更广泛的结构未知场景
