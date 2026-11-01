---
title: 'LOB-Impact Benchmark: Emergent Market Impact in Generative Limit Order Book
  Models'
title_zh: LOB-Impact基准：生成式限价订单簿模型的涌现市场冲击
authors:
- George Nigmatulin
- Valentin Mohl
- Sascha Frey
- Kang Li
- Aramis Marti-Shahandeh
- Mihai Cucuringu
- Anisoara Calinescu
- Jakob Foerster
- Stefan Zohren
affiliations:
- University of Oxford
- British Open-ended Learning and Discovery Lab (BOLD)
- University of California Los Angeles
- Oxford Man Institute of Quantitative Finance
arxiv_id: '2610.27100'
url: https://arxiv.org/abs/2610.27100
pdf_url: https://arxiv.org/pdf/2610.27100
published: '2026-10-18'
collected: '2026-11-01'
category: Eval
direction: Agent世界模型 · 生成式LOB评估基准
tags:
- Benchmark
- Generative Model
- World Model
- Trading Agent
- Counterfactual Evaluation
one_liner: 提出开源LOB-Impact基准，评估生成式限价订单簿模型的市场冲击涌现与反事实响应能力
practical_value: '- 评估生成式世界模型时，不能仅做历史数据分布对齐，需补充反事实注入测试，验证Agent动作对环境的反馈合理性，规避sim-to-real
  gap

  - 多阶段评估框架可直接复用：先自由生成测基础特性，再注入干预测响应规律，最后测干预后恢复情况，适配各类生成式环境模拟器评估

  - 生成式序列模型仅做next-token预测也可能涌现符合真实规律的环境反馈，可降低世界模型的标注训练成本'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
生成式LOB作为交易Agent的世界模型，需精准拟合真实市场冲击机制，否则会导致Agent学习的策略出现严重sim-to-real gap；现有评估指标仅对比生成序列与历史数据的分布差异，未覆盖Agent自身订单带来的反事实响应评估。
### 方法关键点
提出三阶段开源LOB-Impact基准：1）自由生成阶段，评估订单流持续性与价格扩散性的匹配度；2）元订单注入阶段，测量冲击规律的指数与振幅；3）执行后窗口阶段，评估冲击松弛特性；同时通过对比可见注入与模拟器盲测对照，分离模型学习到的响应与订单簿固有机制。
### 关键结果数字
在5只纳斯达克股票、5个自回归生成模型上测试，所有模型均涌现出市场冲击特性，冲击指数范围为0.63~1.21，略高于传统平方根冲击定律的0.5；暂未观测到冲击衰减效应，归因于模型上下文窗口过短。
