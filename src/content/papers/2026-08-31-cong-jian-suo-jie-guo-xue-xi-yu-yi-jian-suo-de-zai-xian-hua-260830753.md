---
title: 'Learning from What You Retrieve: Online RL Fine-Tuning for Semantic Retrieval'
title_zh: 从检索结果学习：语义检索的在线强化学习微调方法
authors:
- Shaowei Wei
- Chong Huang
- Songtao Fang
- Jin Zhang
- Zhuojun Wang
- Chengfu Huo
affiliations:
- Alibaba Group
arxiv_id: '2608.30753'
url: https://arxiv.org/abs/2608.30753
pdf_url: https://arxiv.org/pdf/2608.30753
published: '2026-08-31'
collected: '2026-09-01'
category: RecSys
direction: 语义检索 · RL在线微调
tags:
- Semantic Retrieval
- Reinforcement Learning
- Dual-Encoder
- Frozen Index
- E-commerce Search
one_liner: 提出正优势仅更新的PAO策略，冻结索引约束下实现检索-重排对齐，避免嵌入空间几何坍塌
practical_value: '- 冻结索引的工业级检索场景做在线微调时，直接屏蔽负样本梯度，仅回传正优势样本梯度，可避免嵌入空间几何坍塌，同时拿到NDCG@5近10pt的提升

  - RL微调时添加查询编码器当前策略与预训练基准策略的KL约束，β设为0.3、温度τ设为1.0可取得最优效果，兼顾策略适配与防漂移

  - 检索-重排对齐场景下，PAO效果优于直接用重排分数做KL蒸馏，深召回位提升更显著，可替代蒸馏方案实现检索端在线迭代'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
电商大规模语义检索普遍采用双塔召回+下游重排架构，双塔对比学习目标与重排细粒度相关性目标存在错位，工业场景下数十亿商品索引冻结无法频繁更新，仅能微调查询编码器；传统策略梯度RL微调会强制将查询embedding推离低reward样本，在高维冻结空间中破坏预训练语义流形，引发几何坍塌导致检索效果骤降。

### 方法关键点
- 提出PAO（Positive-Advantage-Only）选择性更新策略：仅对优势值$A_i>0$的检索样本回传梯度，将查询embedding向高reward区域拉动，完全屏蔽负样本的推式更新，避免语义流形破坏
- 增加当前查询编码器策略与预训练基准策略的KL散度约束，作为全局锚点防止策略漂移
- 采用下游重排器输出作为reward信号，基于检索Top-K列表的Softmax分布计算采样概率，用标准化优势值降低梯度方差

### 关键实验结果
基于阿里电商1M训练/50k测试搜索日志、公开MS MARCO基准测试，对比基线为对比学习微调的GTE-Base、全样本策略梯度RL-All、KL蒸馏方案：
1. 工业数据集上PAO较基线NDCG@5提升9.0pt、Recall@5提升6.9pt，而RL-All较基线NDCG@5下降13.6pt
2. MS MARCO上PAO较基线NDCG@5提升2.03pt、Recall@50提升4.23pt，较KL蒸馏方案Recall@50领先2.31pt

### 核心结论
冻结索引场景下做检索侧RL微调，「只拉不推」是避免嵌入几何坍塌的核心原则，效果远好于正负样本全量更新。
