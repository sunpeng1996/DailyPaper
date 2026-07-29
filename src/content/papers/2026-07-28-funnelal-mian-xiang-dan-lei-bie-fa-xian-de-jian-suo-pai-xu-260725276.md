---
title: 'FunnelAL: Retrieve-then-Rank Active Learning for Single-Class Discovery'
title_zh: FunnelAL：面向单类别发现的检索排序主动学习框架
authors:
- Reihaneh Rostami
- Brian Goodwin
affiliations:
- RAIC Labs, USA
arxiv_id: '2607.25276'
url: https://arxiv.org/abs/2607.25276
pdf_url: https://arxiv.org/pdf/2607.25276
published: '2026-07-28'
collected: '2026-07-29'
category: RecSys
direction: 推荐架构适配 · 主动学习样本筛选
tags:
- Active Learning
- Retrieve-then-Rank
- Data Annotation
- Single-Class Discovery
- Funnel Architecture
one_liner: 将工业推荐多阶段漏斗架构适配到主动学习，提升单类别发现的标注效率与抗噪性
practical_value: '- 可借鉴多阶段漏斗思路重构业务困难样本挖掘流程，比如广告/推荐的负例采样、冷门品类样本标注，大幅降低标注成本

  - 排序阶段的精度触发切换策略可复用：高召回阶段用RankNet排序，效率下降后自动混入QBC探索，平衡精准度与覆盖度，适合冷启动场景的样本筛选

  - 抗标注噪声的设计思路可迁移到存在用户反馈噪声的推荐场景，比如用户点击/收藏误操作时，降低噪声对排序模型的影响'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
大规模监督学习标注成本高，现有单阶段主动学习既无法高效从海量语料中定位相关样本，也难以区分embedding空间重叠的难分正负例，标注效率低、抗噪性差。
### 方法关键点
借鉴工业推荐系统的多阶段漏斗架构，设计三级级联流程：1）基于embedding检索从全量语料缩容得到小规模候选集；2）排序阶段采用精度触发机制：批次精度高时用RankNet做精准排序，收益下降后自动混入委员会查询（QBC）做探索；3）用标注员反馈迭代优化前两个阶段的模型效果。
### 关键结果
3个图像分类基准测试中，完美标注场景下F1、标注效率（AULC）、标注轮数均为最优，现有SOTA（GAL、PF-MA）需更高标注成本才能追平效果；存在真实标注噪声时，性能保持Top1，传统不确定性方法的性能下降速度是其2~3倍。
