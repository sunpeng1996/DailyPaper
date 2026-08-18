---
title: 'Hide&Seek: Learning to Explain in an End-to-End Differentiable Network'
title_zh: 《Hide&Seek：面向模型解释的端到端可微分实例级特征选择框架》
authors:
- Tal Ellinson
- Hadi Mohasel Afshar
- Sally Cripps
affiliations:
- University of Technology Sydney, Australia
arxiv_id: '2608.16689'
url: https://arxiv.org/abs/2608.16689
pdf_url: https://arxiv.org/pdf/2608.16689
published: '2026-08-17'
collected: '2026-08-18'
category: Training
direction: 可解释模型 · 实例级特征选择端到端训练
tags:
- Feature Selection
- Interpretability
- End-to-End Training
- Differentiable Model
- Model Explanation
one_liner: 提出无信息泄露的端到端可微分实例级特征选择方法，训练速度快且效果优于现有SOTA
practical_value: '- 推荐/广告排序场景可复用该实例级特征选择思路，为每个用户请求动态选择输入特征，降低推理耗时同时生成可解释的排序依据，满足合规要求

  - 特征掩码操作可参考本文「比例替换而非离散移除」的可微分改造方案，避免训练阶段梯度消失/爆炸，无需强化学习即可完成特征选择器的联合训练

  - 训练稳定性优化可复用parsimony-weight退火框架，平衡特征选择稀疏性与模型预测效果，减少调参成本'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有实例级特征选择方法普遍存在信息泄露、不可微分导致训练速度慢的问题，无法满足高维特征场景下的模型解释与高效训练需求
### 方法关键点
1. 重构特征移除操作为可微分运算：不直接离散删除特征，而是按比例替换部分特征值，实现特征选择与预测任务的端到端联合优化，全程无信息泄露
2. 引入parsimony-weight退火框架，稳定训练过程，平衡特征稀疏性与预测精度
### 关键结果
在多类实验中效果超过现有SOTA模型，训练速度远快于非端到端的同类特征选择方案
