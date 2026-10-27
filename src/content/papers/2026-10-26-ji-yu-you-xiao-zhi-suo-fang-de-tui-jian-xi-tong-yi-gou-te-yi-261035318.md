---
title: Unified Heterogeneous Feature Interaction via Effective-Rank Scaling for Recommender
  Systems
title_zh: 基于有效秩缩放的推荐系统异构特征统一交互框架
authors:
- Ao Zhang
- Haochuan Li
- Boya Du
- Jian Yang
- Qihang Fang
- Yulin Xu
affiliations:
- Alibaba Group
- Renmin University of China
- Institute of Automation, Chinese Academy of Sciences
arxiv_id: '2610.35318'
url: https://arxiv.org/abs/2610.35318
pdf_url: https://arxiv.org/pdf/2610.35318
published: '2026-10-26'
collected: '2026-10-27'
category: RecSys
direction: 多场景推荐 · 异构特征交互
tags:
- CTR Prediction
- CVR Prediction
- Feature Interaction
- Multi-scenario Recommendation
- Sequence Modeling
one_liner: 提出HiRank多场景推荐框架，统一异构特征与序列交互，淘宝实测单用户订单提升2.27%
practical_value: '- 架构层面可直接复用HiRank的门控序列注意力+异构token头混洗的统一骨架，替代现有DIN+DCNv2的分段处理流程，兼顾双向信息融合与线上性能

  - 多场景适配可借鉴场景感知聚合+复合投影生成高秩组合token的设计，无需拆分场景独立训练即可降低跨场景负迁移

  - 工程优化可直接复用用户-物品计算解耦方案，同请求内共享用户序列、特征计算逻辑，单请求多候选打分时可降低30%+冗余计算

  - 调参可参考缩放实验结论：优先拉长主行为序列长度（48→96可提AUC 0.23pp），其次增加高秩注意力的token宽度/数量，投入产出比更高'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业级多场景推荐排序模型需同时捕获异构特征交互、长序列用户行为、跨场景依赖，现有方案多将序列建模与非序列特征交互拆分，限制双向信息流动；直接用自注意力处理全量token效率低，且共享表征易引发跨场景负迁移，难以平衡效果与线上时延要求。
### 方法关键点
- 统一交互骨架：将主行为序列、长时记忆、语义特征token纳入同一交互层，每层先完成门控序列自注意力+候选-序列交叉注意力，再结合头维度token混洗做异构特征交互，输出更新后的序列状态与检索query，实现双向信息融合
- 互补长时记忆检索：同时输入主序列引导的用户兴趣query、候选引导的query检索多份长时行为记忆，兼顾用户静态兴趣与候选相关的动态兴趣
- 场景适配层：用场景感知query聚合全量token得到紧凑表征，再通过多组独立投影生成高秩组合token做高阶交互，降低跨场景负迁移
- 工程优化：支持用户-物品计算解耦，同请求内共享用户侧计算逻辑，大幅降低多候选打分的冗余计算量
### 关键实验
基于淘宝24亿曝光、2.06亿用户的工业级数据集，对比DCNv2+DIN、RankMixer、OneTrans等SOTA方案：离线首页CVR AUC较最优基线高0.0009，GAUC高0.0186，相对提升RI高0.22%；线上A/B测试淘宝首页单用户订单提升2.27%，GMV提升2.86%，日下单用户数提升2.13%。
### 核心结论
推荐大模型缩放的核心是在不损失表征有效秩的前提下实现异构信息融合，优先拉长行为序列的投入产出比高于加宽加深模型
