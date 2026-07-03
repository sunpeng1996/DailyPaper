---
title: Object-centric LeJEPA
title_zh: 基于对象中心的LeJEPA自监督图像预训练方法
authors:
- Jakob Geusen
- Ender Konukoglu
affiliations:
- ETH Zurich
arxiv_id: '2607.02404'
url: https://arxiv.org/abs/2607.02404
pdf_url: https://arxiv.org/pdf/2607.02404
published: '2026-07-02'
collected: '2026-07-03'
category: Multimodal
direction: 多模态表征 · 对象级自监督预训练
tags:
- Self-supervised Learning
- Object-centric Representation
- SAM
- LeJEPA
- Image Encoder
- Representation Learning
one_liner: 采用SAM生成的对象掩码训练对象中心LeJEPA，提升小数据下多视觉任务性能
practical_value: '- 电商商品多模态表征预训练场景，可直接复用「现成SAM生成对象掩码+对象级对齐」的范式，规避纯自监督分割-表征循环依赖的训练不稳定问题，降低预训练数据门槛

  - 同款商品检索、商品重识别任务，可新增同场景其他商品作为负例的实例分离损失，提升表征的实例区分度，小样本场景下收益更明显

  - 多模态召回/排序的商品特征预训练，可替换原有图像级对比学习目标为对象级LeJEPA抗坍塌目标，减少背景、上下文干扰，提升商品本身表征的纯度'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
图像级自监督预训练（如原生LeJEPA）依赖大规模训练数据，纯自监督实现对象级表征存在「分割依赖有效表征、表征依赖稳定分割」的循环依赖问题，训练难度极高。

### 方法关键点
1. 直接引入低成本现成SAM生成的对象掩码作为训练输入，从根源上规避分割与表征的循环依赖问题
2. 扩展LeJEPA原生的分布抗坍塌优化目标，从整图表征对齐适配为可变长度对象集合的表征对齐
3. 新增实例分离损失，将同一场景内的其他对象作为负样本，进一步提升表征的实例区分度

### 关键结果
在10%~100% COCO训练数据规模、两种模型尺寸下，对象级LeJEPA在DAVIS跟踪、ImageNet-1k分类、ADE20k分割、NAVI重识别4类任务上均全面优于原图像级LeJEPA
