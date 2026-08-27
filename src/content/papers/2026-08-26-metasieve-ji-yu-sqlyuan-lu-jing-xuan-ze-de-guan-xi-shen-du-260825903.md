---
title: 'MetaSieve: Faster Relational Deep Learning through SQL-Based Metapath Selection'
title_zh: MetaSieve：基于SQL元路径选择的关系深度学习加速方法
authors:
- Fahim Shahriar Khan
- Ashraf Aboulnaga
affiliations:
- University of Texas at Arlington
arxiv_id: '2608.25903'
url: https://arxiv.org/abs/2608.25903
pdf_url: https://arxiv.org/pdf/2608.25903
published: '2026-08-26'
collected: '2026-08-27'
category: Training
direction: GNN训练加速 · 元路径剪枝优化
tags:
- Metapath Pruning
- GNN Training
- Relational Deep Learning
- SQL Optimization
- Subgraph Sampling
one_liner: 通过SQL统计驱动的轻量元路径剪枝，大幅降低RDL场景GNN训练耗时且精度不降反升
practical_value: '- 在基于多表用户行为、商品属性数据构建GNN做召回/用户建模时，可复用MetaSieve的元路径剪枝逻辑，用SQL统计先筛掉无效关联路径，降低子图采样开销

  - 优先选择轻量高信息增益路径的评分函数思路，可迁移到召回/排序阶段的特征选择流程，减少无效特征的计算成本

  - 无需依赖GNN参数的离线预剪枝逻辑，可直接对接现有数仓的SQL能力，无需改动原有GNN模型架构即可落地降本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
关系深度学习（RDL）将多表业务数据库映射为异构图训练GNN时，子图采样开销占训练成本的核心比例，大量由外键关联生成的元路径无实际信息增益，却显著增加计算负载。
### 方法关键点
1. 新增独立于GNN参数的MetaSieve元路径选择层，仅依赖数仓统计数据与任务标签即可运行，兼容任意GNN架构，适配分类、回归等多类任务；
2. 对候选元路径扩展通过SQL执行join、聚合计算统计量，采用偏好轻量、高信息增益的自定义评分函数评估，得分低于阈值的路径直接剪枝。
### 关键结果
在RelBench基准的多类GNN backbone上测试，单epoch训练耗时大幅下降，同时模型精度保持甚至优于未剪枝的原生模型。
