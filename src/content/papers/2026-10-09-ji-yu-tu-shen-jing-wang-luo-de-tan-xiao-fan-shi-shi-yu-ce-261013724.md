---
title: Amortized Counterfactual Prediction with Graph Neural Networks
title_zh: 基于图神经网络的摊销反事实预测
authors:
- Hendrik Stumpf
- Francesco Quinzan
affiliations:
- Department of Computer Science, University of Oxford
- Department of Engineering, University of Oxford
arxiv_id: '2610.13724'
url: https://arxiv.org/abs/2610.13724
pdf_url: https://arxiv.org/pdf/2610.13724
published: '2026-10-09'
collected: '2026-10-13'
category: Reasoning
direction: 因果反事实推理 · GNN端到端预测
tags:
- Counterfactual Inference
- GNN
- Causal Reasoning
- Amortized Inference
- Graph Learning
one_liner: 提出无需预估计因果图的端到端CFGNP模型，实现更优反事实预测效果及跨图规模泛化能力
practical_value: '- 推荐/广告场景的反事实预估（如不同营销动作对用户转化的影响）可直接复用CFGNP架构，省去因果图预估计步骤，降低误差传播

  - 跨规模图泛化特性可复用在不同流量规模的商家/用户行为图预估场景，无需每个量级单独训练模型

  - 双图跨世界消息传递的约束思路可迁移到多场景对比建模（如A/B测试效果预估、用户不同路径转化预测）'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有反事实预测需先从观测数据估计因果图再做推理，估计误差会向下游传播，且实际业务场景中因果结构通常难以准确获取。

### 方法关键点
提出端到端反事实预测框架CFGNP，无需预估计因果图，直接基于观测数据输出结果；采用GNN建模双图结构，限制跨世界消息传递仅在对应的事实-反事实变量之间进行，避免信息混杂。

### 关键结果
- 德国贷款基准数据集上MSE从4.51×10^-2降至0.19×10^-2，大幅优于现有方法
- 仅用10节点合成因果图训练的模型，无需重训练即可在最多30节点的图上保持优异预测性能
