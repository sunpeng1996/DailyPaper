---
title: 'GFR-SAM: Training-Free Referring Camouflaged Object Segmentation via Cross-Image
  Prompting'
title_zh: GFR-SAM：基于跨图像提示的免训练参考伪装目标分割
authors:
- Yilong Yang
- Jianxin Tian
- Shengchuan Zhang
- Liujuan Cao
affiliations:
- Key Laboratory of Multimedia Trusted Perception and Efficient Computing, Ministry
  of Education of China, Xiamen University
arxiv_id: '2607.11732'
url: https://arxiv.org/abs/2607.11732
pdf_url: https://arxiv.org/pdf/2607.11732
published: '2026-07-13'
collected: '2026-07-15'
category: Other
direction: 视觉大模型免微调适配专用感知任务
tags:
- SAM3
- Training-Free
- Cross-Image Prompting
- Object Segmentation
- DINOv3
- In-Context Learning
one_liner: 提出三阶段免训练GFR-SAM框架，解锁SAM3跨图像上下文能力，实现高性能参考伪装目标分割
practical_value: '- 可复用跨图像上下文提示工程方法，突破SAM系列原生单图像推理限制，适配多图关联的分割/识别需求

  - 生成-过滤-精炼三阶段免微调框架可迁移：大模型生成候选→特征对齐降噪→多模态提示补全细粒度结果，大幅降低标注依赖

  - DINOv3原型对齐过滤背景干扰的方案，可直接复用在电商同款识别、商品瑕疵检测等少标注视觉业务场景'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
参考伪装目标检测（Ref-COD）现有监督方案依赖大量标注，免训练点提示方法对定位误差敏感，SAM3原生仅支持单图像内推理，无法直接适配跨参考图的分割需求。
### 方法关键点
采用「生成-过滤-精炼」三阶段管线：1. 上下文示例引导分割模块，赋予SAM3跨图像推理能力，基于整体视觉示例生成候选掩码，突破原生单图约束；2. 区域-全局对比过滤模块，通过DINOv3原型对齐排序候选，抑制背景干扰；3. 几何-语义精炼模块，融合边界框与文本提示，恢复细粒度边界、提升实例召回。
### 关键结果
在R2C7K基准上，加权F-measure（$F_β^w$）较现有免训练方法提升8.7%，性能比肩监督SOTA方案。
