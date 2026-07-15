---
title: 'Bet on Features: Anytime-Valid and Feature-Aware Auditing of Conditional Quantile
  Forecasters'
title_zh: 特征下注：条件分位数预测器的随时有效、特征感知审计框架
authors:
- Ivane Antonov
- Sohom Mukherjee
- Richard Pibernik
- Yo Joong Choe
affiliations:
- Julius-Maximilians-Universität Würzburg
- Zaragoza Logistics Center
- INSEAD
arxiv_id: '2607.11653'
url: https://arxiv.org/abs/2607.11653
pdf_url: https://arxiv.org/pdf/2607.11653
published: '2026-07-13'
collected: '2026-07-15'
category: Eval
direction: 分位数预测器校准 · 流式模型监控
tags:
- Quantile Forecasting
- Model Auditing
- Distribution-free Testing
- Streaming Monitoring
- Calibration
one_liner: 提出无分布博弈论框架，支持非独立同分布场景下黑盒分位数预测器的特征级流式校准审计
practical_value: '- 电商库存预测、需求分位数预估场景可复用该框架做流式校准度监控，无需独立同分布假设，适配流量漂移、大促等非稳态场景

  - 特征级校准度归因方法可直接复用，快速定位分位数预测偏差关联的核心特征（如价格、活动标签、用户分层特征），降低排查成本

  - 无需模型白盒权限，可直接对接黑盒LLM/时序预测服务输出做线上审计，适配第三方预测服务的监控需求'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
黑盒条件分位数预测广泛用于供应链库存、需求预估等非对称成本决策场景，现有固定窗口期回测校准方法无法适配流式数据漂移、模式切换的线上场景，且未考虑审计方特征粒度差异导致的校准判定偏差。
### 方法关键点
1. 基于博弈论构建无分布假设的测试框架，支持非独立同分布损失下的连续审计，可针对审计方掌握的特征集定制待检测偏差；
2. 推导特征线性关联偏差的有限时间检测保障，证据过程可解释到特征维度，输出特征粒度的校准偏差证据。
### 关键结果
在仿真与真实数据验证中，检测出主流时序预测模型Chronos-2在多个相关特征维度存在严重校准偏差。
