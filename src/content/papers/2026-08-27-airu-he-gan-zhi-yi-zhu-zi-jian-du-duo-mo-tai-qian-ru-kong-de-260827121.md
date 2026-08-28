---
title: 'How AI Experiences Art: Emergent Aesthetic Structure in a Self-Supervised
  Multimodal Embedding Space'
title_zh: AI如何感知艺术：自监督多模态嵌入空间的涌现美学结构
authors:
- Corey D. C. Heath
affiliations:
- Independent Researcher
arxiv_id: '2608.27121'
url: https://arxiv.org/abs/2608.27121
pdf_url: https://arxiv.org/pdf/2608.27121
published: '2026-08-27'
collected: '2026-08-28'
category: Multimodal
direction: 多模态嵌入 · 无监督美学挖掘
tags:
- Multimodal Embedding
- Self-Supervised Learning
- Clustering
- RAG
- Aesthetic Categorization
one_liner: 提出无标签无跨模态监督的自监督框架，挖掘多模态内容的涌现美学结构
practical_value: '- 多模态内容召回场景可复用「跨模态共享低维嵌入+迭代聚类」方案，对异构内容做无标签分类，降低标注成本

  - 电商内容RAG系统可参考该框架组织图文音视频混合的商品素材库，提升跨模态检索匹配精度

  - 个性化美学类推荐（家装、艺术品、穿搭等）可借鉴无监督美学聚类逻辑，补充人工标注外的用户审美偏好标签维度'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有研究对无标签、无跨模态监督场景下，AI如何对人类创作的多模态内容完成美学分类的机制探索不足，而跨模态审美感知是内容检索、个性化推荐等场景的核心需求。
### 方法关键点
1. 搭建自监督框架，将文本、音频、图像、视频4种模态统一映射到256维共享嵌入空间；
2. 基于共享嵌入执行迭代聚类，自动挖掘空间中涌现的美学结构；
3. 在弱监督多模态数据集上，对比AI聚类结果与人类情感标注标签的差异。
### 关键结果
该框架可直接落地于跨模态相似度建模、异构媒体RAG知识库组织、自动化数据标注三类场景，无监督得到的美学分类结果与人类标注存在可解释的差异化分布。
