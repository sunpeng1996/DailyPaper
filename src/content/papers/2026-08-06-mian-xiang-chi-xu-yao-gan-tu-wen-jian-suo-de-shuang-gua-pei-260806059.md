---
title: 'DARAD: Dual Adapters and Ranking-Aware Distillation for Continual Remote Sensing
  Image-Text Retrieval'
title_zh: 面向持续遥感图文检索的双适配器与排序感知蒸馏框架
authors:
- Xi Chen
- Xu Chen
- Xiangyang Jia
- Wei Wang
- Xu Zhang
- Zhenyuan Sun
affiliations:
- School of Computer Science, Wuhan University
- Beijing Institute for General Artificial Intelligence (BIGAI)
arxiv_id: '2608.06059'
url: https://arxiv.org/abs/2608.06059
pdf_url: https://arxiv.org/pdf/2608.06059
published: '2026-08-06'
collected: '2026-08-09'
category: Other
direction: 持续跨模态检索 · 蒸馏与适配优化
tags:
- Continual Learning
- Cross-Modal Retrieval
- Adapter
- Knowledge Distillation
- Multi-Expert Routing
one_liner: 提出双适配器+排序感知蒸馏框架，解决持续跨模态检索的对齐空间扭曲问题
practical_value: '- 跨模态持续更新场景可复用双Adapter架构：视觉侧用粗细粒度特征融合Adapter适配尺度变化，文本侧用MoE路由拆分通用/专属语义，减少旧任务效果退化

  - 跨模态检索的持续学习可引入双向排序蒸馏：用冻结教师模型+历史锚点保留历史跨模态排序结构，缓解对齐空间漂移，不需要全量重训旧数据

  - 多模态大模型微调适配下游跨模态检索任务时，可借鉴语义拆分路由的思路，控制全局embedding漂移，降低新旧数据冲突'
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
持续遥感图文检索场景下，遥感数据尺度差异大、分布偏移问题突出，现有持续学习方法易引发跨模态对齐空间扭曲，无法同时兼顾新数据适配与历史检索效果保留。

### 方法关键点
1. 视觉分支引入空间融合Adapter，融合粗区域特征与细粒度patch特征适配尺度变化，锚定视觉更新不偏移预训练对齐空间；
2. 文本分支采用多专家语义路由，拆分通用文本语义与专属语义残差，吸收新出现的描述的同时约束全局文本embedding漂移；
3. 双向排序蒸馏模块基于冻结教师模型与历史锚点保留历史跨模态排序结构，缓解跨阶段对齐空间扭曲。

### 关键结果
多阶段持续检索实验验证，DARAD性能显著优于现有持续学习方法，新数据适配能力提升的同时，历史数据检索效果无明显退化。
