---
title: Efficient Clustering with Provable Guardrails for LLM Inference at Scale
title_zh: 面向大规模LLM推理的带可证明约束的高效聚类算法
authors:
- Longshaokan Wang
- Wai Tsang Keung
- Punit Ghodasara
- Roman Wang
- Ali Dashti
- Francesc Moreno-Noguer
affiliations:
- Amazon
arxiv_id: '2607.19704'
url: https://arxiv.org/abs/2607.19704
pdf_url: https://arxiv.org/pdf/2607.19704
published: '2026-07-22'
collected: '2026-07-23'
category: LLM
direction: LLM推理降本 带约束大规模聚类
tags:
- Clustering
- LLM Inference
- Cost Optimization
- Scalability
- Recommendation System
one_liner: 提出带相似度与属性可证明约束的两阶段聚类算法，大规模LLM推理降本可达50倍
practical_value: '- 可直接复用两阶段聚类架构：先用Mini-batch K-Means做粗聚类拆分全量数据，再在子簇内用greedy set cover选代表，同时强制属性匹配+相似度阈值，既满足电商场景的用户分群合规要求（如儿童商品适配），又能大幅压缩LLM调用量

  - 利用聚类结果的重尾分布做tail trimming：仅保留头部4%的簇即可覆盖90%用户，可进一步获得25倍降本，少量尾部用户可通过上游oversampling补偿，几乎不影响核心业务指标

  - 调参可参考内置trade-off：初始聚类K越大，二阶计算复杂度越低但压缩比略有下降，优先选择内存/延迟预算允许的最小K；相似度阈值α可根据业务对相关性的容忍度与LLM成本预算动态调整'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
大规模LLM在电商推荐等C端场景落地时，推理成本和延迟随用户规模线性增长，直接调用LLM处理38M用户的个性化推荐需求，仅LLM阶段成本就达113万美元、耗时508天，完全不具备生产可行性。现有聚类方法无法同时满足「簇内样本与代表相似度≥指定阈值、分类属性完全匹配、压缩比≥10倍、可扩展到千万级样本」四个生产要求，导致分群复用LLM输出的降本方案无法落地。
### 方法关键点
- 两阶段架构：阶段1用Mini-batch K-Means做粗聚类，将全量数据拆分为K个初始簇，把二阶的O(n²)相似度计算限制在子簇内，大幅降低复杂度
- 阶段2在每个初始簇内用Johnson–Chvátal贪心集覆盖heuristic选代表：每次选覆盖未匹配样本最多的点作为代表，强制同簇样本与代表的cosine similarity≥α、分类属性完全匹配，从构造上100%满足约束要求
- 可选重分配步骤：将样本重分配到最相似的合格代表，提升平均簇内相似度，不改变簇数量和约束条件
- 整体复杂度为O(nd + n²d/K)，当K与n成正比时计算量线性于n，可支撑千万级样本处理
### 关键结果
在100K规模的内部购物人设、AG News、Cosmopedia数据集上对比6种主流聚类方法，相同簇数量下速度快10~1000倍，无1例违反相似度/属性约束，基线方法有2.9%~21%的样本低于阈值；38M电商用户生产环境部署，强制匹配家庭构成等安全属性，α=0.77时实现50倍下游LLM计算与延迟降低，推荐相关性仅下降0.7%，业务指标正向。
**最值得记住的一句话**：带强约束的聚类降本是千万级用户规模下LLM推荐落地的必要基建，通过构造性约束而非事后校验可同时保证安全性和成本收益
