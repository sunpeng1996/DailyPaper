---
title: 'Cascading Bandits with Noisy Observations: Algorithms and Regret Bounds'
title_zh: 带噪声观测的级联老虎机算法设计与后悔界分析
authors:
- Yashaswini Kaluguri
- Nikhil Karamchandani
arxiv_id: '2610.29381'
url: https://arxiv.org/abs/2610.29381
pdf_url: https://arxiv.org/pdf/2610.29381
published: '2026-10-21'
collected: '2026-10-23'
category: RecSys
direction: 在线学习排序 · 级联老虎机优化
tags:
- Cascading Bandits
- Upper Confidence Bound
- Online Learning to Rank
- Regret Bound
- Noisy Feedback
one_liner: 针对带位置成本、观测噪声的级联老虎机场景，提出两类UCB算法并证明最优后悔界
practical_value: '- 搜索/推荐页排序在线调优场景，可复用DP-UCB框架适配带位置偏置、观测噪声的实时调优需求，避免现有级联老虎机无噪反馈假设带来的效果偏差

  - 冷启动商品/广告排序探索场景，若满足无假阳性反馈（如点击必为真实兴趣），可采用O((L-K)logT)轻量UCB算法，平衡探索效率与算力开销

  - 多位置曝光成本差异的流量分配场景，可先参考论文噪声分类方法判定是否存在单臂可分排序得分，再选择对应算法最小化累计后悔'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有级联老虎机框架大多假设观测反馈无噪、忽略不同排序位置的曝光成本，无法适配真实搜索推荐中用户点击存在误触、顶部位置流量成本更高的场景。

### 方法关键点
1. 定义带位置依赖成本、观测噪声的新型随机级联老虎机范式，划分噪声模型子类：无假阳性场景下存在单臂得分可直接排序选最优短名单，无测量成本场景仅排序可分，噪声+成本同时存在时选品+排序均不可分；
2. 得分可分场景提出UCB基算法，得分不可分场景提出DP-UCB框架，将乐观估计嵌入动态规划求解最优短名单。

### 关键结果数字
得分可分场景下算法达到O((L-K)logT)实例依赖后悔，匹配理论下界；得分不可分场景下算法达到O(LK logT)后悔，两类算法均在合成、真实数据集上通过仿真验证了理论有效性。
