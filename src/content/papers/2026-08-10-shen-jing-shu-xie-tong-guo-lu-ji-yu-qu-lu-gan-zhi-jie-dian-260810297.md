---
title: 'Neural Tree Collaborative Filtering: Rethinking Graph Collaborative Filtering
  as Tree Collaborative Filtering with Curvature-Aware Propagation Depth'
title_zh: 神经树协同过滤：基于曲率感知节点自适应传播深度的图CF方法
authors:
- Jinfeng Xu
- Zheyu Chen
- Ziyue Peng
- Shuo Yang
- Jinze Li
- Wenhao Yuan
- Jian Chen
- Edith C. H. Ngai
affiliations:
- 香港大学
- 北京理工大学
- 香港科技大学
arxiv_id: '2608.10297'
url: https://arxiv.org/abs/2608.10297
pdf_url: https://arxiv.org/pdf/2608.10297
published: '2026-08-10'
collected: '2026-08-12'
category: RecSys
direction: 图协同过滤 · 节点自适应消息传播
tags:
- Collaborative Filtering
- GNN
- Over-smoothing
- Graph Curvature
- Message Passing
one_liner: 基于局部度不平衡曲率实现节点自适应传播深度，同时缓解GCF过平滑与hub节点信息不足问题
practical_value: '- 可直接复用局部度不平衡曲率得分公式，O(|E|)预计算成本极低，无需复杂曲率求解，适合工业级大规模交互图快速计算每个节点的最优传播深度，缓解长尾用户/物品的过平滑问题

  - NTCF可作为LightGCN/NGCF等现有GCF backbone的直接替换，几乎不增加训练成本，还可兼容现有自监督推荐框架，替换后可稳定提升1~3个百分点的Recall/NDCG，无额外落地负担

  - 长尾商品（对应正曲率节点）可设置更浅的传播深度避免过平滑，头部爆品（对应负曲率节点）可加深传播深度捕获更多跨群体关联信号，可直接复用到电商推荐的召回层优化'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有图协同过滤（GCF）普遍采用全局统一的传播层数，完全忽略用户/物品交互图的异构性：长尾用户/物品这类边缘节点仅需1~2层传播就会出现过平滑，而头部用户/爆品这类hub节点2~3层传播仍无法捕获足够的跨邻域协同信号，导致两类节点的表征质量同时受损，已成为GCF性能提升的核心瓶颈。

### 方法关键点
- 将GCF的消息传播等价为每个节点作为根的广度优先遍历树，每个节点的传播深度不再是全局超参，而是由节点专属曲率决定
- 设计O(|E|)可计算的局部度不平衡曲率得分：节点度小于邻域平均度时为正曲率（边缘节点），减1层传播避免过平滑；节点度大于邻域平均度时为负曲率（hub节点），加1层传播捕获更多远邻信号；曲率接近0时保持全局基础层数
- 实现时通过节点掩码控制传播深度，仅在超过节点深度预算时重置为初始embedding，不破坏图的双向传播结构，兼容现有GCF的所有训练逻辑

### 关键实验
在Kindle、Pinterest、Yelp三个公开推荐数据集上对比NGCF、LightGCN、UltraGCN等6个主流GCF backbone，Recall@10最高提升7.2%、NDCG@10最高提升5.4%；替换SimGCL、LightGCL等4个自监督推荐模型的LightGCN backbone后，所有指标均稳定上涨1~2个百分点。

### 最值得记住的结论
GCF的传播深度本质是节点级属性而非全局超参，基于局部图结构的自适应深度调整是无额外负担提升GCF性能的通用方案。
