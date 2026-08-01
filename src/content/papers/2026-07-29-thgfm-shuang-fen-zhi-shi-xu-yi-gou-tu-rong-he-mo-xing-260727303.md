---
title: 'THGFM: Dual-Branch Temporal Heterogeneous Graph Fusion Model'
title_zh: THGFM：双分支时序异构图融合模型
authors:
- Yixin Peng
- Diego Collarana
- Er Jin
- Stefan Decker
affiliations:
- RWTH Aachen University
- Fraunhofer FIT
arxiv_id: '2607.27303'
url: https://arxiv.org/abs/2607.27303
pdf_url: https://arxiv.org/pdf/2607.27303
published: '2026-07-29'
collected: '2026-08-01'
category: Other
direction: 时序异构图表示学习 · 图Transformer
tags:
- Temporal Heterogeneous Graph
- Graph Transformer
- Temporal Attention
- Representation Learning
- Graph Foundation Model
one_liner: 提出双分支时序异构图融合模型THGFM，结合共享/分类型注意力与旋转时间嵌入实现多基准性能领先
practical_value: '- 多行为推荐的跨类型交互建模可复用双分支架构：用共享注意力分支实现参数高效跨域迁移，分类型分支保留点击/收藏/加购等不同关系的专属特性

  - 时序建模可借鉴Rotary Temporal Attention设计：将相对时间直接融入attention计算，替代传统时间特征拼接，提升用户行为序列、交互时序建模效果

  - 多分支融合可采用Type-Conditioned Non-Competitive Gated Sum：避免分支间零和竞争，根据节点/关系类型动态调整各分支权重，适配多语义异构图召回场景'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
时序异构图是动态关系系统的天然抽象，现有方法难以同时兼顾参数高效的跨类型迁移与关系感知专属建模，且时间信息仅作为额外特征拼接在注意力核外，未融入核心计算。
### 方法关键点
1. 双支路架构：共享空间时序注意力分支实现跨类型参数高效迁移，关系类型分区时序注意力分支实现关系感知专属建模
2. 类型条件非竞争门控求和融合：为两个分支分配独立的类型条件特征级门控，避免分支间零和竞争
3. 旋转时序注意力：匹配前按相对时间半相位旋转query和key，将时间直接纳入注意力得分计算
### 关键结果
6个任务平均指标较基线图Transformer提升3.25%，OAG-CS PV任务峰值提升12.37%，OGBN-MAG、HTAG-ArXiv、HTAG-DBLP分别提升4.24%、3.73%、4.61%
