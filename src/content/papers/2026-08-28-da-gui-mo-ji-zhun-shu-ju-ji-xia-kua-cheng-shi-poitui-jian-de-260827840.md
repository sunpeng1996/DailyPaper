---
title: An Empirical Evaluation of Cross-City POI Recommendation on a Large-Scale Benchmark
title_zh: 大规模基准数据集下跨城市POI推荐的实证评估
authors:
- Peibo Li
- Yang Song
- Hao Xue
- Maarten de Rijke
- Flora D. Salim
affiliations:
- University of New South Wales
- The Hong Kong University of Science and Technology (Guangzhou)
- University of Amsterdam
arxiv_id: '2608.27840'
url: https://arxiv.org/abs/2608.27840
pdf_url: https://arxiv.org/pdf/2608.27840
published: '2026-08-28'
collected: '2026-08-31'
category: RecSys
direction: POI推荐 · 跨域迁移实证评估
tags:
- POI Recommendation
- Cross-Domain Recommendation
- Empirical Study
- Benchmark
- Scalable RecSys
one_liner: 基于Trip World基准揭示现有跨城POI推荐三类瓶颈，指明任务专属优化方向
practical_value: '- 做跨域（跨城/跨品类）推荐时，先验证简单基线（如目标域热门先验）的效果，不要盲目开发复杂用户偏好迁移模型，避免无效投入

  - 大规模低重叠跨域推荐场景下优先评估简单模型的精度效率trade-off，复杂SOTA的实际收益可能远低于工程落地成本

  - 通用语义元数据融合方案在跨域冷启动场景增益极低，需针对业务场景设计专属语义对齐逻辑，不要直接复用通用语义增强方法'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
过往跨城POI推荐研究受限于小规模基准数据集，结论普适性不足，且缺乏大规模真实场景下的算法瓶颈系统性分析。
### 方法关键点
基于大规模跨城出行基准Trip World，在全球覆盖、家乡-目的地区域重叠度低、POI语义信息丰富的真实场景下，对多类SOTA跨城POI推荐算法开展系统性实证评估，同时测试了从下一POI推荐任务迁移而来的Agent方法的适配效果。
### 关键结果
1. 现有家乡感知类模型的效果主要来自目的地区域先验，用户个性化偏好迁移贡献极低；
2. 大规模场景下最简单的热门POI基线模型精度跻身Top3，复杂SOTA的精度效率比相比小规模场景下降70%以上；
3. 现有通用语义元数据融合机制仅带来不足2%的精度提升，增益可忽略；
4. 朴素迁移的Agent方法效果比热门基线低15%以上，远未达到可用标准。
