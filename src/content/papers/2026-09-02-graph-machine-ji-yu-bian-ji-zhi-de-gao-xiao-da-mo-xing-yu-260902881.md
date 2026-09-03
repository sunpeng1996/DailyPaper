---
title: 'Graph Machine: Towards Better Pretraining via Edges'
title_zh: Graph Machine：基于边机制的高效大模型预训练架构
authors:
- Lintai Hou
affiliations:
- iterlabs.ai
arxiv_id: '2609.02881'
url: https://arxiv.org/abs/2609.02881
pdf_url: https://arxiv.org/pdf/2609.02881
published: '2026-09-02'
collected: '2026-09-03'
category: Training
direction: 大模型预训练 · 稀疏注意力架构
tags:
- Sparse Attention
- Pretraining
- Transformer Optimization
- Dynamic Routing
- Graph Modeling
one_liner: 用可微分更新的边机制实现稀疏动态路由，替换75%Transformer层降低预训练算力且效果损失极小
practical_value: '- 做长序列用户行为建模时，可复用边+动态路由的稀疏检索思路，仅检索top2-4个相关行为节点，大幅降低长序列attention计算量，效果损失可控

  - 自研业务小模型预训练时，可采用稀疏GM层+少量稠密Transformer层的混合架构，用10-20%的参数增量换10-30%的预训练算力节省，满足小模型快速迭代需求

  - 检索增强类RAG/推荐系统的路由模块，可借鉴软边加权+乘积专家融合思路，把结构化关联权重和语义匹配分数融合，提升召回精度'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有序列建模架构存在明显短板：RNN/SSM仅维护O(1)大小的状态，长序列信息压缩损失大；原生Transformer的注意力复杂度达O(n²)，长序列/大批次预训练计算成本极高；滑动窗口等稀疏注意力方案采用静态路由，无法根据当前内容动态召回相关节点，亟需兼顾长序列记忆、低计算开销、动态感知能力的新架构。
### 方法关键点
- 提出Graph Machine(GM)架构，同时存储浮点型节点特征、整数边索引与浮点边权重，通过可微分的边referral机制实现多跳动态路由，无需离散策略梯度即可端到端更新边结构
- 设计混合架构GLM，按3:1比例混合GM稀疏层与Transformer稠密层，稀疏层先经多轮referral更新边结构，再通过稀疏边注意力(SEA)更新节点特征，全程保持因果约束
- 注意力计算采用乘积专家融合：将边权重的对数与常规QK相似度分数相加后做softmax，同时引入边刷新、注意力结果实对齐机制进一步优化效果
### 关键结果
基于15.7B token的FineWeb-Edu数据集从头预训练，基线为Qwen3-0.6B：
- 每KV头仅检索2个节点的Theia系列模型，最终loss仅比基线高0.014，训练总算力降低5%~15%，attention KV访问仅为原生Transformer的0.098%
- 每KV头检索4个节点的Hyperion系列最优模型，最终loss比基线低0.003，参考+attention计算量降低19%，参数仅增加11%
> 最值得记住的结论：75%的Transformer层可被仅检索2~4个节点的稀疏层替换，几乎不损失预训练效果，同时显著降低计算成本。
