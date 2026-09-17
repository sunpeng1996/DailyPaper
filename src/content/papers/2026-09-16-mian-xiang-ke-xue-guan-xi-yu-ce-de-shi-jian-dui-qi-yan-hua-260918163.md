---
title: Time-Aligned Evolving Concept Graphs for Scientific Relation Forecasting
title_zh: 面向科学关系预测的时间对齐演化概念图
authors:
- Fred Sun
- Jingze Wang
- Minkun Xu
- Shangqi Guo
affiliations:
- 清华大学精密仪器系类脑计算研究中心
- 广东智能科学与技术研究院
arxiv_id: '2609.18163'
url: https://arxiv.org/abs/2609.18163
pdf_url: https://arxiv.org/pdf/2609.18163
published: '2026-09-16'
collected: '2026-09-17'
category: Other
direction: 演化概念图 · 时序关系预测
tags:
- Temporal Graph
- Concept Graph
- Relation Forecasting
- Time Alignment
- Structural Semantic Fusion
one_liner: 提出时间对齐演化概念图框架，联合建模语义与结构演化提升科学关系预测性能
practical_value: '- 电商商品关联预测、用户-物品交互时序预测场景，可复用「同一时序事件同步更新语义表征与图结构」的设计，避免语义和结构演化错位

  - 时序图预测任务可参考 pair-level 融合语义、结构双状态的方案，降低多模态表征对齐损耗，提升预测精度

  - 概念快速迭代场景（如新品关联、热点内容关联），可复用随事件刷新上下文而非固定上下文的trick，可带来AUPRC 10%+的提升空间'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有科学关系预测方法要么单独建模概念语义与图结构，要么基于粗粒度历史快照聚合语义，存在语义表征与快速演化的图证据错位问题，预测精度受限。
### 方法关键点
1. 提出时间对齐的演化概念图框架，联合建模语义与结构两类特征的演化规律
2. 以带时间戳的论文作为共享更新事件，每次预测时基于相同的历史发表数据同时重构语义与结构状态
3. 采用pair-level融合双状态，覆盖首次共现、关系生成、关系类型三类预测任务
### 关键结果
- 固定架构与训练策略时，随图更新刷新上下文相比冻结上下文，平均关系AUPRC提升16.6%
- 在18.7万篇论文构建的含27.07万概念、745万条共现链的数据集上，完整框架相比最强基线，平均关系AUROC从0.9290提升至0.9722，群体加权平均AUPRC达0.005778
