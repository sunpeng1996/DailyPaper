---
title: 'From Shared Patterns to Individual Evidence: Two-Stage Reasoning for Emerging
  Entities in Temporal Knowledge Graphs'
title_zh: 融合共享模式与个体证据的时序知识图谱新兴实体两阶段推理
authors:
- Jinchuan Zhang
- Lei Gao
- Hongyu Jiang
- Chong Mu
- Chenang Cai
- Ke Yan
affiliations:
- School of Computer Science and Engineering, University of Electronic Science and
  Technology of China
arxiv_id: '2611.34708'
url: https://arxiv.org/abs/2611.34708
pdf_url: https://arxiv.org/pdf/2611.34708
published: '2026-11-25'
collected: '2026-11-27'
category: Reasoning
direction: 时序知识图谱 · 新兴实体推理
tags:
- Temporal Knowledge Graph
- Few-shot Learning
- Knowledge Reasoning
- Two-stage Framework
- Emerging Entity
- Adapter
one_liner: 两阶段INSPIRE框架可显著提升时序知识图谱新兴实体的预测推理性能
practical_value: '- 两阶段训练范式可直接迁移到电商新品/新用户冷启动场景：先训全量数据的通用推荐模型，再用轻量Adapter适配新实体的少样本数据，避免全量重训成本

  - 轻量EA模块的「语义先验+长程关联统计+去偏监督」设计，可优化冷启动排序中老实体对新实体的挤压问题，提升新品推荐效果

  - 按角色拆分评估、纵向追踪新兴实体队列指标的评估方法，可复用为电商新品/新内容冷启动效果的专属评估体系'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
时序知识图谱（TKG）持续引入新兴实体，其交互从零样本初现逐步演变为稀疏爆发的少样本轨迹，现有方案存在三类缺陷：模式迁移方法缺乏全库事件记忆，在线记忆模型存在端点角色不对称问题导致新答案排序效果差，稀疏早期交互长程分散且局部冗余。
### 方法关键点
两阶段INSPIRE框架设计：阶段一训练感知可用性的共享模式预测器，融合全候选库的事件更新记忆，同时应用查询侧与库侧协同掩码；阶段二冻结预测器，优化轻量个体证据Adapter，融合文本语义先验与关联加权长程事件统计，采用支持/角色均衡的联合答案监督，搭配先验赔率去偏和软残差对齐。
### 关键结果
在ICEWS、GDELT共4个基准数据集上，较最优基线Emerging MRR提升16.73%~88.83%；相比单阶段预测器，EA模块额外带来Emerging MRR提升8.28%~32.63%，Answer-new MRR提升7.81%~41.24%，队列宏观MRR提升9.64%~39.94%
