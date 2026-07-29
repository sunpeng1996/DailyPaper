---
title: 'BettiSplit: Topology-Guided Privacy-Aware Split Learning Against Feature Inversion
  and Gradient Leakage'
title_zh: BettiSplit：拓扑引导的隐私感知拆分学习 对抗特征反转与梯度泄漏
authors:
- Akarsh K. Nair
- Muhammad Arifur Rahman
- David Brown
- Mufti Mahmud
affiliations:
- Nottingham Trent University
- King Fahd University of Petroleum & Minerals
- SDAIA–KFUPM Joint Research Center for AI
- Interdisciplinary Research Center for Biosystems and Machines
arxiv_id: '2607.24556'
url: https://arxiv.org/abs/2607.24556
pdf_url: https://arxiv.org/pdf/2607.24556
published: '2026-07-27'
collected: '2026-07-29'
category: Training
direction: 拆分学习 · 隐私训练优化
tags:
- Split Learning
- Privacy Leakage
- Persistent Homology
- Betti Numbers
- Federated Learning
one_liner: 基于Betti拓扑复杂度设计拆分学习切分策略与正则，提升隐私性同时保留模型效用
practical_value: '- 多品牌/多机构联合训练电商推荐/广告模型时，可用Betti复杂度替代逐层攻击测试，快速定位隐私敏感层，降低拆分学习切分评估成本

  - 对用户特征敏感的推荐联邦/拆分训练场景，可引入Betti正则，在不损失推荐精度的前提下提升近5倍特征反转攻击难度

  - 拆分学习切点选择不要仅依赖网络深度启发式规则，优先选择Betti复杂度高的层作为切分点，可获得2~5倍的抗特征反转能力'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
拆分学习是跨端/跨机构协同训练的核心方案，但现有基于网络深度的切分策略未考虑层间隐私风险的异质性，易引发特征反转、梯度泄漏，隐私-效用 tradeoff 表现较差。
### 方法关键点
1. 基于激活值的持久Betti复杂度刻画层间表示的拓扑结构，可定位隐私风险突变区域，无需执行显式攻击即可识别隐私敏感层；
2. 提出BettiSafe切分策略，选择低隐私风险层作为拆分点；
3. 新增Betti正则项，提升表示拓扑复杂度以增加攻击难度。
### 关键结果
相比深度启发式切分方法，BettiSafe抗特征反转能力提升2~5倍且分类精度无损失；Betti正则可将特征反转难度提升近5倍，无模型效用下降。
