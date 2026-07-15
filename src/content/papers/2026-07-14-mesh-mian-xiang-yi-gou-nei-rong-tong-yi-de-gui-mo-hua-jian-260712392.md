---
title: 'MESH: Scaling Up Retrieval with Heterogeneous Content Unification'
title_zh: MESH：面向异构内容统一的规模化检索优化框架
authors:
- Jiaxing Qu
- Yilin Chen
- Junpeng Hou
- Jinfeng Rao
- Olafur Gudmundsson
- Sai Xiao
- Huizhong Duan
arxiv_id: '2607.12392'
url: https://arxiv.org/abs/2607.12392
pdf_url: https://arxiv.org/pdf/2607.12392
published: '2026-07-14'
collected: '2026-07-15'
category: RecSys
direction: 推荐系统召回 · 异构内容统一检索
tags:
- Retrieval
- Heterogeneous Content
- Long-tail Recommendation
- Scalable System
- Fresh Content
one_liner: 提出带门控偏差校正的模块化统一检索框架MESH，缓解异构内容检索的缩放偏差
practical_value: '- 可复用异构内容分域建模思路，将特征空间拆分为独立域，减少稀疏/新品信号与热门内容高参与度特征的梯度干扰，提升长尾/新品召回效果

  - 可落地门控偏差校正模块，缓解异构系统缩放偏差问题，避免模型容量提升仅对热门内容有效

  - 异步服务策略可直接复用在大流量推荐检索场景，能大幅提升系统吞吐，降低生产部署成本'
score: 9
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有大规模检索系统为覆盖新鲜、长尾等异构内容，通常堆叠多套专用检索模型，架构碎片化严重；核心瓶颈是**异构缩放偏差**：模型容量提升无法均匀作用于不同内容层，稀疏内容几乎无法享受模型迭代收益。
### 方法关键点
提出MESH统一检索框架：1. 采用模块化架构+门控偏差校正机制，将特征空间划分为独立域，注入结构归纳偏置，隔离稀疏物品信号和高频参与度特征的梯度干扰，为稀疏内容保留独立梯度路径；2. 配套异步服务策略适配生产级大流量场景。
### 关键结果
新鲜内容幂律缩放指数提升14倍；Pinterest十亿级Item-to-Item推荐系统线上实验：新鲜内容转存率+5.5%，漏斗效率+55%，用户留存+0.46%，系统吞吐量提升2.87倍。
