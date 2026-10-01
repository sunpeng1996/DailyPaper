---
title: 'RouteRec: Behavior-Guided Sparse Routing for Sequential Recommendation'
title_zh: RouteRec：行为引导的稀疏路由序列推荐方法
authors:
- Junyeong Song
- Jaemin Yoo
affiliations:
- Korea Advanced Institute of Science and Technology
- Seoul National University
arxiv_id: '2609.39007'
url: https://arxiv.org/abs/2609.39007
pdf_url: https://arxiv.org/pdf/2609.39007
published: '2026-09-30'
collected: '2026-10-01'
category: RecSys
direction: 序列推荐 · 行为引导MoE稀疏路由
tags:
- Sequential Recommendation
- Mixture of Experts
- Sparse Routing
- Behavioral Cues
- Session-aware
one_liner: 基于四类会话行为特征构建分层稀疏MoE路由，大幅提升序列推荐效果
practical_value: '- 可直接复用四类行为特征（Tempo/Focus/Memory/Popularity）+宏/中/微三时间尺度的特征工程方案，适配电商会话/搜索推荐场景的用户行为建模

  - MoE路由可参考分层设计：先用业务可解释的行为特征选专家组，再用隐藏态选组内专家，平衡可解释性和模型效果

  - 训练时可复用路由一致性正则+z-loss的组合，替代传统负载均衡正则，避免行为依赖的专家分配被强制均衡拉低效果

  - 业务侧缺部分元数据时（如无类目标签/时间戳）可零填充对应特征，模型仍能保持优于基线的性能，落地容错性高'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有序列推荐模型对所有会话采用统一计算路径，无法适配不同会话的行为模式差异；MoE支持输入依赖的条件计算，但现有路由多依赖预定义标签，会话感知推荐场景无此类标签，亟需从原生行为日志中提取无监督的路由信号。

### 方法关键点
- 从会话日志提取四类可解释行为特征：交互节奏Tempo、类目/组集中度Focus、跨/会话内重复度Memory、物品热度倾向Popularity
- 采用三时间尺度路由：宏观（跨用户历史会话）、中观（当前会话前缀）、微观（最近5次交互），匹配不同层级的行为模式
- 分层稀疏路由机制：先用行为特征筛选Top3专家组，每组内结合行为特征+模型隐藏态筛选Top2专家，仅激活选中专家完成计算
- 训练采用路由一致性正则（相似行为会话路由分布接近）+ z-loss（控制路由logit量级稳定），放弃传统负载均衡正则避免破坏行为依赖的专家分配

### 关键结果
覆盖短视频、音乐、电商、POI等6个公开数据集，对比SASRec、DuoRec、FAME等9个主流基线，18个数据集-指标组合中12个排名第一、3个第二，平均排名1.61，较次优基线的4.11提升超60%；LastFM数据集上NDCG@10相对次优基线提升6.0%。

**最值得记住的一句话**：业务可解释的原生行为特征比纯模型隐藏态更适合作为MoE的路由信号，不仅能提升推荐效果，还能对齐业务认知降低落地风险
