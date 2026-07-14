---
title: Diversified Multinomial Logit Contextual Bandits
title_zh: 面向多样性感知选品优化的多样化MNL上下文老虎机算法
authors:
- Heesang Ann
- Taehyun Hwang
- Min-hwan Oh
affiliations:
- Seoul National University
arxiv_id: '2607.11684'
url: https://arxiv.org/abs/2607.11684
pdf_url: https://arxiv.org/pdf/2607.11684
published: '2026-07-13'
collected: '2026-07-14'
category: RecSys
direction: RecSys · 多样性感知选品优化
tags:
- Contextual Bandit
- MNL
- Assortment Optimization
- Diversity
- UCB
- Submodular
one_liner: 提出融合相关性与选品多样性的DMNL上下文老虎机模型及高效白盒UCB算法，无需黑盒优化oracle
practical_value: '- 可直接复用DMNL模型结构，把多样性以submodular函数形式嵌入MNL选择概率，代替现有手动调权重的相关性-多样性平衡方案，无需人工调超参

  - 工程上可落地OFU-DMNL的逐物品贪心构造策略，O(NK)每轮复杂度比穷举法降低2-3个数量级，适合电商首页/推荐流等大流量场景的实时选品

  - 做在线A/B实验时可借鉴其regret界设计的参数调优逻辑，优先保证多样性函数的严格submodular性，可大幅降低探索成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有MNL上下文老虎机仅基于物品相关性建模用户选择，完全忽略选品内多样性的收益，而submodular/组合老虎机虽然建模了多样性奖励，却缺乏结构化的用户选择概率支撑，两类方案都无法解决真实电商/推荐场景中相关性与多样性的权衡问题，且现有组合老虎机依赖黑盒优化oracle，工程落地性差。
### 方法关键点
- 提出DMNL（多样化MNL）上下文老虎机模型，在传统MNL选择概率中加入通用submodular多样性函数，将相关性与多样性权衡正式融入统一模型，可兼容品类数、属性覆盖、嵌入空间分散度等各类多样性度量。
- 设计白盒UCB算法OFU-DMNL，采用逐物品最大化乐观边际收益的方式构造选品，无需黑盒优化oracle，每轮复杂度仅O(NK)。
- 理论上证明该算法可获得至少(1-1/(e+1))的近似率，近似效果优于传统submodular最大化的(1-1/e)基准，累计regret界为Õ(d√(T/K))，与纯MNL老虎机的近似最优regret匹配。
### 关键实验
在合成数据集上对比UCB-MNL、TS-MNL、OFU-MNL+等5个基线，在N=20、K=5、T=10000的配置下，OFU-DMNL的regret与穷举法相当，但运行时间仅为穷举法的~0.5%，在不同规模、不同多样性权重配置下均稳定优于所有基线。
### 核心结论
将多样性以submodular函数形式嵌入MNL选择概率，不仅能更好拟合真实用户选择行为，还能在不损失统计效率的前提下实现工程可落地的高效选品优化。
