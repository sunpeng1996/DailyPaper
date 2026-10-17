---
title: 'Classical methods for modern applications: synthetic tabular data generation
  using lightweight discrete response continuous latent variable model'
title_zh: 面向现代应用的经典方法：基于轻量潜变量模型的混合表格数据合成
authors:
- Bartosz Barzdajn
- Mateusz Krzysztoń
affiliations:
- NASK National Research Institute
arxiv_id: '2610.21674'
url: https://arxiv.org/abs/2610.21674
pdf_url: https://arxiv.org/pdf/2610.21674
published: '2026-10-15'
collected: '2026-10-17'
category: Other
direction: 混合表格数据合成 · 轻量潜变量模型
tags:
- Tabular Data Generation
- Latent Variable Model
- Synthetic Data
- MCEM
- Lightweight Model
one_liner: 提出无深度学习依赖的轻量混合表格数据合成算法，训练鲁棒采样高效，特征相关性保留度高
practical_value: '- 电商推荐场景做用户/商品特征数据增强时，可替代GAN/扩散类深度合成模型，依赖少训练快，适合小样本特征快速补全

  - 离散特征（如用户性别、商品类目）连续化表示场景，可复用经验边际分布+分位数函数的转换范式，更好保留特征间相关性

  - 低资源合成数据生成任务，可直接复用MCEM加权潜空间似然优化框架，无需大模型/深度架构即可获得高保真结果'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有混合类型（连续+离散）表格数据合成方法多依赖深度学习架构，依赖包多、训练复杂度高，小样本/低资源场景下易用性差，无法满足轻量快速的合成需求。
### 方法关键点
1. 采用经验边际分布+指定分位数函数，将混合类型数据映射到连续潜空间，可选用多元高斯等分布做高效估计；
2. 针对离散变量连续化后单观测对应潜空间区域的歧义问题，采用MCEM框架，将辅助目标转化为加权潜空间似然，可直接复用传统最大似然估计器优化。
### 关键结果
相比深度合成架构，本方法仅需少量依赖，训练鲁棒性更强、采样效率显著更高，可完整保留特征边际分布与相关性，单峰分布数据保真度表现优异。
