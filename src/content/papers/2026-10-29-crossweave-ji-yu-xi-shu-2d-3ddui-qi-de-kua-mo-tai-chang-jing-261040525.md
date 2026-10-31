---
title: 'CrossWeave: Cross-Modal Scene and Instance Retrieval from Sparse 2D-3D Alignment'
title_zh: CrossWeave：基于稀疏2D-3D对齐的跨模态场景与实例检索
authors:
- Aadith Warrier
- Gnana Prakash Punnavajhala
- Siddharth Tourani
- Muhammad Haris Khan
- Avinash Sharma
- Madhava Krishna
affiliations:
- IIIT Hyderabad
- University of Heidelberg
- MBZUAI
- IIT Bombay
arxiv_id: '2610.40525'
url: https://arxiv.org/abs/2610.40525
pdf_url: https://arxiv.org/pdf/2610.40525
published: '2026-10-29'
collected: '2026-10-31'
category: Other
direction: 跨模态检索 · 2D-3D多粒度对齐
tags:
- Cross-Modal Retrieval
- 2D-3D Alignment
- Optimal Transport
- Sparse Supervision
- Feature Aggregation
one_liner: 提出仅靠稀疏2D-3D对应监督的单模型CrossWeave，实现跨模态场景与实例检索SOTA
practical_value: '- 稀疏局部对应监督代替全局对比学习的训练思路，可迁移到多模态商品检索（如2D实拍图搜3D商品模型）场景，降低全局标注成本

  - 基于最优传输的特征聚合去冗余方法，可复用在各类多模态检索任务的特征编码阶段，提升特征区分度

  - 单模型支持多粒度检索的架构设计，可参考用于实现电商统一的跨粒度（品类/单品）多模态检索能力'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有2D到3D跨模态场景/实例检索仅做全局层级对齐，缺乏细粒度局部结构监督，且两类任务需独立训练模型，部署成本高。
### 方法关键点
1. 仅用稀疏2D-3D对应关系做监督，无需全局场景/实例级对比损失，即可训练统一的多任务检索模型
2. CrossWeave先学习稀疏patch-point特征对齐，再通过最优传输聚合器聚类冗余结构区域，释放特征容量给语义独特的局部特征
### 关键结果
在ScanNet、3RScan数据集上单模型同时实现场景级、实例级跨模态检索SOTA，无需为两个任务单独建模，验证了全局编码非跨模态检索必需，稀疏局部监督效率更优。
