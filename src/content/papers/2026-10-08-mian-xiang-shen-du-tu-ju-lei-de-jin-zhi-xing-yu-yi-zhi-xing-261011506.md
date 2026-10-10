---
title: 'Compactness and Consistency: A Conjoint Framework for Deep Graph Clustering'
title_zh: 面向深度图聚类的紧致性与一致性联合框架CoCo
authors:
- Wei Ju
- Siyu Yi
- Kangjie Zheng
- Yifan Wang
- Ziyue Qiao
- Li Shen
- Yongdao Zhou
- Xiaochun Cao
- Jiancheng Lv
affiliations:
- Sichuan University
- Wellcome Sanger Institute
- University of International Business and Economics
- Great Bay University
- Sun Yat-sen University
arxiv_id: '2610.11506'
url: https://arxiv.org/abs/2610.11506
pdf_url: https://arxiv.org/pdf/2610.11506
published: '2026-10-08'
collected: '2026-10-10'
category: Other
direction: 深度图聚类 · 图节点表征优化
tags:
- Graph Clustering
- GNN
- Node Embedding
- Low-rank Embedding
- Consistency Learning
one_liner: 提出兼顾节点表征紧致性与一致性的深度图聚类框架CoCo，多数据集性能超SOTA
practical_value: '- 用户-物品异构图、用户社交图等业务图场景可复用低秩紧致嵌入方法，过滤表征冗余噪声，提升下游召回、聚类任务效果

  - 多视图表征学习场景可借鉴一致性学习策略，实现局部拓扑与全局结构信息的知识迁移，增强表征鲁棒性

  - 用户分层、商品归类、兴趣社群挖掘等业务可直接复用CoCo开源代码，降低图聚类落地成本'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有基于GNN的图聚类方法依赖局部消息传递机制，难以捕获节点间全局关联，且图数据自带的冗余、噪声易导致节点表征紧致性、鲁棒性不足，无法适配复杂图结构的聚类需求。
### 方法关键点
1. 提出CoCo联合框架，通过图卷积滤波器同时从局部、全局双视角学习鲁棒节点表征
2. 引入低秩编码层将原始表征映射为紧致嵌入，过滤冗余噪声的同时挖掘图内在结构
3. 基于紧致嵌入设计一致性学习策略，实现双视角表征的知识迁移，丰富节点语义
### 关键结果
在多类公开图数据集上，CoCo的聚类精度、NMI等核心指标全面超越现有SOTA深度图聚类方法，代码已开源。
