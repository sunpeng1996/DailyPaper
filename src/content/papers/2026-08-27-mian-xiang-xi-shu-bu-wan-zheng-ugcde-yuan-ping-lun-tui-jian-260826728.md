---
title: 'Beyond a Single Story: Meta-Reviewing Sparse and Incomplete User-generated
  Contents for Recommendation'
title_zh: 面向稀疏不完整UGC的元评论推荐框架MOSAIC
authors:
- Hongren Wang
- Tianjun Wei
- Yingpeng Du
- Jie Zhang
- Yin-Leng Theng
affiliations:
- Nanyang Technological University, Singapore
- City University of Hong Kong
arxiv_id: '2608.26728'
url: https://arxiv.org/abs/2608.26728
pdf_url: https://arxiv.org/pdf/2608.26728
published: '2026-08-27'
collected: '2026-08-28'
category: RecSys
direction: 基于UGC的可解释推荐 · 多任务学习
tags:
- Review-based Recommendation
- Multi-task Learning
- MMoE
- UGC Sparsity
- Explainable Recommendation
one_liner: 聚合邻居用户属性-情感对构建元评论，结合MMoE多任务学习提升推荐准确率与可解释性
practical_value: '- UGC冷启场景可复用元评论构建逻辑：离线用LLM抽取领域属性-情感对，聚合10-15个同物品交互邻居的属性级信号，可将属性覆盖率从单评论的<50%提升至80%+，无需依赖用户自身评论数据

  - 多任务架构可直接复用：采用3个专家的MMoE联合优化评分预测与属性-情感预测任务，避免任务负迁移，比单任务模型在稀疏用户群MAE最高下降30%

  - 可解释性落地可参考：通过个性化注意力模块对齐元评论属性与用户偏好，直接输出属性级情感解释，避免LLM生成解释的hallucination问题，无需额外解释生成模块

  - 可扩展冷启适配：新品/新用户场景可将邻居选择逻辑从同物品交互扩展到同偏好人群，进一步提升冷启效果'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
推荐系统中UGC（如评论）可捕捉细粒度用户偏好，但天然存在两大痛点：一是完全缺失（有交互无评论），二是内容不完整（单条评论仅覆盖部分属性，实验显示单评论的属性覆盖率不足50%），现有方法仅依赖单用户自身评论，无法补全缺失的属性信号，冷启用户效果尤其差。

### 方法关键点
1. 离线预处理：用LLM从评论中抽取预定义领域属性的属性-情感对，再经BERT分类为4类情感（正负/轻微正负），LLM仅做离线抽取不参与训练推理，无额外线上开销；
2. 元评论构建：对目标用户-物品对，随机采样10-15个同物品交互的邻居用户，通过均值池化和多数投票聚合得到属性级元评论，属性覆盖率可提升至80%+；
3. 多任务框架：采用3个专家的MMoE联合优化评分预测、元评论属性-情感预测两个任务，通过任务专属门控避免负迁移；
4. 个性化校准：增加注意力模块，以目标用户特征为query筛选元评论中的相关属性，校准评分预测同时输出属性级解释。

### 关键结果
在Yelp、TripAdvisor、Amazon Beauty/Sports四个公开数据集上，相比SOTA基线，RMSE最高下降13.6%，MAE最高下降19.7%；稀疏用户（≤1条交互）上MAE最高下降30.38%，属性-情感预测F1最高提升45.2%。

最值得记住的一句话：基于真实用户反馈的属性级聚合，比单用户的孤立评论或LLM生成的辅助内容，更能可靠地缓解UGC稀疏问题，同时兼顾可解释性。
