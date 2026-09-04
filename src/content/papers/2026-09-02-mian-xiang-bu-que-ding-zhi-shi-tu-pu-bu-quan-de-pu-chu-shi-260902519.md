---
title: Spectral Initialization and Scheduled Graph Smoothness for Uncertain Knowledge
  Graph Completion
title_zh: 面向不确定知识图谱补全的谱初始化与调度图平滑方法
authors:
- Md Abrar Jahin
- Taufikur Rahman Fuad
- Jay Pujara
- Craig A. Knoblock
affiliations:
- University of Southern California
- Islamic University of Technology
arxiv_id: '2609.02519'
url: https://arxiv.org/abs/2609.02519
pdf_url: https://arxiv.org/pdf/2609.02519
published: '2026-09-02'
collected: '2026-09-04'
category: Other
direction: 不确定知识图谱补全 · 图结构正则优化
tags:
- Uncertain Knowledge Graph
- Graph Embedding
- Spectral Initialization
- Graph Regularization
- Semi-supervised Learning
one_liner: 无需新增可训练参数的QUEST方法，通过谱初始化与图正则提升UKG补全精度和训练稳定性
practical_value: '- 电商带置信度知识图谱（商品/用户/行为关联图谱）补全场景，可直接复用置信加权图拉普拉斯特征向量初始化实体嵌入，无额外参数即可提升嵌入质量

  - 训练带权图模型时可在训练早期加入无偏小批量狄利克雷能量正则，消除稠密图训练波动，提升训练稳定性

  - 半监督图类任务（如用户行为图谱召回、商品关联挖掘）可参考无额外参数的结构先验注入思路，不增加推理成本提效'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有不确定知识图谱（UKG）补全的半监督方法初始化实体嵌入时未利用置信加权图的全局社区、枢纽结构，存在训练不稳定、精度受限问题，且依赖伪标签生成导致效果波动。

### 方法关键点
提出无额外可训练参数的QUEST框架：1）用置信加权图拉普拉斯的最小非平凡特征向量初始化实体嵌入，训练前就注入全局结构先验；2）训练早期加入无偏小批量狄利克雷能量正则，保障结构一致性，无需修改原有训练 pipeline。

### 关键结果
在2个UKG数据集的8组指标-数据集配对中，6组效果超越现有SOTA，剩余2组追平SOTA，同时完全消除稠密图上的训练不稳定尖峰，大幅提升checkpoint可靠性。
