---
title: 'P3Rec: Distilling Prior--Posterior Preference Reasoning for LLM-based Recommendation'
title_zh: P3Rec：蒸馏先验后验偏好推理的LLM增强推荐框架
authors:
- Jinfei Chen
- Weihai Lu
- Jiawei Cheng
affiliations:
- Chongqing University of Technology
- Peking University
- Chongqing University
arxiv_id: '2609.13993'
url: https://arxiv.org/abs/2609.13993
pdf_url: https://arxiv.org/pdf/2609.13993
published: '2026-09-12'
collected: '2026-09-16'
category: GenRec
direction: 生成式推荐 · 偏好知识蒸馏
tags:
- Sequential Recommendation
- Knowledge Distillation
- LLM4Rec
- Preference Reasoning
- Contrastive Learning
one_liner: 联合蒸馏LLM输出的先验后验偏好知识到轻量推荐模型，兼顾效果与推理效率
practical_value: '- 可复用先验+后验偏好蒸馏范式：离线用LLM分别生成用户全局通用偏好（无目标item）、当前决策相关细粒度偏好（带目标item），蒸馏到轻量行为编码器，无需线上调用LLM，兼顾效果与latency，适合电商顺序推荐/猜你喜欢场景

  - 兴趣熵自适应校准trick：通过用户历史交互的语义相似度聚类计算兴趣熵，对偏好分散的用户的表征做自适应残差校正，可直接迁移到多兴趣推荐、冷启动用户推荐场景，解决多兴趣聚合的检索方向模糊问题

  - 跨域迁移优化思路：先验后验联合蒸馏的偏好表征具备更强的跨域迁移性，可直接用于低资源小类目推荐的冷启动，无需大量域内交互数据即可获得不错的效果'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM-as-Enhancer范式的推荐方法大多仅从单一视角蒸馏偏好知识：仅用无目标的先验偏好（用户稳定长期兴趣）对当前即时决策指导有限，仅用带目标的后验偏好（当前决策相关细粒度兴趣）易过度依赖目标线索、泛化性差，无法完整迁移LLM的偏好推理能力到轻量模型，同时难以平衡推荐效果与线上推理 latency，不适合高并发电商场景。

### 方法关键点
- 多视角偏好推理：离线调用LLM生成三类偏好知识：用户侧无目标的先验偏好（基于历史交互总结通用兴趣）、带ground truth目标item的后验偏好（提取当前决策相关细粒度兴趣）、item侧偏好表征（基于item属性和前置交互总结偏好该item的用户特征）
- 先验后验偏好内化：用可学习门控机制自适应融合用户行为表征与先验偏好表征，再以后验偏好为监督做MSE蒸馏，同时用后验偏好与行为、先验表征的相似度指导门控系数学习，兼顾行为模式、通用兴趣与当前决策需求
- 偏好检索适配：基于用户历史交互的语义相似度聚类计算兴趣熵，对兴趣分散的用户的融合表征做自适应残差校准，再用InfoNCE损失做对比检索优化，解决多兴趣聚合的检索方向模糊问题

### 关键实验
在Amazon三个公开数据集（Sports、Beauty、Toys）上对比14个SOTA基线（含传统序列推荐、LLM直接增强、LLM蒸馏三类），相比最优蒸馏基线R2END，H@10最高提升13.77%，平均提升8%~12%，跨域迁移时H@10最高提升15.85%，仅增加边际训练开销，线上推理延迟与基线持平。

### 核心结论
LLM偏好蒸馏不能只取单一视角的知识，先验通用偏好与后验决策相关偏好互补，结合兴趣熵适配可以在不增加线上推理成本的前提下同时提升推荐效果与泛化性。
