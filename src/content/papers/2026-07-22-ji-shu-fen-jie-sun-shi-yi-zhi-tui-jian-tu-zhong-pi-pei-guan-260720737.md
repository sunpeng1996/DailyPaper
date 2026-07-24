---
title: 'Cardinality-Decomposed Loss: Matching Training Objectives to Relation Structure
  in Heterogeneous Recommendation Graphs'
title_zh: 基数分解损失：异质推荐图中匹配关系结构的训练目标
authors:
- Parul Maheshwari
- Amulya Paruchuri
- Yiqing Zou
- Alireza Sahami Shirazi
- Farhad Farahani
- Prakhar Mehrotra
affiliations:
- PayPal AI
- PayPal Inc.
arxiv_id: '2607.20737'
url: https://arxiv.org/abs/2607.20737
pdf_url: https://arxiv.org/pdf/2607.20737
published: '2026-07-22'
collected: '2026-07-24'
category: RecSys
direction: 异构图推荐 · 多任务损失优化
tags:
- Heterogeneous Graph
- BPR
- Multi-Task Learning
- GNN4Rec
- Embedding
one_liner: 针对异质推荐图不同基数关系拆分损失，解决属性嵌入静默坍缩问题同时优化排序效果
practical_value: '- 异构图训练时先按关系基数拆分损失：一对多的交互关系用BPR，一对一的属性分类用CE，避免统一用BPR导致的属性嵌入坍缩

  - 上线前可通过两个低成本指标预判效果：计算属性与用户交互的互信息得到语义对齐，检查属性节点是否直连用户/商品判断拓扑泄露，提前确定λ调优范围

  - 若业务需要用户/商品嵌入用于下游分群、冷启动、公平性审计，优先使用CDL，可将属性线性探针AUC提升30~42pp，避免常规指标正常但嵌入不可用的静默故障

  - 语义对齐高的场景（属性与用户偏好强相关）直接取λ=1.0作为默认值，可同时获得NDCG提升和属性嵌入质量优化'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
异质GNN是当前推荐系统的主流骨干，但工业界通常对所有关系统一使用BPR损失，而BPR仅适合一对多的用户-商品交互关系，用于一对一的属性关系（如用户性别、年龄）时会导致属性嵌入坍缩到两两余弦相似度0.93~0.98的近随机分布，且这种故障不会被NDCG等常规排序指标检测到，会污染用户/商品嵌入，严重影响下游分群、冷启动、公平审计等任务。

### 方法关键点
- 提出Cardinality-Decomposed Loss (CDL)，按关系基数匹配损失：一对多(OTM)交互关系用BPR，一对一(OTO)属性用CE，总损失为$L_{CDL}=L_{BPR}+\lambda\cdot L_{CE}$，λ是唯一新增超参
- 每个OTO关系单独对接线性分类头，缺失属性标签自动mask不参与CE计算
- 提出语义对齐、拓扑泄露两个可提前计算的低成本指标，用于预判λ调优的最优区间

### 关键实验
覆盖5个跨领域数据集：MovieLens-1M、Last.fm-360K、Yelp、BookCrossing、PayPal工业数据集（1M用户、1.78亿交互），对比仅OTM关系用BPR的CF基线、全关系统一用BPR的基线。效果：属性线性探针AUC一致提升30~42pp；语义对齐高的场景NDCG@10显著提升：Last.fm+7.8%、Yelp+2.9%、工业数据集+3.3%；语义对齐低的场景可通过λ在NDCG损失和属性嵌入质量间做可控帕累托权衡。

### 核心结论
异质推荐图训练不要统一用BPR，按关系结构匹配损失目标，花几分钟计算语义对齐和拓扑泄露就能提前预判收益，避免难以发现的嵌入静默坍缩故障。
