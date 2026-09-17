---
title: 'Same Flow, Different Paths: Variance Reduction in Flow Matching'
title_zh: 相同流不同路径：面向流匹配的方差降低方法
authors:
- Alexander Tyurin
affiliations:
- AXXX, Moscow, Russia
- Applied AI Institute, Moscow, Russia
arxiv_id: '2609.17287'
url: https://arxiv.org/abs/2609.17287
pdf_url: https://arxiv.org/pdf/2609.17287
published: '2026-09-15'
collected: '2026-09-17'
category: Training
direction: 流匹配训练优化 · 梯度方差降低
tags:
- Flow Matching
- Variance Reduction
- SGD
- Training Optimization
- Diffusion Model
one_liner: 在不改变流匹配训练目标的前提下，通过最优路径选择降低SGD梯度方差加快收敛
practical_value: '- 基于流匹配做生成式推荐（如生成个性化Semantic ID、广告素材、推荐文案）的团队，可复用PathOpt_θ路径选择逻辑，在不改动原有生成目标的前提下降低训练梯度方差，减少训练步数

  - 流匹配生成模型训练可放弃默认线性路径，基于业务数据分布拟合最优路径，在相同算力下更快达到目标精度

  - 做LLM/生成模型训练优化的团队，可借鉴「约束下方差降低」思路，避免无约束降方差导致的收敛变慢问题'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
流匹配(FM)默认采用线性路径连接数据与噪声样本，现有研究未关注路径选择对SGD梯度方差、收敛速度的影响，相同训练目标下不同路径的训练效率存在显著差异。
### 方法关键点
1. 限定可选路径需满足相同边缘分布$p_t$与边缘速度场$v^*_t$，确保路径优化完全不改动原FM训练目标；
2. 针对线性速度模型与一维高斯数据场景，推导出SGD迭代复杂度紧界，给出线性路径类中的解析最优路径；
3. 通用FM场景下提出PathOpt$_θ$框架，将路径选择转化为带可采样验证约束的方差最小化问题，支持数值求解最优路径。
### 关键结果
在高斯数据、高斯混合模型及真实数据集上均验证，最优路径可显著降低梯度方差，大幅加快SGD收敛速度。
