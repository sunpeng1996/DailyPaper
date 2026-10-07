---
title: Variance-Optimal Off-Policy Evaluation with Conjunct Effect Modeling
title_zh: 基于联合效应建模的方差最优离轨策略评估方法
authors:
- Nicolò Felicioni
- Michael Benigni
- Maurizio Ferrari Dacrema
- Paolo Cremonesi
affiliations:
- Spotify
- Politecnico di Milano
arxiv_id: '2610.08677'
url: https://arxiv.org/abs/2610.08677
pdf_url: https://arxiv.org/pdf/2610.08677
published: '2026-10-06'
collected: '2026-10-07'
category: RecSys
direction: 推荐系统离线评估 · OPE方差优化
tags:
- Off-Policy Evaluation
- Doubly Robust
- Recommender System
- Contextual Bandit
- Variance Reduction
one_liner: 构建插值于DR与OffCEM的无偏估计族，推导闭式最优系数得到VOCEM，所有测试场景MSE均优于两个端点
practical_value: '- 电商推荐/广告新策略上线前的离线A/B测试，可直接用VOCEM替换原有DR/IPS estimator，降低高维商品/广告空间下OPE的方差，避免长尾动作极端权重导致的评估失真

  - 已有动作聚类（如商品类目、广告创意分组、内容标签聚类）的业务场景，无需改动原有聚类逻辑，仅额外计算样本层面的A、B统计量即可得到最优插值系数，工程落地成本极低

  - 超大规模动作空间（如百万级SKU推荐）场景，默认以聚类级权重打底，自适应引入动作级权重校正，既保留DR的无偏性，又规避其在长尾动作上的不稳定性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
上下文老虎机场景下的离轨策略评估（OPE）是推荐、广告系统上线新策略前的核心离线评估手段，传统Doubly Robust（DR）估计虽无偏，但动作级重要性权重在大动作空间（如电商百万SKU、信息流海量内容）下方差极高，极端权重易导致评估结果完全失真；OffCEM用聚类级权重降低方差，但依赖奖励模型局部正确性，且无方差最优的理论保证，二者间缺乏可量化的最优中间方案。
### 方法关键点
- 证明DR与OffCEM属于同一无偏估计族的两个端点，通过λ∈[0,1]插值聚类级和动作级权重，在动作级共同支撑、奖励模型局部正确假设下，所有插值估计均保持无偏
- 推导方差关于λ的二次函数表达式，得到闭式最优系数λ*，截断到[0,1]区间后保证最优估计方差严格不大于DR或OffCEM的方差
- 基于离线日志样本直接计算A、B两个统计量即可得到经验最优λ̂，无额外数据依赖，计算复杂度O(n)，工程落地成本极低
### 关键实验
在15组合成数据、8组真实基准数据集（EUR-Lex 4K、Wiki10-31K）上对比DR、OffCEM，VOCEM在全部23个测试场景下MSE均优于两个基线：合成场景下MSE较OffCEM降低25.1%~36.6%，4000动作的大空间下DR MSE是OffCEM的83.38倍，VOCEM仍较OffCEM低68.2%；真实数据集上MSE较OffCEM最高降低39.9%，DR MSE最高达OffCEM的132.94倍。
### 核心记忆点
大动作空间OPE场景下，自适应插值聚类级与动作级重要性权重，可在无偏前提下实现方差最优，比单一使用DR或聚类级权重稳定性大幅提升
