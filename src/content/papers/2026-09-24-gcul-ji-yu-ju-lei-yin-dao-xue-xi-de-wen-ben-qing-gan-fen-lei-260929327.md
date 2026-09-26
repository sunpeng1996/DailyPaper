---
title: 'GCUL: Ambiguity Identification in Text Emotion Classification via Cluster-Guided
  Learning'
title_zh: GCUL：基于聚类引导学习的文本情感分类歧义识别方法
authors:
- Zhongqi Fan
- Tianyou Zhang
- Fei Chen
affiliations:
- Beijing Normal-Hong Kong Baptist University
arxiv_id: '2609.29327'
url: https://arxiv.org/abs/2609.29327
pdf_url: https://arxiv.org/pdf/2609.29327
published: '2026-09-24'
collected: '2026-09-26'
category: LLM
direction: 大模型下游分类 · 选择性分类与歧义识别
tags:
- Selective Classification
- Uncertainty Estimation
- Clustering
- Text Classification
- Emotion Recognition
one_liner: 聚类引导的选择性分类框架GCUL，基于表示空间几何结构识别文本情感分类歧义样本
practical_value: '- 可迁移到电商评论情感分类、query意图识别、客服话术分类场景，对歧义样本做拒识转人工审核，降低badcase率

  - 可复用GCUL三阶段聚类识别不确定区域的思路，替代传统基于置信度的拒识逻辑，避免预设覆盖率的不合理性

  - 部署前可复用论文提出的selectivity score做可行性评估，提前判断当前任务是否适合引入选择性分类能力'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有选择性分类方法依赖置信度、预设覆盖率或单样本距离度量做拒识，忽略难例在表示空间的集体几何结构，无法精准识别歧义样本，拒识效率低。
### 方法关键点
1. GCUL是几何引导的选择性分类框架，通过初始化表示、聚类识别混淆吸引子区域、不确定区域显式重标注三阶段流程，让拒识边界从表示空间几何结构自然生成，无需预设拒识率
2. 推导得到selectivity score和几何充分条件，支持部署前评估选择性分类的业务收益可行性
### 关键结果
- 仅需<9%拒识率，即可将DistilBERT情感分类精度从89.37%提升至94.98%
- selectivity score可正确预判GoEmotion数据集上所有基线失效的情况，受控模拟下仅6.1% Type-I错误、0% Type-II错误
