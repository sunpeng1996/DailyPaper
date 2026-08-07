---
title: Intrinsic-Hybrid Latent Diffusion Models for Generative Modeling on Unknown
  Manifolds
title_zh: 面向未知流形生成建模的内禀混合隐扩散模型
authors:
- Yizhu Wang
- Mu Niu
- Xiaochen Yang
arxiv_id: '2608.04827'
url: https://arxiv.org/abs/2608.04827
pdf_url: https://arxiv.org/pdf/2608.04827
published: '2026-08-05'
collected: '2026-08-07'
category: Other
direction: 未知流形生成 · 隐扩散模型优化
tags:
- Diffusion Model
- Latent Diffusion
- Generative Modeling
- Riemannian Manifold
- Low Data Regime
one_liner: 提出内禀混合隐扩散模型ILDM，解决少数据场景下隐扩散无法捕获数据底层流形几何的问题
practical_value: '- 少样本生成场景可参考ILDM的混合扩散设计，根据数据局部不确定性切换欧氏/黎曼动力学，降低小数据集下生成偏差

  - 生成式推荐生成Item语义表示/Semantic ID时，可引入概率解码器量化隐空间几何结构，提升冷启动场景生成准确性

  - 高维用户/物品embedding生成任务中，不默认强制隐空间为欧氏结构，可结合数据底层流形设计扩散过程优化效果'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有扩散模型依赖大量训练数据且忽略数据内在几何结构，标准隐扩散模型（LDM）强制隐空间为欧氏结构，无法捕获底层流形几何，在数据稀疏场景效果下降明显。

### 方法关键点
1. 将隐空间视为未知黎曼流形的坐标图，通过概率解码器量化几何结构与不确定性；
2. 设计混合扩散前向过程，根据局部不确定性动态切换黎曼/欧氏动力学，黎曼分量由解码器导出的概率度量张量控制；
3. 适配混合扩散场景设计近似去噪得分匹配方法，基于混合朗之万动力学实现反向生成过程。

### 关键结果
在COIL-100、MNIST、心脏MRI数据集上，相比标准扩散与LDM，FID、LPIPS指标显著降低，生成质量大幅提升。
