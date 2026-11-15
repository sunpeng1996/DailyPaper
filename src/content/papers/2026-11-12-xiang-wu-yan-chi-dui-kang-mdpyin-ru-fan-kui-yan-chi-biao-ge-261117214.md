---
title: 'Introducing Feedback Delays to Non-Delayed Adversarial MDPs: Optimal $\sqrt
  S$ and $\sqrt K$ Dependencies in Tabular and Linear AMDPs'
title_zh: 向无延迟对抗MDP引入反馈延迟：表格与线性AMDP最优√S/√K界
authors:
- Aarush Kulkarni
- Khang Nguyen
- William Chang
- Yan Dai
arxiv_id: '2611.17214'
url: https://arxiv.org/abs/2611.17214
pdf_url: https://arxiv.org/pdf/2611.17214
published: '2026-11-12'
collected: '2026-11-15'
category: Agent
direction: Agent 对抗MDP最优regret界算法优化
tags:
- Adversarial MDP
- Regret Minimization
- Feedback Delay
- Reinforcement Learning
- Online Learning
one_liner: 提出主动引入反馈延迟的通用技术，解决表格与线性AMDP的长期regret界开放问题
practical_value: '- 电商广告/推荐动态策略迭代场景，可借鉴主动引入短反馈延迟的思路，缓解新旧策略数据分布偏差对Q值估计的影响

  - 延迟反馈场景（如电商转化回流延迟、广告效果滞后）的策略优化，可复用论文适配延迟的regret界推导逻辑

  - 稀疏访问的state-action对优化，可借鉴访问概率阈值截断方法，避免过长时间等待低概率样本反馈'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
表格型AMDP现有K轮regret界为$	ilde O(HS\\sqrt{AK})$，与下界$\\Omega(H\\sqrt{SAK})$存在$\\sqrt S$ gap，是多年未解决的开放问题；线性AMDP无模拟器/强探索假设的高效算法regret界仅为$	ilde O(K^{3/4})$，远未达到最优$	ilde O(\\sqrt K)$。核心难点是动态策略的Q函数估计：旧策略采集的数据与当前策略存在分布偏差，冻结策略等待反馈会恶化K依赖项。
### 方法关键点
提出主动引入反馈延迟的通用技术，用未来episode数据估计当前策略Q值且不停止策略更新；配套设计带拒绝的几何重采样（GRR）处理延迟期间的策略变化，设置访问概率阈值避免低频次state-action对等待过长延迟。
### 关键结果
1. 表格AMDP取得$	ilde O(\	ext{poly}(H)\\sqrt{SAK})$ regret界，匹配下界，解决长期开放问题；
2. 线性AMDP取得$	ilde O(\	ext{poly}(d,H)\\sqrt K)$ regret界，为首个K依赖最优的高效算法；
3. 原生适配总延迟为$\\mathfrak D$的延迟AMDP场景，取得S与$\\mathfrak D$（表格）、K与$//
ewcommand{\rak}[1]{//#1}$\rak D$（线性）均最优的regret界。
