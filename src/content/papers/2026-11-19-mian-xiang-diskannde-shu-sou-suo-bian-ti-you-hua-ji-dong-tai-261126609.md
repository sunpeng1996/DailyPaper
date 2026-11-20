---
title: Variants of Beam Search for DiskANN
title_zh: 面向DiskANN的束搜索变体优化及动态束宽预测方法
authors:
- Viraj Agrawal
- Kirankumar Shiragur
affiliations:
- Microsoft Research India
arxiv_id: '2611.26609'
url: https://arxiv.org/abs/2611.26609
pdf_url: https://arxiv.org/pdf/2611.26609
published: '2026-11-19'
collected: '2026-11-20'
category: RAG
direction: RAG 向量检索效率优化
tags:
- DiskANN
- Beam Search
- Approximate Nearest Neighbor
- Vector Retrieval
- RAG
one_liner: 推导自适应束搜索近似理论界，提出单查询动态束宽预测器，大幅降低DiskANN检索延迟
practical_value: '- 电商/Agent系统的RAG检索层、向量召回环节可直接替换原有CBS/ABS为论文提出的beam predictor，SSD环境下同召回最高降低29.6%检索延迟

  - 可复用动态资源分配思路：给不同难度的搜索/推荐query分配不同计算预算，难query多探召回池、易query提前终止，平衡整体延迟和效果

  - 可复用6种轻量pilot搜索特征（TopK距离统计、距离和下降率等）预测query难度，特征计算成本极低，适合线上低延迟场景

  - 磁盘存储的大规模向量索引可参考pilot搜索复用机制，无需重启搜索即可实现动态束宽调整，几乎无额外 overhead'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
图向量检索是RAG、电商向量召回、个性化推荐的核心底座，现有经典束搜索（CBS）给所有query分配固定束宽，资源浪费严重；自适应束搜索（ABS）缺乏通用α可达图上的理论保证，且资源分配未全局最优，SSD部署的大规模索引检索延迟仍有较大优化空间。
### 方法关键点
- 理论推导：统一证明ABS在α可达图上的近似界为$\frac{\alpha+1}{\alpha(\gamma+1)-1}$，ℓ2度量下排序α可达图可得到更紧界，覆盖过往所有相关理论结果
- 最优分配：对训练query扫描不同束宽的召回表现，用拉格朗日松弛求解带召回约束的最小计算量最优束宽分配，近似误差<0.5%
- Beam Predictor：先跑短pilot束搜索（束宽等于返回TopK数），提取6个轻量特征，用加权线性回归预测最优束宽，直接复用pilot搜索结果继续检索，无重复开销
### 关键实验
在3个1亿点ANN基准数据集（SIFT100M、DEEP100M、MSSpaceV100M）上对比CBS、ABS，SSD环境下同召回下，延迟比CBS最高降29.6%，11/15场景比ABS更快，最高快6.5%，95%召回下TopK=500时优势扩大到4.6~5.6%；内存环境下比CBS少1.3~23.7%的距离计算量。

> 核心结论：给不同难度的查询动态分配计算资源，是无召回损失下大幅降低大规模向量检索延迟的最有效手段之一
