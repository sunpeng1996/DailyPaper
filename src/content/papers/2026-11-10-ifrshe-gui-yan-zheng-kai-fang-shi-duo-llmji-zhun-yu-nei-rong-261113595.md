---
title: 'IFRS Compliance Verification: An Open Multi-LLM Benchmark and Content-Conditioned
  Ensemble Classifier'
title_zh: IFRS合规验证：开放式多LLM基准与内容条件集成分类器
authors:
- Aghoghomena Akasukpe
- Li Yang
- Xinyao Zhou
- Chen Shen
- Miguel Vargas Martin
affiliations:
- Ontario Tech University
arxiv_id: '2611.13595'
url: https://arxiv.org/abs/2611.13595
pdf_url: https://arxiv.org/pdf/2611.13595
published: '2026-11-10'
collected: '2026-11-11'
category: Other
direction: LLM多模型集成 · 垂直领域基准构建
tags:
- LLM Ensemble
- Benchmark
- Domain Adaptation
- Contrastive Learning
- Gradient Boosting
one_liner: 提出IFRS合规验证多LLM公开基准与内容感知集成分类器，显著提升高风险场景验证精度
practical_value: '- 多模型融合场景可复用「TPE优化梯度提升树融合多模型输出概率+领域嵌入特征」的方案，替代简单多数投票，解决单模型系统性偏差问题，可直接迁移到电商多召回源融合、多排序模型集成场景

  - 垂直领域嵌入优化可复用三段式pipeline：先领域语料MLM预训练，再TSDAE/SimCSE无监督适配，最后监督对比对齐，可直接提升电商商品、用户、query的垂直场景匹配精度

  - 数据集构建可复用「高置信度一致样本自动标注+分歧样本人工标注」的流程，大幅降低业务标注成本，适合电商类大规模标注场景'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
IFRS合规验证需人工交叉核对数百条细粒度监管条款，成本高、易出错；现有单LLM精度无法满足高风险场景要求，naive多模型集成易受单模型系统性偏差影响，效果甚至弱于最强单模型。
### 方法关键点
1. 构建含19998条IFRS监管-披露对的公开基准：11161条为多LLM一致标注样本，8837条为LLM分歧后的人工标注样本；
2. 三段式领域适配句嵌入pipeline：SEC EDGAR filings语料BERT MLM预训练→TSDAE+SimCSE无监督适配→监督对比对齐；
3. 集成分类器融合冻结嵌入、GPT-4.1/Claude Sonnet 4/Gemini 2.5 Pro的概率特征，采用TPE优化的梯度提升树实现融合。
### 关键结果数字
分歧样本集上加权F1达81.7%，较最强单LLM高10.4pp，较多数投票高14.6pp；召回pipeline在未见过的监管规则上Recall@15达45.3%
