---
title: 'FINALLY: A Dataset Recommender System for Recommender-Systems Research'
title_zh: FINALLY：面向推荐系统研究的数据集推荐系统
authors:
- Louis Owie
affiliations:
- University of Siegen
- Intelligent Systems Group
- Faculty of Science and Technology
arxiv_id: '2609.08941'
url: https://arxiv.org/abs/2609.08941
pdf_url: https://arxiv.org/pdf/2609.08941
published: '2026-09-08'
collected: '2026-09-10'
category: RecSys
direction: 推荐系统 · 科研数据集推荐
tags:
- Dataset Recommendation
- RecSys Evaluation
- Offline Evaluation
- Configurable Recommendation
- Diversity Optimization
one_liner: 面向推荐系统研究场景，推出支持多约束配置的数据集推荐工具FINALLY
practical_value: '- 做约束型集合推荐（如凑单商品组合、营销资源包推荐）可复用「硬约束过滤+集合级目标优化」两级架构，先筛符合规则的候选池再做组合优化

  - 集合推荐的多样性/同质化目标实现，可直接适配本工作的Effective Covariance、Convex Hull两种目标函数，无需从零设计

  - 开发配置化推荐工具时，可参考多维度配置项设计（必填项、候选池限制、数量约束、优化目标开关）覆盖用户个性化需求'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
推荐系统离线评估的数据集选择需同时满足实验约束和集合级选择目标，现有工具缺乏对符合要求的完整数据集组合的构建支持。
### 方法关键点
FINALLY是网页端数据集推荐工具，支持必填数据集指定、候选池限制、元数据过滤、目标集大小配置，内置3类选择策略：随机选择、基于Effective Covariance和Convex Hull目标的多样化/非多样化选择策略。
### 关键结果
10组不同配置下共420次推荐运行，生成的数据集集100%满足大小、去重、必填项、元数据过滤等约束；40组确定性策略-配置组合全部可复现；多样化策略得分全部高于对应配置下的随机结果，非多样化策略得分全部低于随机结果，符合优化预期
