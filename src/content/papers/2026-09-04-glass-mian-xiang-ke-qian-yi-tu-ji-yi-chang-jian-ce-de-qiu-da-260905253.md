---
title: 'GLASS: Graph-Language Alignment with Spherical Scoring for Transferable Graph-Level
  Anomaly Detection'
title_zh: GLASS：面向可迁移图级异常检测的球面打分图语言对齐框架
authors:
- Xudong Wang
- Chris Ding
- Tongxin Li
- Jicong Fan
affiliations:
- School of Data Science, The Chinese University of Hong Kong, Shenzhen (CUHK-Shenzhen),
  China
arxiv_id: '2609.05253'
url: https://arxiv.org/abs/2609.05253
pdf_url: https://arxiv.org/pdf/2609.05253
published: '2026-09-04'
collected: '2026-09-07'
category: Other
direction: 图异常检测 · 跨域多模态对齐
tags:
- Graph Anomaly Detection
- Multimodal Alignment
- Zero-shot Transfer
- Hyperspherical Learning
- Prompt Engineering
one_liner: 提出基于单位超球图-文本对齐的GLASS框架，实现高鲁棒性跨域图级异常检测，支持零/少样本适配
practical_value: '- 可复用GraphDP序列化思路，将电商用户行为图、商品关联图、社交关系图转化为语义prompt，接入LLM实现刷单刷评账号、虚假交易等异常场景识别

  - 超球多模态打分方法可迁移至多模态推荐的召回排序阶段，替代传统余弦相似度计算，提升多模态特征匹配的鲁棒性

  - 零/少样本跨域适配方案可用于新业务场景冷启动，仅需少量正常样本校准即可快速上线异常检测能力，降低标注成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有图级异常检测（GLAD）模型仅适配单数据集训练，跨域泛化能力弱，无法满足分子筛选、社交网络、电商行为等多领域异构图的异常识别需求。
### 方法关键点
1. 提出Graph Descriptor Prompt（GraphDP），序列化图的局部、全局、语义属性，搭建图到文本的语义桥梁，实现域无关异常打分
2. 以多切片软余弦目标对齐结构感知图编码器与指令感知文本嵌入，在单位超球上构建统一表征空间，通过套娃表征切片捕获多粒度异常偏差
3. 提出Spherical Multi-Modal Scoring（SMS），在图、文本嵌入空间基于von Mises-Fisher核密度估计做异常打分，融合结构与语义异常信号
### 关键结果
在12个基准数据集、3个元域上，平均AUROC与排名均优于当前SOTA GLAD基线；支持无目标域训练数据的零样本检测，仅需少量正常样本即可完成少样本适配
