---
title: The Price of Current-Effect Inference in Nonstationary Multi-Armed Bandits
title_zh: 非平稳多臂老虎机中当前效应推断的代价
authors:
- Sharan Sahu
- Martin T. Wells
arxiv_id: '2610.29982'
url: https://arxiv.org/abs/2610.29982
pdf_url: https://arxiv.org/pdf/2610.29982
published: '2026-10-21'
collected: '2026-10-24'
category: RecSys
direction: 非平稳多臂老虎机 · 推断-后悔权衡
tags:
- Multi-Armed Bandits
- Nonstationary Bandit
- Dynamic Regret
- Treatment Effect
- Adaptive Experiment
one_liner: 刻画非平稳多臂老虎机收益最大化与当前效应推断的权衡，给出匹配极小极大界与TRACE算法
practical_value: '- 电商大促、广告实时投放等动态场景的bandit探索策略可参考TRACE框架，平衡收益与当前干预效果的估计精度

  - 需要实时估计不同策略（创意、推荐规则）的当前效果差时，可复用其基于Hölder平滑度的样本窗口选择逻辑，降低过时数据干扰

  - 自适应A/B实验的流量分配可借鉴其empirical-Bernstein e-process扩展，在保证效果估计置信度的同时降低探索成本'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
非平稳场景（如电商促销、广告实时投放）下的bandit算法既要最大化累计收益，又要可靠估计当前各臂相对参考臂的效应差，两个目标天然冲突，过往研究未系统性刻画该权衡的理论边界。
### 方法关键点
针对满足Hölder平滑条件的K臂非平稳bandit，建立带当前效应高概率覆盖约束（置信区间宽度≤w）下的匹配极小极大动态后悔界，提出TRACE算法实现该界，同时扩展empirical-Bernstein e-process适配实际观测误差，保留最坏情况保证。
### 关键结果
TRACE在时间 horizon T下的后悔阶为$	ilde{O}_β\left(\sqrt{KT}+K^{β/(2β+1)}L^{1/(2β+1)}T^{(β+1)/(2β+1)}+Kw^{-2}(1+L^{1/β}w^{-1/β})\right)$，即使存在全局最优臂，推断带来的额外后悔仍不可避免，数值实验验证了所有理论结论。
