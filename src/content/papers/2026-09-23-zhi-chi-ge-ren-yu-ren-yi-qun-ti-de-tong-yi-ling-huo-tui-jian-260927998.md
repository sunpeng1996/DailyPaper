---
title: A Flexible Recommendation System for Individuals and Groups
title_zh: 支持个人与任意群体的统一灵活推荐系统
authors:
- Yacine Mokhtari
- Grégory Smits
affiliations:
- IMT Atlantique - Lab-STICC, UMR CNRS 6285
- Intescia Group
arxiv_id: '2609.27998'
url: https://arxiv.org/abs/2609.27998
pdf_url: https://arxiv.org/pdf/2609.27998
published: '2026-09-23'
collected: '2026-09-24'
category: RecSys
direction: 群体推荐 · 双用户表征自适应聚合
tags:
- Group Recommendation
- GAT
- Knowledge Graph
- User Profiling
- Preference Aggregation
one_liner: 基于GNN学习用户个人/群体双偏好表征，自适应聚合实现个人与任意群体的统一推荐
practical_value: '- 可复用双偏好建模思路，针对家庭组队、好友拼单等场景，分别学习用户单独消费、群体消费的表征，提升群体推荐效果

  - 自适应聚合策略可直接迁移：根据用户群体场景的偏好偏移度、互动多样性划分用户类型，优先满足非自适应用户偏好，再用自适应用户偏好重排，平衡群体满意度

  - 双表征结构天然支持个人、已知/未知群体的统一推荐，无需维护多套模型，降低工程维护成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有群体推荐分为两类：将群体作为元用户建模的PGR泛化性差，无法适配未见过的新群体；直接聚合个体偏好的OGR忽略用户在群体场景下的偏好偏移（如陪孩子看片放弃自身偏好、跟随专家选择等），且需要分别维护个人、群体两套推荐模型，灵活性不足。

### 方法关键点
1. 基于KG+GAT架构，为每个用户学习两套表征：单独消费的个体偏好表征、群体场景下的成员偏好表征，用调制向量实现非线性转换
2. 定义双维度用户画像：对偶度（个人与群体表征的余弦相似度差值，衡量偏好偏移程度）、多样性（群体场景下互动物品的平均相似度差值，衡量互动内容离散度），将用户划分为自适应（AU）、恒定（CU）、双型（DU）三类
3. 基于群体成员构成采用双极聚合策略：优先用最小痛苦策略聚合非自适应用户（CU/DU）偏好筛选候选集，再用平均策略聚合自适应用户偏好重排

### 关键实验
基于MovieLens-KG生成三类不同群体交互量的数据集，对比KGAT系列、KGAG等SOTA基线：
- 个人推荐HR@20最高提升1.5%，NDCG@20最高提升5.2%
- 未知群体推荐HR@20最高达0.883，比OGR最优基线提升9.2%，NDCG@20最高达0.178，提升2.3%
- 已知群体推荐性能接近针对群体建模的PGR基线，同时具备PGR不具备的未知群体适配能力

### 最值得记住的一句话
用户在个人、群体场景下的偏好并非完全一致，区分建模+自适应聚合是实现统一灵活推荐的核心
