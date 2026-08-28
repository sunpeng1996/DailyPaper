---
title: Inductive Correlation Clustering with Graph Neural Networks
title_zh: 基于图神经网络的归纳式关联聚类方法
authors:
- Francesco Paolo Nerini
- Francesco Bonchi
- Arijit Khan
- André Panisson
affiliations:
- Sapienza University of Rome
- Intesa Sanpaolo AI Research
- Bowling Green State University
arxiv_id: '2608.27153'
url: https://arxiv.org/abs/2608.27153
pdf_url: https://arxiv.org/pdf/2608.27153
published: '2026-08-27'
collected: '2026-08-28'
category: Other
direction: 图结构数据 · 归纳式关联聚类
tags:
- Correlation Clustering
- GNN
- Graph Pooling
- Inductive Learning
- Clustering
one_liner: 基于GNN实现归纳式关联聚类，推理提速5个数量级，精度仅比最优基线低约10%
practical_value: '- 电商/推荐场景中用户/物品的图结构聚类可复用该归纳式框架，新增样本无需全量重训，大幅降低聚类算力开销

  - 可作为GNN pooling层嵌入用户/物品表征建模流程，提升模型对图层级结构信息的捕捉能力，优化召回/排序效果

  - 实时用户分群、动态商品打标等需要增量聚类的业务场景可参考其低延迟推理方案，满足线上性能要求'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统关联聚类（CC）无需预设簇数、适配性强，但存在两大核心缺陷：一是可扩展性差，二是属于直推式范式，新增图实例必须从头重训，无法适配增量、动态业务场景。

### 方法关键点
提出基于GNN的归纳式关联聚类框架，训练阶段学习同分布图的通用结构模式与节点特征关联，可直接泛化到未见过的新图实例无需重训，还可作为可学习的pooling模块用于图分类任务。

### 关键结果
归纳场景下推理速度最高提升5个数量级，近似比仅比最优基线低约10%；在传统直推式CC基准上也取得有竞争力的效果；作为GNN pooling层使用时可显著增强模型对图层级结构信息的捕捉能力。
