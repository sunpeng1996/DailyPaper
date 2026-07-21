---
title: 'Vector Search As Nearest Neighbor Matching: RAG-based Policy Learning in Causal
  Inference'
title_zh: 基于最近邻匹配的向量搜索：因果推断下的RAG策略学习
authors:
- Masahiro Kato
- Taka Kato
affiliations:
- The University of Tokyo
- NP-hard Inc.
arxiv_id: '2607.18225'
url: https://arxiv.org/abs/2607.18225
pdf_url: https://arxiv.org/pdf/2607.18225
published: '2026-07-20'
collected: '2026-07-21'
category: RAG
direction: RAG策略学习 · 因果推断理论保障
tags:
- RAG
- causal inference
- policy learning
- vector search
- nearest neighbor matching
one_liner: 将RAG动作选择与因果最近邻匹配关联，给出带理论regret边界的一/两步RAG策略学习方法
practical_value: '- RAG驱动的业务决策（如广告出价、权益发放、推荐排期）可复用两步框架：先向量搜索召回相似场景历史样本，再生成模型预估不同动作收益，选最优解

  - 可借鉴其regret拆解思路，定位RAG策略效果瓶颈是召回阶段候选漏召还是生成阶段排序错误，针对性优化模块

  - 电商智能体动作选择场景下，可借用因果最近邻匹配逻辑优化向量搜索召回规则，提升相似历史案例匹配精度，降低决策偏差'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
RAG已广泛应用于推荐、智能体动作选择等场景，但缺乏决策层面的理论保障，无法量化决策误差的来源与边界，难以支撑高可靠性要求的业务场景。

### 方法关键点
1. 在因果潜在结果框架下形式化RAG动作选择问题，首次将面向动作的向量搜索与因果推断中的最近邻匹配建立理论关联；
2. 两类RAG策略学习方法：两步法先通过向量搜索召回嵌入空间中与当前动作关联的邻域证据，再由生成器估计条件预期收益差，经插件规则选最优动作；一步法适配中间计算过程不可观测的端到端决策场景；
3. 将两步法的regret拆解为候选生成regret、候选内选择regret，结合最近邻估计器与Transformer的预测误差保证，给出后者的严格理论上界。

### 关键结果
从理论上证明了两步RAG策略的选择误差可控，为RAG在决策类场景的落地提供了可量化的理论支撑。
