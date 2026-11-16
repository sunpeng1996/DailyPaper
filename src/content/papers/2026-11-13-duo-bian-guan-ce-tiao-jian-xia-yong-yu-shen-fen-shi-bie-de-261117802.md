---
title: Multimodal Person Concept Model for Person Identification under Varying Observation
  Conditions
title_zh: 多变观测条件下用于身份识别的多模态人物概念模型
authors:
- Mizuho Okitani
- Yoshinobu Hagiwara
affiliations:
- Faculty of Science and Engineering, Soka University, Tokyo, Japan
arxiv_id: '2611.17802'
url: https://arxiv.org/abs/2611.17802
pdf_url: https://arxiv.org/pdf/2611.17802
published: '2026-11-13'
collected: '2026-11-16'
category: Multimodal
direction: 多模态无监督人物身份识别
tags:
- Multimodal
- CLIP
- CLAP
- Unsupervised Clustering
- Person Identification
one_liner: 提出无标注小样本下融合多模态特征的鲁棒无监督人物身份识别方案
practical_value: '- 线下门店/服务机器人场景的用户身份识别任务，可复用CLIP+CLAP+PCA降维的多模态特征融合方案，适配穿着变化、环境噪音等复杂观测条件

  - 无标注小样本用户聚类场景可参考基于中餐馆过程的非参数贝叶斯生成模型，无需提前预设聚类数量

  - 多模态匹配/召回任务可借鉴该方案的跨模态特征对齐思路，提升弱观测条件下的识别鲁棒性'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
家用/办公服务机器人需识别用户提供个性化服务，但存在训练样本少、观测条件多变（穿着变化、环境噪音、转录错误）、无身份标注的痛点。
### 方法关键点
1. 采用基于中餐馆过程的非参数贝叶斯生成模型，无需提前预设用户数量、无需标注即可完成小样本学习
2. 融合CLIP提取的视觉特征、CLAP提取的声学+语言特征，经PCA降维后输入模型
### 关键结果
8种干扰条件（单种或组合叠加穿着变化、加性噪音、转录错误）下平均识别准确率达0.89，优于拿到真实用户数的k-means聚类的0.88，已在丰田助行机器人上完成落地验证。
