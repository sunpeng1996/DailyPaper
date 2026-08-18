---
title: 'SAHC-NS: Structure-Aware and Hardness-Calibrated Negative Sampling for Implicit
  Collaborative Filtering'
title_zh: 面向隐式协同过滤的结构感知与硬度校准负采样方法SAHC-NS
authors:
- Jiayi Wu
- Zhengyu Wu
- Xunkai Li
- Hongchao Qin
- Rong-Hua Li
- Guoren Wang
affiliations:
- Beijing Institute of Technology
arxiv_id: '2608.16587'
url: https://arxiv.org/abs/2608.16587
pdf_url: https://arxiv.org/pdf/2608.16587
published: '2026-08-17'
collected: '2026-08-18'
category: RecSys
direction: 推荐系统·负采样优化
tags:
- Negative Sampling
- Collaborative Filtering
- GNN4Rec
- Implicit Feedback
- Training Strategy
one_liner: 针对GNN推荐负采样痛点，提出兼顾层间结构差异与候选池硬度的自适应负采样方案
practical_value: '- 可直接复用结构感知负采样思路：不用仅依赖最终embedding匹配分筛选负例，新增计算GNN各层匹配分的均值和标准差，可调权重α融合后选负例，能低成本挖掘更多高训练价值的难负例；

  - 候选池硬度自适应校准trick可直接落地：通过每层正负样本分差动态调整负例与正例的插值强度，既避免过难假负例，又保证负例有足够训练信号，无需调整模型架构；

  - 该方法额外训练开销仅占单epoch总时间的0.68%~2.12%，兼容LightGCN、NGCF、SimGCL等主流GNN推荐backbone，可直接替换现有两阶段负采样策略，迁移成本极低。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
隐式协同过滤的两阶段负采样存在两大普遍痛点：一是不同用户的候选负例池硬度差异极大，全局固定的增强策略要么让本就偏难的候选池生成过难负例，提升假负例风险，要么让偏易的候选池负例训练价值不足；二是仅用GNN最终聚合embedding的匹配分筛选负例，会掩盖不同传播层捕获的多跳结构差异，最终得分相近的负例实际训练价值可能差距显著，现有方法无法充分挖掘高价值负例。
### 方法关键点
- 结构感知负选择：对每个候选负例，计算其与用户最终embedding在GNN所有传播层的匹配分，用匹配分均值表征整体硬度，标准差表征层间结构差异，池内归一化后加权求和作为选择得分，优先选取硬度高且结构差异大的负例；
- 候选池感知硬度校准：逐层计算候选池最高负分与正分的差距，映射为层级池硬度得分，动态决定每层负例embedding与正例embedding的插值比例，对易池增强负例硬度，对难池降低增强强度避免假负例；
- 无需修改推荐模型架构与损失函数，仅替换负采样逻辑，推理阶段无任何额外开销。
### 关键实验
在Amazon-toys、Yelp、ML-1M三个公开数据集上，对比DNS、MixGCF、AHNS等8个SOTA负采样基线，以LightGCN为骨干时，Recall@20最高提升2.7%（Yelp数据集，从0.1454到0.1477），NDCG@20最高提升5.8%（Amazon-toys，从0.0631到0.0662），额外训练开销仅占单epoch总时间的0.68%~2.12%，兼容NGCF、SimGCL等多种主流GNN推荐骨干。
### 核心结论
GNN推荐的负采样不仅要关注最终embedding的匹配分，更要挖掘层间结构差异带来的训练价值，同时根据每个候选池的硬度动态调整增强强度，才能有效平衡负例的信息量与可靠性。
