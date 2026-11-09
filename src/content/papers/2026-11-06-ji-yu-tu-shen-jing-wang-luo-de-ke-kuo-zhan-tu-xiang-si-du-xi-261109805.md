---
title: Scaling Graph Similarity Learning with Graph Neural Networks
title_zh: 基于图神经网络的可扩展图相似度学习框架
authors:
- Ahmet Tüzen
- Helge Langseth
- Kjetil Nørvåg
affiliations:
- Department of Computer Science, Norwegian University of Science and Technology
arxiv_id: '2611.09805'
url: https://arxiv.org/abs/2611.09805
pdf_url: https://arxiv.org/pdf/2611.09805
published: '2026-11-06'
collected: '2026-11-09'
category: Other
direction: 大规模图相似度学习 · GNN优化
tags:
- GNN
- Graph Similarity Learning
- Scalability
- Graph Edit Distance
- Large Graph
one_liner: 提出可扩展GNN框架FiLSim，支持15万节点级大图的秒级高精度相似度计算
practical_value: '- 可复用FiLSim的轻量化GNN pipeline，优化电商用户行为图、商品关联图的相似度计算，解决大图计算OOM问题

  - 可借鉴顺序图编辑的自动打标策略，快速生成带真实相似度标签的业务图数据集，大幅降低标注成本

  - 单GPU秒级大图推理的优化思路可迁移到用户兴趣匹配、相似商品召回的在线服务场景'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
图相似度计算（GED、MCS）是图挖掘核心任务，精确求解为NP-hard问题；现有GNN方案仅适配小规模图，10万节点以上大图场景无成熟可落地方案，也缺乏配套标注评测数据集。

### 方法关键点
提出FiLSim可扩展GNN框架，采用轻量化简化GNN pipeline平衡精度与算力开销；设计顺序图编辑策略，自动生成带可靠GED标签的大规模图数据集，解决大图标注成本高的问题。

### 关键结果
在4个标准基准数据集+4个新构建的大规模数据集上验证，FiLSim可稳定处理15万+节点的大图，同类基线方法均出现OOM或训练失败；单GPU上所有测试对相似度打分仅需数秒，精度与小图场景SOTA持平。
