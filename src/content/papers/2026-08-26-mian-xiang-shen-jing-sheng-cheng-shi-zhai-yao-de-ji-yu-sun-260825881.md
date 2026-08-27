---
title: Loss-Based Active Learning for Neural Abstractive Summarization
title_zh: 面向神经生成式摘要的基于损失的主动学习框架
authors:
- Michail Ioannou
- Tatiana Passali
- George Michalopoulos
- Grigorios Tsoumakas
affiliations:
- Aristotle University of Thessaloniki
- Microsoft
arxiv_id: '2608.25881'
url: https://arxiv.org/abs/2608.25881
pdf_url: https://arxiv.org/pdf/2608.25881
published: '2026-08-26'
collected: '2026-08-27'
category: Training
direction: 生成式摘要 · 主动学习训练优化
tags:
- Active Learning
- Abstractive Summarization
- LLM Fine-tuning
- Data Efficiency
one_liner: 提出针对生成式摘要的LOBSTER主动学习框架，降标注成本同时实现样本选择最高665倍加速
practical_value: '- 电商场景下做商品详情摘要、用户评价聚合摘要、营销文案生成等LLM微调任务时，可复用LOBSTER的高损失样本优先标注逻辑，大幅降低人工标注成本，提升微调效率

  - 主动学习的样本选择环节可参考其「匹配高损失样本语义相似未标注数据」的思路，替代传统复杂的信息度打分策略，在保证效果的同时大幅提升样本筛选速度，适配大规模无标注数据场景

  - 所有生成类任务的标注成本优化都可直接复用该框架的流程，无需重新设计主动学习的样本选择逻辑'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
生成式摘要微调依赖高质量人工标注数据，标注过程需要通读长文本，成本高、周期长；现有面向摘要任务的主动学习方法普遍存在稳定性差、计算瓶颈高的问题，落地难度大。
### 方法关键点
提出LOBSTER主动学习框架，核心逻辑为：迭代过程中优先筛选与当前模型训练集内高损失样本语义相似的未标注实例进行标注，针对性补全模型能力短板，无需复杂的样本信息度预打分。
### 关键结果
在3个公开基准数据集、2个主流摘要骨干模型上验证，效果持平或超过现有SOTA主动学习方法，同时样本选择速度最高提升665x。
