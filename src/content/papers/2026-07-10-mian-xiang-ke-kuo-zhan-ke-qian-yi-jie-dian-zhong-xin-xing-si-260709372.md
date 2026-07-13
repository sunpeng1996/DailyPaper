---
title: Graph Neural Networks for Scalable and Transferable Node Centrality Approximation
title_zh: 面向可扩展可迁移节点中心性近似的图神经网络方法
authors:
- Samra Sana
- Giorgio Mantica
- Saul Imbrici
affiliations:
- Center for Nonlinear and Complex Systems, Università degli Studi dell’Insubria
- Data Science Institute, Hasselt University
arxiv_id: '2607.09372'
url: https://arxiv.org/abs/2607.09372
pdf_url: https://arxiv.org/pdf/2607.09372
published: '2026-07-10'
collected: '2026-07-13'
category: Other
direction: 图表示学习 · 节点中心性近似
tags:
- GNN
- Node Centrality
- Transfer Learning
- Graph Representation
- Scalable Inference
one_liner: 用混合分布训练GNN实现节点中心性快速近似，跨拓扑迁移性提升，推理提速最高97.7倍
practical_value: '- 电商用户/商品关系图的节点重要性排序（如KOL、爆品识别）可复用该GNN近似方案替换传统中心性计算，大幅降低计算延迟

  - 跨不同业务场景图拓扑做迁移训练时，可借鉴混合分布训练策略，提升GNN结构表示的跨域迁移性

  - 需大规模图实时计算的场景（如实时社交传播链路预测、广告流量分发节点优先级排序）可复用该推理加速方案，最高获近百倍提速'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统节点中心性（介数、接近度）精确计算复杂度极高，无法支撑大规模图实时计算需求，现有GNN近似方案跨不同拓扑的迁移性差。
### 方法关键点
将中心性近似转化为节点排序任务，用精确中心性值做监督，以Kendall's tau作为排序质量评估指标；采用混合分布训练策略，在Erdos renyi、Barabasi-Albert、高斯随机分区三类拓扑的图上联合训练，提升GNN结构表示的跨图族迁移性。
### 关键结果
unseen Erdos renyi图上介数tau=0.851、接近度tau=0.894；5000节点规模训练的介数模型tau达0.938，推理速度较精确计算最高提升97.7倍；混合训练显著提升介数跨图族迁移性，接近度中心性对社区结构拓扑仍敏感，向真实拓扑的迁移效果较差。
