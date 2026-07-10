---
title: 'Tensor Train Diffusion: Leveraging Low-Rank Structures for High-Dimensional
  Score-Based Sampling'
title_zh: 张量列扩散：利用低秩结构实现高维基于得分的采样
authors:
- Robert Gruhlke
- Julius Berner
- David Sommer
- Lorenz Richter
affiliations:
- Freie Universität Berlin
- NVIDIA
- WIAS
- dida
- Zuse Institute Berlin
arxiv_id: '2607.06841'
url: https://arxiv.org/abs/2607.06841
pdf_url: https://arxiv.org/pdf/2607.06841
published: '2026-07-07'
collected: '2026-07-10'
category: Other
direction: 扩散模型 · 高维采样效率优化
tags:
- Diffusion Model
- Tensor Train
- Low-Rank Approximation
- Score-Based Sampling
- High-Dimensional Sampling
one_liner: 提出基于函数张量列的HJB方程求解器，实现高效鲁棒的高维扩散采样
practical_value: '- 生成式推荐场景下用扩散模型生成候选Item/营销文案时，可引入FTT低秩结构压缩高维得分函数，降低推理延迟

  - 高维用户/物品表征的采样类任务，可复用FTT+BSDE的迭代求解框架，减少超参调优的人力成本

  - 业务侧扩散类生成模型的训练环节，可参考该方法替代PINNs求解HJB方程，大幅缩短训练周期'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
扩散模型基于得分的采样需求解HJB类偏微分方程，现有PINNs、轨迹法等主流方案训练耗时长、对超参数高度敏感，是高维场景落地的核心瓶颈。
### 方法关键点
1. 采用函数张量列（FTT）格式作为HJB方程求解器，利用隐式低秩结构高效近似高维函数，同时实现模型压缩与快速计算；
2. 结合反向随机微分方程（BSDE）推导的时间反向迭代策略，端到端构建快速、鲁棒、高精度的采样流程。
### 关键结果
相比现有方案，在高维目标分布采样任务中，训练效率大幅提升，超参鲁棒性显著增强，同时保持高保真采样效果。
