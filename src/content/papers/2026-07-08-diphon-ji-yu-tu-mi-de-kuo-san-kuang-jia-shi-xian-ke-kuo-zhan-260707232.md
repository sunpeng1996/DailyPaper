---
title: 'DiPhon: Diffusion on Graphons for Scalable Graph Generation'
title_zh: DiPhon：基于图幂的扩散框架实现可扩展图生成
authors:
- Sergio Rozada
- Yiming Qin
- Manuel Madeira
- Pascal Frossard
- Alejandro Ribeiro
affiliations:
- King Juan Carlos University
- EPFL
- University of Pennsylvania
arxiv_id: '2607.07232'
url: https://arxiv.org/abs/2607.07232
pdf_url: https://arxiv.org/pdf/2607.07232
published: '2026-07-08'
collected: '2026-07-09'
category: Other
direction: 可扩展图生成 · 扩散模型
tags:
- Diffusion Model
- Graph Generation
- Graphon
- Stochastic Process
- Scalable AI
one_liner: 提出基于图幂的扩散框架DiPhon，小图训练后无需重训即可生成任意规模拓扑一致的大图
practical_value: '- 大规模图生成思路可迁移到用户-物品交互图、社交关系图的规模化生成，无需全量大图训练，大幅降低训练成本

  - 基于规模无关极限对象建模的思路，可借鉴到跨规模用户行为建模、冷启动场景下的图结构补全任务

  - Jacobi SDE的边际得分可解形式推导思路，可用于简化扩散模型反向采样流程，提升图生成推理效率'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有图扩散模型存在明显规模瓶颈，不仅大图训练部署成本极高，小图训练得到的模型也无法直接生成不同规模的大图，拓扑一致性难以保障。

### 方法关键点
引入图幂（稠密图序列的规模无关极限对象）建模跨尺度图结构统计特性，基于Jacobi随机微分方程构建图幂空间的连续扩散过程，设计有限图上的离散化扩散过程DiPhon匹配该动态；推导得到可解的边际得分形式，通过图去噪任务从数据中估计得分后执行反向生成。

### 关键结果
理论上可精确匹配连续图幂过程的一阶矩，二阶矩误差有闭式上界；仅需在小图上训练，无需重训即可生成任意规模大图，核心拓扑属性与训练分布保持一致。
