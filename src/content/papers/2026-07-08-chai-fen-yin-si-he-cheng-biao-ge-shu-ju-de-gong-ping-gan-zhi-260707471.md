---
title: Where to Intervene? Benchmarking Fairness-Aware Learning on Differentially
  Private Synthetic Tabular Data
title_zh: 差分隐私合成表格数据的公平感知干预节点基准测试
authors:
- Vinícius Gabriel Angelozzi
- Héber H. Arcolezi
affiliations:
- Centre Inria de l’Université Grenoble Alpes
- ÉTS Montréal
- Inria Grenoble
arxiv_id: '2607.07471'
url: https://arxiv.org/abs/2607.07471
pdf_url: https://arxiv.org/pdf/2607.07471
published: '2026-07-08'
collected: '2026-07-09'
category: Eval
direction: 算法公平 · 差分隐私合成数据评估
tags:
- Differential Privacy
- Synthetic Data
- Algorithmic Fairness
- Benchmark
- Tabular Data
one_liner: 首次系统评估不同隐私预算下三类公平干预在DP合成表格数据上的效用-公平权衡
practical_value: '- 业务中采用DP生成用户隐私数据训练模型时，优先选择后处理公平干预方案，跨隐私预算的效用-公平权衡更稳定

  - 可直接复用论文开源的DP+公平干预benchmark工具，快速验证自身业务场景下不同干预节点的效果

  - DP合成数据导致推荐/广告模型对小众群体效果下降时，可通过后处理公平干预部分恢复效果，无需改动上游DP合成逻辑'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
高风险场景下ML模型同时面临隐私合规与算法公平要求，但DP（差分隐私）通常会放大不同人群的效果差异，现有公平干预方案在DP约束下的有效性缺乏系统性验证。
### 方法关键点
以SOTA边际DP合成器AIM为核心基准，覆盖4个数据集、多组公平指标、全范围隐私预算，对比预处理/训练中/后处理三类公平干预方案的效果，共测试原数据训练、仅DP、仅公平、DP+公平四类管线。
### 关键结果
单独使用DP会同时降低模型效用和公平性，叠加公平干预可部分恢复公平效果；其中后处理方法的公平-效用权衡在所有隐私预算下最稳定，公平提升幅度显著的同时效用损失远低于预处理/训练中干预方案。
