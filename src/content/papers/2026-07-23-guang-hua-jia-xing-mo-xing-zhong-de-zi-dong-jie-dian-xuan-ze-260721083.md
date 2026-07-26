---
title: Automatic knot selection in smooth additive models
title_zh: 光滑加性模型中的自动节点选择方法
authors:
- Nicolás Carrizosa
- Vanesa Guerrero
- María Durbán
affiliations:
- Universidad de Oviedo
- Universidad Carlos III de Madrid
arxiv_id: '2607.21083'
url: https://arxiv.org/abs/2607.21083
pdf_url: https://arxiv.org/pdf/2607.21083
published: '2026-07-23'
collected: '2026-07-26'
category: Other
direction: 广义加性模型 · 非参数回归节点优化
tags:
- Generalized Additive Models
- B-spline
- Knot Selection
- Nonparametric Regression
- Sparse Model
one_liner: 针对广义加性模型提出新型显式节点选择方法，性能与P样条相当且基元数量显著更少
practical_value: '- 推荐系统做用户行为非线性建模、转化率预估等场景用GAM时，可借鉴该节点选择方法压缩基元数量，降低推理延迟

  - 做非线性连续特征编码（如用户消费时长、价格敏感度分箱）时，可复用该自动节点选择逻辑替代人工/等频分箱，提升拟合效率

  - 小样本预估场景（如冷启动商品转化预估）用非参数模型时，可结合该方法在保证效果的前提下降低参数量，缓解过拟合'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
B-spline是非参数回归的主流框架，其节点（knot）的数量与位置直接决定模型的平滑度、拟合效果与参数量。传统P-splines等正则化方案是广义加性模型（GAMs）的通用选择，但显式节点选择方法因计算、建模限制被长期忽略，具备稀疏化降参的独特潜力。
### 方法关键点
1. 扩展自适应样条（A-splines）的节点选择逻辑，适配广义加性模型的建模需求
2. 搭配定制化Fellner-Schall方案，自动调优节点选择关联参数，无需人工预定义节点数量、位置
### 关键结果
在多组合成、真实数据集上与P-splines、SOTA节点选择方法对比，拟合效果完全持平，生成模型所需的基元数量大幅降低，整体模型更轻量化、解释性更强
