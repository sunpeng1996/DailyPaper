---
title: Alternatives to Shallow Autoencoders for Collaborative Filtering
title_zh: 面向协同过滤的浅自编码器优化替代方案
authors:
- Mario Mallea
- Angela Nebot
- Francisco Mugica
affiliations:
- Universitat Politècnica de Catalunya
arxiv_id: '2611.06610'
url: https://arxiv.org/abs/2611.06610
pdf_url: https://arxiv.org/pdf/2611.06610
published: '2026-11-04'
collected: '2026-11-05'
category: RecSys
direction: 协同过滤 · 浅自编码器性能优化
tags:
- Collaborative-Filtering
- Autoencoder
- EASE
- Implicit-Feedback
- Recommender-System
one_liner: 提出用户侧u-EASE与双视角混合u-EASE-i，超越经典EASE的协同过滤效果
practical_value: '- 业务上可根据用户/物品规模选择模型：用户数>物品数时优先用u-EASE，训练速度更快、推荐精度更高；反之用原EASE

  - 资源充足时可直接上线u-EASE-i，通过user-user+item-item双视角特征融合，在Yelp/ML-1M数据集上比EASE nDCG@100提升2.5%~6.3%，无额外推理开销

  - 可复用论文的正则调优经验：u-EASE最优正则一般在10^3量级，u-EASE-i的两个正则参数可在10^1~10^4网格搜索，存在互补效应容错率高'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
经典EASE模型凭借闭式解、训练快、精度高的优势成为CF领域常用基线，但其仅基于item-item共现关系建模，无法捕捉细粒度user-user关联，在用户数远大于物品数的场景下性能受限，同时参数规模受物品数限制存在优化空间。

### 方法关键点
- u-EASE：对称复刻EASE的优化框架，改为基于user-user共现Gram矩阵建模，仅需调优1个正则参数，同样保留闭式解无迭代训练开销
- u-EASE-i：融合user侧和item侧双视角特征，闭式解直接结合u-EASE和EASE的权重矩阵，同时捕捉用户社群和物品关联特征
- 计算复杂度：u-EASE训练耗时由用户数决定，当用户数小于物品数时训练速度比EASE快40%以上，u-EASE-i需同时计算两个Gram矩阵，耗时约为单视角模型的2~3倍

### 关键实验结果
在Gowalla、Yelp2018、ML-1M三个公开CF数据集上对比EASE、LightGCN、SVD-AE等8个基线模型：1）用户数大于物品数的ML-1M数据集上，uEASE-i比EASE nDCG@100提升6.3%，达到SOTA水平；2）Yelp2018数据集上uEASE-i比EASE nDCG@100提升3.7%；3）u-EASE在用户数少的场景下训练速度比EASE快40%，精度损失可接受适合资源受限场景。

**最值得记住的结论**：浅自编码器类CF模型的最优建模视角由用户/物品的规模比例决定，双视角融合可无额外推理开销提升推荐精度。
