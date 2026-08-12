---
title: 'TEAMMix: Taxonomy Enrichment Augmentation and Minority-augmented Mixing Strategy
  for LLM-enhanced Weak-Supervised Hierarchical Text Classification'
title_zh: TEAMMix：LLM增强弱监督层次文本分类的分类体系增强与小类混合策略
authors:
- Jian Zhang
- Zhuohao Yang
- Songlin Lei
- Bangli Liu
- Ziwei Wang
- Xufeng Weng
- Gehan Amaratunga
- Yu Lin
- Hongwei Wang
affiliations:
- Zhejiang University
- ZJU-UIUC Institute, Zhejiang University
- Shaoxing K3i Technology Co. Ltd
- State Key Laboratory of CAD&CG, Zhejiang University
arxiv_id: '2608.11044'
url: https://arxiv.org/abs/2608.11044
pdf_url: https://arxiv.org/pdf/2608.11044
published: '2026-08-11'
collected: '2026-08-12'
category: Other
direction: 弱监督层次分类 · LLM数据增强
tags:
- Hierarchical Text Classification
- Data Augmentation
- Weakly Supervised Learning
- Long-tail Distribution
- LLM
one_liner: 提出基于LLM数据增强的弱监督层次文本分类框架，解决标签结构丢失与样本长尾问题
practical_value: '- 电商类目匹配/商品自动打标场景可复用标签语义增强思路：通过关键词生成+语料挖掘补充分类体系语义，解决层级标签歧义问题，提升小类目识别准确率

  - 长尾类目样本不足场景可借鉴「LLM伪样本生成+GMM置信度重采样」流程，生成小类样本后过滤低置信度数据，避免噪声降低模型效果

  - 弱监督标注场景下可直接复用该数据增强范式，无需大量人工标注即可提升层级分类任务表现，大幅降低标注成本'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
层次文本分类（HTC）存在标签层级复杂、类别分布长尾不平衡问题，现有LLM驱动方法存在Prompt过长、标签结构信息丢失缺陷，弱监督场景下效果受限。
### 方法关键点
1. 提出TEAMMix弱监督HTC框架，先通过关键词生成、语料挖掘对标签层级做语义增强，强化模型对层级标签的理解，避免Prompt过长导致的结构信息丢失。
2. 引导LLM生成小类伪样本缓解长尾问题，再用高斯混合模型（GMM）基于置信度重采样生成数据，过滤低质量伪样本，降低噪声干扰。
### 关键结果
方法有效提升LLM生成伪标签的可靠性，在细粒度、不平衡数据集上的层级分类效果得到显著提升。
