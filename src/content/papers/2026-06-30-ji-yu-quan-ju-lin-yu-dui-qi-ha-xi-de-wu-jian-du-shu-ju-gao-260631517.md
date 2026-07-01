---
title: Unsupervised Data-Efficient Cross-Modal Retrieval with Global-Neighborhood
  Alignment Hashing
title_zh: 基于全局-邻域对齐哈希的无监督数据高效跨模态检索
authors:
- Runhao Li
- Xiaoxu Ma
- Zhenyu Weng
- Yue Zhang
- Guibo Luo
- Huiping Zhuang
- Zhiping Lin
- Yap-Peng Tan
affiliations:
- Nanyang Technological University
- South China University of Technology
- Henan Normal University
- Peking University Shenzhen Graduate School
- VinUniversity
arxiv_id: '2606.31517'
url: https://arxiv.org/abs/2606.31517
pdf_url: https://arxiv.org/pdf/2606.31517
published: '2026-06-30'
collected: '2026-07-01'
category: Multimodal
direction: 跨模态检索 · 低资源无监督哈希
tags:
- Cross-Modal Retrieval
- Unsupervised Hashing
- Data Efficient
- Contrastive Learning
- Vision-Language Model
one_liner: 仅用少量图文对实现高性能无监督跨模态哈希检索，数据受限场景优于现有方案
practical_value: '- 电商多模态召回（图文商品匹配、以图搜商品）缺标注数据时，可复用GNAH的低资源无监督哈希方案降本

  - 可借鉴Prototype-Anchored全局对齐模块，把多模态大模型的语义结构迁移到紧凑哈希空间，大幅提升检索速度

  - 小样本跨模态训练时，可引入随机邻域对齐的对比学习思路，缓解稀疏配对的过拟合问题'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有无监督跨模态哈希（CMH）无需人工标注，但高度依赖大规模图文对，采集成本高，无法适配数据受限的业务场景。

### 方法关键点
提出GNAH框架，仅用少量图文对即可将视觉语言基础模型的语义结构映射到紧凑二进制汉明空间：
1. 原型锚定全局对齐模块：提取连续隐空间的全局结构信息，直接迁移到二进制汉明空间保留全局语义关系
2. 对比随机邻域对齐模块：建模随机邻域关系改进传统成对对比学习，缓解稀疏成对关联带来的过拟合问题

### 关键结果
在数据受限场景下，GNAH性能持续超越现有所有无监督跨模态检索方法，可直接落地实际跨模态哈希应用
