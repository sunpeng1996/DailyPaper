---
title: 'Multistage Defer Trees for Hybrid Interpretability: If at First You Can''t
  Succeed, Tree Again'
title_zh: 面向混合可解释性的多阶段延迟决策树方法
authors:
- Zakk Heile
- Hayden McTavish
- Margo Seltzer
- Cynthia Rudin
affiliations:
- Duke University
- University of British Columbia
arxiv_id: '2606.30995'
url: https://arxiv.org/abs/2606.30995
pdf_url: https://arxiv.org/pdf/2606.30995
published: '2026-06-30'
collected: '2026-07-01'
category: Training
direction: 可解释模型 · 决策树训练优化
tags:
- Decision Tree
- Interpretability
- Ensemble Learning
- Hybrid Model
- Inference Efficiency
one_liner: 提出序列稀疏决策树级联结构，多数样本走可解释树、难样本递交给后续树或黑盒，平衡精度与可解释性
practical_value: '- 推荐/广告排序场景可复用级联推理框架：大部分简单样本走LR/浅层树等可解释白盒，难样本才调用复杂DNN/LLM，在不损失精度的前提下提升推理速度、降低算力成本，同时满足监管要求的可解释性

  - 可直接复用样本路由机制：基于单棵模型的预测置信度设置defer阈值，阈值可根据业务对精度/可解释占比的要求动态调优，适配不同业务场景

  - 排序链路特征排查/用户申诉场景，可先用该方法筛选出大部分样本的决策规则，快速定位特征异常、用户申诉的决策原因，降低运营成本'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
单棵最优决策树仅在噪声域能匹配黑盒模型精度，其余场景下集成树/复杂黑盒精度更高但完全丧失可解释性，业界亟需平衡精度与可解释性的混合建模方案。

### 方法关键点
1. 构建多阶段稀疏决策树序列，每棵树对置信度达标的样本直接输出预测结果，置信度不足的样本defer给下一棵树，最终难样本递交给黑盒模型处理
2. 配套轻量化训练策略保证每棵树的稀疏性与路由逻辑合理性，无额外过重训练开销

### 关键结果
可完全匹配复杂树集成模型的精度，同时80%+的样本仅需经过1~2棵稀疏决策树即可得到预测结果，大幅提升可解释样本的覆盖占比
