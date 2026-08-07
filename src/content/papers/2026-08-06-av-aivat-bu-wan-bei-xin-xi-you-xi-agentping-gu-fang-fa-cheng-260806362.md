---
title: 'AV-AIVAT: 74x Cheaper Agent Evaluation with Certified Anytime-Valid Stopping
  in Imperfect-Information Games'
title_zh: AV-AIVAT：不完备信息游戏Agent评估方法，成本降至1/74且带有效性证明
authors:
- Boning Li
- Yu Chen
- Longbo Huang
affiliations:
- Tsinghua University
arxiv_id: '2608.06362'
url: https://arxiv.org/abs/2608.06362
pdf_url: https://arxiv.org/pdf/2608.06362
published: '2026-08-06'
collected: '2026-08-07'
category: Agent
direction: Agent 交互式评估效率优化
tags:
- Agent Evaluation
- Confidence Sequence
- Variance Reduction
- Anytime Valid
- Imperfect Information Game
one_liner: 结合AIVAT方差缩减与置信序列，实现统计有效、成本低74倍的不完备信息场景Agent评估
practical_value: '- 多轮交互式Agent（如电商导购Agent、广告竞价策略Agent）评估时，可借鉴AIVAT方差缩减+置信序列（CS）的架构，在保证统计有效性的前提下提前终止评估，大幅降低推理/人工标注成本

  - 推荐/广告策略A/B测试早停场景，可复用本文past-only在线价值模型设计：仅用历史样本更新校正模型，避免当前样本影响自身校正，防止早停的统计显著性被高估

  - 对外发布算法效果验证结论时，可参考本文的release protocol，公开校正后数据流、停止规则、置信度配置等元数据，让第三方可复现验证结论，规避选择性停止的造假风险'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
不完备信息场景下的Agent评估（如游戏对战、导购交互、竞价博弈）通常需要大量交互样本才能区分能力差异，固定预算评估要么在结论明确后仍浪费成本，要么样本量不足无法得出有效结论；而直接用普通置信区间早停会破坏统计显著性，导致假阳性率飙升，亟需同时满足统计有效、低成本的早停评估方案。

### 方法关键点
- 提出AV-AIVAT框架，结合AIVAT方差缩减与置信序列（CS）：AIVAT通过条件零均值校正降低收益方差，CS保证任意时间监控、早停时统计有效性仍成立
- 设计past-only在线价值模型：仅用历史样本更新校正模型，当前样本不参与自身校正，保留AIVAT的无偏性，解决校正模型冷启动问题
- 双置信序列设计：Asymptotic CS（AsympCS）适配实际业务场景，随样本方差自适应调整区间，实现极致早停；Empirical-Bernstein CS（EB-CS）提供有限样本下的严格有效性证明，适配需要审计的合规场景

### 关键实验
在15组LLM Poker Agent、共71439手德州扑克数据集上验证：AIVAT将收益方差中位数降低54×，AsympCS下达到±1BB精度所需样本量比原始收益少74×，EB-CS下早停效率中位数提升1.37×；零效应模拟实验中，普通固定置信区间早停假阳性率达61%，而AV-AIVAT的CS几乎完全筛除假阳性结论。

**最值得记住的一句话**：只要保证校正模型仅用历史样本更新，方差缩减+任意时间有效置信序列的架构，可在不损失统计有效性的前提下，将交互式Agent评估成本降低1-2个数量级。
