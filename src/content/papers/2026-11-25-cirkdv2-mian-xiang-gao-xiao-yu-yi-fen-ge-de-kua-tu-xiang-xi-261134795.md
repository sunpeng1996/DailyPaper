---
title: 'CIRKDV2: Cross-Image Relational Knowledge Distillation with Contextual Modeling
  for Efficient Semantic Segmentation'
title_zh: CIRKDV2：面向高效语义分割的跨图像关系知识蒸馏与上下文建模
authors:
- Chuanguang Yang
- Yu Wang
- Chengqing Yu
- Xinqiang Yu
- Weilun Feng
- Yuqi Li
- Zhulin An
- Libo Huang
- Boyu Diao
- Fei Wang
affiliations:
- 中国科学院计算技术研究所
- 中国科学院大学
arxiv_id: '2611.34795'
url: https://arxiv.org/abs/2611.34795
pdf_url: https://arxiv.org/pdf/2611.34795
published: '2026-11-25'
collected: '2026-11-27'
category: Other
direction: 知识蒸馏 · 语义分割小模型优化
tags:
- Knowledge Distillation
- Semantic Segmentation
- Model Compression
- Context Aggregation
one_liner: 提出跨图像关系+上下文特征蒸馏方案，大幅提升语义分割小模型性能
practical_value: '- 电商场景做端侧/轻量化商品图像分割、属性识别模型时，可复用跨图像全局关系蒸馏思路，无需仅对齐单张图的教师特征，提升小模型特征表征能力

  - 蒸馏训练时可引入上下文聚合增强学生模型的像素嵌入，对齐师生语义层级，缓解传统特征蒸馏普遍存在的语义Gap问题

  - 该蒸馏范式对数据集、网络架构兼容性强，可直接迁移到商品抠图、货架识别、违规内容检测等CV任务的小模型迭代中'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有语义分割知识蒸馏方法仅引导学生模型拟合单张图像的教师结构化输出，忽略数据集内跨图像的全局语义关系价值，同时师生模型固有的语义Gap也会限制蒸馏效果。
### 方法关键点
1. 提出CIRKDV2框架，迁移从数据集全局图像中建模的像素-像素、像素-区域、通道-通道三类结构化关系，让学生模型对齐教师的全局结构化语义空间，提升特征表征能力。
2. 新增上下文特征蒸馏模块，通过上下文聚合增强学生的像素嵌入，对齐师生语义层级，规避传统特征蒸馏的语义Gap问题。
### 关键结果
在Cityscapes、ADE20K、Pascal VOC、COCO-Stuff-164K等多个主流数据集上，CIRKDV2在各类网络架构下均大幅领先现有SOTA语义分割蒸馏方法。
