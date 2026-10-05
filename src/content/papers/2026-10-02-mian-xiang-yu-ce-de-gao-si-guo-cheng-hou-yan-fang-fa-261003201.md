---
title: Predictively Oriented Gaussian Process Posteriors
title_zh: 面向预测的高斯过程后验方法
authors:
- Callum Lau
- Jeremias Knoblauch
- Louis Sharrock
affiliations:
- University College London
arxiv_id: '2610.03201'
url: https://arxiv.org/abs/2610.03201
pdf_url: https://arxiv.org/pdf/2610.03201
published: '2026-10-02'
collected: '2026-10-05'
category: Training
direction: 高斯过程 · 不确定性校准优化
tags:
- Gaussian Process
- Uncertainty Calibration
- Model Robustness
- Posterior Sampling
- Predictive Modeling
one_liner: 提出面向预测的PrO-GP，解决标准GP模型误设下预测分布校准差的问题
practical_value: '- 推荐系统冷启动/稀疏样本场景下，可采用PrO-GP替代标准GP做用户行为建模，降低核函数选择不当带来的预测偏差

  - Agent 决策环节的不确定性估计需求中，可复用PrO-GP的高效采样方案，提升模型误设下的预测分布校准度

  - 电商转化率预估等对概率校准要求高的场景，可借鉴PrO-GP以预测不确定性为核心的建模思路，提升预估可靠性'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
标准Gaussian Processes (GP) 依赖核函数、观测模型的人工选择，子优选择会导致模型误设，无法拟合真实数据生成过程，尤其多模态、稀疏数据场景下预测校准度差，影响下游决策可靠性。
### 方法关键点
1. Predictively Oriented Gaussian Processes (PrO-GPs) 直接以预测不确定性为核心推理目标，替代传统GP以参数拟合为核心的逻辑，对模型误设鲁棒性更强
2. 推导非参数场景下PrO后验的简化表达式，配套可落地的高效采样方案，解决原非参数模型PrO后验计算不可解的问题
### 关键结果
合成数据与真实数据实验验证，在模型误设场景下，PrO-GPs的预测分布校准效果显著优于标准GP；针对多模态数据可同时覆盖多个分布分支，避免传统GP单峰拟合的偏差。
