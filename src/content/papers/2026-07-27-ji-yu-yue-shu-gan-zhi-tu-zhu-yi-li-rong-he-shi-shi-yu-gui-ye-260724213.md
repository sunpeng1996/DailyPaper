---
title: Integrating Factual and Normative Industrial Knowledge via Constraint-Aware
  Graph Attention for Process Plan Recommendation
title_zh: 基于约束感知图注意力融合事实与规范工业知识的工艺方案推荐
authors:
- Yuntong Chen
- Yingqi Li
- Yingying Xiao
- Ziang Wang
- Zewei Liu
- Jiahao Liu
- Xitian Tian
- Lijiang Huang
affiliations:
- School of Mechanical Engineering, Northwestern Polytechnical University
- State Key Laboratory of Complex Product Intelligent Manufacturing System Technology,
  Beijing Institute of Electronic System Engineering
arxiv_id: '2607.24213'
url: https://arxiv.org/abs/2607.24213
pdf_url: https://arxiv.org/pdf/2607.24213
published: '2026-07-27'
collected: '2026-07-29'
category: RecSys
direction: 工业场景推荐 · 约束感知图注意力
tags:
- Graph Attention Network
- Knowledge Graph
- Collaborative Filtering
- Bayesian Personalized Ranking
- Cold Start
- Industrial Recommendation
one_liner: PCA-GAT框架融合知识图谱与领域约束注意力实现高鲁棒高精度工业工艺方案推荐
practical_value: '- 多规则约束推荐场景可借鉴「可学习约束偏置+自适应门控」的注入方式，替代硬约束截断，避免规则对推荐效果的负向影响，适合电商合规推荐、广告准入、商品属性适配等场景

  - 低交互稀疏/冷启动场景可复用KG增强协同过滤+BPR排序目标的范式，用KG补充语义信号，适配新品推荐、小众品类推荐等业务场景

  - 多维度约束重要性自动学习的思路可直接迁移，无需人工预设不同规则的权重，降低运营调优成本'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
工业信息系统融合事实关联、决策约束两类异质知识难度大，现有工艺方案推荐依赖相似检索或分类，无统一排序目标与标准评估体系，稀疏冷启动场景表现差。
### 方法关键点
1. PCA-GAT框架将工艺方案推荐建模为KG增强的协同过滤问题，采用BPR作为排序学习目标，Recall@K、NDCG@K作为标准化评估指标
2. 图传播阶段将材料兼容、精度要求、特征适用、工序顺序4类领域约束作为注意力偏置注入，通过类别专属权重自动学习约束重要性，搭配自适应门控基于局部上下文调整约束影响
### 关键结果
- 航空航天真实数据集（115个零件、507个方案）上Recall@1达0.9087，严重稀疏下冷启动性能退化仅为最强基线的1/2
- 消融验证KG增强为必选模块，无门控的原始约束注入会损害性能；无约束场景下无性能下降，泛化性良好
