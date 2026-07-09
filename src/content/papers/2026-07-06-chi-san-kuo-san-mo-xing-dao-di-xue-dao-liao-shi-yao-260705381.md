---
title: What Does a Discrete Diffusion Model Learn?
title_zh: 离散扩散模型到底学到了什么？
authors:
- Rodrigo Casado Noguerales
- Bernhard Schölkopf
- Thomas Hofmann
- Aran Raoufi
affiliations:
- ETH Zurich
- Max Planck Institute for Intelligent Systems, Tübingen
- ELLIS Institute Tübingen
arxiv_id: '2607.05381'
url: https://arxiv.org/abs/2607.05381
pdf_url: https://arxiv.org/pdf/2607.05381
published: '2026-07-06'
collected: '2026-07-09'
category: Training
direction: 离散扩散模型训练理论研究
tags:
- Discrete Diffusion
- ELBO
- CTMC
- Score Matching
- Parameterization
one_liner: 从连续时间马尔可夫链视角推导离散扩散ELBO本质，统一不同参数化形式的底层逻辑
practical_value: '- 用离散扩散做生成式推荐/商品文案生成时，优先选择bridge plug-in（cavity）参数化，避免uniform ELBO初始化发散问题

  - 落地离散扩散类模型时，可直接复用论文给出的denoiser、score、cavity三者闭式转换公式，无需自行推导适配不同训练目标

  - 离散扩散训练的最优可实现负ELBO等于数据熵，可直接用该值作为训练收敛的参考阈值，减少调优成本'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有离散扩散存在denoiser、score ratio、bridge plug-in等多种参数化实现，不同方案训练采样效果差异大，底层逻辑缺乏统一的严谨理论解释。
### 方法关键点
基于连续时间马尔可夫链（CTMC）推导包含边界项的任意噪声过程ELBO，提出Oracle Distance定理，证明负ELBO等于数据熵加oracle反向过程到学习过程的路径KL，并非传统意义的上界；针对token分解噪声的序列场景，给出denoiser、cavity（bridge plug-in）、score三种最优参数化的闭式转换关系。
### 关键结果
统一了MDM、UDM、SEDD、GIDD等现有离散扩散方法的理论框架，解释了掩码扩散中denoiser与cavity等价、均匀扩散中二者不等价的原因；证明denoiser参数化会导致均匀ELBO初始化发散，bridge plug-in参数化可避免该问题；所有结论在可解模型上得到无近似数值验证。
