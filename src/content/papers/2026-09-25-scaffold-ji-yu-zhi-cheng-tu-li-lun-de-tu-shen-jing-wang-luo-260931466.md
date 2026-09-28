---
title: 'Scaffold: Support Graph Theory Based Sparsification for Graph Neural Networks'
title_zh: Scaffold：基于支撑图理论的图神经网络稀疏化方法
authors:
- Siddhartha Shankar Das
- Sai Karthik Navuluru
- S M Ferdous
- Ryan A. Rossi
- Baris Coskunuzer
- Lakshman Tamil
- Edoardo Serra
- Alex Pothen
- Robert Rallo
- Mahantesh M Halappanavar
affiliations:
- Pacific Northwest National Laboratory
- University of Texas at Dallas
- University of North Carolina at Charlotte
- Adobe
- Purdue University
arxiv_id: '2609.31466'
url: https://arxiv.org/abs/2609.31466
pdf_url: https://arxiv.org/pdf/2609.31466
published: '2026-09-25'
collected: '2026-09-28'
category: Training
direction: GNN训练优化 · 图稀疏化降本
tags:
- GNN
- Graph Sparsification
- Training Optimization
- Computational Efficiency
- Message Passing
one_liner: 提出联合控制扩张与拥塞的无监督GNN图稀疏化框架，降内存提速度同时基本无损性能
practical_value: '- 电商推荐场景下构建用户行为图/商品关联图GNN召回/排序模型时，可复用Scaffold的dilation-congestion联合控制规则做图稀疏化，保留核心关联路径的同时砍掉冗余边，降低GNN训练推理的内存与耗时开销

  - 大图GNN训练遇到算力瓶颈时，可直接调用开源Scaffold工具做预稀疏化，仅保留10%-50%边即可接近全图性能，无需额外标注数据，适配业务成本低

  - 构建多Agent协作拓扑时，可借鉴该框架的结构指标做拓扑剪枝，避免消息传递瓶颈同时降低多Agent通信开销'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
GNN依赖边消息传递，计算内存成本随图密度上升显著提升，传统无差别剪边会破坏核心通信结构，导致预测性能大幅下降，缺少可扩展的兼顾性能与效率的稀疏化方案。
### 方法关键点
基于支撑图理论预条件器的无监督稀疏化框架Scaffold，联合控制两个核心结构指标：dilation（剪边后重路由路径的长度增量）、congestion（重路由路径在保留边上的集中程度），既保留短通信路径，又避免出现结构瓶颈，是首个采用扩张-拥塞联合判据的可扩展GNN稀疏化框架。
### 关键结果数字
在19个同配/异配、覆盖小到大尺寸的图基准测试中综合排名第一；仅保留10%-50%原始边时，即可恢复或接近全图GNN性能，训练内存不足全图的1/2，端到端训练耗时（含稀疏化开销）明显降低
