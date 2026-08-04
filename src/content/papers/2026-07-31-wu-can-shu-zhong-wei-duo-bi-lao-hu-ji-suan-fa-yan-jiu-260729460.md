---
title: Parameter-Free Heavy-Tailed Bandits
title_zh: 无参数重尾多臂老虎机算法研究
authors:
- Gianmarco Genalti
- Alberto Maria Metelli
affiliations:
- Politecnico di Milano
arxiv_id: '2607.29460'
url: https://arxiv.org/abs/2607.29460
pdf_url: https://arxiv.org/pdf/2607.29460
published: '2026-07-31'
collected: '2026-08-04'
category: RecSys
direction: 重尾在线学习 · 广告推荐探索决策
tags:
- Multi-Armed Bandits
- Heavy-tailed Distribution
- Online Learning
- Regret Minimization
- Online Advertising
one_liner: 解决重尾老虎机未知尾参数的自适应难题，给出最优权衡边界与无参数调度探索算法
practical_value: '- 在线广告出价、爆品挖掘等存在极端收益的场景，可直接复用该无参数重尾老虎机算法，无需提前预估尾部分布参数，降低前期数据依赖

  - 冷启动探索场景可借鉴其调度探索策略，平衡分布相关/无关的regret指标，在未知reward分布特性时也能保证次线性regret

  - 存在极端值的推荐场景（比如高客单商品、爆款内容），可参考其统计代价量化方法，评估无参算法的性能损耗边界'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有重尾老虎机的regret最小化算法均要求预先已知尾指数ε、矩边界u，而这两个决定极端事件频率与量级的参数，在有限观测下极难可靠推断，是COLT 2025公开待解问题。
### 方法关键点
1. 推导未知u时所有算法必须遵守的分布依赖、分布无关regret的严格权衡边界；
2. 提出调度探索算法，无需已知u即可在对数因子范围内匹配该自适应边界；
3. 将探索调度校准到ε=1端点，实现算法无需已知ε即可运行。
### 关键结果
该算法对任意固定ε>0均可实现次线性regret，同时证明不存在算法能对所有ε∈(0,1]一致保证次线性regret，完整解决公开问题，严格刻画了适配未知重尾的统计代价。
