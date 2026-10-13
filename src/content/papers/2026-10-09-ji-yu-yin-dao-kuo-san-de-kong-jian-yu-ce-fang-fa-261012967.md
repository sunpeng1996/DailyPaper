---
title: Spatial Prediction with Guided Diffusion
title_zh: 基于引导扩散的空间预测方法
authors:
- Andrew Zammit-Mangion
- Lachlan Astfalck
- Raphaël Huser
- Christopher Nemeth
- Henry B. Moss
affiliations:
- UNSW Sydney
- King Abdullah University of Science and Technology (KAUST)
- Lancaster University
arxiv_id: '2610.12967'
url: https://arxiv.org/abs/2610.12967
pdf_url: https://arxiv.org/pdf/2610.12967
published: '2026-10-09'
collected: '2026-10-13'
category: Other
direction: 扩散模型 · 空间分布预测
tags:
- Diffusion Models
- Spatial Prediction
- Generative Modeling
- MCMC
- Non-Gaussian Models
one_liner: 将引导扩散模型应用于可微似然场景的空间预测，解决传统方法采样难、高维扩展性差的痛点
practical_value: '- LBS类电商/广告场景（如到店推荐、商圈流量预测）的空间分布推断可复用该框架，替代传统MCMC提升高维场景采样效率

  - 带约束的条件生成任务可借鉴引导扩散注入可微似然的思路，降低生成结果与真实观测数据的偏差

  - 非高斯分布的多源异构数据聚合预测场景，可参考该方法的模型适配逻辑，提升复杂约束下的预测准确率'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
传统空间预测依赖层级模型计算隐空间过程的条件预测分布，该分布通常无闭式解，采样难度高；主流MCMC采样方法在高维隐场景下不可行，扩展性差。
### 方法关键点
基于引导扩散的空间预测框架仅要求数据模型导出的似然函数可微（支持松弛后可微），可适配高斯/非高斯过程模型，兼容直接部分观测、线性/区域聚合、计数、右删失等多类数据模式。
### 关键结果
在多组仿真实验与英国爱尔兰甲烷通量反演实验中，引导扩散可准确采样目标预测分布，支持MCMC不可行的模型场景，隐过程维度升高时扩展性远优于传统方法。
