---
title: Defensive Boosting for Online Probabilistic Forecasting
title_zh: 面向在线概率预测的防御式提升算法
authors:
- Georgy Noarov
- Aaron Roth
arxiv_id: '2608.13554'
url: https://arxiv.org/abs/2608.13554
pdf_url: https://arxiv.org/pdf/2608.13554
published: '2026-08-13'
collected: '2026-08-14'
category: Training
direction: 在线概率预测 · Boosting 算法优化
tags:
- Online Learning
- Boosting
- Probabilistic Forecasting
- Brier Score
- Adversarial Learning
one_liner: 提出仅需单弱学习器的防御式在线提升框架，同时覆盖两类现有在线提升的性能保证，速度快数个量级
practical_value: '- 电商CTR/CVR实时预估场景可复用该单弱学习器boosting架构，相比多集成基线降低数倍在线计算开销

  - 对抗性流量（作弊/突发流量）下的概率预测可复用其双重性能保证，既保常规流量Brier score精度，弱学习条件满足时又能快速收敛

  - 在线流式训练场景可借鉴其错误权重平滑重加权机制，无需维护大模型集成即可获得媲美多模型的预测效果'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有在线boosting两类核心保证无法兼顾：在线梯度提升可在任意序列上保证Brier score与H空间最优预测器可比，但H空间无准确预测器时失效；弱到强提升在满足弱学习条件时可将分类误差降为0，但条件不满足时无性能兜底，且现有方案均需维护大量弱学习器集成，在线计算开销极高。
### 方法关键点
提出Defensive Booster，基于boosting双视角实现双重保证：当随机分类误差持续偏高时，错误权重会生成平滑重加权的硬核证书，证明弱学习条件不成立；仅需调用1个弱分类学习器，无需维护多模型集成。同时推出强自适应变种，可在任意时间区间内满足两类性能保证。
### 关键结果
实验显示其预测效果优于所有现有基线，运行速度提升数个量级；Brier score收敛速率与在线梯度提升一致，弱学习条件满足时分类误差收敛速率与在线分类boosting持平
