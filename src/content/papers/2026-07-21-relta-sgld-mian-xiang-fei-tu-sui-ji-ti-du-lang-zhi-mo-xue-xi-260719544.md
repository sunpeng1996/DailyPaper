---
title: 'RELTA-SGLD: Relative-Growth Localized Taming for Nonconvex Stochastic-Gradient
  Langevin Learning'
title_zh: RELTA-SGLD：面向非凸随机梯度朗之万学习的相对增长局部校正算法
authors:
- Yiwei Zhou
- Ziheng Chen
affiliations:
- School of Mathematics and Statistics, Yunnan University
arxiv_id: '2607.19544'
url: https://arxiv.org/abs/2607.19544
pdf_url: https://arxiv.org/pdf/2607.19544
published: '2026-07-21'
collected: '2026-07-24'
category: Training
direction: 非凸学习 · SGLD优化算法
tags:
- SGLD
- Nonconvex Learning
- Optimization
- Stochastic Gradient
- Lyapunov Stability
one_liner: 提出相对增长规则驱动的SGLD校正方案，提升非凸学习稳定性同时减少对原始更新的不必要抑制
practical_value: '- 做LLM/推荐模型非凸训练时，可引入阈值触发的梯度校正逻辑，避免梯度爆炸同时保留有效更新drift

  - 可借鉴相对增长的Lyapunov稳定性推导思路，优化现有自适应优化器（如AdamW）的梯度裁剪策略

  - 对需要SGLD做贝叶斯推荐/不确定性估计的场景，该方案可在不损失收敛精度的前提下提升训练稳定性'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有非凸学习场景下SGLD算法的超线性梯度更新易导致训练不稳定，传统校正方案会过度抑制原始学习漂移，收敛精度边界损失大。
### 方法关键点
1. 引入阈值判断校正触发时机，仅在梯度异常时启动校正；
2. 基于单步Lyapunov稳定性条件推导相对增长原则，动态确定校正强度，生成更轻量的λ尺度分母，保留非零长尾更新收益；
3. 理论证明了该方案的多项式矩稳定性以及W₁、W₂空间下的一阶平稳精度，优于现有同类方案的半阶、1/4阶边界。
### 关键结果
对比未校正SGLD和TUSLA，在Fashion-MNIST高压稳定场景下平均学习指标显著提升，性能与调优后的AdamW相当；普通训练场景下几乎不干扰原始更新动态，收敛速度接近未校正SGLD。
