---
title: Bellman Calibration for Marginalized Importance Weighting in Offline Reinforcement
  Learning
title_zh: 离线强化学习中边缘化重要性加权的Bellman校准
authors:
- Lars van der Laan
- Nathan Kallus
affiliations:
- Stanford University
- Netflix
- Cornell University
arxiv_id: '2608.24858'
url: https://arxiv.org/abs/2608.24858
pdf_url: https://arxiv.org/pdf/2608.24858
published: '2026-08-25'
collected: '2026-08-27'
category: Eval
direction: 离线强化学习 · 重要性加权校准
tags:
- Offline-RL
- Importance-Weighting
- Bellman-Calibration
- Post-Processing
- Policy-Evaluation
one_liner: 提出模型无关的保序Bellman校准后处理，降低离线RL重要性加权的残差占用失衡
practical_value: '- 电商/推荐场景用离线RL优化排序/出价策略时，可复用该后处理校正重要性权重，降低离线日志分布偏移带来的策略评估误差

  - 离线策略调优缺乏在线A/B测试条件时，可引入该校准逻辑补充监督验证信号，解决无标注离线数据下的超参选择、早停依据缺失问题

  - 该方法是模型无关的轻量后处理，可直接对接现有任何离线RL重要性权重估计管线，无需改动原有模型结构，接入成本极低'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
离线RL中边缘化重要性加权通过折扣占用率比对离线状态-动作样本重加权，实现目标策略评估；现有估计器因函数近似、正则化、优化不完全存在残差占用失衡问题，且目标缺乏直接监督验证损失，无法支撑超参调优、模型选择与早停。
### 方法关键点
提出保序Bellman校准，为一维、模型无关的后处理方法，通过在一维非递减变换类上执行拟合占用率比评估（FORE），校正初始估计的尺度与形状，同时保留原始估计的排序信息。
### 关键结果
推导校准-细化边界，证明小校准误差的拟合比性能接近最优后处理效果；保序Bellman校准具备有限样本校准保证，相对初始估计的最优单调变换满足KL神谕不等式，下游策略价值估计等目标占用泛函的误差控制在统计误差范围内。
