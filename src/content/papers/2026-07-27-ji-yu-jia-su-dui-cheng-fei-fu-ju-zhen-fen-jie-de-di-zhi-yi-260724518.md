---
title: Low-Rank Dependence Decomposition via Accelerated Symmetric Non-negative Matrix
  Factorization
title_zh: 基于加速对称非负矩阵分解的低秩依赖分解方法
authors:
- Lavinia Ghita
- Dhruv Desai
- Jake Goldberg
- Roman Yokunda Enzmann
affiliations:
- NVIDIA
arxiv_id: '2607.24518'
url: https://arxiv.org/abs/2607.24518
pdf_url: https://arxiv.org/pdf/2607.24518
published: '2026-07-27'
collected: '2026-07-29'
category: Training
direction: 矩阵分解训练加速 · 大规模SymNMF求解
tags:
- SymNMF
- Matrix Factorization
- GPU Acceleration
- Clustering
- Embedding
- Large-scale Training
one_liner: 提出trace恒等重写等优化，实现百万级规模对称非负矩阵分解的高效GPU求解
practical_value: '- 做用户/物品共现矩阵、相似度矩阵的低秩分解时，可复用trace-identity重写技巧，避免生成n×n中间矩阵，大幅降低内存开销，单卡就能支撑10万级规模的隐向量生成

  - 大规模SymNMF求解可直接复用论文验证的最优求解器组合：低秩占优的相似度矩阵（比如用户兴趣共现）用全批量AdaGrad，病态长尾依赖矩阵（比如小众商品共现）用Block-SVRG
  AdaptGrow，最大化训练速度

  - 软聚类与硬聚类选型可参考论文结论：有明确角聚类结构时用球形K-means降本，矩阵趋向单共因子时必须保留SymNMF软分解保证效果'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
SymNMF可从依赖矩阵中恢复隐群组结构，输出软聚类结果与嵌入向量，可用于协同过滤、用户分群等推荐场景，但原有方法依赖n×n级稠密中间矩阵，内存开销为二次型，仅能支撑中等规模数据。
### 方法关键点
1. 用trace-identity重写目标函数，完全消除n×n中间矩阵开销；
2. 对比7类共30余种算法配置，新增3种AdaGrad系优化器（Piecewise AdaGrad、Row-Stochastic SVRG、Block-SVRG AdaptGrow），适配不同矩阵谱特性。
### 关键结果
单GPU支持n≈1e5规模求解，多机分布式可扩展至n=1e6及以上；1e6规模下，病态长尾依赖矩阵场景Block-SVRG AdaptGrow速度最优，低秩占优的相关矩阵场景全批量AdaGrad速度最优；球形K-means在存在角聚类结构时成本更低，但矩阵趋向单共因子时会退化，必须保留软分解。
