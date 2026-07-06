---
title: Unveiling the Non-Monotonic Effect of Privacy on Generalization under Byzantine
  Robustness
title_zh: 拜占庭鲁棒分布式学习下隐私对泛化的非单调效应揭示
authors:
- Thomas Boudou
- Batiste Le Bars
- Nirupam Gupta
- Aurélien Bellet
affiliations:
- Inria
- Université de Montpellier
- INSERM
- Université de Lille
- University of Copenhagen
arxiv_id: '2607.01492'
url: https://arxiv.org/abs/2607.01492
pdf_url: https://arxiv.org/pdf/2607.01492
published: '2026-07-01'
collected: '2026-07-06'
category: Training
direction: 分布式训练 · 拜占庭鲁棒隐私优化
tags:
- Distributed Learning
- Local Differential Privacy
- Byzantine Robustness
- Generalization
- Federated Learning
one_liner: 证明拜占庭鲁棒分布式学习中隐私对泛化的影响非单调，高低隐私区间效应完全相反
practical_value: '- 端侧联邦推荐/广告模型训练时，强隐私合规场景下可直接提高LDP噪声强度，既满足隐私要求又能降低模型过拟合、提升泛化能力

  - 弱隐私场景下做分布式多参与方推荐模型训练，提升隐私强度时需同步叠加正则、dropout等策略抵消泛化下降的副作用

  - 跨商户联合训练电商推荐/广告模型时，可根据不同参与方的隐私合规等级动态调整噪声量级，匹配对应的泛化优化方案'
score: 4
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有分布式学习研究提出拜占庭鲁棒性、Local Differential Privacy (LDP)、优化误差三者存在三元悖论，但未明确该规律是否适用于泛化误差，联邦学习等场景下隐私保护与模型泛化的权衡缺乏明确理论指导。
### 方法关键点
通过推导LDP约束下拜占庭鲁棒分布式学习的算法稳定性上下界，对不同隐私噪声区间的泛化误差变化规律进行严格理论证明，配套多组对照实验验证理论结论的普适性。
### 关键结果
1. 高噪声（强隐私）区间，提升隐私强度可降低泛化误差，鲁棒性与隐私无冲突，原有三元悖论不成立；
2. 低噪声（弱隐私）区间，提升隐私强度会劣化泛化表现，原有三元悖论生效；
3. 理论推导的稳定性边界与实验结果完全匹配，验证了隐私对泛化的非单调效应的普适性。
