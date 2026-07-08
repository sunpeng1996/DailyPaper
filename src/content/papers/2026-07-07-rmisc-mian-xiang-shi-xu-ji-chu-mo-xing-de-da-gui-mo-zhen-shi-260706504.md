---
title: 'RMISC: A Large-scale Real-world Multivariate Corpus for Time Series Foundation
  Models'
title_zh: RMISC：面向时序基础模型的大规模真实世界多元时序语料库
authors:
- Qian Sun
- Yong-Ming Tian
- Jia-Wei Huang
- Cheng Feng
- Shao-Qun Zhang
affiliations:
- State Key Laboratory of Novel Software Technology, Nanjing University
- School of Intelligent Science and Technology, Nanjing University
- Siemens Data and AI Research, Beijing
- Nanjing University – Siemens Joint Research Center on Industrial AI
arxiv_id: '2607.06504'
url: https://arxiv.org/abs/2607.06504
pdf_url: https://arxiv.org/pdf/2607.06504
published: '2026-07-07'
collected: '2026-07-08'
category: Training
direction: 时序基础模型 · 预训练语料构建
tags:
- Time Series Foundation Model
- Pre-training Corpus
- Multivariate Time Series
- Zero-shot Generalization
- OOD Generalization
one_liner: 构建含200数据集1420亿时间点的真实多元时序语料，验证真实数据对时序基础模型泛化的提升作用
practical_value: '- 电商场景下做用户行为序列建模、销量/流量时序预测等任务时，预训练阶段优先引入业务真实多元时序数据替代纯合成数据，可显著提升跨场景泛化能力

  - 跨业务域时序预训练语料构建可参考RMISC的多领域覆盖、高数据量设计思路，整合搜索、推荐、广告等不同业务域的时序数据，提升预训练模型通用性

  - 评估时序预训练模型效果时，需同时纳入分布内、分布外benchmark验证零样本泛化能力，避免模型过拟合单业务场景数据'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有多元Time Series Foundation Models (TSFM)多基于合成数据预训练，易扩展但无法捕捉真实场景复杂时序动态、跨变量关联，真实数据对TSFM的性能增益程度缺乏系统验证。

### 方法关键点
1. 构建RMISC大规模公开真实多元时序语料，覆盖多领域，包含约200个数据集、1420亿时间点；
2. 选取4个主流TSFM，分别在单变量、合成多元、真实多元数据上预训练，在分布内/分布外基准上测试零样本泛化能力。

### 关键结果数字
引入真实多元时序数据预训练后，单变量、多元TSFM的泛化性能均获得一致性提升，验证了真实时序数据是强化TSFM能力的核心要素之一。
