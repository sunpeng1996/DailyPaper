---
title: Enhancing Relation Modeling with Social Attributes for Social Media Popularity
  Prediction
title_zh: 结合社会属性增强关系建模的社交媒体热度预测
authors:
- Bolun Zheng
- Yuhao Luo
- Wei Zhu
- Ning Xu
- An-An Liu
- Lingyu Zhu
- Canjin Wang
affiliations:
- Hangzhou Dianzi University
- Tianjin University
- City University of Hong Kong
- Xinhua Zhiyun Technology Co., Ltd.
arxiv_id: '2607.19200'
url: https://arxiv.org/abs/2607.19200
pdf_url: https://arxiv.org/pdf/2607.19200
published: '2026-07-21'
collected: '2026-07-22'
category: RecSys
direction: 检索增强推荐 · 内容热度预测
tags:
- RAG
- Relation Modeling
- Popularity Prediction
- Retrieval
- Social Attributes
- Multimodal
one_liner: 提出语义与社会属性双对齐的关系增强RAG框架RE-Rag，提升社交媒体热度预测的准确率与检索效率
practical_value: '- 做内容/商品热度预估时，检索召回阶段可同时对齐语义和社会属性（如作者/商家层级、历史互动数据），提升召回相关度

  - 多源特征融合时，可引入相对属性关系图引导Transformer注意力权重分配，强化跨特征交互捕捉

  - RAG落地预估类任务时，可参考RE-Rag的检索-编码-关系引导-融合四步架构，平衡效果与效率'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有检索增强类社交媒体热度预测方法忽略UGC实例间的相对关联，导致检索准确率低，模型效果受限。
### 方法关键点
1. 提出RE-Rag框架，将UGC相似度建模为语义内容与社会属性共同驱动的连续关系；
2. 设计Semantic-Attribute Retriever（SAR），召回语义、社会属性分布双对齐的历史实例；
3. 搭建Relation-Guided Predictor（RGP）：先通过交叉注意力编码召回实例的多模态特征，再引入相对属性关系图构建Relation-Guided Transformer，动态调整注意力权重捕捉语义与社会属性的交互，最终融合目标实例特征完成热度预测。
### 关键结果
在3个公开基准数据集上，RE-Rag的预测准确率、检索效率均显著优于当前SOTA方法
