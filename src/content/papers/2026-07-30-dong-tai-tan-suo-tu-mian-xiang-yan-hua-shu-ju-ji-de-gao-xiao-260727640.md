---
title: 'Dynamic Exploration Graph: A Novel Approach for Efficient Nearest Neighbor
  Search in Evolving Multimedia Datasets'
title_zh: 动态探索图：面向演化数据集的高效近似近邻搜索新方法
authors:
- Nico Hezel
- Kai Uwe Barthel
- Bruno Schilling
- Konstantin Schall
- Klaus Jung
affiliations:
- HTW Berlin
arxiv_id: '2607.27640'
url: https://arxiv.org/abs/2607.27640
pdf_url: https://arxiv.org/pdf/2607.27640
published: '2026-07-30'
collected: '2026-07-31'
category: RecSys
direction: 向量检索·动态近邻图索引优化
tags:
- ANNS
- Dynamic Graph
- Vector Search
- Retrieval
- RecSys
one_liner: 提出支持全动态增删的DEG近邻图索引，兼顾三类场景下ANNS的构建效率与检索精度
practical_value: '- 动态商品/内容库的推荐召回场景，可直接复用开源DEG替换HNSW，无需标记删除僵尸节点，相同95%+ recall下检索QPS比删改后HNSW高1倍以上，索引构建速度快2-3倍

  - 向量库扩容/缩容时可复用DEG的分布无关扩展机制，无需针对图文/用户embedding等不同模态特征调优超参，降低跨场景适配成本

  - 实时流推荐的滑动窗口向量索引场景，可复用DEG的节点删除+子图重连逻辑，无需定期全量重建索引，节省运维成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有图based ANNS算法（如HNSW、crEG）仅支持静态/增量数据集，节点删除只能标记为僵尸节点，长期运行会导致检索性能骤降；而电商实时商品库、用户行为embedding动态更新等流/在线场景，需要支持频繁增删的高性能索引，现有方案要么存储开销翻倍、要么无法保证图连通性，兼顾静态/动态场景的通用ANNS索引缺失。

### 方法关键点
- 基于欧拉正则图特性设计顶点删除机制：删除节点后通过BFS探索邻接子图、合并连通分量、环形重连三步修复图结构，保证2边连通性，无孤立节点/断裂路径
- 分布无关的图扩展机制：新增节点优先连接符合MRNG性质的近邻，超出度数时删除最长边，再复用删除修复逻辑恢复正则性，无需针对特征分布调整超参
- 全程保证图的偶正则、无桥特性，无论增删都无需反向图辅助，存储开销与HNSW持平

### 关键实验
采用SIFT1M、Deep1M、GloVe三个公开数据集，对比HNSW、DiskANN、SWINN、crEG四个基线，覆盖静态（T1）、批量删除（T2）、滑动窗口流（T3）三个场景：
- 静态场景T1：DEG构建时间比HNSW快67%，95% recall下QPS与crEG持平、比HNSW高15%
- 批量删除场景T2：HNSW QPS下降50%，DEG性能无衰减反而因边优化提升10%，构建+删除总耗时比HNSW低53%
- 流场景T3：DEG QPS比DiskANN高3倍，索引更新延迟比SWINN低97%

支持全动态增删的近邻图索引无需牺牲静态场景性能，通过连通性保证机制即可同时覆盖静态、流、在线三类ANNS场景。
