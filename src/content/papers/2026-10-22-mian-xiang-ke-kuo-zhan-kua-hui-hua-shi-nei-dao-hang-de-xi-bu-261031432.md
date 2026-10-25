---
title: A Sparse Topometric Graph for Scalable Cross-Session Indoor Navigation
title_zh: 面向可扩展跨会话室内导航的稀疏拓扑度量图
authors:
- Eun Sun Lee
- Minkyun Seo
- Gwangtak Bae
- Junho Kim
- Seunggu Kang
- Jaesik Park
- Young Min Kim
affiliations:
- Seoul National University
arxiv_id: '2610.31432'
url: https://arxiv.org/abs/2610.31432
pdf_url: https://arxiv.org/pdf/2610.31432
published: '2026-10-22'
collected: '2026-10-25'
category: Agent
direction: 具身Agent · 室内跨会话导航结构表示
tags:
- Embodied Agent
- Indoor Navigation
- Graph Representation
- Cross-Session Matching
- Topometric Graph
one_liner: 提出融合几何特征与邻域连通性的稀疏拓扑度量图，实现低内存高鲁棒跨会话室内导航
practical_value: '- 线下门店AR导购、仓储巡检机器人等场景的跨会话路径规划，可复用「节点局部特征+邻域连通性」全局匹配思路，降低局部特征歧义带来的匹配错误

  - 大规模室内场景地图存储可借鉴稀疏拓扑度量图设计，相比点级表征降2个数量级内存，大幅提升端侧部署可行性

  - 跨模态/异源数据的场景匹配任务，可复用子图结构匹配方法，无需依赖细粒度特征对齐，降低场景变化、传感器差异的负面影响'
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
传统具身Agent室内导航依赖细粒度测量数据累计建图，计算开销大、内存占用高，易受场景变化、传感器差异、局部特征重复/辨识度低等问题影响，跨会话导航鲁棒性不足。
### 方法关键点
1. 设计稀疏拓扑度量图作为高效结构表征，节点编码局部3D几何特征，距离加权边记录可通行连通性，规避高成本的细粒度特征匹配；
2. 训练图匹配网络，同时融合节点级几何描述符与邻域连通性信息，跨会话匹配一致子图结构，基于全局上下文匹配抵御局部特征歧义。
### 关键结果数字
跨会话点目标导航任务中，Gibson数据集成功率达77.1%，3D-FRONT场景变化下成功率达40.0%，内存占用相比点级表征降低两个数量级以上。
