---
title: Extended Depth-First Representations of $k^2$-trees
title_zh: k²树的扩展深度优先表示
authors:
- Gabriel Carmona
- Paolo Ferragina
- Giovanni Manzini
- Francesco Tosoni
affiliations:
- Department of Computer Science, University of Pisa
- L'EMbeDS Department, Sant'Anna School of Advanced Studies
arxiv_id: '2607.28136'
url: https://arxiv.org/abs/2607.28136
pdf_url: https://arxiv.org/pdf/2607.28136
published: '2026-07-30'
collected: '2026-08-03'
category: Other
direction: 图压缩 · 高效数据结构优化
tags:
- k2-tree
- graph compression
- succinct data structure
- cache optimization
- linear algebra
one_liner: 提出4种k²树深度优先表示及线性压缩方法，提升图压缩率与矩阵运算缓存效率
practical_value: '- 电商大规模商品图谱、用户行为图存储可复用CEDF压缩方案，平衡存储成本与访问性能

  - 图推荐场景下的矩阵向量乘、邻接矩阵运算可替换原k²树的层序布局为深度优先布局，提升缓存命中率降低运算时延

  - 基于后缀数组与LCP数组的相同子树线性压缩算法，可迁移到类目树、倒排索引树等推荐相关结构的压缩优化'
score: 3
source: arxiv-cs.IR
depth: abstract
---

### 动机
传统k²树采用层序布局，数据局部性差导致缓存性能低，在矩阵向量乘、矩阵乘等图运算场景时延高，无法支撑大规模知识图谱、用户行为图的高效存储与运算需求。

### 方法关键点
1. 提出4种k²树深度优先表示：基础深度优先布局EDF-1、平衡括号表示BP，及二者的压缩版本CEDF、CBP；
2. 基于后缀数组与LCP数组设计线性时间压缩方法，可自动识别并合并压缩相同子树。

### 关键结果
在网页图、Wikidata、随机邻接矩阵三类数据集上测试：CEDF在多数场景下取得最优压缩率；EDF-1与CEDF可稳定降低峰值内存占用；不同布局适配不同工作负载，整体性能优于传统层序k²树与DFUDS表示方案。
