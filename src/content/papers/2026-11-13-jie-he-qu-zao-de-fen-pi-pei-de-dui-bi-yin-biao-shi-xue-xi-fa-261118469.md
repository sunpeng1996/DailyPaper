---
title: Contrastive latent representation learning with denoising score matching
title_zh: 结合去噪得分匹配的对比隐表示学习方法
authors:
- Christopher Marouani
- Grigory Bartosh
- Christian A. Naesseth
affiliations:
- ENS Paris-Saclay
- University of Amsterdam
arxiv_id: '2611.18469'
url: https://arxiv.org/abs/2611.18469
pdf_url: https://arxiv.org/pdf/2611.18469
published: '2026-11-13'
collected: '2026-11-16'
category: Training
direction: 对比表示学习 · 训练效率优化
tags:
- Contrastive Learning
- Representation Learning
- Denoising Score Matching
- Self-Supervised Learning
- Efficiency Optimization
one_liner: 提出ScoreCLR对比学习方法，用去噪得分匹配替代显式负样本，将batch计算复杂度从二次降为线性
practical_value: '- 召回/排序阶段的对比学习训练可复用ScoreCLR思路，用去噪得分匹配替代显式负采样，解决大batch负采样算力瓶颈，降低训练成本

  - 多模态特征预训练时，可引入本文的高斯先验正则+多噪声水平训练策略，提升隐向量有效秩，缓解特征坍缩问题

  - 用户/物品语义表示预训练时，可直接替换原SimCLR类对比目标，在精度损失极小的前提下获得更高训练吞吐量'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统对比学习需大batch显式负样本估计排斥项，存在方差高、易受维度灾难影响、batch维度计算复杂度为二次的问题，训练成本高。
### 方法关键点
ScoreCLR对比表示学习框架通过最大化样本两个隐视图的互信息推导等价目标，将香农熵对编码器参数的梯度转化为隐表示得分项，用轻量网络联合训练做去噪得分匹配估计该得分，替代显式负样本的排斥项，同时引入多噪声水平训练、隐表示高斯先验正则策略。
### 关键结果数字
batch维度计算复杂度从二次降至线性；在CIFAR-10、ImageNet-100数据集上，相同实验配置下相比SimCLR线性探测精度损失极小，生成的投影输出有效秩更高，更接近高斯先验分布。
