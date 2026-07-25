---
title: Reading and Steering Representations of Materials-Science Mechanisms in an
  Open-Weight Language Model
title_zh: 开源大模型中材料科学机制表征的读取与调控
authors:
- Markus J. Buehler
affiliations:
- Massachusetts Institute of Technology
arxiv_id: '2607.20058'
url: https://arxiv.org/abs/2607.20058
pdf_url: https://arxiv.org/pdf/2607.20058
published: '2026-07-21'
collected: '2026-07-25'
category: LLM
direction: 大模型可解释性 · 内部表征干预
tags:
- Mechanistic Interpretability
- LLM Internal Representation
- Causal Intervention
- Jacobian Lens
- Open LLM
one_liner: 验证开源Gemma模型中材料科学知识的三类可分离表征，证明状态变化比静态状态表征效果更优
practical_value: '- Jacobian lens+静态隐状态联合读取的方法，可迁移用于LLM4Rec的决策逻辑归因，定位和推荐偏好、业务规则相关的隐空间维度

  - 对比输入扰动前后的隐状态变换而非仅分析静态隐状态的思路，可用于验证LLM在推荐/广告场景下对约束规则的实际学习效果，避免过拟合表层语义

  - 因果干预+反事实状态补丁的实验范式，可复用为LLM4Rec的鲁棒性测试工具，快速定位bad case对应的内部表征缺陷'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
大模型输出正确结果无法证明其真正掌握领域底层规则，科学知识在大模型内部的表征形式缺乏可落地的量化验证手段

### 方法关键点
针对gemma-4-E4B-it开源模型，结合直接词汇读取、Jacobian lens、隐状态几何分析、60条规则反事实基准、因果干预多种工具，拆分材料科学机制的三类可分离表征形式，对比静态隐状态、输入调整后状态变换的表征有效性

### 关键结果
- 50份留出材料描述测试中，3个独立训练的Jacobian lens可复现概念排序，两种读取方式的无目标词集实现9/10机制家族的盲识别
- 60组固定物理关系测试中，状态变换可正确区分正向/中性/逆向规则，定向规则识别准确率达39/40，远高于词汇对照组的随机水平
- 12组对比测试中双向隐状态干预可100%调控输出向物理正确/错误方向偏移，反事实状态补丁可跨机制迁移决策信号
