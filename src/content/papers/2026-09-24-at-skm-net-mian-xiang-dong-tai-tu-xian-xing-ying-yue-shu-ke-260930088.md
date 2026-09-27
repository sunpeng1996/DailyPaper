---
title: 'AT-SKM-Net: An Accelerated Trainable Sampling Kaczmarz-Motzkin Framework for
  Linear Hard-Constraint Feasibility on Dynamic Graphs'
title_zh: AT-SKM-Net：面向动态图线性硬约束可行问题的加速可训练求解框架
authors:
- Xiaochen Zhang
- Haoyu Zhu
- Yao Zhang
- Qingchun Hou
affiliations:
- Zhejiang University
arxiv_id: '2609.30088'
url: https://arxiv.org/abs/2609.30088
pdf_url: https://arxiv.org/pdf/2609.30088
published: '2026-09-24'
collected: '2026-09-27'
category: Other
direction: 动态图约束优化 · 可训练求解器加速
tags:
- Dynamic Graph
- GNN
- Constrained Optimization
- Trainable Solver
- Acceleration
one_liner: 提出融合拓扑感知GNN采样与Cholesky更新的动态图硬约束优化框架，提速2.95-7.29倍且零约束违反
practical_value: '- 电商/推荐场景大规模约束优化任务（如流量分配、广告库存约束求解）可复用GNN引导的活跃约束筛选思路，大幅降低冗余计算

  - 动态规则变更场景（如促销期约束更新）可借鉴Cholesky Update低秩扰动优化方法，将矩阵求逆复杂度从O(N³)降至O(N²)，提升求解实时性

  - 硬约束零容忍业务场景（如广告预算控制、合规性校验）可参考其保可行性的可训练求解器设计，兼顾性能与约束满足'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
动态图线性硬约束优化是电网、交通等基础设施的核心问题，现有可训练投影类求解器需全量处理约束集、依赖高开销矩阵分解，动态场景下计算成本过高，无法满足实时性要求。
### 方法关键点
1. 引入拓扑感知异质GNN引导的混合采样策略，仅聚焦活跃约束计算，消除冗余开销；
2. 采用Cholesky Update机制处理图拓扑变动，低秩扰动下将等式投影复杂度从O(N³)降至O(N²)。
### 关键结果
在随机几何图、N-1安全约束直流最优潮流、最低成本燃气传输三类任务上，迭代次数最多降低85%，SKM层提速2.95x-7.29x，同时保持零约束违反。
