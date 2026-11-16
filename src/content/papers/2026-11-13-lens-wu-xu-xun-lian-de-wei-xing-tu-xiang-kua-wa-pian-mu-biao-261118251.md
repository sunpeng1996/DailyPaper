---
title: 'Lens: Training-Free Semantic Search for Cross-Tile Object and Scene Retrieval
  in Satellite Imagery'
title_zh: Lens：无需训练的卫星图像跨瓦片目标与场景语义检索系统
authors:
- Ata Akbari Asanjan
- Anit Upadhyaya
- Jeremy Kravitz
- Subash Yeggina
affiliations:
- Pixxel Space Technologies
- Pixxel Space India Pvt Ltd
arxiv_id: '2611.18251'
url: https://arxiv.org/abs/2611.18251
pdf_url: https://arxiv.org/pdf/2611.18251
published: '2026-11-13'
collected: '2026-11-16'
category: Other
direction: 图像语义检索 · 无训练特征优化
tags:
- Semantic Search
- Training-free
- Feature Debiasing
- DINOv3
- Vector Index
- Cache
one_liner: 提出无训练Lens语义检索系统，通过ViT特征去偏实现卫星图像跨瓦片低延迟目标与场景检索
practical_value: '- 特征去偏trick可复用：通过固定图像预计算位置基、特征投影到正交子空间的方案，可消除商品图/内容特征的构图、位置偏差，提升多模态检索精度

  - 两级索引架构可直接迁移：字节量化细粒度索引+粗粒度全局索引的方案，适配大规模商品/内容语义检索的低延迟部署需求

  - 预计算缓存机制可复用：提前计算瓦片级上采样结果并缓存的思路，可用于推荐系统高频用户/物品Embedding预计算，降低查询latency

  - 零训练部署思路适用垂类场景：冻结预训练大模型+特征后处理的方案，可快速上线小众垂类检索需求，避免小样本训练成本过高问题'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
卫星影像规模爆发式增长，传统检索方案需针对目标类别单独训练检测器，部署成本高、泛化性差，无法满足灵活跨瓦片检索需求。
### 方法关键点
1. 用冻结的DINOv3提取瓦片特征，通过投影到固定图像预计算的位置基正交子空间消除位置偏差，再基于全区域特征均值中心化；
2. 构建两级量化索引：细粒度字节量化patch特征索引支持实时范围检索，粗粒度全瓦片嵌入索引支持场景级检索；
3. 预跑AnyUp上采样网络得到单瓦片像素级边界并缓存，降低重复查询开销；
4. 查询时取选点邻域或全瓦片平均特征，通过余弦相似度匹配。
### 关键结果
在DFC2020 5128瓦片测试集上，单点击查询8类地物平均F1达0.39，6类效果优于INSID3基线，查询成本仅为基线的1/400；单CPU线程索引131万patch仅需169s，单点击查询返回延迟6~10ms。
