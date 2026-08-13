---
title: 'Faithful, Sufficient and Understandable: Rethinking Graph Counterfactual Explanations
  via Discrete Diffusion Inversion'
title_zh: 兼顾可信性充分性可理解性：基于离散扩散反转的图反事实解释
authors:
- David Bechtoldt
- Sidney Bender
affiliations:
- TU Berlin
- BIFOLD–Berlin Institute for the Foundations of Learning and Data
arxiv_id: '2608.12083'
url: https://arxiv.org/abs/2608.12083
pdf_url: https://arxiv.org/pdf/2608.12083
published: '2026-08-12'
collected: '2026-08-13'
category: Other
direction: 图神经网络 · 反事实解释
tags:
- GNN
- Counterfactual Explanation
- Discrete Diffusion
- Diffusion Inversion
- Graph Interpretation
one_liner: 提出GDCE-I图反事实解释方法，兼顾数据流形约束与全编辑空间搜索，性能大幅超过同类方案
practical_value: '- 离散扩散反转的约束编辑思路可迁移到用户兴趣图谱/行为序列的反事实解释，用于定位改变推荐结果的最小干预点

  - 兼顾数据分布约束与全空间搜索的设计逻辑，可复用在推荐运营策略生成，避免输出违反业务规则的无效干预方案

  - 统一的反事实解释评估框架可直接用于推荐可解释性算法的横向对比，解决不同指标评估结论不一致的问题'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
GNN在化学、生物、网络分析等领域预测性能优异，但本身是黑箱模型，难以解释预测逻辑，限制了其在高风险场景的落地。现有图反事实解释方法存在两类缺陷：要么生成的结构编辑偏离数据流形不符合领域规则，要么搜索空间受限无法覆盖全部可行编辑，同时行业缺乏统一的图反事实解释评估标准。
### 方法关键点
提出GDCE-I图反事实解释方法，基于搭载全新离散反转机制的离散去噪扩散模型，实现同时满足领域分布感知、全编辑空间覆盖的最小结构修改生成；同时推导了覆盖可信性、充分性、可理解性的统一评估框架，支持所有方法在同一协议下对比。
### 关键结果
在4个基准数据集上，GDCE-I在统一评估框架下性能大幅领先现有同类方法；分子领域定性实验验证其生成的反事实解释符合数据分布、可解释性强。
