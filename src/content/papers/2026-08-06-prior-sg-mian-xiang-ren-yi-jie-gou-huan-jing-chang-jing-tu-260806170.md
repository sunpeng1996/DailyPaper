---
title: 'Prior-SG: Task and Prior Driven Region Segmentation for Scene Graphs in Arbitrarily-Structured
  Environments'
title_zh: Prior-SG：面向任意结构环境场景图的任务与先验驱动区域分割
authors:
- Giorgio Tonetti
- Laurent Kneip
- Abel Gawel
- Marco Hutter
arxiv_id: '2608.06170'
url: https://arxiv.org/abs/2608.06170
pdf_url: https://arxiv.org/pdf/2608.06170
published: '2026-08-06'
collected: '2026-08-09'
category: Agent
direction: Agent空间感知 · LLM驱动场景图生成
tags:
- Scene Graph
- LLM
- Open Vocabulary
- Semantic Segmentation
- Zero-shot
one_liner: 提出融合LLM动态先验的Prior-SG框架，实现任意结构环境下SOTA语义区域分割与零样本任务适配
practical_value: '- 借鉴LLM动态生成任务相关先验的思路，用于生成式推荐冷启动，动态适配不同业务目标的召回排序偏好，降低规则迭代成本

  - 异源多模态特征融合+MAP优化的歧义消解框架，可迁移至多模态商品跨域召回场景，解决局部特征匹配模糊的问题

  - 零样本本体灵活适配的设计，可用于导购Agent动态调整用户兴趣语义划分规则，支撑个性化推荐的快速任务切换'
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有3D场景图提取框架依赖局部视觉聚类或严格几何启发规则（如墙体隔断划分房间），在开放式无隔断等任意结构环境下失效，无法灵活适配动态任务需求。
### 方法关键点
1. 提出Prior-SG框架，将场景图生成转化为概率对齐问题，通过多尺度开放词汇特征融合策略，将RGB-D传感器流聚合为物理可落地的Instance Graph；
2. 调用LLM动态生成环境结构先验图与任务相关词汇表，以其为引导通过MAP估计推理地图高层功能语义；
3. 优化马尔可夫随机场融合视觉、几何、离散对象等异源特征与拓扑先验，消解局部感知歧义。
### 关键结果
在模拟住宅数据集与真实开放式环境中语义区域分割精度达SOTA，可在无物理墙场景下鲁棒识别功能边界，支持零样本本体适配，可基于高层任务完全重构空间划分规则。
