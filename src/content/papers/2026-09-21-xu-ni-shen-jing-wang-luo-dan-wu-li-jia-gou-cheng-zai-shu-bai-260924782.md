---
title: 'Virtual neural networks: hundreds of souls in a body'
title_zh: 虚拟神经网络：单物理架构承载数百虚拟模型的新框架
authors:
- Petr Hurtik
- Marek Vajgl
- Zahra Alijani
- Vojtech Molek
affiliations:
- University of Ostrava
- Centre of Excellence IT4Innovations
- Institute for Research and Applications of Fuzzy Modeling
arxiv_id: '2609.24782'
url: https://arxiv.org/abs/2609.24782
pdf_url: https://arxiv.org/pdf/2609.24782
published: '2026-09-21'
collected: '2026-09-22'
category: Training
direction: 深度学习集成 · 低参数量扩容训练
tags:
- deep-ensemble
- siamese-network
- parameter-efficient
- model-robustness
- CNN
one_liner: 提出参数量固定仅靠计算资源扩容的虚拟神经网络框架，效果优于SWA、Masksembles等集成方案
practical_value: '- 推荐/广告排序场景可复用该框架：在不增加模型参数量与部署存储成本的前提下，生成多个虚拟模型做预测融合，可提升排序AUC与异常样本鲁棒性

  - 冷启动场景可借鉴核心思路：用少量物理模型生成多虚拟模型做预测融合，降低小样本下的预测方差，提升用户/物品冷启动阶段的召回、排序准确率

  - 算法竞赛可直接复用开源代码：该框架效果优于SWA、Masksembles等常用集成提分方案，可作为竞赛榜单冲分的低成本trick'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有深度集成方案需存储多份独立模型参数，部署与存储成本随集成规模线性上涨，难以低成本落地大规模集成方案。
### 方法关键点
1. 融合孪生网络与深度集成思路，基于少量物理模型的共享权重生成上百个虚拟模型，总训练参数量全程保持恒定，仅靠计算资源即可实现集成规模扩容
2. 所有虚拟模型共享输入，互联结构引入的内部失真可显著提升整个集成的鲁棒性，无需额外引入正则模块
3. 框架可基于任意标准CNN实现，无架构侵入性，改造成本低
### 关键结果
1. 效果优于更大容量的单模型、普通深度集成、SWA、Masksembles等现有主流集成方案
2. 集成中最优的单个虚拟模型表现也超过同等甚至更高参数量的单独训练模型
3. 集成准确率随虚拟模型数量上升持续提升，无需调整参数量
