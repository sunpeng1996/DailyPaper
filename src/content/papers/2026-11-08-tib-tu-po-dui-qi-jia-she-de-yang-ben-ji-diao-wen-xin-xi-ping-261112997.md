---
title: 'TIB: Sample-wise Tempered Information Bottleneck for Multimodal Attribution
  beyond Alignment Assumption'
title_zh: TIB：突破对齐假设的样本级调温信息瓶颈多模态归因框架
authors:
- Qiming Huang
- Peixi Liu
- Jianbo Jiao
affiliations:
- The MIx group, School of Computer Science, University of Birmingham
arxiv_id: '2611.12997'
url: https://arxiv.org/abs/2611.12997
pdf_url: https://arxiv.org/pdf/2611.12997
published: '2026-11-08'
collected: '2026-11-12'
category: Multimodal
direction: 多模态可解释性 · 信息瓶颈优化
tags:
- Multimodal Attributions
- Information Bottleneck
- Vision-Language
- Model Interpretability
- Alignment-free
one_liner: 提出样本级自适应调温信息瓶颈框架，解决多模态归因依赖语义对齐假设的共性缺陷
practical_value: '- 多模态召回/检索场景下，可复用TIB的样本级跨模态可信度评估逻辑，过滤图文不对齐的低质训练样本，提升模型鲁棒性

  - 现有IB-based用户建模/特征压缩方案，可叠加自适应调温机制，避免全局约束导致的有效信息损失

  - 多模态归因能力可直接复用在电商商品图文匹配质检、广告素材归因分析场景，降低人工审核成本'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有多模态归因方法默认图文对语义完全对齐，依赖配对模态作为代理监督，真实场景中普遍存在的跨模态语义错位、对应关系不可靠问题，会导致IB类归因方法出现后验过度收缩、强制解释的结构缺陷，无法输出可靠归因结果。
### 方法关键点
- 提出样本级调温信息瓶颈TIB框架，无需假设跨模态语义对齐，根据单样本的跨模态可信度自适应调整归因强度
- 从理论层面证明了原有IB目标在对齐失效场景下的结构局限性
### 关键结果
在受控基准数据集与大规模公开数据集上验证了原有IB类方法的失效模式真实性，TIB的归因效果显著优于各类基线方案。
