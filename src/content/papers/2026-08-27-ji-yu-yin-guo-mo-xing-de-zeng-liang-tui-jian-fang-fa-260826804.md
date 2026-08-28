---
title: Incremental Recommendation via Causal Models
title_zh: 基于因果模型的增量推荐方法
authors:
- Athanasios Vlontzos
- David Gustafsson
- Michael O'Riordan
- Ciarán M. Gilligan-Lee
affiliations:
- Hologen
- Imperial College London
- Spotify
- University College London
arxiv_id: '2608.26804'
url: https://arxiv.org/abs/2608.26804
pdf_url: https://arxiv.org/pdf/2608.26804
published: '2026-08-27'
collected: '2026-08-28'
category: RecSys
direction: 因果推荐 · 增量效率优化
tags:
- CausalRec
- UpliftModel
- IncrementalRecommendation
- ProductionRecSys
- ABTesting
one_liner: 利用现有holdback数据改造生产推荐模型，解决归因窗口不匹配问题，削减7%无效曝光且不影响内容消费
practical_value: '- 现有生产多任务模型改因果架构无需新增数据采集，直接复用已收集的holdback实验数据，仅新增一个holdback头用分区损失训练即可，改造成本极低

  - 遇到实验组与对照组归因窗口不一致的场景，无需强行计算p1-p0作为CATE，直接采用双阈值策略（p1≥θ1且p0≤θ0）做过滤，逻辑简单可解释，阈值可根据业务曝光-消费tradeoff灵活调优

  - 共享trunk同时用实验组和holdback数据训练，可提升原有转化预测头的校准度，对依赖阈值调优的推荐/广告策略增益明显

  - 电商大促/信息流广告场景可直接复用这套逻辑，过滤掉本来就会下单/点击的“总是转化者”，节省的曝光/预算可用于拉新或拓展潜在用户，提升资源ROI'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
推荐曝光是稀缺资源，现有推荐模型优化点击/转化率目标，会将大量曝光分配给即使不推荐也会消费的「always-taker」用户，造成资源浪费。生产系统普遍收集的holdback实验数据很少被用于因果建模，核心障碍是实验组与对照组的归因窗口不匹配：实验组用短窗口归因推荐带来的转化，对照组用长窗口统计自然转化，二者直接相减计算CATE完全无效。

### 方法关键点
- 对现有共享trunk的多任务生产模型做最小改造，新增holdback头，分别预测p1（下发推荐后的转化概率）和p0（不下发推荐的自然转化概率）
- 采用分区损失训练：实验组样本仅更新p1头和共享trunk，holdback样本仅更新p0头和共享trunk，避免两类不同归因规则的标签互相干扰
- 放弃无效的CATE差值计算，采用双阈值决策规则：仅当p1高于阈值（推荐后转化概率足够高）且p0低于阈值（自然转化概率足够低）时才下发推荐，可通过阈值灵活调控效率与reach的平衡

### 关键实验结果
在Spotify首页推荐场景开展千万级用户线上A/B测试，对比基线为仅用p1排序的生产模型：双阈值策略实现推荐曝光下降7.1%，推荐内容消费仅下降0.37%且统计不显著，同时p1头的校准度相比基线明显提升，高预测分区间的校准误差显著降低。

### 核心结论
生产场景落地因果推荐不需要追求学术上完美的CATE估计，结合业务实际约束设计简单可解释的决策规则，往往能以极低的改造成本拿到明确的业务收益。
