---
title: 'Poisson Subspace Clustering: Focusing on the Essentials in Count Data'
title_zh: 泊松子空间聚类：聚焦计数数据核心特征的聚类方法
authors:
- Collin Leiber
- Kai Puolamäki
- Heikki Mannila
affiliations:
- Aalto University
- University of Helsinki
arxiv_id: '2608.23287'
url: https://arxiv.org/abs/2608.23287
pdf_url: https://arxiv.org/pdf/2608.23287
published: '2026-08-24'
collected: '2026-08-25'
category: Other
direction: 计数数据 · 子空间聚类算法
tags:
- Clustering
- Count Data
- Poisson Distribution
- Subspace Clustering
- Interpretability
one_liner: 提出基于泊松统计建模的3CPO计数聚类算法，可同时输出簇标签和关联特征子集提升可解释性
practical_value: '- 电商用户分群/商品分群场景中，针对点击、加购、购买、曝光等计数型特征，可替换通用KMeans等聚类算法，避免分布不匹配导致的分群偏差

  - 做人群/商品聚类时可复用3CPO的特征自动选择能力，直接输出对分群贡献最高的特征子集，降低后续运营侧的分群解释成本

  - 开源代码可直接二次封装接入用户画像、人群圈选链路，无需从零实现泊松分布聚类逻辑，快速落地统计鲁棒的分群能力'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
计数数据（非负整数矩阵，如列联表、行为次数统计等）广泛存在于各领域，通用聚类算法未适配其独有的分布特性，输出结果可靠性低，且聚类结果可解释性差。
### 方法关键点
1. 基于泊松分布对计数数据做统计建模，提出3CPO迭代聚类算法，通过最大化后验概率求解最优聚类结果；
2. 除输出簇标签外，可自动识别与聚类相关的特征列子集，无需额外特征筛选即可支撑结果解释。
### 关键结果
在基因表达、文本、经济等多领域数据集上验证，可生成高质量关联子空间内的聚类结果，鲁棒性显著优于通用无适配的聚类方案，代码已开源可直接使用。
