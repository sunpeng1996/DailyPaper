---
title: 'Linking Rapid Learning to Compositional Structure in Neural Networks: Evidence
  from Additive Analogies in Meta-Learned Parameter Spaces'
title_zh: 元学习参数空间加性类比揭示神经网络快速学习的组合结构
authors:
- Abigail L. Tenenbaum
- R. Thomas McCoy
affiliations:
- Department of Linguistics, Yale University
- Wu Tsai Institute, Yale University
arxiv_id: '2611.17314'
url: https://arxiv.org/abs/2611.17314
pdf_url: https://arxiv.org/pdf/2611.17314
published: '2026-11-12'
collected: '2026-11-15'
category: Training
direction: 元学习 · 神经网络参数空间机制研究
tags:
- Meta-Learning
- Parameter Space
- Compositional Structure
- Few-Shot Learning
- Inductive Bias
one_liner: 发现元学习参数向量存在类似词向量的加性类比关系，可零样本构造实现目标功能的神经网络
practical_value: '- 电商推荐冷启动场景可借鉴参数加性组合思路，直接组合已有任务的适配参数向量，零样本生成适配新类目/新活动的推荐模型，大幅降低小样本场景的训练成本

  - 电商多技能Agent可对不同技能对应的LoRA参数向量做加性组合，无需额外微调即可得到同时适配多场景（如导购+售后）的复合技能参数

  - 可基于参数向量的加性关系构建推荐模型的可解释性框架，通过参数运算溯源模型适配新任务的逻辑，降低黑盒模型的决策风险'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
人类可基于有限经验快速学习，但神经网络通常需要大量训练数据才能收敛，元学习网络虽已被证实可实现快速小样本学习，但其背后的内部作用机制尚未明确。
### 方法关键点
参考词向量的加性类比特性（如`king - man + woman ≈ queen`），将元学习网络适配不同任务时的微调参数拼接为单一向量作为对应任务的功能表征，验证不同功能的参数向量是否存在符合符号逻辑的加性关系。
### 关键结果
1. 元学习参数向量的加性组合可零样本生成实现目标功能的网络，无需额外训练；
2. 该特性在不同网络架构和功能域均存在，鲁棒性显著优于随机初始化或普通预训练网络；
3. 元学习可将参数空间组织为具备功能语义的几何结构，为神经网络引入归纳偏置提供了新的几何路径。
