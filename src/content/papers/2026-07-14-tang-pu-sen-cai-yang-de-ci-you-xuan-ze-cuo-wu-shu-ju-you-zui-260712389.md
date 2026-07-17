---
title: Thompson Sampling Is 2-Competitive for Mistakes
title_zh: 汤普森采样的次优选择错误数具有2倍最优竞争比
authors:
- Mark Sellke
- Gregory Valiant
arxiv_id: '2607.12389'
url: https://arxiv.org/abs/2607.12389
pdf_url: https://arxiv.org/pdf/2607.12389
published: '2026-07-14'
collected: '2026-07-17'
category: RecSys
direction: 推荐系统基础 · 多臂老虎机理论
tags:
- Thompson Sampling
- Multi-Armed Bandit
- Bayesian Model
- Regret Minimization
one_liner: 证明贝叶斯多臂老虎机下汤普森采样的期望次优选择次数最多为最优策略的2倍
practical_value: '- 新品冷启动、新广告探索等场景可优先选汤普森采样，其错误上限为最优策略的2倍，可直接量化探索损失做ROI预估

  - 短周期促销、限时流量测试等对错误次数敏感的场景，可直接复用该结论作为算法选型的理论依据

  - 结论在固定时间窗口、几何折扣等不同时间权重设置下均成立，适配日常推荐、大促等不同业务周期的探索需求'
score: 7
source: arxiv-stat.ML
depth: abstract
---

## 动机
多臂老虎机是推荐、广告系统探索策略的核心基础，现有研究多聚焦累积收益/后悔最小化，针对次优选择次数的优化缺乏通用理论支撑。2014年Guha等人提出猜想：汤普森采样的次优选择次数不超过最优策略的2倍，仅在双臂场景下获证，通用场景有效性未得到证实。
## 方法关键点
基于贝叶斯老虎机框架，仅要求臂的潜在过程相互独立、且仅在被选中时更新状态，通过建立单步估计对比最优策略与汤普森采样的贝尔曼递归完成推导，不依赖额外分布假设。
## 关键结果数字
证明汤普森采样的期望次优选择（错误）次数最多是任意策略的2倍，该2倍系数已达理论最优；结论适配任意非递增轮次权重序列，包括固定时间窗口、几何折扣等工业界常用设置，完整验证了2014年的猜想。
