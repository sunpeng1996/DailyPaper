---
title: Gauge-Invariant, Parameter-Insensitive Regularization for Potential Recovery
  from Flow on Directed Graphs
title_zh: 面向有向图流势恢复的规范不变参数不敏感正则化方法
authors:
- Mohammad Forouhesh
affiliations:
- Amirkabir University of Technology, Iran
arxiv_id: '2607.13609'
url: https://arxiv.org/abs/2607.13609
pdf_url: https://arxiv.org/pdf/2607.13609
published: '2026-07-15'
collected: '2026-07-17'
category: Training
direction: 图正则化 · 有向图势恢复与GNN过平滑优化
tags:
- Regularization
- Directed Graph
- GNN
- Oversmoothing
- Clickstream
one_liner: 提出规范不变图狄利克雷能量正则化，解决有向图势恢复中岭正则化排序反转、参数敏感问题
practical_value: '- 处理电商用户点击流、页面跳转等有向图数据时，可替换岭正则化为规范不变狄利克雷能量正则化，避免潜势排序反转，无需反复调优正则化参数λ

  - 训练深层有向GCN做用户/物品表征、用户行为建模时，可引入每层常数模态抵消机制，缓解过平滑问题，保留特征动态范围

  - 电商流量链路分析、商品流转路径潜势计算场景，可复用泊松残差方法仅通过流数据定位吸收边界，无需额外标注数据'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
有向图（如点击流、流量网络）的潜势恢复是典型不适定问题，传统岭正则化会向无实际意义的规范原点收缩，导致恢复结果排序反转、动态范围坍缩，且正则化参数λ调参难度极高，λ>0时就会出现排序反转。

### 方法关键点
1. 采用规范不变的图狄利克雷能量作为正则项，证明简化求解为对称正定（SPD）问题，天然避免规范原点偏移，实现参数不敏感；
2. 引入泊松残差，仅通过流数据即可定位吸收边界，无需额外标注；
3. 可拓展到GNN训练：每层抵消常数模态，缓解深层有向GCN过平滑问题。

### 关键结果
- 正则化参数λ跨4个数量级时结果仍稳定，岭正则化任意λ>0均出现排序反转，人工真值下秩相关从+0.81降至-0.42；
- 3个公开点击流数据集上，该方法保留28%~41%的内部动态范围，岭正则化仅保留最低0.2%；
- 可直接迁移到深层有向GCN训练，有效解决过平滑问题。
