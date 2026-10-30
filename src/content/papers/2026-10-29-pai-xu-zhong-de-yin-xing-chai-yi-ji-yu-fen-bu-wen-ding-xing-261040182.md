---
title: 'Hidden Disparities in Ranking: Category-Aware Fairness via Distributional
  Stability'
title_zh: 排序中的隐性差异：基于分布稳定性的类别感知公平性方法
authors:
- Gayane Taturyan
- Charlotte Laclau
- Stephan Clémençon
affiliations:
- LTCI, Télécom Paris
- Institut Polytechnique de Paris
arxiv_id: '2610.40182'
url: https://arxiv.org/abs/2610.40182
pdf_url: https://arxiv.org/pdf/2610.40182
published: '2026-10-29'
collected: '2026-10-30'
category: RecSys
direction: 公平推荐 · 类别感知公平排序
tags:
- FairRanking
- UserSideFairness
- DistributionalStability
- ConditionalUtilityParity
- SOCP
one_liner: 提出基于分布稳定性的类别感知公平排序框架，通过混合策略SOCP优化消除跨品类隐性公平偏差
practical_value: '- 可复用类别感知公平校验逻辑：现有聚合公平指标会掩盖跨品类的反向偏差（如女性在高客单价品类曝光不足、男性在低客单价品类曝光不足，整体抵消看似公平），可在现有推荐
  fairness 评估体系中新增分品类utility parity校验，提前发现隐性歧视。

  - 工程上可快速落地的后处理方案：无需修改现有排序模型训练逻辑，仅需训练少量不同重加权策略的排序基模型，通过SOCP求解混合权重即可实现公平约束，单任务求解耗时<10ms，适合线上实时调整公平-效用
  tradeoff。

  - 跨人群分布变化的鲁棒性设计：当平台用户结构发生变化（如新客群涌入导致性别/年龄占比变动）时，该框架的分布稳定性约束可保证公平性和服务质量不随人群结构波动，无需频繁重新校准公平参数。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有推荐公平性方法大多采用全品类聚合的效用 parity 指标，会掩盖跨品类的隐性偏差（比如女性在管理类岗位、高客单价品类的曝光不足，和男性在行政类岗位、低客单价品类的曝光不足，整体抵消后看似公平，实际存在严重的群体歧视）；同时现有方法缺乏人群结构变化下的公平性鲁棒性保证，当用户群体占比发生变化时，公平性和服务质量会出现大幅波动。

### 方法关键点
- 提出条件效用 parity（CUP）公平指标，要求每个item品类下不同用户群体的归一化效用（对应用户感兴趣item的曝光加权和，等价于NDCG@K）完全相等，避免聚合指标的偏差掩盖问题；
- 将公平性等价为用户群体占比扰动下的效用分布稳定性，通过优化多个不同重加权策略训练的排序基模型的混合权重，将公平约束下的效用最大化问题转化为二阶锥规划（SOCP）求解，可提供有限样本下的公平性、效用、部署鲁棒性理论保证；
- 支持设置各品类的最低效用目标，避免为了实现公平而拉低所有群体的服务质量（levelling down问题）。

### 关键实验
在合成求职推荐数据集和MovieLens-1M数据集上测试，对比ITFR、CatFAIR等SOTA类别公平方法：1）在MovieLens数据集上，CUP可将跨品类的最大性别效用 gap 降低70%以上，仅损失不到10%的整体NDCG@20；2）求解混合权重的SOCP耗时<10ms，远低于基线的全量重新训练耗时（2-38分钟）；3）在用户性别占比在0.1-0.9区间波动时，CUP的效用波动幅度比基线低60%以上。

### 核心结论
聚合公平指标的「平等」本质上是对跨品类隐性歧视的掩盖，品类粒度的公平约束+分布稳定性设计才是实现真实公平、同时适应业务动态变化的核心。
