---
title: 'DICS: Data-Informed Centroid Splitting for Decision Tree Classifiers'
title_zh: DICS：面向决策树分类器的数据驱动质心分裂方法
authors:
- MD Saifur Rahman Mazumder
- Feng Yu
affiliations:
- University of Texas at El Paso
- Department of Mathematical Sciences, University of Texas at El Paso
arxiv_id: '2608.20258'
url: https://arxiv.org/abs/2608.20258
pdf_url: https://arxiv.org/pdf/2608.20258
published: '2026-08-20'
collected: '2026-08-21'
category: Training
direction: 决策树类模型训练效率优化
tags:
- Decision Tree
- Training Efficiency
- Random Forest
- Gradient Boosting
- Classification
one_liner: 提出基于类感知聚类的决策树分裂策略，精度无损下大幅降低树类模型训练耗时
practical_value: '- 可将DICS替换现有GBDT/随机森林的分裂策略，在CTR/CVR预估等排序任务中不损失精度的前提下降低离线训练耗时，提速迭代效率

  - 针对电商高维稀疏特征的树模型训练场景，可复用DICS类感知聚类剪枝搜索空间的思路，减少高维特征下的分裂点遍历开销

  - 理论保证精度无损的特性，适合直接落地到对效果稳定性要求高的广告/推荐排序链路，无需额外设计效果兜底策略'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：决策树及RF、GBDT等集成模型是推荐广告排序的主流基础模型，但高维大数据场景下，每个节点遍历所有候选分裂点的穷举策略训练开销极高，是大规模训练的核心瓶颈之一。

**方法关键点**：提出DICS聚类驱动框架，引入类感知结构生成数据驱动的先验候选分裂点，大幅压缩分裂搜索空间；可无缝嵌入决策树、随机森林、梯度提升树等主流树类模型，理论证明符合假设时分类效果不劣于穷举分裂策略。

**关键结果**：在多类合成数据集及公开基准数据集上，DICS取得与穷举分裂相当的分类精度，同时训练耗时实现显著下降。
