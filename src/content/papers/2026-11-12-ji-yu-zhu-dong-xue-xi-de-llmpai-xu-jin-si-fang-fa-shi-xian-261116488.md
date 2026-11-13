---
title: Active Learning of Approximate LLM Ranking for Energy-Efficient Retrieval of
  Long Queries
title_zh: 基于主动学习的LLM排序近似方法实现长查询低能耗检索
authors:
- Ohad Porat
- Elad Yom-Tov
affiliations:
- Bar Ilan University
arxiv_id: '2611.16488'
url: https://arxiv.org/abs/2611.16488
pdf_url: https://arxiv.org/pdf/2611.16488
published: '2026-11-12'
collected: '2026-11-13'
category: RecSys
direction: 低能耗检索 · LLM重排主动学习近似
tags:
- LLM
- Active Learning
- Document Retrieval
- Energy Efficient
- Learning to Rank
one_liner: 提出轻量主动学习模型近似LLM重排，长查询下用3.3%能耗达到87%的P@10性能
practical_value: '- 长query检索/重排场景可直接复用该混合框架：先用BM25等传统方法粗排召回，再用梯度提升树拟合少量LLM标注的高信息样本，大幅降低LLM重排成本

  - 主动学习采样策略可直接迁移：初始采样优先覆盖排序头部候选，迭代时选择轻量模型与粗排结果差异最大的样本标注，用最少LLM调用获得最大收益

  - 特征组合方案可复用：语义embedding（BGE/MiniLM等）+ lexical特征（TF-IDF相似度、词重叠率）的组合作为轻量重排模型输入，效果最优

  - 可根据query复杂度动态分配算力：短query直接返回粗排结果，长/复杂query开启混合重排链路，进一步优化整体能耗与延迟'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM重排在长复杂查询场景的语义理解能力远优于BM25等传统 lexical 检索，但全量调用LLM重排数百候选的能耗是传统检索的10倍以上，成本难以落地；而长查询恰好是传统检索效果最差、LLM增益最高的场景，亟需兼顾效果与能耗的混合检索方案。

### 方法关键点
- 混合检索链路：先通过BM25召回Top500候选，再用轻量梯度提升模型LAAM近似LLM的相关性打分，避免全量LLM调用
- 主动学习迭代策略：初始采样15个候选送LLM标注训练LAAM，每轮选择LAAM预测分与BM25得分差异最大的单样本送LLM标注，增量更新LAAM，直至达到预设LLM调用预算
- 多源特征组合：输入包含query-文档语义embedding、TF-IDF余弦相似度、query词重叠率三类特征

### 关键实验
基于TREC Robust 2004数据集测试，对比BM25、全量DeepSeek V3重排两个基线，针对最长的叙事类query：
- 100次LLM调用预算下，LAAM达到全量DeepSeek重排87%的P@10（0.459 vs 0.526），仅消耗3.3%的能耗
- 50次LLM调用预算下，达到78%的P@10，仅消耗1.7%的能耗
- 效果显著优于BM25，P@1、P@10指标与全量DeepSeek无统计显著性差异

### 核心结论
LLM重排的大部分性能增益可通过仅标注不到10%的高信息候选实现，边际效益递减明显，无需为少量性能提升付出数倍成本。
