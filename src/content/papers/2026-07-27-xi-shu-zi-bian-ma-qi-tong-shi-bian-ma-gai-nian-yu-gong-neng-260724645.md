---
title: 'Sparse Autoencoders Encode Both Concepts and Functions: The Downstream Geometry
  of Feature Effects'
title_zh: 稀疏自编码器同时编码概念与功能：特征效应的下游几何研究
authors:
- Phu Gia Hoang
- Anwoy Chatterjee
- Tanmoy Chakraborty
- Iryna Gurevych
- Subhabrata Dutta
affiliations:
- Technical University of Darmstadt
- UKP Lab
- Indian Institute of Technology Delhi
arxiv_id: '2607.24645'
url: https://arxiv.org/abs/2607.24645
pdf_url: https://arxiv.org/pdf/2607.24645
published: '2026-07-27'
collected: '2026-07-29'
category: LLM
direction: 大模型可解释性 · 稀疏自编码器特征分析
tags:
- Sparse Autoencoder
- Interpretability
- Feature Analysis
- LLM Steering
- Mechanistic Interpretability
one_liner: 提出FEGA无监督框架分析SAE特征干预效应几何，区分两类特征解释行为不一致性
practical_value: '- 做LLM4Rec/推荐文案生成的可控 steering 时，优先选用对应静态属性（如商品类目、价格）的value-like
  SAE特征，生成稳定性更高

  - 不要依赖单一SAE特征实现稳定的模型输出导向，可组合多个低维效应的value-like特征提升可控性

  - FEGA无监督框架可直接复用，用于评估业务定制SAE的特征因果效应，筛除效果不稳定的pointer-like特征'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
SAE作为LLM可解释性工具落地受限：特征激活描述清晰但因果效应不稳定、跨prompt导向差异大、基于激活的特征选择易遗漏有效特征，此前研究仅聚焦模型内部特征几何，未关注干预后的输出侧变化。
### 方法关键点
提出无监督框架Feature-Effect Geometry Analysis(FEGA)，跨上下文移除同一激活的SAE特征，分析对应logit变化的分布特征；将SAE特征分为两类：绑定静态属性（如事实属性）的value-like特征、关联上下文依赖操作的pointer-like特征。
### 关键结果
仅极少数SAE特征表现出一致的一维可复用导向；value-like特征多呈现结构化低维效应，pointer-like特征超80%呈现弥散效应；可解释、因果相关的特征未必能提供稳定的steering方向。
