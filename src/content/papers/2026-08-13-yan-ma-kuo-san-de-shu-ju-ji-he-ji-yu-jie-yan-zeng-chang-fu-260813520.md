---
title: 'The data geometry of masking diffusion: Certified-optimal schedules via unmasking
  growth complexity'
title_zh: 掩码扩散的数据几何：基于解掩增长复杂度的认证最优调度
authors:
- Martin J. Wainwright
affiliations:
- Massachusetts Institute of Technology
- Lab for Information and Decision Systems
- Statistics and Data Science Center
- EECS and Mathematics Department
arxiv_id: '2608.13520'
url: https://arxiv.org/abs/2608.13520
pdf_url: https://arxiv.org/pdf/2608.13520
published: '2026-08-13'
collected: '2026-08-16'
category: Training
direction: 离散扩散模型 · 采样调度优化
tags:
- Diffusion Model
- Discrete Sampling
- Masking Schedule
- KL Divergence
- Sampling Optimization
one_liner: 提出解掩增长复杂度UGC度量，推导离散掩码扩散的认证最优采样调度，降低高维采样误差
practical_value: '- 生成式推荐中用离散扩散生成Semantic ID/候选集时，可基于UGC度量自适应调整掩码调度，在保证采样质量的前提下减少采样步数，提升推理效率

  - 离散扩散的KL误差控制方法可复用至用户行为序列生成、营销文案生成等场景的采样过程，实现指定精度下的采样效率最优

  - UGC的样本估计方法可用于评估生成式推荐模型的采样复杂度，指导业务场景下的算力分配与模型迭代优化'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
离散掩码扩散已广泛应用于生成式AI等高维采样场景，但通用粗粒度调度未适配数据几何特征，高维场景下采样误差高、步数多，缺乏可认证的最优调度理论支撑。

### 方法关键点
1. 提出路径级数据几何度量**UGC（解掩增长复杂度）**，其局部增量直接控制KL离散化误差，统一了伯努利子集、固定基数两类解掩方案的分析框架；
2. 基于对数揭示odds坐标推导单块/多块优化调度，可通过耦合揭示轨迹的KL增量从样本中估计UGC增量，构造认证最优采样器。

### 关键结果
适配数据几何的自适应调度相比粗调度可获得$	ilde{Ω}(√d)$的维度相关性能收益，仅需常数个自适应放置的块即可实现；最优欧拉离散化误差由UGC密度平方根的平方积分精确决定，迭代复杂度与oracle方法仅差常数因子。
