---
title: 'AspectCLIP: Optimizing CLIP Representation Space via Aspect-Guided Consistency
  Regularization'
title_zh: AspectCLIP：基于方面引导一致性正则的CLIP表征空间优化
authors:
- Yiyang Yao
- Shanglin Liu
- Jianming Lv
- Chengjun Wang
- Jinyi Li
- Yuchan Jie
- Zhihua Jin
affiliations:
- South China University of Technology
arxiv_id: '2607.13805'
url: https://arxiv.org/abs/2607.13805
pdf_url: https://arxiv.org/pdf/2607.13805
published: '2026-07-15'
collected: '2026-07-16'
category: Multimodal
direction: 多模态预训练 · CLIP表征优化
tags:
- CLIP
- Contrastive Learning
- Consistency Regularization
- Multimodal Representation
- Pre-training
one_liner: 提出基于文本属性聚类的差异化一致性正则方案，优化CLIP多模态表征空间
practical_value: '- 电商多模态检索场景可复用「文本聚类划分属性组+组内/组间差异化正则」的优化思路，提升同款/同品不同描述商品的检索准确率

  - 商品图文表征训练阶段可借鉴组间原型对比的trick，避免不同角度描述的相似商品表征出现语义偏移

  - 多模态商品召回/排序模块的CLIP微调阶段，可直接引入该正则方法提升表征结构化程度，无需大规模改动训练流程'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
CLIP预训练中图文存在天然信息不对称：单张图片可对应多维度文本描述，现有全局一致性正则会强制视觉相似但文本描述维度不同的样本对齐，导致表征语义失真。

### 方法关键点
1. 基于文本相似度将训练样本划分为属性聚类，识别出描述维度一致的样本组；
2. 同组内执行全循环一致性约束，不同组间仅在原型维度做正则对比；
3. 仅在图文描述维度一致时做严格几何对齐，不同维度间保留表征灵活性。

### 关键结果
在零样本分类、零样本检索、线性探测等多个下游任务上效果持续优于传统CLIP正则方法，表征空间结构化程度显著提升。
