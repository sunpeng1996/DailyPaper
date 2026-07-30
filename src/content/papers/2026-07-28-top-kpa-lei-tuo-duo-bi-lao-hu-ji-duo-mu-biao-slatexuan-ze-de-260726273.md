---
title: 'Top-$k$ Pareto Bandits: Hypervolume Regret for Multi-Objective Slate Selection'
title_zh: Top-k帕累托多臂老虎机：多目标Slate选择的超体积后悔研究
authors:
- Nicolas Gutowski
- Fabien Chhel
- Alexandre Letard
- Sylvain Lamprier
affiliations:
- Université d’Angers
- ESEO
- ESAIP
- AlphaEdge
arxiv_id: '2607.26273'
url: https://arxiv.org/abs/2607.26273
pdf_url: https://arxiv.org/pdf/2607.26273
published: '2026-07-28'
collected: '2026-07-30'
category: RecSys
direction: 多目标推荐 · Slate选择Bandit优化
tags:
- Multi-Objective Bandit
- Slate Recommendation
- Pareto Frontier
- UCB
- Regret Bound
one_liner: 提出THV-UCB多目标bandit算法，给出严格regret界，支持小集合近似帕累托前沿
practical_value: '- 多目标推荐/广告场景可直接借鉴THV-UCB思路，用边际超体积贡献做greedy slate选择，兼顾GMV、点击率、多样性等多维度指标，无需手动调权重

  - 小k值slate近似帕累托前沿的结论可复用，平衡计算效率与多目标tradeoff效果，适合高并发的推荐/广告serving场景

  - 超体积regret可作为多目标推荐的离线评测指标，替代传统单指标加权求和，更客观反映多维度均衡表现'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
多目标决策（如推荐需兼顾点击率、GMV、多样性等冲突指标）通常需要帕累托最优解集合，传统多目标bandit多针对单臂选择，缺乏面向top-k slate选择的优化框架与理论保证。

### 方法关键点
定义α-近似超体积regret作为优化目标（α=1-1/e，对应单调次模函数贪心最大化的近似保证），THV-UCB乐观算法基于臂的边际超体积贡献的乐观估计贪心选臂，适配半bandit反馈场景。

### 关键结果
给出无gap的regret界为$	ilde{O}(d\sqrt{nkT})$，gap依赖的regret界为$	ilde{O}(nk^{2.5}/Δ_{\min})$，当臂区分度足够时regret随T呈多对数级增长，验证了小集合近似帕累托前沿的可行性。
