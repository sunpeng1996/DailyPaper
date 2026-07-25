---
title: Semantic-Aware Task Clustering for Constructive and Cooperative Multi-Tasking
title_zh: 面向建设性协作多任务的语义感知任务聚类方法
authors:
- Ahmad Halimi Razlighi
- Maximilian H. V. Tillmann
- Edgar Beck
- Bho Matthiesen
- Armin Dekorsy
affiliations:
- University of Bremen, Germany
- Paderborn University, Germany
arxiv_id: '2607.21426'
url: https://arxiv.org/abs/2607.21426
pdf_url: https://arxiv.org/pdf/2607.21426
published: '2026-07-23'
collected: '2026-07-25'
category: Training
direction: 多任务训练 · 语义感知任务聚类
tags:
- Multi-Task Learning
- Task Clustering
- HDBSCAN
- Semantic Alignment
- Negative Transfer
one_liner: 提出语义感知任务聚类方案，消除多任务学习负迁移，提升联合训练精度
practical_value: '- 推荐系统多目标训练可借鉴该范式：先做短周期预训得到各目标任务语义表征，用HDBSCAN聚类后仅同簇目标联合训练，避免负迁移

  - 电商大模型多下游场景微调可复用该流程：对不同品类、不同业务场景的微调任务做语义聚类，同簇任务联合微调降低训练成本的同时提升效果

  - Agent多工具调用的多任务训练可参考该思路：按任务语义相似度分簇训练，避免低关联任务之间的干扰，提升工具调用准确率'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
协作多任务训练依靠跨任务共享表征降低计算冗余、提升整体性能，但任务语义关联度低时会出现破坏性协作、负迁移问题，反而劣化任务执行效果。
### 方法关键点
1. 采用两阶段优化流程，先经过短周期初始训练得到各任务的语义表征
2. 基于HDBSCAN分层密度空间聚类算法对语义对齐的任务做自动分簇
3. 后续仅在同簇任务内部开展端到端联合训练，完全隔离跨簇任务的参数共享路径
### 关键结果
仿真实验验证该框架可完全消除破坏性协作与负迁移问题，相比无聚类全量多任务训练、单任务独立训练两个基线，均取得稳定的准确率提升
