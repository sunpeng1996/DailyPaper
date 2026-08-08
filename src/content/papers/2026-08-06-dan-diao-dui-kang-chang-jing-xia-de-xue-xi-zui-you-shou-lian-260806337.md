---
title: Optimal Rates for Learning with Monotone Adversaries
title_zh: 单调对抗场景下的学习最优收敛速率
authors:
- Anay Mehrotra
affiliations:
- Stanford University
arxiv_id: '2608.06337'
url: https://arxiv.org/abs/2608.06337
pdf_url: https://arxiv.org/pdf/2608.06337
published: '2026-08-06'
collected: '2026-08-08'
category: Other
direction: 机器学习理论 · 对抗场景泛化边界
tags:
- Learning Theory
- VC Dimension
- Generalization Bound
- Adversarial Learning
- Minimax Rate
one_liner: 证明VC维≥2时单调对抗插入正确标注样本场景下对数泛化误差损失为固有代价
practical_value: '- 训练数据增强/清洗阶段，避免引入依赖原始样本分布的策略性正确样本插入，否则可能抬升泛化误差

  - 低VC维简单模型对该类样本污染的鲁棒性显著优于高VC维复杂模型

  - 其余结论为纯理论推导，暂无直接可复用的工程落地方法'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统PAC学习假设训练样本独立同分布，但实际数据清洗、增强等操作会破坏样本可交换性。已有研究发现单调对抗场景（对手观测干净i.i.d.样本后插入若干正确标注样本，混合洗牌后给学习者）下ERM泛化误差为$O((d/n)\log(n/d))$，高于普通PAC的$\Theta(d/n)$，但不确定额外对数项是算法缺陷还是固有代价。
### 方法关键点
构造统一反例框架推导下界，针对d=1场景基于单包含图的留一法分析设计非proper学习器得到上界。
### 关键结果
d=1时最小最大期望误差为$\Theta(1/n)$，d≥2时为$\Theta((d/n)\log(n/d))$；替换为Littlestone维时结论一致，即插入正确标注样本反而会让学习难度提升对数倍。
