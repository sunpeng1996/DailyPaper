---
title: 'FUSE: Feature-Wise Unified Specialization with Cross-Column Exchange for Mixed-Type
  Tabular Flow Matching'
title_zh: FUSE：面向混合类型表格流匹配的特征级统一专业化与跨列交换方法
authors:
- Suman Cha
- Seongchan Lee
- Dohyun Ko
- Hyunjoong Kim
affiliations:
- Yonsei University
- KAIST
arxiv_id: '2608.07294'
url: https://arxiv.org/abs/2608.07294
pdf_url: https://arxiv.org/pdf/2608.07294
published: '2026-08-07'
collected: '2026-08-10'
category: Other
direction: 混合类型表格生成 · 流匹配优化
tags:
- Tabular Generation
- Flow Matching
- Synthetic Data
- Categorical Feature
- Numerical Feature
one_liner: 针对混合类型表格生成任务，提出显式分离特征专属处理与跨列交互的FUSE流匹配框架
practical_value: '- 处理电商混合类型用户/商品属性表格数据时，可借鉴数值/分类特征分治的自适应混合模块设计，提升特征表征质量

  - 做表格数据增广时可引入跨列联合注意力机制，保留特征间业务依赖，避免生成的合成样本违背现实逻辑

  - 用户/商品冷启动缺训练样本场景下，可复用FUSE的流匹配逻辑生成高保真合成数据，降低数据收集成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
混合类型表格生成需同时建模异质特征分布与复杂跨列依赖，现有变分流匹配方法将特征专属处理、跨列交互隐式封装在共享骨干网络中，特征适配性差、依赖捕捉能力不足，且缺乏受限条件下的风险量化机制。
### 方法关键点
1. 对数值、分类特征分别设置独立自适应混合模块，支持每个特征组合共享的专属子网络；
2. 引入联合注意力机制保障所有列间的信息交互，精准捕捉跨列依赖；
3. 理论上刻画受限条件上下文带来的超额群体风险，给出连续Wasserstein生成误差的端点预测风险上界。
### 关键结果
在8个公开表格数据集上实验，FUSE在分布保真度、下游任务效用两类指标上均取得稳定领先的性能。
