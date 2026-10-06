---
title: 'To Learn is to Wander: Learning Across Graphs and Tasks with Random Walks'
title_zh: 《学习即游走：基于随机游走的跨图跨任务图基础模型》
authors:
- Louis Tichelman
- Xingyue Huang
- Jinwoo Kim
- İsmail İlkan Ceylan
affiliations:
- TU Wien
- AITHYRA
- University of Oxford
- KAIST
arxiv_id: '2610.06694'
url: https://arxiv.org/abs/2610.06694
pdf_url: https://arxiv.org/pdf/2610.06694
published: '2026-10-05'
collected: '2026-10-06'
category: Training
direction: 图基础模型 · 跨图跨任务预训练
tags:
- Graph Foundation Model
- Random Walk
- Cross-graph Transfer
- Cross-task Learning
- Pre-training
one_liner: 提出基于随机游走统一接口的图基础模型Wander，单预训练checkpoint跨多图模态与任务达SOTA级效果
practical_value: '- 可复用随机游走统一接口思路，适配电商推荐场景下用户行为图、商品关联图、知识图谱等多模态图数据的统一建模，降低多图任务的模型维护成本

  - 推理时无需调整参数即可扩展结构上下文的设计，可迁移到推荐冷启动场景，无需重训模型即可适配新增用户/商品的图结构特征

  - 跨任务联合预训练保留专项性能同时实现正向迁移的结论，可用于商品召回、用户兴趣预测、关联推荐等多任务联合训练的框架设计'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有图基础模型仅能在特定图模态或任务内泛化，无法支撑跨图、跨特征空间、跨关系schema、跨预测任务的通用建模需求，需为每类任务/图训练单独模型，开发与维护成本高。
### 方法关键点
1. 从先验预测视角将图学习定义为部分观测图补全任务，基于随机游走设计统一接口，支持同构图、多关系图等不同结构、特征、标签、关系schema的图输入；
2. 推理时无需修改已学习参数即可扩展结构上下文，理论上可在有界连通图上通用逼近贝叶斯最优预测器。
### 关键结果
单预训练checkpoint在节点分类、同构链接预测、知识图谱链接预测三类任务上均达到SOTA或极具竞争力的性能；跨图模态与任务的联合预训练在保留专项场景性能的同时，实现推理时的正向迁移与独立学习能力的组合。
