---
title: 'Distributional Matching for Vector Quantization: A Unified Theoretical and
  Empirical Framework'
title_zh: 面向向量量化的分布匹配：统一的理论与实验框架
authors:
- Xianghong Fang
- Litao Guo
- Hengchao Chen
- Yuxuan Zhang
- XiaofanXia
- Dingjie Song
- Yexin Liu
- Hao Wang
- Harry Yang
- Qiang Sun
affiliations:
- University of Toronto
- The Hong Kong University of Science and Technology
- Boston College
- Lehigh University
- Southern University of Science and Technology
arxiv_id: '2607.15933'
url: https://arxiv.org/abs/2607.15933
pdf_url: https://arxiv.org/pdf/2607.15933
published: '2026-07-17'
collected: '2026-07-20'
category: Training
direction: 向量量化训练优化 · 分布匹配框架
tags:
- Vector Quantization
- Codebook Collapse
- Distribution Alignment
- Wasserstein Distance
- Representation Learning
one_liner: 通过特征与编码向量分布对齐，统一解决向量量化训练不稳定与码本坍塌问题
practical_value: '- 生成式推荐场景下做Semantic ID编码时，可引入分布匹配目标优化VQ码本，降低码本坍塌概率，提升离散ID的表征质量

  - 多模态召回的特征量化环节，可复用高斯近似下的Wasserstein闭形式损失，无需额外复杂运算即可提升VQ训练稳定性

  - 若业务场景对分布假设约束较强，可替换为MMD非参数分布匹配损失，在保证效果的同时放宽假设限制'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有VQ方法普遍存在训练不稳定、码本坍塌问题，根源是直通估计器带来的梯度不匹配、编码向量利用率低，本质是特征向量与编码向量的分布不匹配，导致表征效率低、信息损失严重。
### 方法关键点
提出分布匹配VQ框架，从理论层面论证特征与编码分布对齐可统一解决上述两类问题；落地两种可行实现：一是高斯近似下带高效闭形式解的Wasserstein目标，二是基于最大均值偏差（MMD）的非参数方案，两种方案效果相当。
### 关键结果
在视觉Tokenization基准任务上验证了方法的有效性与鲁棒性，码本利用率提升30%以上，训练波动降低40%，表现优于现有主流VQ方案。
