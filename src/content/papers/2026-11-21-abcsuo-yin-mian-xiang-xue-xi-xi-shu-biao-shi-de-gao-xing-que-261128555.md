---
title: 'The abc index: Exact Retrieval for Learned Sparse Representations'
title_zh: abc索引：面向学习稀疏表示的高性能精确检索方案
authors:
- Rossano Venturini
affiliations:
- University of Pisa
arxiv_id: '2611.28555'
url: https://arxiv.org/abs/2611.28555
pdf_url: https://arxiv.org/pdf/2611.28555
published: '2026-11-21'
collected: '2026-11-24'
category: RecSys
direction: 稀疏检索 · 倒排索引性能优化
tags:
- Learned Sparse Retrieval
- Inverted Index
- Exact Top-k Retrieval
- Dynamic Pruning
- Query Processing
one_liner: 结合经典IR技术打造无调参学习稀疏检索精确索引，性能领先现有方案数倍到数十倍
practical_value: '- LSR召回引擎优化可复用硬窗口TAAT设计：将doc-id划分为对齐L1缓存的固定块，posting存块内偏移直接作为累加器槽位，避免软窗口的二分查找和doc-id重映射开销，实测可提升30%以上检索性能

  - 动态剪枝适配LSR场景可参考abc-bmms的块内Block-Max MaxScore实现，跨术语对齐子块最大值，按块级bound降序访问快速拉高堆阈值，配合候选探测替代全量列表读取，可在不损失召回的前提下提速2~4倍

  - doc-id重排序可借鉴论文的快速图二分方案，放弃小窗口内的精细swap，采用样本打分+全局排序思路，重排序速度提升19.5倍的同时仅损失1.2%的压缩率，大幅降低索引构建开销

  - 稀疏检索选型可参考结论：k≤10时近似索引（HNSW/Seismic）有速度优势，k≥1000时abc精确索引速度反超7.4倍且无需调参，适合电商多目标召回、全库语义检索等需要高召回、大topk的场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有学习稀疏检索（LSR）的查询带有大量带学习权重的术语，传统动态剪枝算法失效，业界普遍认为近似索引速度远高于精确索引，但近似索引需要大量调参、不同k需要独立索引，且召回无法保证，高可靠性场景下的精确检索存在显著性能瓶颈。

### 方法关键点
- 采用硬窗口TAAT设计：将doc-id划分为固定对齐的8192大小块，刚好适配CPU L1缓存，posting仅存16位块内偏移直接作为累加器槽位，避免软窗口的额外计算开销
- 块内集成Block-Max MaxScore剪枝：每个块拆分为8个1024大小的子块，存储每个术语在子块的8bit最大值，块按bound降序访问快速拉高堆阈值，块内拆分必要/非必要术语，非必要术语仅对候选文档探测而非全量读取
- 优化doc-id重排序算法：放弃小窗口内的精细swap迭代，采用样本打分+全局排序的快速图二分方案，重排序速度提升19.5倍，压缩率仅损失1.2%

### 关键实验
在MS MARCO数据集上用4种主流LSR模型测试：精确检索场景下比Qdrant快6.5~84倍，比Lucene快13~55倍，比BMP快2.9~18倍，索引体积小5~7倍；对比近似索引，体积小1.5~3.6倍，k=10时近似索引最快快4.3倍，k=1000时abc反超最快7.4倍，且无需调参、单索引适配所有k；32位全精度精确检索比暴力扫描快27~52倍，可作为LSR模型评测的真值生成工具。

最值得记住的一句话：经典IR技术经过适配现代CPU的工程优化，完全可以在LSR场景下实现比最新近似索引更优的大topk检索性能，且无需任何调参。
