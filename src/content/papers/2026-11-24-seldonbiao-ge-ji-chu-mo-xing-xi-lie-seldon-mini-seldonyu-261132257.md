---
title: 'Seldon TFM family: Seldon-Mini, Seldon and Seldon+'
title_zh: Seldon表格基础模型系列：Seldon-Mini、Seldon与Seldon+
authors:
- Stanislas Angebault
- Nicolas Atienza
- Nicola Cancedda
- Aziz Fouché
- Salomé Gobbi
- Ekaterina Iakovleva
- Nicolas Makaroff
- Arthur Nahmias
- Paul Novello
- Alexandre Pasquiou
affiliations:
- Neuralk-AI Research Team
arxiv_id: '2611.32257'
url: https://arxiv.org/abs/2611.32257
pdf_url: https://arxiv.org/pdf/2611.32257
published: '2026-11-24'
collected: '2026-11-25'
category: Training
direction: 表格基础模型 · 合成数据预训练
tags:
- Tabular Foundation Model
- Synthetic Pre-training
- Pareto Optimization
- Classification
- Regression
one_liner: 推出仅用合成表训练的Seldon系列表格基础模型，多基准性能领先，大小版均处速度精度帕累托前沿
practical_value: '- 可直接引入开源Seldon-Mini/Seldon替代电商推荐/广告场景的XGBoost类CTR预估/排序模型，省去单场景调参成本，兼顾推理速度与精度

  - 纯合成表预训练范式可复用，针对电商用户/商品/行为类表格特征生成专属合成数据预训练领域TFM，降低真实敏感数据依赖

  - 精度-推理速度帕累托最优的选型思路可借鉴，业务上线时可根据算力配额在Seldon系列中选择适配的模型规格'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
传统梯度提升树（XGBoost、CatBoost等）是表格数据建模的主流方案，但每个新业务场景都需要单独训练、调参，落地效率低；表格基础模型（TFM）无需场景级训练即可直接推理，是降本提效的关键路径。
### 方法关键点
推出3款Seldon系列TFM：27M参数的Seldon-Mini、213M参数的Seldon开源，仅用合成表预训练，同时支持分类、回归任务，架构对齐现有主流TFM方案；闭源Seldon+为分类专用版。
### 关键结果数字
- Seldon+在124个数据集的TabBench分类榜、含缺失值变体榜、BeyondArena IID分类榜、TabBench-Bio榜均排第1，TabArena分类榜排第2
- 开源版Seldon、Seldon-Mini均处于TabArena Elo精度-推理时间帕累托最优前沿，109个参赛模型中分别排第4、第7；BeyondArena IID分类榜42个参赛模型中Seldon排第2
