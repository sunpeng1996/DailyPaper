---
title: Local-Global Geometric Insights for Graph Neural Networks via Entropic Curvature
title_zh: 基于熵曲率的图神经网络局部-全局几何特性分析与优化
authors:
- Rachid Caich
- Yassine Abbahaddou
affiliations:
- Université de Montréal
- École Polytechnique, IP Paris
arxiv_id: '2607.22381'
url: https://arxiv.org/abs/2607.22381
pdf_url: https://arxiv.org/pdf/2607.22381
published: '2026-07-24'
collected: '2026-07-27'
category: Other
direction: 图神经网络 · 几何优化与性能增强
tags:
- GNN
- Entropic Curvature
- Oversmoothing
- Oversquashing
- Graph Rewiring
- Structural Encoding
one_liner: 提出全局熵曲率框架统一GNN过平滑过压缩问题，落地3种实用优化机制
practical_value: '- 电商用户/社交关系召回用GNN可直接复用E-Gate聚合器、ENT结构编码，缓解深层GNN过平滑问题，提升节点特征区分度

  - 多跳用户行为链路图可采用MCR重布线方法优化拓扑，缓解长距离信息传播的过压缩问题，提升跨行为序列建模效果

  - 熵曲率的扩张悖论结论可指导大规模用户-item关联图构造，平衡图稀疏性与长程信息传输效率'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有Ollivier-Ricci、Forman等图曲率仅做局部边级对比，无法刻画长距离信息传播规律，难以从根源统一解决GNN过平滑、过压缩核心痛点。
### 方法关键点
将Lott-Sturm-Villani框架拓展到图结构，基于Wasserstein测地线的熵位移凸性提出全局传输型熵曲率，设计可计算的弱熵曲率代理作为全局熵曲率的下界；基于该理论推导得出控制过平滑的Poincaré型不等式、传输熵泛化界，证明大图中稀疏性、强谱扩张、正熵曲率三者无法共存的扩张悖论，首次将过平滑和过压缩统一为曲率谱的两个极端。落地3种实用机制：E-Gate聚合器、ENT结构编码、中点补全重布线（MCR）。
### 关键结果
在6个节点分类、图分类基准任务上，性能优于SDRF、FoSR、Graph Ricci Flow等SOTA曲率优化方法。
