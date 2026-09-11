---
title: 'UniRec: Cross-stage Multi-Task Fusion with Preference Alignment for Cascaded
  Recommender Systems'
title_zh: UniRec：级联推荐系统面向偏好对齐的跨阶段多任务融合框架
authors:
- Lingyuan Kong
- Jiaqi Cui
- Fanjiao Zeng
- Congqi Wang
- Yu Li
- Yuan Cheng
- Jingxin Liu
- Xiaoshuang Chen
- Kaiqiao Zhan
affiliations:
- Kuaishou Technology
arxiv_id: '2609.11052'
url: https://arxiv.org/abs/2609.11052
pdf_url: https://arxiv.org/pdf/2609.11052
published: '2026-09-10'
collected: '2026-09-11'
category: RecSys
direction: 级联推荐 · 跨阶段融合与偏好对齐
tags:
- Cascaded-RecSys
- Multi-Task-Fusion
- Preference-Alignment
- Pre-Ranking
- Ranking
- Regularization
one_liner: 联合优化预排序与排序融合模块，解决级联推荐跨阶段偏好不一致问题
practical_value: '- 可直接复用跨阶段联合训练范式：仅共享预排序和排序融合模块的输入embedding，训练时梯度双向流动，推理时拆分为两个独立子图，无额外线上
  latency，适配现有级联推荐架构

  - 多任务偏好聚合trick：将数十个任务的 pairwise 偏好按正负方向聚合为两个双向信号，训练吞吐量提升30.1%，解决内存占用随任务数线性增长的问题

  - 可迁移属性偏置抑制方法：基于GRPO思想实现属性组相对正则AGRR，仅在组内计算优势和策略归一化，避免模型过度偏好高 reward 属性组，同时不影响跨组排序能力

  - 跨阶段对齐优先用偏好序对齐而非分数回归：避免下游分数校准漂移的影响，上线后无需随 backbone 迭代频繁调整对齐逻辑'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业级推荐普遍采用级联架构，各阶段独立优化会导致跨阶段偏好不一致：预排序可能过滤掉排序阶段更偏好的item，下游融合优化也可能抵消上游收益，现有跨阶段方法仅优化上游打分模型，未触及决定候选池的多任务融合模块，难以达成全局最优。
### 方法关键点
- 耦合双Agent架构：预排序、排序融合Agent共享输入embedding，训练时梯度双向流动，推理时拆分为独立子图无额外延迟；预排序用轻量MLP-Mixer适配低延时要求，排序用裁剪版AutoInt建模候选依赖；新增Adapter将预排序输出作为排序特征，切断梯度避免冲突
- 双轴偏好对齐：垂直轴用跨阶段一致性损失将排序的pairwise偏好传递给预排序，仅对齐序而非分数，避免下游分数漂移影响；水平轴将数十个异构任务的pairwise损失聚合为正负双向信号，计算量从O(MN²)降至O(N²)
- 属性组相对正则（AGRR）：按item属性（如视频时长）分桶，仅在桶内计算优势和策略归一化，消除模型整体拉高高reward属性组得分的优化捷径，避免属性分布漂移
### 关键结果
离线在RecFlow公开数据集、快手工业数据集测试，对比Weighted-Sum、EMER、UMRE、COPR等基线，跨阶段一致性指标ASH达0.9978，较最优基线提升1.25%，NDCG@50提升1.4%；线上A/B测试app使用时长提升0.616%，总观看时长提升0.675%，目前已全量部署于快手。
### 核心结论
级联推荐的跨阶段优化核心不止于打分模型对齐，更要联合优化决定候选准入的融合模块，训练阶段的耦合无需增加推理延迟
