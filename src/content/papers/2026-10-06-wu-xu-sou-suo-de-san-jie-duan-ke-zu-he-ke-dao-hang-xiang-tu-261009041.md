---
title: Building Navigable Graphs Without Search in Three Composable Stages
title_zh: 无需搜索的三阶段可组合可导航向量图构建方法
authors:
- Édgar Chávez
affiliations:
- CICESE, Ensenada, Mexico
arxiv_id: '2610.09041'
url: https://arxiv.org/abs/2610.09041
pdf_url: https://arxiv.org/pdf/2610.09041
published: '2026-10-06'
collected: '2026-10-08'
category: Other
direction: 向量检索 · 可导航图索引构建
tags:
- Navigable Graph
- Approximate Nearest Neighbor
- Vector Index
- Graph Construction
- Deterministic Index
one_liner: 提出三阶段可组合无搜索可导航向量图构建框架，性能超主流方案且构建速度最高提升49%
practical_value: '- 做RAG向量索引的团队可直接复用三阶段框架，替换现有PiPNN的剪枝模块，相同召回下距离计算量降低3~14%，构建时间仅增加8~16%

  - 可复用半空间近端（HSP）spine设计替换现有索引的连通性生成模块，成本仅为原有生成树的1/10~1/500，召回损失<1.1%甚至有所提升

  - 向量库规模扩大时可参考kNN图零聚类尾部占比调整每个点的分块成员数，无需盲目调参，均匀分配成员数即可接近最优效果

  - 需确定性向量索引的业务可复用论文中消除PiPNN随机性的方案，仅损失3%构建时间即可得到线程无关的一致索引'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有HNSW、Vamana等主流可导航图索引均依赖搜索式构建，存在大量依赖随机访问的距离计算，性能受内存墙限制严重，且构建过程不确定性高、不同分块策略的效果边界不清晰，难以快速适配不同规模向量库的索引需求。

### 方法关键点
- 拆分为三个完全独立可组合的阶段：1）Pool：将向量划分为重叠块，块内全量计算两两距离生成候选集，支持任意分块器接入；2）Ending：每个点保留最近C个候选，用带松弛因子的遮挡规则剪枝到R条出边，添加反向边后仅对溢出列表重剪；3）Spine：剪枝后添加豁免剪枝的连通边保证全图可达，论文实现的半空间近端（HSP）spine无需搜索即可保证到采样点的单调路由。
- 修复PiPNN的三个非确定性问题，实现了与线程数、执行顺序无关的确定性构建流程。

### 关键结果
在GloVe、SIFT、GIST、Deep（10M/100M）、Wikipedia共6个百万到亿级数据集上测试，对比Vamana、PiPNN、HNSW等基线：
- 组合方案（PiPNN分块+本文Ending+HSP spine）效果匹配或优于全量稠密构建，构建时间仅为后者的0.51~0.86倍；
- Deep-100M数据集上，相同召回下距离计算量比Vamana少11~23%，构建时间仅为全量稠密构建的60%；
- HSP spine仅需原有生成树1/10~1/500的计算量，召回最高提升5%，损失不超过1.1%。

### 核心结论
可导航图质量核心由剪枝阶段决定，只要分块池本地化程度足够，不同分块策略效果差距不超过4%，均匀分配分块成员数即可接近最优效果。
