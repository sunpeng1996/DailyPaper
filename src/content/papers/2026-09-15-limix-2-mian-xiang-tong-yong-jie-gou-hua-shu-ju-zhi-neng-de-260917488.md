---
title: 'LimiX-2: A Contextual Mechanism Network Towards General Structured-Data Intelligence'
title_zh: LimiX-2：面向通用结构化数据智能的上下文机制网络
authors:
- Xingxuan Zhang
- Gang Ren
- Hao Yuan
- Hao Zou
- Hongze Tan
- Hui Wang
- Jianhao Song
- Jiansheng Li
- Jiayao Zhang
- Jinghan Zhang
affiliations:
- Stable AI
- Tsinghua University
arxiv_id: '2609.17488'
url: https://arxiv.org/abs/2609.17488
pdf_url: https://arxiv.org/pdf/2609.17488
published: '2026-09-15'
collected: '2026-09-16'
category: Other
direction: 通用结构化数据基座 · 因果感知建模
tags:
- Tabular Foundation Model
- Causal Modeling
- In-context Learning
- Masked Pretraining
- Structured Data
one_liner: 提出基于上下文机制网络的通用结构化数据基座LimiX-2，性能超现有表格模型且具备因果感知能力
practical_value: '- 电商用户/商品/交易等结构化特征建模可参考CMN的联合分布建模思路，替代传统target-centric的拟合目标，提升跨业务场景的泛化性能

  - 推荐特征工程环节可复用LimiX-2的特征注意力机制，直接挖掘特征间的因果关联，大幅降低无效特征试错成本

  - 小样本冷启动场景可借鉴CCMM预训练范式，用SCM生成对应场景的合成数据预训练基座，减少对真实标注数据的依赖'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有表格PFN等模型采用target-centric的上下文学习范式，仅建模$p(y|x,D_{context})$，缺乏对数据生成底层联合结构的刻画，跨数据集泛化性弱且不具备因果感知能力。
### 方法关键点
1. 提出Contextual Mechanism Networks(CMNs)范式，将建模目标切换为学习$p(x,y|D_{context})$的上下文依赖联合结构，实现机制导向的联合建模；
2. 采用Context-Conditional Masked Modeling(CCMM)预训练，预训练数据由覆盖多样图结构、函数机制、观测过程的结构因果模型(SCM)生成的合成数据集构成。
### 关键结果
在TabArena、TALENT、BCCO三个基准上Elo得分分别达1935、1506、1432，全面优于现有数据集特定模型、AutoGluon 1.6及其他表格基座模型，同时特征注意力可编码直接因果关系，支持准确的因果骨架恢复。
