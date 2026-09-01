---
title: 'Generative Retrieval for E-commerce: Jointly Learning Embedding and Codebook
  with Same Product Cluster'
title_zh: 面向电商的生成式检索：基于同品簇的嵌入与码本联合学习
authors:
- Songtao Fang
- Zihao Xu
- Shaowei Wei
- Jin Zhang
- Zhuojun Wang
affiliations:
- Alibaba Group
arxiv_id: '2608.30606'
url: https://arxiv.org/abs/2608.30606
pdf_url: https://arxiv.org/pdf/2608.30606
published: '2026-08-31'
collected: '2026-09-01'
category: GenRec
direction: 生成式检索 · 嵌入与码本联合学习
tags:
- Generative Retrieval
- E-commerce Search
- Codebook Learning
- RQ-VAE
- Semantic ID
one_liner: 提出同品簇约束的嵌入与码本联合训练框架，解决电商生成式检索两阶段误差累积问题
practical_value: '- 搭建生成式检索系统时可抛弃传统两阶段Pipeline，采用嵌入、码本联合训练方案，避免误差累积，实测Recall@100可提升4pct以上

  - 可引入同品簇（同款不同SKU/不同商家的商品）作为弱监督信号，用MSE Loss约束同簇商品嵌入一致性，既能提升ID语义一致性，又能拉高检索召回

  - LLM学习商品ID映射时可采用两阶段渐进训练：先学商品信息到ID的映射，再学query到ID的映射，降低新增ID特殊token的学习成本'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前电商生成式检索主流采用两阶段方案：先训练商品嵌入模型，再训练码本将嵌入映射到商品ID，存在两个核心缺陷：一是误差累积，第一阶段嵌入的偏差会被第二阶段码本放大，最终拉低检索效果；二是码本学习仅依赖静态商品嵌入，未建模query-商品、商品-商品交互，导致同簇商品（同款不同SKU/商家）的ID语义不一致，进一步降低检索准确率。

### 方法关键点
- 嵌入与码本联合训练：将RQ-VAE重建损失、query-商品对比学习损失、同品簇约束损失整合到统一优化目标，端到端优化两个模块，消除两阶段误差传播
- 加入同品簇弱监督：随机采样同簇商品的嵌入计算均值，用MSE Loss约束当前商品嵌入与簇均值的一致性，提升同簇商品ID的语义重合度
- LLM两阶段渐进训练：第一阶段先学商品属性到ID的映射，让LLM适配新增的ID特殊token；第二阶段再学query到ID的映射，降低学习难度

### 关键实验
基于阿里内部2000万商品、4000万query-商品对训练，对比BM25、DPR、DSI、Tiger RQ-VAE等基线；核心结果：Recall@1达4.49%，较Tiger RQ-VAE提升0.16pct；Recall@10达9.90%，提升1.06pct；Recall@100达30.71%，提升4.33pct；同簇商品ID平均共享前缀长度（ALSP）达4.42，提升0.5，ID语义一致性显著提升。

### 核心结论
生成式检索的核心优化方向之一是让ID的语义结构与业务天然的商品语义分组对齐，端到端联合训练是消除两阶段方案缺陷的有效路径。
