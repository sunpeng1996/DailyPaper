---
title: 'Monetizing Intelligence: Advertising and Subscription Design on LLM Platforms'
title_zh: LLM平台的广告与订阅组合商业化机制设计
authors:
- Yuhang Ji
- Fasheng Xu
- Tianjun Feng
affiliations:
- School of Management, Fudan University
- School of Business, University of Connecticut
arxiv_id: '2610.32945'
url: https://arxiv.org/abs/2610.32945
pdf_url: https://arxiv.org/pdf/2610.32945
published: '2026-10-23'
collected: '2026-10-26'
category: LLM
direction: LLM平台商业化 · 广告订阅组合设计
tags:
- LLM Platform
- Monetization
- Advertising
- Subscription
- Mechanism Design
one_liner: 推导垄断LLM平台广告+订阅组合最优定价机制，揭示效用极化、广告阈值、算力成本三大影响规律
practical_value: '- 自研LLM/AI Agent产品商业化可直接复用四档分层逻辑：零门槛全广告引流层、低付费全广告高权益层、中付费半广告层、高付费无广告层，平衡用户规模、广告收入与会员收入

  - 电商AI导购类产品可落地「广告收入反哺免费层服务质量」策略，扩大低价值用户覆盖的同时降低高付费用户的信息租金，无广告会员定价可较纯订阅模式提升15%-20%

  - 若需合规限制AI广告，可选择中等强度的广告曝光上限，相比完全禁投或无限制投放，消费者总剩余可提升20%左右，同时不影响平台对低价值用户的服务供给'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM平台普遍采用广告+订阅混合商业化模式，但现有媒体定价模型未考虑LLM服务质量与广告价值的强正相关性：更高的响应质量可提升广告匹配精度与转化价值，但广告会降低用户信任、感知体验甚至减少用户提供的个性化上下文，同时免费层高体验会挤压付费会员转化，三类决策的耦合逻辑缺乏量化指引。

### 方法关键点
• 构建垄断平台机制设计模型，核心决策变量为每个用户分层的响应质量（模型能力/推理算力/使用额度）、广告强度、订阅价格
• 引入质量关联广告溢价假设：广告收入随服务质量提升而增长，同时广告成比例降低用户感知的有效服务质量
• 基于消费者质量估值异质性，采用虚拟价值法求解满足激励相容、个体理性约束的最优分层策略

### 关键结果
1. 混合模式可将正质量服务的覆盖阈值从纯订阅下的前50%用户拓展到前70%-80%，但半广告层、无广告层用户效用低于纯订阅模式，出现效用极化，无广告会员定价可提升15%-20%
2. 中等强度的广告上限可最大化消费者总剩余，相比完全禁止广告提升18%，相比无限制广告提升22%
3. 算力成本下降50%时，平均广告强度降低35%，但总广告收入反而提升12%，因为服务质量提升拉高单用户广告价值

### 核心记忆点
LLM平台的广告设计影响的不止看到广告的用户，还会通过分层替代效应改变无广告用户的付费价格与剩余。
